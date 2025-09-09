def Main():
    with open("students.txt", "r") as file:
        for line in file:
            if line != "\n":
                if line.endswith("\n"):
                    line = line[:-1]
                else:
                    parts = line.split(",")
                    studentId = parts[0]
                    lastName = parts[1]
                    firstName = parts[2]
                    major = parts[3]
                    gpa = parts[4]
    while True:
        print("Choose an option: ")
        print("1) Search by Last Name")
        print("2) Search by Major")
        print("3) Quit")
        answer = int(input("Enter your choice: "))
        if answer == 1:
            lastname = input("Enter last name: ").split()
                
                
Main()