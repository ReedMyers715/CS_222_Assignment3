def Main():
    students = {}
    file = open("students.txt", "r")
    for line in file:
        if line.endswith("\n"):
            line = line[:-1]
                
        parts = line.split(",")
        studentId = parts[0]
        lastName = parts[1]
        firstName = parts[2]
        major = parts[3]
        gpa = parts[4]

        students[studentId] = [lastName, firstName, major, gpa]
    file.close()

    while True:
        print("Choose an option: ")
        print("1) Search by Last Name")
        print("2) Search by Major")
        print("3) Quit")
        answer = int(input("Enter your choice: "))
        if answer == 1:
            searchLastName = input("Enter last name: ")
            for studentId in students:
                info = students[studentId]
                if info[0] == searchLastName:
                    print(studentId, info[0], info[1], info[2], info[3])
        
        if answer == 2:
            searchMajor = input("Enter major: ")
            for studentId in students:
                info = students[studentId]
                if info[2] == searchMajor:
                    print(studentId, info[0], info[1], info[2], info[3])

        if answer == 3:
            print("quitting now")
            break

        if answer > 3:
            print("Invalid Choice")
Main()

                
                
