import csv
import os

while True:
    try:
        income = float(input("Enter your monthly income: "))

        if income < 0:
            print("Income cannot be negative. Try again.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

expenses={}
budget={}
while True :
    category=input("enter budget category(or 'done' to finish):")
    if category.lower()=="done":
        break

    limit= float(input("enter budget limit for "+category+":" ))
    budget[category]=limit

while True:
    category = input("enter expense category (or 'done' to finish):")
    
    if category.lower()=="done":
        break

    while True:
        try:
            amount = float(input("enter expense amount:"))
            if amount < 0:
                print("expense cannot be negative.  try again.")
                continue
            break
        except ValueError:
            print("please enter a valid number.")

    if category in expenses:
        expenses[category]+=amount
    else:
        expenses[category]=amount

total_expenses=sum(expenses.values())
savings = income-total_expenses

print("---Monthly Budget Report---",end="\n")
print("Income: Rs.",income)

for category,amount in expenses.items():
    print(category,"Rs.",amount)

    if category in budget:
        if amount>budget[category]:
            print("warning! You exceeded your",category,"budget!")
        else:
            print("you are within your",category,"budget.")

print("Total Expenses: Rs.",total_expenses)
print("Remaining savings: Rs.",savings)

file_exists = os.path.exists("budget_report.csv")

with open("budget_report.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists or os.path.getsize("budget_report.csv") == 0:
        writer.writerow(["Category", "Budget Limit", "Actual Expense"])

    for category, amount in expenses.items():
        limit = budget.get(category, 0)
        writer.writerow([category, limit, amount])

print("Expense report saved successfully!")

    

if savings<0:
    print("Warning: You exceeded your income!")
else:
    print("Budget Report Completed!")
