# Description: One Stop Insurance Company - Main Program for new customers' policy information
# Author: Harini Manohar
# Dates: July 15 - July 26, 2024


# PROGRAM IMPORTS
from datetime import datetime
import time
import sys
from FormatValues import FNumber, FDate

# PROGRAM FUNCTIONS:
def read_defaults(file_path='Const.dat'):
    defaults = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            defaults[key] = float(value) if '.' in value else int(value)
    return defaults

def validate_province(Province):
    valid_provinces = ["ON", "QC", "NS", "NB", "MB", "BC", "PE", "SK", "AB", "NL"]
    return Province in valid_provinces

def validate_payment_method(PaymentMethod):
    valid_methods = ["Full", "Monthly", "Down Pay"]
    return PaymentMethod in valid_methods

def collect_claims():
    claims = []
    while True:
        claim_number = input("Enter claim number (or 'done' to finish): ")
        if claim_number.lower() == 'done':
            break
        claim_date = input("Enter claim date (YYYY-MM-DD): ")
        claim_amount = float(input("Enter claim amount: "))
        claims.append({'number': claim_number, 'date': claim_date, 'amount': claim_amount})
    return claims

def display_claims(claims):
    print("Claim #  Claim Date        Amount")
    print("---------------------------------")
    for claim in claims:
        print(f" {claim['number']}    {claim['date']}     {FNumber(claim['amount'])}")
    print("---------------------------------")


def SaveData(iteration, total, prefix='', suffix='', length=30, fill='█'):
# Generate and display a progress bar with % complete at the end.
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

    default_values['policy_number'] += 1  # Increment policy number after saving

def calculate_total_extra_costs(extra_liability, glass_coverage, loaner_car):
    total_extra_costs = 0
    if extra_liability == 'Y':
        total_extra_costs += default_values['cost_extra_liability']
    if glass_coverage == 'Y':
        total_extra_costs += default_values['cost_glass_coverage']
    if loaner_car == 'Y':
        total_extra_costs += default_values['cost_loaner_car']
    return total_extra_costs

def calculate_total_insurance_premium(basic_premium, num_cars, discount, total_extra_costs):
    if num_cars > 1:
        additional_cost = basic_premium * discount * (num_cars - 1)
    else:
        additional_cost = 0
    return basic_premium + additional_cost + total_extra_costs

def calculate_hst(total_premium, hst_rate):
    return total_premium * hst_rate

def calculate_total_cost(total_premium, hst, processing_fee=None):
    total_cost = total_premium + hst
    if processing_fee:
        total_cost += processing_fee
    return total_cost

def calculate_monthly_payment(total_cost, down_payment, months=8):
    remaining_balance = total_cost - down_payment
    return remaining_balance / months

def get_claims():
    #Prompts the user to enter claims and returns a list of claim dictionaries.
    claims = []
    while True:
        try:
            claim_number = int(input("Enter your previous claim number (or type '0' to finish): "))
            if claim_number == 0:
                break
            claim_date = input("Enter previous claim date (YYYY-MM-DD): ")
            claim_amount = float(input("Enter previous claim amount: "))
            claims.append({
                "claim_number": claim_number,
                "claim_date": FDate(datetime.strptime(claim_date, "%Y-%m-%d")),
                "amount": claim_amount,
                "amount_display": FNumber(claim_amount)
            })
        except:
            print(f"Error. Please enter a valid input for previous claims")
    return claims

claims = collect_claims()

# Load default values
default_values = read_defaults()

# USER INPUTS:
print()
Message = "Saving previous claims data... Please wait to enter new policy details."
for _ in range(5): # Change to control no. of 'blinks'
    print(Message, end='\r')
    time.sleep(.5) # To create the blinking effect
    sys.stdout.write('\033[2K\r') # Clears the entire line and carriage returns
    time.sleep(.5)

