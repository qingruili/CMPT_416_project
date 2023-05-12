import inspect
from faker import Faker
from Property_input_generator import test_cases_maker_property, random_str
import itertools
import os
#from do_test import question_function
from import_file import *
import importlib
import sys
from extract_path import *
import copy

supported_properties = ["Commutative", "Idempotent", "Always True", "Always False", "Always Positive", "Always Negative", "Always Zero",
                        "Zero Testing", "Preserve Input"]

fake = Faker()
#parsing functions
##################################################################################################################################################
def argType_parser(fn):
    signature = str(inspect.signature(fn))
    arg_list = signature[1:-1].split(',')
    for i, s in enumerate(arg_list): arg_list[i] = s[s.find(':')+2:]
    return arg_list

def argName_parser(fn):
    arg_names = inspect.getfullargspec(fn) # get all parameter_names
   # for i in range(len(arg_names[0]) - 1): arg_names[0][i] += ',' # comma seperate all parameters
    return ' '.join(arg_names[0])

def property_parser(fn, student_fn,st):
    s = fn.__doc__
    s = s.splitlines()

    for i in range(len(s)):
        s[i] = s[i].strip()
    properties = s[s.index("@Properties") + 1 : len(s) - 1] # get all properties

    return [item.replace(fn.__name__, str(st) + '.'+student_fn.__name__) for item in properties],properties # replace all properties with func name with student function name


def parse_function(fn, student_fn,st):
    properties,properties_name = property_parser(fn, student_fn,st)
    argNames = inspect.getfullargspec(fn)[0]
    argTypes = argType_parser(fn)
    
    signature = str(inspect.signature(fn))
    return {"properties" : properties, 
            "argNames" : argNames,
            "argTypes" : argTypes,
            "signature" : signature,
            "fn" : fn,
            "student_fn" : student_fn,
            "properties_name": properties_name
           }
#####################################################################################################################################################

#testing functions
def input_generator(fn, student_fn,test_cases,student):
    index = student.__name__.find(".")
    st = student.__name__
    html =''
    if index != -1:
        st = st[index + 1:]
    dict = parse_function(fn, student_fn,st)
    if(dict["properties"][0]!="(optional)"):
        html = property_tester(dict, test_cases,st)
    return html

    
''' make sure that the function to be tested has the same argument names as those
    defined in the properties.

    for example if we have the property: 
        len(s) == len(clean_text(s))

    then clean_text declartion should look like this:
        def clean_text(s: str): ....
'''

def generate_function_call_string(function_name, argNames):
    s = function_name + '('
    for i, n in enumerate(argNames):
        s += n
        if i != len(argNames) - 1:
            s += ','
    s += ')'

    return s

def default_properties(property, dict, case,st):
        var_name = []
        check = True
        for i, x in enumerate(dict["argNames"]): # create new variables named the same as the strings from argNames, and assign them value of the test case
            var_name.append(x)
            value = case[i]
            exec(f"{var_name[i]} = {value!r}")
        
        default_call = generate_function_call_string(str(st) +'.'+ str(dict["student_fn"].__name__), dict["argNames"])

        if property == "Commutative":
            permutations = itertools.permutations(dict["argNames"])
            for perm in permutations:
                call_string = generate_function_call_string(str(st) +'.'+ str(dict["student_fn"].__name__), list(perm))
                if (eval(default_call) == eval(call_string)) == False:
                    check = False
                    
        elif property == "Idempotent":
            if (eval(default_call) == (dict["fn"](eval(default_call))) == False):
                check = False

        elif property == "Zero Testing": # all arguments are equal to zero ex: add2ints(0, 0)
            for i, x in enumerate(dict["argNames"]):
                var_name.append(x)
                value = 0
                exec(f"{var_name[i]} = {value!r}")
            if eval(default_call) != eval(generate_function_call_string(dict["fn"].__name__, dict["argNames"])):
                check = False

        elif property == "Preserve Input":
            copy_var_values = []
            for i in range(len(var_name)):
                copy_var_values.append(eval(f"{var_name[i]}"))
            copy_var_values = copy.deepcopy(copy_var_values)
            eval(default_call)
            for i in range(len(var_name)):
                if eval(f"{var_name[i]}") != copy_var_values[i]:
                    check = False
                # print(eval(f"{var_name[i]}"))
                # print(copy_var_values)
        
        elif property == "Always True":
            if eval(default_call) != True:
                check = False
        
        elif property == "Always False":
            if eval(default_call) != False:
                check = False

        elif property == "Always Positive":
            if eval(default_call) <= 0:
                check = False
        
        elif property == "Always Negative":
            if eval(default_call) >= 0:
                check = False
        
        elif property == "Always Zero":
            if eval(default_call) != 0:
                check = False

        return check



def property_tester(dict, test_cases,st):

    html = '<table  border="1" cellspacing="0" cellpadding="4">'

    html += '<tr>\n<th>Test Cases\n</th>'
    para = ''

    for k in range(len(dict["properties_name"])):

        para +='\n<th>'+ dict["properties_name"][k] + '</th>'
    
    para+= '\n<th>Pass Rate\n</th><th>Pass Percentage</th>'
    
    html += para +'</tr>'

    for case in (test_cases):
        para = '<tr>'
        var_name = []
        for i, x in enumerate(dict["argNames"]): # create new variables named the same as the strings from argNames, and assign them value of the test case
            var_name += x
            value = case[i]
            exec(f"{var_name[i]} = {value!r}")

        p = '' 
        for i in range(len(dict["argNames"])):
            if type(eval(var_name[i])) == str:
                p += f"{var_name[i]}: '{eval(var_name[i])}'<br>"
            else:
                p += f"{var_name[i]}: {eval(var_name[i])}<br>"
        
        para += '\n<th>'+ p + '</th>'
        
        
        count = 0
        suc= 0
        for k in range(len(dict["properties"])):
            count = count+1

            if dict["properties"][k] in supported_properties:
                re = default_properties(dict["properties"][k], dict, case,st)
                if re == True:
                    suc = suc +1
                    para+= '\n<td>'+ str(re) + '</td>'
                else:
                    para+= '\n<td style="color:red;">'+ str(re) + '</td>'
            else:
                try:
                    eval(dict["properties"][k])
                except:
                    para+= '\n<td style="color:red;">False</td>'
                    
                else:
                    result = eval(dict["properties"][k])
                
                    if result == True:
                        suc = suc+1
                        para+= '\n<td>'+ str(result) + '</td>'
                    else:
                        para+= '\n<td style="color:red;">'+ str(result) + '</td>'
        para += '\n<td>'+ str(suc) + '&nbspof&nbsp' + str(count)+ '</td>'
        para += '\n<td>'+ str(round((suc)/count*100,1)) + '<span>&#37;</span>'+'</td>'
        para += '</tr>'
        html += para

    html +='</table>'
    
    return html


if __name__ != '__main__':
    question_folder_path=paths(sys.argv[1])
    files = os.listdir(question_folder_path)
    new_files = []
    for file in files:
        if file.endswith(".py"):
            module_name = file[:-3]
            new_files.append(module_name)
            module = importlib.import_module(f"{sys.argv[1]}.{module_name}")
            globals()[module_name] = module
