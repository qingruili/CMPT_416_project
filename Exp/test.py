import doctest
import io
import os
from Random_input_generator import *
from import_file import *
import importlib
from extract_path import *
import sys




def append_random_test(teacher_fn,n):
    # append random test into docstring
    teacher_fn.__doc__ += "\n\n@ Automatically Added Random Tests Cases\n"
    inputs = test_cases_maker(teacher_fn,n)
    test_input = amendment_input(inputs)
    test_output = random_test_output(inputs,teacher_fn)
    for l in range(len(test_input)):
        append_docstring_random(teacher_fn,test_input[l],test_output[l])


def append_doctest(teacher_fn, student_fn,st): # correct func, student func, num of random test want to do
    # assign teacher_fn doc string to student_fn doc string
    if student_fn.__doc__ == None:
        student_fn.__doc__ = teacher_fn.__doc__
    else:
        student_fn.__doc__ += teacher_fn.__doc__

    docstring = student_fn.__doc__
    new_docstring = docstring.replace(teacher_fn.__name__, st+'.'+student_fn.__name__)
    student_fn.__doc__ = new_docstring



def append_docstring_random(fn, input, output):
    doc = f"\n>>> {fn.__name__}("
    for i in input:
        if type(i) == str:
            doc += f"'{i}',"
        else:
            doc += f"{i},"
    doc = doc[:-1]
    
    if type(output) == str:
        index = output.find('\'')
        index1 = output.find('\"')
        if index != -1 and index1 == -1: 
            doc += f")\n\"{output}\""
        elif index != -1 and index1 != -1:
            output = output.replace('\'', '\\\'', -1)
            doc += f")\n'{output}'"
        else:
            doc += f")\n'{output}'"
    else:
        doc += f")\n{output}"
    fn.__doc__ += f"""{doc}"""



def random_test_output(inputs,teacher_fn):
    test_output = []
    for char in inputs:
        new ='teacher_fn('
        for i in range(len(char)):
            if type(char[i]) == str:
                char[i] = char[i].replace('\\', '', -1)
            new +=f"char[{i}],"
        new = new[:-1]
        new += ')'
        output = eval(new)
        test_output.append(output)
    return test_output



def amendment_input(inputs):
    test_input = []
    for ch in inputs:
        test_input_per_test = []
        for char in ch:
            if type(char) == str:
                new = char.replace('\\', '', -1)
                num = 0
                new_string_doc=''
                while num in range(len(new)):
                    if new[num] == '\'':
                        if new[num-1] != '\\':
                            new_string_doc += '\\\''
                            num +=1
                        else:
                            new_string_doc += new[num]
                            num += 1
                    else:
                        new_string_doc += new[num]
                        num +=1
                test_input_per_test.append(new_string_doc)
            else:
                test_input_per_test.append(char)
        
        test_input.append(test_input_per_test)
    return test_input
    

def exp_html(answer,student_fn,result,teacher_fn,st,htl):


    html =  "<html>\n<head>\n<style>\nbody { font-family: Arial, Helvetica, sans-serif; }\nh3 { margin-top: 40px; text-align: center; }\nh4 { margin-top: 30px; }\np { margin: 0; }\n.test { margin-bottom: 20px; }\n.passed { color: green; }\n.failed { color: red; }\n</style>\n</head>\n<body>\n"
    
    title = st + '.' + student_fn.__name__
    html += f"<h3>Running marker for {teacher_fn.__name__} on {title}</h3>\n"
    html += "<h4>Running Extra and Random Tests</h4>\n"

    line = answer.splitlines()
    i = 0
    num = 1
    while i < len(line):
        if line[i] == "Trying:":
            para = f'<br><div class="test"><p><strong>Test {num}:</strong></p>\n'
            para += f'<p>{line[i]} {line[i+1]}</p>\n'
            i += 2
            num += 1
        elif line[i] == "Expecting:":
            para = f'<p>{line[i]} {line[i+1]}</p></div>\n'
            i += 2
        elif line[i].startswith("****"):
            para = f'<p><strong>{line[i]}</strong></p>\n'
            i += 2
        else:
            para = f'<p>{line[i]}</p>\n'
            i += 1
        html += para
    
    html += '<br><p>Done Extra and Random Tests</p>\n'

    html += f"<p>{result.attempted - result.failed} of {result.attempted} tests passed "
    if result.failed == 0:
        html += '<span class="passed">(100% passed)</span></p>\n'
    else:
        html += f'<span class="failed">({round(((result.attempted-result.failed)/result.attempted)*100, 1)}% passed)</span></p>\n'

    if htl != '':
        html += '\n<br><br><h4> Running Property test </h4>\n'
        html += htl
    html += "</body>\n</html>"


    return html

        


def run_doctest(teacher_fn,student_fn,student,htl):
    

    index = student.__name__.find(".")
    st = student.__name__
    if index != -1:
        st = st[index + 1:]

    append_doctest(teacher_fn, student_fn,st)

    parser = doctest.DocTestParser()
    test = parser.get_doctest(student_fn.__doc__, globals(), '{student_fn.__name__}', None, None)
    output = io.StringIO()
    runner = doctest.DocTestRunner(verbose=True)

    result = runner.run(test, out=output.write)

    # Get the output from the StringIO object
    answer = output.getvalue()

    html = exp_html(answer,student_fn,result,teacher_fn,st,htl)
    
    folder_name = teacher_fn.__name__ +'_result' 
    file_name = st+'_' + student_fn.__name__ + '.html'
    folder_paths = question_folder_path + '/teacher.py'
    f_path = os.path.join(os.path.dirname(folder_paths), folder_name)

    file_path = os.path.join(f_path, file_name)

    if not os.path.exists(f_path):
        os.makedirs(f_path)


    # Write the HTML report to a file
    with open(file_path, 'w') as f:
        f.write(html)
    
    

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
