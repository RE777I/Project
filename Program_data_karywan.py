import csv , re
#This program is very adaptive, you could change most of the parameters to your need 

# Parameters
title = ["Name", "ID", "Gender", "Department", "Position", "Salary"] #To check title
int_data = ["Salary"] #Data listed hear can only take interger
non_capitalize_data = ["ID"] # Data listed hear can't be Int or Gender
Negative_Value = False #True mean int_data could be negative and Vise versa
file_name = "Employee_data.csv" # File name
regularExp = re.compile(",") # Don't delete comma
wellcome_text = "Wellcome to employee data"
main_data = []

def reading_data () :
    try :
        with open(file_name, mode="r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                main_data.append(row)
            csv_file.close()
        print("File Found")
        
    except FileNotFoundError :
        print("File not found \nCreating new file...")
        with open(file_name, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(title)
            csv_file.close()
        print("File Created\n\nReading file again...")
        reading_data()

def Saved_data():
    with open("Employee_data.csv", mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerows(main_data)
        csv_file.close()

def checking_title ():
    repeater = 0
    checker = 0
    print("Checking Title...")
    for data in main_data[0]:
        if data == title[repeater] and checker == 0:
            repeater += 1
        else:
            while checker == 0:
                print("\nFile is not in the correct format")
                chose = input("If the data not fix the program will exit \nDo you want to fix the data (y/n) : ")
                if chose.lower() == "y":
                    checker = 1
                    main_data[0] = title
                    Saved_data()
                    break   
                elif chose.lower() == "n":
                    exit()
                else:
                    print("Please chose y or n")
    if repeater == 6:
        print("Title is in the correct format")
    else :
        print ("Recovery Successed")

def delete_data ():
    if len(main_data) > 1:
        while True:
            Num = input(f"Enter the data number you want to delete : 1 - {len(main_data)-1} and type {len(main_data)} to exit : ")
            if Num.isdigit() == True:
                Num = int(Num)
                if Num == 0:
                    print("Title can't be deleted")
                elif Num <= len(main_data)-1 :
                    main_data.remove(main_data[Num])
                    print ("Data Deleted Successfully")
                    if len(main_data) == 1:
                        print("Data is empty")
                    elif Num == len(main_data):
                        print("Last Data Deleted")
                        pass
                    else:
                        print(f"The {Num} data will be : \nNo : {Num}  [ " + ", ".join(main_data[Num]) + "]")
                    break
                elif Num == len(main_data):
                    break
                else:
                    print("There is no data with that number")
            else:
                print("Please enter a number")
    else:
        print("There is no data to be deleted")

def print_all_data ():
    Num = 1
    for data in main_data:
        if data[0] == title[0]:
            print("\nTitle = [" + ", ".join(data) + "]")
            continue
        else :
            print(f"No : {Num}  [ " + ", ".join((data)) + "]")
        Num += 1

def sort_data ():
    main_data.remove(main_data[0])
    main_data.sort()
    main_data.insert(0, title)
    print("Data Sorted")

def create_data ():
    input_data = []
    for data in range(0,len(title)):
        if title[data].capitalize() == "Gender":
            Gender = input ("Enter Gender : ")
            while Gender.lower() not in ["male", "female", "other"] or regularExp.search(Gender) != None:
                print ("Gender must be male, female or other and cannot have comma[,]")
                Gender   = input ("Enter Gender Again : ")
            input_data.append(Gender.capitalize())
        elif title[data] in int_data :
            while True:
                Salary   = input (f"Enter {title[data]} : ")
                try :
                    Salary = float(Salary)
                    if Salary < 0 and Negative_Value == False:
                        print(f"{title[data]} cannot be below zero")
                        continue
                    Salary = str(Salary)
                    break
                except:
                    print ("Salary must be number and cannot be below zero")
            input_data.append(Salary)
        elif title[data] in non_capitalize_data:
            prompt = input(f"Enter {title[data]} : ")
            while prompt == "" or prompt.isspace() or regularExp.search(prompt) != None:
                print(f"{title[data]} cannot be empty or has comma[,] ")
                prompt = input (f"Enter {title[data]} : ")
            input_data.append(prompt)
        else:
            prompt = input(f"Enter {title[data]} : ")
            while prompt == "" or prompt.isspace() or regularExp.search(prompt) != None:
                print(f"{title[data]} cannot be empty or has comma[,] ")
                prompt = input (f"Enter {title[data]} : ")
            input_data.append(prompt.capitalize())
                
    main_data.append(input_data)
    print("Data Created")
    

def change_data ():
    while len(main_data) > 1:
        Num_data = input(f"Enter the data number you want to change : 1 - {len(main_data) - 1} : ")
        if Num_data.isdigit():
            Num_data = int(Num_data)
            if Num_data not in [i for i in range(1, len(main_data) )]:
                print (f"Number must be in range 1 - {len(main_data) - 1}" )
                continue
            print(f"\nThe data that you choose to change is : [{", ".join(main_data[Num_data])}]")
            while True:
                for i in range(0,len(title)):
                    print(f"{i+1}. {title[i]} : {main_data[Num_data][i]}")
                print(f"{len(title) + 1}. to exit ")
                selection = input(f"Select the data you want to change 1-{len(title)} or {len(title) + 1} to exit : ")
                if selection.isdigit():
                    selection = int(selection)                
                    if selection == (len(title) + 1):
                        break
                    elif title[selection-1].capitalize() == "Gender":
                        Gender = input ("Enter New Gender : ")
                        while Gender.lower() not in ["male", "female", "other"]:
                            print ("Gender must be male, female or other")
                            Gender   = input ("Enter Gender Again : ")
                        main_data[Num_data][selection - 1] = Gender.capitalize()

                    elif title[selection-1] in int_data:
                        while True:
                            New_num   = input (f"Enter New {title[selection - 1]} : ")
                            try :
                                New_num = float(New_num)
                                if New_num < 0 and Negative_Value == False:
                                    print(f"{title[selection - 1]} cannot be below zero")
                                    continue
                                New_num = str(New_num)
                                main_data[Num_data][selection - 1] = New_num
                                break
                            except:
                                print (f"{title[selection - 1]} must be number")

                    else :
                        prompt = input(f"Enter New {title[selection - 1]} : ")
                        while prompt == "" or prompt.isspace() or regularExp.search(prompt) != None:
                            print(f"{title[selection - 1]} cannot be empty or has comma[,] ")
                            prompt = input (f"Enter New {title[selection - 1]} : ")
                        if title[selection - 1] in non_capitalize_data:
                            main_data[Num_data][selection - 1] = prompt
                            continue
                        main_data[Num_data][selection - 1] = prompt.capitalize()
                else :
                    print("Please enter the showned numbers")
                    continue
            break
        else:
            print("Please enter a number")
        # selection = input("1. Name \n2. ID \n3. Gender \n4. Department \n5. Position \n6. Salary \nSelect the data you want to change 1-6 : ")
    else :
        print("There isn't any data")

#searching from all
def searching_data ():
    print("Searching Data :")
    indicator = 0
    first_search = 0
    while True:
        if indicator == 0 and first_search == 1:
            print("No data was found")
        elif indicator >= 1 and first_search == 1:
            print (f"Founded {indicator} Data")
        else :
            pass
        indicator = 0
        first_search += 1
        for word in title:
            print(f'{title.index(word) + 1}. {word}')
        print (f"{len(title) + 1}. back ")
        search = input(f"Enter the data you want to search from 1 - {len(title)} and {len(title) + 1} to back: ")
        if search == str(len(title) + 1):
            break
        elif search.isdigit():
            search = int(search)
            holder = []
            for data in range(1,len(main_data)):
                holder.append(main_data[data][search-1])
            if title[search - 1] in int_data:
                while True:
                    if title[search - 1] in int_data:
                        print("Searching \n1. >= [more than equal] \n2. <= [less than equal] \n3. = [equal] \n4. Back")
                        input_search = input(f"Choose the following data you want to search 1 - 3 : ")
                        if input_search.isdigit() and int(input_search) in [1,2,3]:
                            value = input("Enter the value you want to search : ")
                            try:
                                value = float(value)
                                match input_search:
                                    case "1":
                                        repeater = 0
                                        for number in main_data[1:]:
                                            repeater += 1
                                            if float(number[search-1]) >= value:
                                                print(f"No. {repeater}  = [ " + ", ".join(number) + "]")  
                                                indicator += 1                     
                                    case "2":
                                        repeater = 0
                                        for number in main_data[1:]:
                                            repeater += 1
                                            if float(number[search-1]) <= value:
                                                print(f"No. {repeater}  = [ " + ", ".join(number) + "]")
                                                indicator += 1
                                    case "3":
                                        repeater = 0
                                        for number in main_data[1:]:
                                            repeater += 1
                                            if float(number[search-1]) == value:
                                                print(f"No. {repeater}  = [ " + ", ".join(number) + "]")  
                                                indicator += 1        
                            except:
                                print("Value must be number")
                                continue
                        elif input_search == "4":
                            break
                        else :
                            print("please enter the correct value")
            else :
                input_search = input(f"Enter the {title[search - 1]} you want to search : ")
                if title[search - 1] in non_capitalize_data:
                    if input_search in holder:
                        repeater = 0
                        for main_search in main_data:
                            if input_search in main_search :
                                print(f"No. {repeater}  = [ " + ", ".join(main_search) + "]")
                                indicator += 1
                            repeater += 1
                else:
                    if input_search.capitalize() in holder:
                        repeater = 0
                        for main_search in main_data:
                            if input_search.capitalize() in main_search :
                                print(f"No. {repeater}  = [ " + ", ".join(main_search) + "]")
                                indicator += 1
                            repeater += 1 
        else :
            print("\nPLEASE ENTER SHOWED NUMBERS\n")
            continue

def main ():
    reading_data()
    checking_title()
    while True:
        print(f"=================  {wellcome_text} =================")
        sel = input("1. Print all data \n2. Create Data \n3. Change Data \n4. Delete Data \n5. Search Data \n6. Sort data \n7. Save and Exit \n8. Exit Only\nSelect your option : ")
        if sel.isdecimal():
            sel = int(sel)
            match sel:
                case 1:
                    print_all_data()
                case 2:
                    create_data()
                case 3:
                    change_data()
                case 4:
                    delete_data()
                case 5:
                    searching_data()
                case 6:
                    sort_data()
                case 7:
                    Saved_data()
                    print("\n\n ================= Thank you for using this program =================\n\n\n")
                    break
                case 8:
                    print("\n\n ================= Thank you for using this program =================\n\n\n")
                    break
                case _:
                    print("\nPlease Enter Showed Number !!!\n")
                    continue
        else :
            print("\nPlease Enter A Number !!!\n")
            continue

#Start The Program
main()
