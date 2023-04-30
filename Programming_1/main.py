import csv
import random


class StudentPage:
    def __init__(self, forename, surname, age, student_id, phone_number, email_address, password,):
        self.forename = forename
        self.surname = surname
        self.age = age
        self.student_id = student_id
        self.email_address = email_address
        self.phone_number = phone_number
        self.password = password
        self.module1 = None
        self.module2 = None
        self.student_points = 400.0

    def module_selection(self, module1, module2):  # module selection function
        self.module1 = module1
        self.module2 = module2

    def deposit(self, amount):
        self.student_points += amount

    def change_password(self, password_new):  # updates Password
        self.password = password_new
        print('\n\t\t\tPassword Changed To ', self.password)

    def change_email(self, email_address_new):  # updates Email Address
        self.email_address = email_address_new
        print('\n\t\t\tEmail Address Changed To ', self.email_address)

    def change_phone_number(self, phone_number_new):   # updates Phone number
        self.phone_number = phone_number_new
        print('\n\t\t\tPhone Number Changed To ', self.phone_number)

    def self_serve(self, amount):
        if self.student_points >= amount:
            self.student_points -= amount
            print("\n\t\t\t", amount,
                  "Has been removed from your account, your current balance is: ",
                  self.student_points)
        else:
            print("\n\t\t\tError Incorrect Funds For Purchase")

    def show_student_info(self):  # prints student info
        print('\n\t\t\tStudent ID-    ', self.student_id)
        print('\n\t\t\tForename-      ', self.forename)
        print('\n\t\t\tSurname-       ', self.surname)
        print('\n\t\t\tAge-           ', self.age)
        print('\n\t\t\tPhone Number-  ', self.phone_number)
        print('\n\t\t\tEmail Address- ', self.email_address)
        print('\n\t\t\t1st Module-    ', self.module1)
        print('\n\t\t\t2nd Module-    ', self.module2)
        print('\n\t\t\tStudent Points-', self.student_points)

    def overwrite_student_point_value(self, amount):
        self.student_points = amount


def enter_studentID_and_password():  # id/password enter function
    while True:
        try:
            student_id = int(input("\n\t\t\tPlease enter your student ID: "))
        except ValueError:
            print('\n\t\t\tStudent ID must be a number')
            continue
        else:
            break
    password = str(input("\n\t\t\t Please enter the password for this account"))
    return student_id, password


########################---- checking balance module----####################


def checking_balance():
    while (True):
        student_id, password = enter_studentID_and_password()
        if student_id in student_dic.keys():
            if student_dic[student_id].password == password:
                print("\n\t\t\tHello Mr/Ms", student_dic[student_id].surname, "your account balance is",
                      student_dic[student_id].student_points)
                break
            else:
                tempInput = str(input(print("""\n\t\t\tThe ID and password entered do not match, would you like to enter 
                                your details again? You will be returned to the main page if you say no:
                                y: Yes
                                n: No""")))
                if tempInput == 'y' or tempInput == 'Y':
                    pass
                elif tempInput == 'n' or tempInput == 'N':
                    break
                else:
                    print("\n\t\t\tPlease enter a valid input")
        elif student_id == 'Q' or student_id == 'q' or password == 'Q' or password == 'q':
            break


#################################### --- Shopping Module --- ######################################


def shopping(student_id):
    food_amt = 0
    printed_amt = 0
    t_cost = 0
    while True:
        print("""\n\t\t\tPlease Choose One Of The Following Options:
                                             1: Purchase Food (7.5 Points)
                                             2: Use Printer (1.5 Points)
                                             Q: Exit""")

        option = str(input("\n\t\t\tPlease Enter Your Option: "))

        if option == "1":
            while True:
                try:
                    food_amt = int(input("\n\t\t\tPlease enter how much food portions are needed: "))
                except ValueError:
                    print("\n\t\t\tError - Enter a Valid Amount")
                    continue
                if food_amt < 0:
                    print("\n\t\t\tError - Enter a Valid Amount")
                    continue
                else:
                    break

            f_cost = food_amt * 7.5
            t_cost = t_cost + f_cost
            student_dic[student_id].self_serve(f_cost)


        elif option == "2":
            while True:
                try:
                    printed_amt = int(input("\n\t\t\tPlease enter how many printed pages are needed: "))
                except ValueError:
                    print("\n\t\t\tError - Enter a Valid Amount")
                    continue
                if printed_amt < 0:
                    print("\n\t\t\tError - Enter a Valid Amount")
                    continue
                else:
                    break

            p_cost = printed_amt * 1.5
            t_cost = t_cost + p_cost
            student_dic[student_id].self_serve(p_cost)


        elif option == "Q" or option == "q":
            print("\n\t\t\t", t_cost, "has been removed from this account the new balance on this account is: ",
                  student_dic[student_id].student_points)
            if t_cost > 0:
                print("\n\t\t\tYou are entitled to a reward here is a coupon for ", random.randint(1, 100),
                      "% off your next purchase")
                return
            else:
                return

