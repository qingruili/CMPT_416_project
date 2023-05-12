def extract_path(question_folder_path ):

    chart = "/\\"

    last_position = -1
    for i, letter in enumerate(question_folder_path):
        if letter in chart:
            last_position = i
    return last_position


def paths(question_function):
    question_folder_path = __file__
    last_position = extract_path(question_folder_path )
    question_folder_path = question_folder_path[:last_position+1]
    question_folder_path += question_function
    
    return question_folder_path