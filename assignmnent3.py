def Main():
    with open("students.txt", "r") as file:
        content = file.read()
        while True:
            print("1) Search by Last Name")
            print("2) Search by Major")
            print("3) Quit")
            answer = int(input("Choose an option: "))
            if answer == 1:
                lastname = input("Enter last name: ")
                
                
Main()