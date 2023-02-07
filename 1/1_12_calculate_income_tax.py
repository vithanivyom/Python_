'''
Calculate income tax for the given income by adhering to the below rules

Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20


'''
def Tax_calculation(income):                            # defining function
    tax_payable = 0
    print("Given income", income)
    if income <= 10000:
        tax_payable = 0
    elif income <= 20000:
        x = income - 10000                               # no tax on first 10,000
        tax_payable = x * 10 / 100                       # 10% tax
    else:
        tax_payable = 0                                  # no tax on first 10,000

        tax_payable = 10000 * 10 / 100                   # next 10,000 10% tax

        tax_payable += (income - 20000) * 20 / 100       # remaining 20%tax

    print("Total tax to pay is", tax_payable)

income = 10001
c1 = Tax_calculation(income)                             # calling function
