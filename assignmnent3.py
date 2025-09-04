def Main():
    file = open("students.txt", "r")
    content = file.read()
    print("Choose an option")
    print("1) Search by Last Name")
    print("2) Search by Major")
    print("3) Quit")

    answer = int(input(""))


