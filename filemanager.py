import os

import shutil


# Define the function that will simulate the switch statement
def switch_options(case):
    """"
    Return :
        function user choice
    Args :
        case(int) :option number
    Returns :
        func
    """
    # Get the function from the dictionary
    func = operations.get(int(case), lambda: "Invalid case")
    # Call the function
    return func()


def list_all_files():
    """
    list the contents of the directory
    :returns None
    """
    try:
        contents = os.listdir(directory)
        print('\n'.join(contents))
        return True
    except Exception as e:
        print(f"There was no file in this directory {directory}")
        return False


def create_file():
    """
    create a new directory
    :return: return true if there was no errors
    """
    try:
        file_name = input("Please enter file name :").strip()
        #  join new directory and the path
        os.mkdir(os.path.join(directory, file_name))
        return True
    except Exception as e:
        print(f"file already exists :{os.path.join(directory, file_name)}")
        return False


def rename_file():
    """
    rename a specific file bu enter the name of file you want to change and the new name and join it with the path
    :return: return true if there was no errors
    """
    try:
        old_name = input("What is the name of file you want to change name").strip()
        new_name = input("What is the new name of file you want").strip()
        os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
        return True
    except Exception as e:
        print("An error occurred:", e)
        return False



def delete_file():
    """
    remove a specific file by join the name user entered with path and give it to rmtree function in shutil  library
    :return: boolean, true if there was  no errors
    """
    try :
        file_select = input("please enter the name of file you want to delete").strip()
        shutil.rmtree(os.path.join(directory, file_select))
        return True
    except Exception as e :
        print(f"There was no file {file_select} in this directory {directory}")
        return False



def search_file():
    """
    search for a function and return exist  message if exist and not exist if not
    :return: boolean, true if there was  no errors
    """

    file_name = input("please enter the name of file you want to search").strip()
    if os.path.exists(os.path.join(directory, file_name)):
        print('Directory exists')
    else:
        print('Directory does not exist')
    return True


def exit():
    """
    exit the program
    :return: false to exit from inf loop
    """
    print("Goodbye\U0001F600!")
    return False


def main():
    """
    run the program
    """
    while True:
        try:
            print("Menu:\n"
                  "1. List all files\n"
                  "2. Create a new file\n"
                  "3. Rename a file\n"
                  "4. Delete a file\n"
                  "5. Search for a file\n"
                  "6. Exit\n")
            operation = input("Please Enter Your Choice: ")

            if not switch_options(operation):
                break
        except Exception as e:
            print("An error occurred:", e)
            print("Please enter number between 1-6")


if __name__ == '__main__':
    directory = "C:/Users/11805/PycharmProjects/pythontraining/Week1"
    # Define the dictionary to map cases to actions in list
    operations = {
        1: list_all_files,
        2: create_file,
        3: rename_file,
        4: delete_file,
        5: search_file,
        6: exit
    }
    main()
