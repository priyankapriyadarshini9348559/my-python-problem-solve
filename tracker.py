import csv
filename="expenses.csv"
def add_expence(name,amount):
    with open(filename,"a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([name,amount])
    print("✅ Expense added successfully!")   
def view_expence():

    try:

        with open(filename,"r") as file:
         reader=csv.reader(file)
         print("\n--- All Expenses ---")
         for row in reader:
             print(f"Item: {row[0]} | Amount: ₹{row[1]}")
    except FileNotFoundError:
        print("❌ No expenses found! Add something first.")


   
while True:
    print("\n 1. add expence")
    print('2.view expence')
    print("3.exit")
    choice=input("enter your choice:")
    if choice=="1":
        name = input("Enter expense name: ")
        amount = input("Enter amount: ")
        add_expence(name, amount)



    elif choice=="2":
        view_expence()



    elif choice=="3":
        print("👋 Exiting... Have a nice day!")
        break

    else:
        print("Invalid choice, try again!")
