import os, sys

def read_file(filename):
    try:
        with open(filename, "r") as file:
            print(f"{filename} contents:")
            for line in file:
                print(f"{line.strip()}")
            input("Press enter key to continue...")
    except:
        print("file does not exist")
        input("Press enter key to continue...")

def input_file_name():
    file = input("Enter txt file name[no extension]: ")
    return file + ".txt"

def write_file(filename):
    if os.path.exists(filename):
        print(f"File with name {filename} already exists.\nOverwrite file?")
        while True:
            yn = input("Y|N: ").lower().strip()
            match yn:
                case "y":
                    content = []
                    clear_console()
                    print("Start writing your file content [press enter twice to finish]:")
                    while True:
                        line = input()
                        if line:
                            content.append(line + "\n")
                        else: break
                    with open(filename, "w") as file:
                        file.writelines(content)
                    break
                case "n":
                    print("operation cancelled")
                    input("Press enter key to continue...")
                    break
                case _:
                    print("invalid input. Try again")
            
    

def append_file():
    pass
def rename_file():
    pass
def delete_file():
    pass

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_console()
    print("""
What would you like to do?
[1] Read a file
[2] Create a new file
[3] Add data to a file
[4] Rename a file 
[5] Delete a file
[6] Read program docs
[7] Exit
""")
    while True:
        user_input = input("Your choice: ")
        match user_input:
            case "1":
                clear_console()
                file = input_file_name()
                read_file(file)
                break
            case "2":
                clear_console()
                file = input_file_name()
                write_file(file)
                break
            case "3":
                clear_console()
                break
            case "4":
                clear_console()
                break
            case "5":
                clear_console()
                break
            case "6":
                clear_console()
                break
            case "7":
                clear_console()
                sys.exit("bye bye")
            case _:
                print("invalid input. try again")
