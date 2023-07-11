from fastapi import FastAPI
import uvicorn
import json
import platform
import os

app = FastAPI()

if platform.system() == 'windows':
    chemin = os.getcwd() + '\data_processed.json'
else:
    chemin = os.getcwd() + '/data_processed.json'

with open(chemin) as f:
    pre = f.read()
    income_distrib = json.loads(pre)

# give the position of someone in world income distribution : return the percentile
@app.get("/income_positionning")
def income_positionning(income: int):
    percentile = -1
    for i in range(len(income_distrib)):
        if income < income_distrib[i]["threshold"]:
            percentile = i
            break
    if percentile == -1:
        percentile = 100
    return percentile

# give the position of someone in the world income distribution with a given amount of donation : return the percentile
@app.get("/post_donation_position")
def post_donation_position(income: int, donation:int):
    r_donation = real_donation(income, donation)
    post_donation_income = income - r_donation
    new_income_positionning = income_positionning(post_donation_income)
    return new_income_positionning

#give the real amount of donation after tax exemption in (%)
@app.get("/tax_exempted_donation")
def real_donation(income: int, donation: int):

    if donation < 0 or donation > 100:
        real_donation = 0
    else :
        eligibility_cap = 0.20 * income
        deduction_rate = 1-0.66
        eligible_amount = min((donation/100)*income, eligibility_cap)
        real_donation = ((eligible_amount * deduction_rate)/income)*100
        real_donation = round(real_donation, 2)
    return real_donation



if __name__ == '__main__':
    uvicorn.run(app='api:app', reload=True)