########################----student registration module----####################


def student_registration():
    # get student info
    forename = str(input("\n\t\t\tPlease enter your name: "))
    surname = str(input("\n\t\t\tPlease enter your last name: "))

    ########-- validation for age --########
    while (True):
        try:
            age = int(input("\n\t\t\tPlease enter your age: "))
        except ValueError:
            print("\n\t\t\tPlease enter a valid age")
            continue
        if age < 0:
            print("\n\t\t\tPlease enter a valid age")
            continue
        else:
            break

    ########-- validation for phone number --########
    while (True):
        phone_number = str(input("\n\t\t\tPlease enter your phone number: "))
        if len(phone_number) != 11 or phone_number.isdigit() != True:
            print("\n\t\t\tThat phone number is not valid, please enter a valid phone number")
            continue
        else:
            break

    ########-- validation for email --########
    while (True):
        email_address = str(input("\n\t\t\tPlease enter your email address: "))
        split = list(email_address)
        asciiValues = []
        asciiFound1 = False
        asciiFound2 = False
        for counter in range(len(split)):
            asciiValues.append(ord(split[counter]))
            if asciiValues[counter] == 64:
                asciiFound1 = True
            if asciiValues[counter] == 46:
                asciiFound2 = True
        if asciiFound1 == True and asciiFound2 == True:
            break
        else:
            print("\n\t\t\tPlease enter a valid email address")
            continue

    password = str(input("\n\t\t\tPlease enter your choice of password: "))

    # this loop checks the random generated account number is unique
    while (True):
        # ID's numbers are in a range of 1 to 10000
        ID = random.randint(1, 10000)
        if ID not in student_dic.keys():
            temp_object = StudentPage(forename=forename, surname=surname, age=age, student_id=ID,
                                      phone_number=phone_number, email_address=email_address, password=password)
            student_dic[ID] = temp_object
            print("\n\t\t\tMr/Ms", forename, surname, "Your account number is: ", ID)
            return student_dic
########################----main----######################################


student_dic = dict()  # dictionary

with open('students.csv', mode='r') as read_file:
    r = csv.reader(read_file)
    for rows in r:  # reads data into the dictionary
        try:
            id = int(rows[0])
            age =int(rows[3])
            student_points = float(rows[9])
            temp_object = StudentPage(forename=rows[1], surname=rows[2], age=age, student_id=id,
                                        phone_number=rows[5], email_address=rows[6], password=rows[4])
            student_dic[id] = temp_object
            while True:
                if rows[7] == "" and rows[8] == "":
                    break
                else:
                    student_dic[id].module_selection(rows[7], rows[8])
                    break
            student_dic[id].overwrite_student_point_value(student_points)
        except FileNotFoundError:
            break
        except IndexError:  # if csv empty stop the script from failing
            break
        else:
            continue


print("\n\t\t\tWelcome To The Self-Service Student System")

