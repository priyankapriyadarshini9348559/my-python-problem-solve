#take addmission for Python
print("Welcome To Nareshit Technology")
name="priya"
password=123
#login 
students={}
attempt=0
for attempt in range(3):
    user_name=input("please enter your name:")
    user_pass=int(input("enter your password here"))
    if user_name == name and user_pass==password:
        print("welcome to NareshIt Technology")
        course=["python","java","Webtechnology"]
        print(course)
        user_choice=input("enter the couse you want to study:")
        if user_choice in course:
            print(f"heloo {user_name}you are intrest in {user_choice}")
            print("from which faculty you want to study?")
            faculty_lst=["Ravi verma","xyz","mr.zt","mr.sahu"]
            print(faculty_lst)
            user_want=input("Please enter the faculty name you want to study:")
            if user_want in faculty_lst:
                print(f"you want to training from {user_want} sir")
                print(f"{user_want} he is our most ineligent sir welcome you for his training session")
                some_ques=input("How do you want traing online\offline: ")
                if some_ques=='online':
                    print("welcome to online batch")
                else:
                    print("welcome to our offline batch")
                    
                    class_time={
                                 "Ravi verma":"6 P.m",
                                 "ravi verma":"9 a.m",
                                 "verma":"4p.m"
                    }
                    choice=input('Please mention your batch timing')
                    if choice in   class_time:
                             print(f"You want to join the {choice} batch.")
                             print('welcome to your 1st day at naresh it!')
                             print("here is some rule before you entery the class you have to show your id card")
                             more="y"
                             while more== "y":
                                 name=input('Enter your name!')
                                 age=input("enter your age")
                                 course=input("enter your course:")
                                 students[name]={"age":age , "course":course}
                                 more = input("Do you want to add another student? (y/n): ")
                             print("\n all students are:")
                             for s in students:
                                 print(s,":",students[s])
                                 
                             check = input("Enter student name to check valid or not: ")    
                            
                            
                             

                             
                             if check in students:
                                 print('you are a valid student')
                                 
                             else:
                                 print("you are not a valid student")

                    else:
                      print("Sorry, this time batch is not available.")

            else:
                print("please choose the faculty for your requirement") 
        else:
            print("please choose one of the course")  
        break
    else:
        remaing=3-attempt
        print(f"you have remaing attempt :{remaing}")
else:
    print("too many attempts inncorect !system take more time to restart")
    