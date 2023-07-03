# How rich am I ?
## Description
**API** for ***data processing*** on the ***French version of the "How rich am I ?"***   

The *goal* 💪 was also to ***update the data*** (original website data come from *2013 - 2015*)   

See the original project [here](https://howrichami.givingwhatwecan.org/how-rich-am-i "the original project")   

## Documentation
To get someone's position in world income distribution, depending on his/her income (it returns the percentile) :    

`[url]/income_positionning?income=[income]`

To get someone's position in the world income distribution with a given amount of donation (it returns the percentile) :

`[url]/post_donation_position?income=[income]&donation=[donation]`

To get the real amount of donation after tax exemption in (%) :

`[url]/tax_exempted_donation?income=[income]&donation=[donation]`

### Nota bene

Note that the ***donation*** is expected to be an ***integer between 0 and 100*** as well as the ***income is the annual post-tax household income in €*** and it's expected to be an ***integer***.