while True:
    print("""\n\t\t\tPlease Choose One Of The Following Options:
                     1: Student Registration
                     2: Module Selection
                     3: Top-Up Balance
                     4: Shopping
                     5: Display Balance
                     6: Change Account Information
                     7: Display Account Information
                     q: Exit""")
    option = str(input("\n\t\t\tPlease Enter Your Option: "))
    if option == "Q" or option == "q":
        write_list = []
        for keys in student_dic:  # turns dictionary into a list
            student = [student_dic[keys].student_id, student_dic[keys].forename, student_dic[keys].surname,
                       student_dic[keys].age, student_dic[keys].password, student_dic[keys].phone_number,
                       student_dic[keys].email_address, student_dic[keys].module1, student_dic[keys].module2,
                       student_dic[keys].student_points]
            write_list.append(student)
        with open("students.csv", mode='w', newline='') as write_file:  # open csv file in write mode
            w = csv.writer(write_file)
            w.writerows(write_list)  # writes to csv
        break
    elif option == "1":
       student_registration()
    elif option == "2":
        module_list = ["Programming 1", "Programming 2", "Networking 1", "Networking 2"]  # list of possible modules
        while True:  # runs a loop to check if ID and password match to student details
            id, password = enter_studentID_and_password()
            if id in student_dic.keys():
                if student_dic[id].password == password:
                    if student_dic[id].module1 == None and student_dic[id].module2 == None:
                        while True:
                            try:
                                module1 = int(input("\n\t\t\tFrom the following please choose a module by entering 0,1,2 or 3. [0 - Programming 1, 1 - Programming 2, 2 - Networking 1, 3- Networking 2]: "))
                                module2 = int(input("\n\t\t\tFrom the following please pick another module by entering 0,1,2 or 3. [0 - Programming 1, 1- Programming 2, 2- Networking 1, 3- Networking 2]: "))
                            except ValueError:
                                print("\n\t\t\tPlease enter a valid input")
                                continue
                            if module1 == module2:  # checks whether user has chosen the same module twice
                                print("\n\t\t\tYou cannot choose the same modules. Please pick another!")
                                continue
                            elif module1 < 0 or module1 > 3 or module2 < 0 or module2 > 3:
                                print('\n\t\t\tInput must be from the options above. Please try again.')
                                continue
                            else:
                                break
                        module1 = module_list[module1]  # takes from the list the users inputs
                        module2 = module_list[module2]  # takes from the list the users inputs
                        student_dic[id].module_selection(module1, module2)
                        print("\n\t\t\tYou have chosen the selected modules: ", module1, "&", module2)
                        break
                    else:
                        print("\n\t\t\tYou already have the selected modules chosen: ", module1, "&", module2)
                        break
                else:
                    print('\n\t\t\tPassword incorrect please try again.')
                    continue
            else:
                print('\n\t\t\tStudent ID incorrect please try again.')
                continue
    elif option == "3":
        while True:  # runs a loop to check if ID and password match to student details
            id, password = enter_studentID_and_password()
            if id in student_dic.keys():
                if student_dic[id].password == password:
                    while True:
                        try:
                            points = float(input("\n\t\t\tPlease enter amount of points you want to deposit in your account."))
                        except ValueError:
                            print("\n\t\t\tPlease enter a value")
                            continue
                        if points <= 0:
                            print('\n\t\t\tmust be more than 0')
                            continue
                        else:
                            break
                    print("\n\t\t\tYour ID: ", id, "Amount of points to deposit: ", points)
                    confirmation = input("\n\t\t\tContinue? Y/N: ").lower()
                    if confirmation == "y":

                        student_dic[id].deposit(points)
                        print("\n\t\t\t", points, "is added to your account and your current balance: ",
                              student_dic[id].student_points)
                        break
                    else:
                        print("\n\t\t\t No points added to your account!!!")
                        break
                else:
                    print('\n\t\t\tPassword incorrect please try again.')
                    continue
            else:
                print('\n\t\t\tStudent ID incorrect please try again.')
                continue
    elif option == "4":
        food_amt = 0
        printed_amt = 0
        t_cost = 0
        id, password = enter_studentID_and_password()
        if id in student_dic.keys():
            if student_dic[id].password == password:
                shopping(id)
            else:
                print('\n\t\t\tPassword incorrect please try again.')
                continue
        else:
            print('\n\t\t\tStudent ID incorrect please try again.')
            continue
    elif option == "5":
        checking_balance()
    elif option == "6":  # changing account information
        print('\n\t\t\tChange Account Information.')
        while True:
            id, password_temp = enter_studentID_and_password()  # gets id and password from enter_studentID_and_password function
            if id in student_dic.keys():
                if student_dic[id].password == password_temp:
                    while True:
                        print("""\n\t\t\tTo Please Choose From One Of The Following
                              1: Change Phone Number
                              2: Change Email Address
                              3: Change Password
                              r: Return To Main Menu""")
                        option_edit = str(input('\n\t\t\tPlease Enter Your Option'))  # user input option for this module
                        if option_edit == '1':  # change phone number
                            print('\n\t\t\tCurrent Phone Number Is', student_dic[id].phone_number)
                            while True:
                                phone_number_new = str(input('\n\t\t\tPlease Enter The New Phone Number '))  # user input new phone number
                                if len(phone_number_new) == 11 and phone_number_new.isdecimal():  # checks if is a valid phone number
                                    break
                                else:
                                    print('\n\t\t\tNot a Valid Phone Number Please enter Again')
                                    continue
                            print('\n\t\t\tChange Phone Number', student_dic[id].phone_number, 'to', phone_number_new, '?')
                            while True:
                                confirm = str(input('\n\t\t\tcontinue (Y/N)'))  # confirms change with user
                                if confirm == 'y' or confirm == 'Y':
                                    student_dic[id].change_phone_number(phone_number_new)  # updates phone number in the class
                                    break
                                elif confirm == 'n' or confirm == 'N':
                                    print('\n\t\t\tPhone Number Change Canceled')
                                    break
                                else:
                                    print('\n\t\t\tInvalid input')
                                    continue
                        elif option_edit == '2':  # change email address
                            print('\n\t\t\tCurrent Email Address Is', student_dic[id].email_address)
                            while True:
                                email_address_new = str(input('\n\t\t\tPlease Enter The New Email Address '))  # user input new email
                                if '@' and '.' in email_address_new:  # checks if is a valid email
                                    break
                                else:
                                    print('\n\t\t\tNot a valid Email Address Please Enter Again')
                                    continue
                            print('\n\t\t\tChange Email Address', student_dic[id].email_address, 'to', email_address_new, '?')

                            while True:
                                confirm = str(input('\n\t\t\tcontinue (Y/N)'))  # confirms change with user
                                if confirm == 'y' or confirm == 'Y':
                                    student_dic[id].change_email(email_address_new)  # updates email in the class
                                    break
                                elif confirm == 'n' or confirm == 'N':
                                    print('\n\t\t\tEmail Address Change Canceled')
                                    break
                                else:
                                    print('\n\t\t\tInvalid input')
                                    continue
                        elif option_edit == '3':  # change password
                            print('\n\t\t\tCurrent Password Is', student_dic[id].password)
                            password_new = str(input('\n\t\t\tPlease Enter The New Password'))  # input password
                            print('\n\t\t\tChange Password', student_dic[id].password, 'To', password_new, '?')
                            while True:
                                confirm = str(input('\n\t\t\tcontinue (Y/N)'))  # confirms change with user
                                if confirm == 'y' or confirm == 'Y':
                                    student_dic[id].change_password(password_new)  # updates password in the class
                                    break
                                elif confirm == 'n' or confirm == 'N':
                                    print('\n\t\t\tPassword Change Canceled')
                                    break
                                else:
                                    print('\n\t\t\tInvalid input')
                                    continue
                        elif option_edit == 'r' or option_edit == 'R':  # returns to main menu
                            print('\n\t\t\tReturning to Main Menu')
                            break
                        else:
                            print('\n\t\t\tNot a valid option')
                    break  # breaks from while loop
                else:
                    print('\n\t\t\tStudent ID or Password incorrect please try again.')
                    continue
            else:
                print('\n\t\t\tStudent ID or Password incorrect please try again.')
                continue
    elif option == "7":  # display account information
        print('\n\t\t\tDisplay Account Information')
        while True:
            id, password = enter_studentID_and_password()  # gets id and password from enter_studentID_and_password function
            if id in student_dic.keys():
                if student_dic[id].password == password:
                    student_dic[id].show_student_info()  # send user to display account info in class
                    while True:
                        return_to_main = input('\n\t\t\tenter r To Return To Main Menu')  # return to main menu
                        if return_to_main == 'r' or return_to_main == 'R':
                            break
                        else:
                            continue
                    break
                else:
                    print('\n\t\t\tStudent ID or Password incorrect please try again.')
                    continue
            else:
                print('\n\t\t\tStudent ID or Password incorrect please try again.')
                continue
    else:
        print('\n\t\t\tInvalid Option')
        continue