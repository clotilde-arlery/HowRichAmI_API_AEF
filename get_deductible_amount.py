def get_deductible_amount(income, donation_share):
    """Return the tax-deductible amount from a donation
    
    In France, donations below 20% of income are 66% tax-deductible.
    That means that the eligible amount is the whole donation if it is
    below the 20% cap, and just 20% of income otherwise.
    The actual deductible amount is 66% of the deductible amount, except
    if that value is lower than the income tax payed: you can't deduct
    more than what you pay. In that case, the deductible amount is equal
    to the income tax payed.
    """
    donation = donation_share * income
    income_tax = get_income_tax(income)
    eligibility_cap = 0.20 * income
    deduction_rate = 0.66
    
    eligible_amount = min(donation, eligibility_cap)
    deductible_amount = min(eligible_amount * deduction_rate, income_tax)
        
    return deductible_amount


def get_absolute_post_tax_donation(income, donation_share):
    absolute_pre_tax_donation = donation_share * income
    deductible_amount = get_deductible_amount(income, donation_share)
    absolute_post_tax_donation = absolute_pre_tax_donation - deductible_amount
    return absolute_post_tax_donation


def get_relative_post_tax_donation(income, donation_share):
    absolute_post_tax_donation = get_absolute_post_tax_donation(income,
                                                                donation_share)
    relative_post_tax_donation = absolute_post_tax_donation / income
    return relative_post_tax_donation


def get_absolute_pre_tax_donation(income, donation_share):
    absolute_post_tax_donation = donation_share * income
    income_tax = get_income_tax(income)
    eligibility_cap = 0.20 * income
    deduction_rate = 0.66
    multiplier = 1 / (1 - deduction_rate)
    
    multipliable_part = min(absolute_post_tax_donation,
                            eligibility_cap / multiplier)
    multiplied_donation = multipliable_part * multiplier
    maximum_deduction = multiplied_donation * deduction_rate
    deduction = min(maximum_deduction, income_tax)
    
    absolute_pre_tax_donation = absolute_post_tax_donation + deduction
    return absolute_pre_tax_donation


def get_relative_pre_tax_donation(income, donation_share):
    absolute_pre_tax_donation = get_absolute_pre_tax_donation(income,
                                                              donation_share)
    relative_pre_tax_donation = absolute_pre_tax_donation / income
    return relative_pre_tax_donation


# Test 
def get_income_tax(income):
    return 0.1 * income

get_relative_post_tax_donation(100, 0.10)
get_relative_pre_tax_donation(100, 0.034)

get_relative_pre_tax_donation(100, 0.10)
get_relative_post_tax_donation(100, 0.20)


def get_income_tax(income):
    return 0.3 * income

get_relative_post_tax_donation(100, 0.10)
get_relative_pre_tax_donation(100, 0.034)

get_relative_pre_tax_donation(100, 0.10)
get_relative_post_tax_donation(100, 0.232)
