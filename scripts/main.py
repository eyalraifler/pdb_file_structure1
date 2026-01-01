import sys


def ask_user_for_structure():
    user_input = 0
    file = None
    while user_input != 1 and user_input != 2 and user_input != 3:
        user_input = int(input("Please enter the number of a protein: 1-3W8W, 2-4BS7, 3-2YMW: "))
    if user_input == 1:
        file = "3W8W.pdb"
    elif user_input == 2:
        file = "4BS7.pdb"
    elif user_input == 3:
        file = "2YMW.pdb"
    else:
        raise ValueError(f"Invalid input. you entered: {user_input}")
    return file
    
def open_file(file_path):
    try:
        file = open(f"Data/{file_path}", "r")
        return file
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        sys.exit(1)



if __name__ == "__main__":
    file_path = ask_user_for_structure()
    file = open_file(file_path)
    for i in range(10):
        line = file.readline()
        print(line.strip())
    
    
    file.close()