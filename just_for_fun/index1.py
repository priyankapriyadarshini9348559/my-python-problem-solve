print("Welcome To Nareshit Technology")

names = {
    "priya": 1234,
    "mama": 2345,
    "mamun": 3456
}

students = {}
attempt = 0

while attempt < 3:
    user_name = input("please enter your name: ")
    user_pass = int(input("enter your password here: "))

    if user_name in names and user_pass == names[user_name]:
        print("welcome to NareshIt Technology")

        course = ["python", "java", "Webtechnology"]
        print(course)
        user_choice = input("enter the course you want to study: ")

        if user_choice in course:
            print(f"Hello {user_name}, you are interested in {user_choice}")
            print("From which faculty you want to study?")
            faculty_lst = ["Ravi verma", "xyz", "mr.zt", "mr.sahu"]
            print(faculty_lst)
            user_want = input("Please enter the faculty name you want to study: ")

            if user_want in faculty_lst:
                print(f"You want training from {user_want} sir")
                print(f"{user_want} is our most intelligent faculty. He welcomes you for his training session.")
                some_ques = input("How do you want training? (online/offline): ")

                if some_ques == 'online':
                    print("Welcome to online batch")

                if some_ques == 'offline':
                    print("Welcome to our offline batch")

                    class_time = {
                        "Ravi verma": "6 P.M",
                        "xyz": "9 A.M",
                        "mr.zt": "4 P.M",
                        "mr.sahu": "7 P.M"
                    }

                    print("\nAvailable faculty timings:")
                    for i in class_time:
                        print(i, ":", class_time[i])

                    faculty_choice = input("\nPlease mention the faculty name for your batch timing: ")

                    if faculty_choice in class_time:
                        print(f"You want to join the {class_time[faculty_choice]} batch with {faculty_choice}.")
                        print('Welcome to your 1st day at NareshIT!')
                        print("Here are some rules: before entering the class, you have to show your ID card.")

                        more = "y"
                        while more == "y":
                            name = input('Enter your name: ')
                            age = input("Enter your age: ")
                            course = input("Enter your course: ")
                            students[name] = {"age": age, "course": course}
                            more = input("Do you want to add another student? (y/n): ")

                        print("\nAll students are:")
                        for s in students:
                            print(s, ":", students[s])

                        check = input("Enter student name to check valid or not: ")
                        if check in students:
                            print("You are a valid student")
                        if check not in students:
                            print("You are not a valid student")

                    if faculty_choice not in class_time:
                        print("Sorry, this time batch is not available.")

            if user_want not in faculty_lst:
                print("Please choose the faculty for your requirement")

        if user_choice not in course:
            print("Please choose one of the available courses")

        attempt = 3  # exit login loop after success

    if user_name not in names or user_pass != names[user_name]:
        remaining = 2 - attempt
        print(f"Incorrect username or password! You have {remaining} attempts left.")
        attempt = attempt + 1

if attempt >= 3 and (user_name not in names or user_pass != names[user_name]):
    print("Too many incorrect attempts! System will restart later...")