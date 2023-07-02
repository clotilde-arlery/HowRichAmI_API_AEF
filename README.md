# HowRichAmI_API_AEF
API for data processing on the French version of the "How rich am I ?"

[red] Documentation [\red]



To get the position of someone in world income distribution (it returns the percentile) :

[url]/income_positionning?income=[income]



To get the position of someone in the world income distribution with a given amount of donation (it returns the percentile) :

[url]/post_donation_position?income=[income]&donation=[donation]



To get the real amount of donation after tax exemption in (%) :

[url]/tax_exempted_donation?income=[income]&donation=[donation]



Note that the donation is expected to be an integer between 0 and 100 as well as the income is the annual post-tax household income in € and it's expected to be an integer.
