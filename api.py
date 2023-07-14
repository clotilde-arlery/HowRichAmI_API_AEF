from fastapi import FastAPI
import uvicorn
from pathlib import Path
import pandas as pd

app = FastAPI()

data_path = Path("data_processed.json")
income_df = pd.read_json(data_path)


def get_percentile(income):
    """Give the position of someone in the world income distribution"""
    percentile = (
        income_df
        .query(f"threshold <= {income}")
        .percentile
        .tail(1).item()
    )
    return percentile

@app.get("/equivalent_household_size")
def get_equivalent_household_size(n_adults, n_children):
    """Get equivalent household size using the OECD modified scale"""
    first_adult_weight = 1
    other_adult_weight = 0.5
    child_weight = 0.3
    
    if n_adults <= 1:
        equivalent_household_size = (first_adult_weight * n_adults
                                     + child_weight * n_children)
    else:
        equivalent_household_size = (first_adult_weight * 1
                                     + other_adult_weight * (n_adults - 1)
                                     + child_weight * n_children)
    return equivalent_household_size


@app.get("/household_percentile")
def get_household_percentile(income, n_adults, n_children):
    """Get a household's position in the global income distribution
    
    Returns an integer corresponding to the percentile threshold that is
    right below the household's equivalised income. For example, if the
    function returns 91, it means that the household earns more than at
    least 91% of the world's population, and earns less than at least
    92%.
    """
    equivalent_household_size = get_equivalent_household_size(n_adults,
                                                              n_children)
    household_income = income / equivalent_household_size
    household_percentile = get_percentile(household_income)
    return household_percentile


@app.get("/post_donation_percentile")
def get_post_donation_percentile(income: int, donation:int):
    """Get the post-donation position in the income distribution"""
    post_deduction_donation = get_post_deduction_donation(income, donation)
    post_donation_income = income - post_deduction_donation
    post_donation_percentile = get_percentile(post_donation_income)
    return post_donation_percentile


@app.get("/post_deduction_donation")
def get_post_deduction_donation(income: int, donation: int):
    """Give the real amount of donation after tax exemption in (%)"""
    if donation < 0 or donation > 100:
        post_deduction_donation = 0
    else :
        eligibility_cap = 0.20 * income
        deduction_rate = 1-0.66
        eligible_amount = min((donation/100)*income, eligibility_cap)
        post_deduction_donation = ((eligible_amount * deduction_rate)/income)*100
        post_deduction_donation = round(post_deduction_donation, 2)
    return post_deduction_donation


if __name__ == '__main__':
    uvicorn.run(app='api:app', reload=True)
