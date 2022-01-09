# Loan Analyzer Tool with Automated Calculations

import csv
from pathlib import Path

#A list called loan_costs is represented below with each loan's respective cost

loan_costs = [500, 600, 200, 1000, 450]

#The following script prints the total number of loans in the list

total_number_of_loans = len(loan_costs)
print(f"There are {total_number_of_loans} loans")

# The following script prints the Sum of all loans

total_of_all_loans = sum(loan_costs)
print(f"The total amount between all loans is ${total_of_all_loans}")

# Thew following script prints the average loan cost amongst all loans in the list

average_loan_amount = total_of_all_loans / total_number_of_loans
print(f"The average loan amount is ${average_loan_amount}")



# Below is a dictionary input of key valued pairs representing specific information for a given loan.

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# The following script extracts the Future Value and Remaining Months on the loan.

future_value = loan.get("future_value", 1000)
remaining_months = loan.get("remaining_months", 9)
print(f"The future value is ${future_value}, and there are {remaining_months} months remaining")

# The following calculation prints the present value of the loan.

present_value = future_value / (1+(0.2/12)) ** remaining_months
print(f"The fair value is ${present_value}")

# The following conditional statement determines if the loan is worth the cost to purchase.

loan_price = loan.get("Loan_price", 500)
if present_value >= loan_price:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive")


# The following dictionary is a key valued pair representing information for a new loan. 
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# The following script defines a function for calculating the present value of a loan given its key valued pairs in a dictionary. 

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1+(annual_discount_rate/12)) ** remaining_months
   # print(f"The present value is ${present_value}")
    return present_value

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


# The following script uses the new defined function, calculate_present_value, to calculate the present value of the new_loan given the discount rate of 20%.

new_loan_present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], 0.2)
print(f"The present value of the new loan is ${new_loan_present_value}")


#The following list, called loans, is comprised of dictionary inputs of key valued pairs. 

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# The following scripte creates a new, empty list called inexpensive_loans. 

inexpensive_loans = []

# The following script loops through all the loans and adds any loan with a cost less than or equal to $500 to the new list inexpensive_loans, and then prints the results.

for price in loans:
    if price["loan_price"] <= 500:
        inexpensive_loans.append(price)

print(inexpensive_loans)


# The follwoing steps are used to create a CSV file of the inexpensive_loans. The first step is to set the header.

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# The next step is to set the output path

csvpath = Path("inexpensive_loans.csv")

print("Writing the data to a CSV file...")

# The following writes the header and the inputs from the inexpensive list

with open(csvpath, "w") as csvfile:
    # Create a csvwriter
    csvwriter = csv.writer(csvfile, delimiter=",")

    #Write the header to the CSV file
    csvwriter.writerow(header)

    #Write the values of each dictionary inside of "inexpensive_loans"
    for item in inexpensive_loans:
        csvwriter.writerow(item.values())

#The loan_analyzer is complete.