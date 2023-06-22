def get_deductible_amount(donation, income):
    """Return the tax-deductible amount from a donation
    
    In France, donations below 20% of income are 66% tax-deductible.
    That means that the eligible amount is the whole donation if it is
    below the 20% cap, and just 20% of income otherwise.
    The actual deductible amount is 66% of the deductible amount, except
    if that value is lower than the income tax payed: you can't deduct
    more than what you pay. In that case, the deductible amount is equal
    to the income tax payed.
    """
    income_tax = get_income_tax(income)
    eligibility_cap = 0.20 * income
    deduction_rate = 0.66
    
    eligible_amount = min(donation, eligibility_cap)
    deductible_amount = min(eligible_amount * deduction_rate, income_tax)
        
    return deductible_amount


# Test 
def get_income_tax(income):
    return 0.1 * income

get_deductible_amount(0, 100)
get_deductible_amount(5, 100)
get_deductible_amount(10, 100)
get_deductible_amount(11, 100)
get_deductible_amount(20, 100)
get_deductible_amount(21, 100)

def get_income_tax(income):
    return 0.3 * income

get_deductible_amount(0, 100)
get_deductible_amount(5, 100)
get_deductible_amount(10, 100)
get_deductible_amount(20, 100)
get_deductible_amount(21, 100)