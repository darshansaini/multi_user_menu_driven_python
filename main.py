import plotly.express as px

def display():
    print("************************\n"
          "Analysis :\n"
          "************************"
          "\n"
          "1. Log in \n"
          "2. Signup \n"
          "3. Users List \n"
          "************************\n"
          "------------------------\n")
    choice = input()


    if choice == "1":

        user = input("Enter Username : ")
        with open("data.txt","a+") as data:
            data.write("login attempt")
        with open("data.txt","r+") as data:

            temp = data.read()
            temp = temp.split()
            for i in temp:
                if user==i:
                    break

            else:
                print("Invalid Username")

                display()
        password = input("Enter Password : ")

        with open("data.txt","r+") as data:

            temp = data.read()
            temp = temp.split()
            for i in temp:
                if password==i:
                    print("logged in Successfully ...\n")

                    def login():

                        print("************************\n"
                              "ANALYSIS :\n"
                              "************************\n"
                              "1. Salary Growth Analysis \n"
                              "2. Student Growth Analysis \n"
                              "3. List Of All Entries in Salary  \n"
                              "4. List Of All Entries in Student  \n"
                              "6. Exit/Logout\n"
                              "************************\n"
                              "------------------------")

                        key = input("Select your Choice ... ")
                        if key == "1":
                            print("for how many year's analyse you want : ")
                            x = int(input())
                            x_cord = []
                            y_cord = []

                            print("Enter your past ", x, " years salary :")
                            for i in range(1, x + 1):
                                y_cord.append(i)
                                continue
                            for i in range(1, x + 1):
                                a = input()
                                x_cord.append(a)

                            x_cord_str = str(x_cord)
                            y_cord_str = str(y_cord)

                            with open("Salary.txt", "a+") as salary:
                                salary.write("Years : ")
                                salary.write(y_cord_str)
                                salary.write(" Salary : ")
                                salary.write(x_cord_str)
                                salary.write("\n")

                            # Creating the Figure instance

                            fig = px.line(x=x_cord, y=y_cord)

                            # showing the plot
                            fig.show()

                            input("Hit Enter to continue...\n\n")
                            login()

                        elif key == "2":
                            print("for how many year's analyse you want : ")
                            x = int(input())
                            x_cord = []
                            y_cord = []

                            print("Enter your past ", x, " years Marks :")
                            for i in range(1, x + 1):
                                y_cord.append(i)
                                continue
                            for i in range(1, x + 1):
                                a = input()
                                x_cord.append(a)

                            x_cord_str = str(x_cord)
                            y_cord_str = str(y_cord)

                            with open("Student.txt", "a+") as salary:
                                salary.write("Years : ")
                                salary.write(y_cord_str)
                                salary.write(" Marks : ")
                                salary.write(x_cord_str)
                                salary.write("\n")

                            # Creating the Figure instance

                            fig = px.line(x=x_cord, y=y_cord)

                            # showing the plot
                            fig.show()

                            input("Hit Enter to continue...\n\n")
                            login()


                        elif key == "3":
                            with open("Salary.txt", "r+") as salary:
                                print(salary.read())

                            input("Hit Enter to continue...\n\n")
                            login()

                        elif key == "4":
                            with open("Student.txt", "r+") as student:
                                print(student.read())

                            input("Hit Enter to continue...\n\n")
                            login()

                        elif key == "5":
                            input("Hit Enter to LogOut...\n\n")
                            print("Loogged out ...\n\n")
                            display()

                    login()



            else:
                print("Invalid Password\n\n")


                display()

    elif choice == "3":

        with open("datadisplay.txt", "r+") as datadisplay:

            print(datadisplay.read())
            input("Hit Enter to go main menu... \n\n")

            display()

    elif choice == "2":
        username = input("Enter a username to signup (No white Space allowed) : ")
        cred = input("Enter a password :((No white Space allowed))")
        count = 1
        with open('datadisplay.txt', 'a+') as datadisplay:
            datadisplay.write(f"{0} Username : ".format(count))
            datadisplay.write(username)
            datadisplay.write("\n")

        with open('data.txt',"a+") as data:
            data.write(f"{0} Username : ".format(count))
            data.write(username)
            data.write(" Password : ")
            data.write(cred)
            data.write("\n")
        count = count+1
        print("Signup Successful...\n\n")
        display()

    else:
        print("Invalid Selection... Try again...\n\n")

        display()

display()
