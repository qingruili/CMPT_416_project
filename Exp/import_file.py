

def import_file(folder_path,function_name):

    import os
    import importlib


    files = os.listdir(folder_path)
    new_files = []
    for file in files:
        if file.endswith(".py"):
            module_name = file[:-3]
            new_files.append(module_name)
            module = importlib.import_module(f"{function_name}.{module_name}")
            globals()[module_name] = module

    specific_word = 'teacher'
    index_of_specific_word = new_files.index(specific_word)
    new_files.pop(index_of_specific_word)
    new_files.insert(0, specific_word)


    return new_files