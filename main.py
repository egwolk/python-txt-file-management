print("""
What would you like to do?
[1] Read a file
[2] Create a new file
[3] Add data to a file
[4] Rename a file 
[5] Delete a file
""")
while True:
    user_input = input("Your choice: ")
    match user_input:
        case "1":
            break
        case "2":
            break
        case "3":
            break
        case "4":
            break
        case "5":
            break
        case _:
            print("invalid input. try again")

print(f"You picked {user_input}")