while True:
    print()
    while True:
        CustFirst = input("Enter the customer's first name (END to quit): ").title()
        if CustFirst == "":
            print("Entry Error - first name must be entered.")
            print()
        else:
            break
    if CustFirst.upper() == "END":
        print("Exiting. Have a nice day!")
        break

    while True:
        CustLast = input("Enter the customer's last name: ").title()
        if CustLast == "":
            print("Entry Error - last name must be entered.")
            print()
        else:
            break

    while True:
        Phone = input("Enter the customer's phone number(9999999999): ")
        if Phone == "":
            print("Entry Error - phone number must be entered.")
            print()
        elif len(Phone) != 10:
            print("Entry Error - phone number must be 10 digits.")
            print()
        else:
            break

    StAdd = input("Enter your street address: ").title()
    City = input("Enter your city: ").title()
    Province = input("Enter your province (XX): ").upper()
    while not validate_province(Province):
        print("Invalid province. Please enter a valid province.")
        Province = input("Enter province again: ").upper()
    PostalCode = input("Enter your postal code: ").upper()
    
    NumCars = input("Enter the number of cars being insured: ")
    NumCars = int(NumCars)

    Liability = input("Extra liability (Y/N): ").upper()
    if Liability == "Y":
        LiabilityDsp = "Yes"
    elif Liability == "N":
        LiabilityDsp = "No"

    GlassCoverage = input("Glass coverage (Y/N): ").upper()
    if GlassCoverage == "Y":
        GlassDsp = "Yes"
    elif GlassCoverage == "N":
        GlassDsp = "No"

    LoanerCar = input("Loaner car (Y/N): ").upper()
    if LoanerCar == "Y":
        LoanerDsp = "Yes"
    elif LoanerCar == "N":
        LoanerDsp = "No"

    PaymentMethod = input("Enter payment method (Full, Monthly, Down Pay): ").title()
    while not validate_payment_method(PaymentMethod):
        print("Invalid payment method. Please enter a valid method.")
        PaymentMethod = input("Enter payment method again: ").title()
    down_payment = 0
    if PaymentMethod == "Down Pay":
        down_payment = float(input("Enter the amount of the down payment: "))

    # PROGRAM CONCATENATION:
    CustName = CustFirst + " " + CustLast
    CustPhone = "(" + Phone[0:3] + ")" + Phone[3:6] + "-" + Phone[6:10]
    Address = StAdd + "," + " " + City + "," + " " + Province + "," + " " + PostalCode

    # PROGRAM CALCULATIONS:
    total_extra_costs = calculate_total_extra_costs(Liability, GlassCoverage, LoanerCar)
    total_premium = calculate_total_insurance_premium(default_values['basic_premium'], NumCars, default_values['discount_additional_cars'], total_extra_costs)
    hst = calculate_hst(total_premium, default_values['hst_rate'])
    total_cost = calculate_total_cost(total_premium, hst)
    monthly_payment = calculate_monthly_payment(total_cost, down_payment)

    # PROGRAM FORMATS:
    # Dollar Values:
    total_extra_costs_display = FNumber(total_extra_costs)
    total_premium_display = FNumber(total_premium)
    hst_display = FNumber(hst)
    total_cost_display = FNumber(total_cost)
    monthly_payment_display = FNumber(monthly_payment)

    # Dates:
    CurDate = datetime.now()
    FCurDate = FDate(CurDate)
    if CurDate.month == 12:
        NewDate = datetime(year=CurDate.year + 1, month=1, day=1)
    else:
        NewDate = datetime(year=CurDate.year, month=CurDate.month + 1, day=1)
    FNewDate = FDate(NewDate)


    # PROGRAM OUTPUT:

    print()
    print("-----------------------------------------------------")
    print(f"             One Stop Insurance Company")
    print(f"           New Customer Policy Information")
    print(f"                    {FCurDate}")
    print("-----------------------------------------------------")
    print(f"Name: {CustName:<13s}      Phone Number: {CustPhone}")
    print(f"Full Address: {Address:<30s}")
    print(f"Policy Number: {default_values['policy_number']:<4d}       Cars Insured: {NumCars:<3d}")
    print("-----------------------------------------------------")
    print(f"Extra Liability: {LiabilityDsp:<3s}       Glass Coverage: {GlassDsp:<3s}")
    print(f"Loaner Car     : {LoanerDsp:<3s}       Payment Method: {PaymentMethod}")
    print("-----------------------------------------------------")
    print(f"                  Total Extra Costs :  {total_extra_costs_display:>10s}")
    print(f"                  Total Premium     :  {total_premium_display:>10s}")
    print(f"                                       ----------")
    print(f"                  HST @ 15%         :  {hst_display:>10s}")
    print(f"                                       ----------")
    print(f"                  Total Cost        :  {total_cost_display:>10s}")
    print(f"                                       ----------")
    if PaymentMethod == "Monthly":
        print(f"                  Monthly Payment   :  {monthly_payment_display:>10s}")
    elif PaymentMethod == "Down Pay":
        print(f"                  Balance Monthly   :  {monthly_payment_display:>10s}")
    print(f"                                       ----------")
    print(f"**********First Payment Date: {FNewDate:>10s}**********")
    print()
    print(f"Previous Claims Details:")
    print()
    display_claims(claims)
    print()
    TotalIterations = 30 
    Message = "Saving Policy Data ..."
    for i in range(TotalIterations + 1):
        time.sleep(0.2) 
        SaveData(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
    print()


    print("Successfully Saved! Welcome to One Stop Insurance Family!")
    print()
    Continue = input("Do you want to add another policy? (Y / N): ").upper()
    if Continue == "N":
        break
    print()

# HOUSEKEEPING:
print()
print("Thank you. Your Insurance Policy has been mailed to your address. Have a nice day.")
print()