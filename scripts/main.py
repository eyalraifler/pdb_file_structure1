import sys
import math


def ask_user_for_structure():
    user_input = 0
    file = None
    while user_input != 1 and user_input != 2 and user_input != 3:
        user_input = int(input("Please enter the number of a protein:\n1: 3W8W, 2: 4BS7, 3: 2YMW: "))
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
        


def longest_distance_between_2_atoms(file):
    valid_atoms = [] #we'll store here the coordinates of each valid atom: x, y, z
    
    for line in file:
        first_word = line[0:4]
        if first_word == "ATOM":

            # the line is now split. the first element is "ATOM", 
            # the fifth is A or B(we want only A), 
            # the seventh, eight and nineth elements are the x y and z.
            if line[21] == "A":
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])          
                valid_atoms.append((x, y, z))
    
    max_distance = 0.0
    nnumber_of_atoms = len(valid_atoms)
    for i in range(nnumber_of_atoms - 1):
        x1, y1, z1 = valid_atoms[i]
        for j in range(i + 1, nnumber_of_atoms):
            x2, y2, z2 = valid_atoms[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d2 = dx * dx + dy * dy + dz * dz
            if d2 > max_distance:
                max_distance = d2

    return math.sqrt(max_distance)
                
            
        

if __name__ == "__main__":
    file_path = ask_user_for_structure()
    file = open_file(file_path)
    longest_distance = longest_distance_between_2_atoms(file)
    with open ("results/longest_distance.txt", "w") as output_file:
        output_file.write(f"The longest distance between 2 atoms for {file_path} is: {longest_distance}\n")
    
    file.close()