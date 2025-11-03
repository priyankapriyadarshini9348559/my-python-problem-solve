card_number=input("enter your card number:")
pin_num=int(input("enter your pin number:"))
if len(card_number)==16:
    if card_number.startswith("7787") and card_number.endswith("0018"):
        if pin_num==9907:
            print("plese select method 1.withdraw 2.deposit 3.balanace_check")
            user_input=int(input("enter your chocice:"))
            if user_input==1:
                print("user want to withdraw money")
                print("from which account you want to withdraw money current account or savings account:")
                user_choice=input("please select one method")
                if user_choice=="savings account":
                    print("withdraw the money from savings account")
                    print("please enter the amount:")
                    amount=int(input(" amount: "))
                    if amount==100:
                        print("₹100")
                    elif amount==200:
                        print("₹200")
                    elif amount==500:
                        print("₹500")
                    elif amount==1000:
                        print("₹1000")
                    else:
                        print("money out of range")

                
                else:
                    print("withdraw the money from current account")
                    amount=int(input(" amount: "))
                    if amount==100:
                        print("₹100")
                    elif amount==200:
                        print("₹200")
                    elif amount==500:
                        print("₹500")
                    elif amount==1000:
                        print("₹1000")
                    else:
                        print("money out of range")
            elif user_input==2:
                print("you want to deposit the money")
            elif user_input==3:
                print("you want to check your account balance")
                print("your current account balance is:9999.45")
            else:
                print("please select one option")
        else:
            print("incorrect pin number!")
    else:
       print ("please check your card_number")
else:
    print("invalid card")
        
