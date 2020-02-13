import datetime
from datetime import timedelta

def countries(country_name,country_details,inr):
    '''
    Parameters
        country_name : string
        country_details : Dictionary (Key  : country_name, value : tuple(time_zone, time, currency, language, currency_rate))
        inr : int
        
        Returns : nothing
    '''
    for k,v in country_details.items():
        if k == country_name.upper():
            for i in range(0,len(v)):
                print("Country : {0}".format(k))
                print("Current time : {0} {1}".format(act_time(v[1]),v[0]))       
                print("Language : {0}".format(v[3]))
                print("Currency Value : {0}".format(v[4]))
                eq_curr = eval(str(inr) + "/" + v[4])
                print("Equivalent currency value for {0} INR : {1} {2}".format(inr,eq_curr,v[2]))
                break

def act_time(cur_timezone):
    '''
    Parameter : time 
    
    Return : actual_time
    '''
    cur_time = datetime.datetime.now()
    if '-' in cur_timezone:
        x_time = int(float(cur_timezone.split("-")[1])*60)
        actual_time = cur_time - timedelta(0,0,0,0,x_time)
    else:
        x_time = int(float(cur_timezone.split("+")[1])*60)
        actual_time = cur_time + timedelta(0,0,0,0,x_time)
    return actual_time

country=["UK","USA","INDIA","MEXICO","AUSTRALIA"]
time_zone=["GMT","EST","IST","CST","ADET"]
time=["GMT-5.5","EST-10.5","IST+0.0","CST-11.5","ADET+5.5"]
currency=['POUND','USD','INR','USD','AUD']
language=['ENGLISH','ENGLISH','HINDI','SPANISH','ENGLISH']
currency_rate=['92.72','71.32','1','71.32','47.73']

country_name = input("Enter country name from (UK, USA, MEXICO, AUSTRALIA) : ")      # input from user country_name : string
inr = int(input("Enter amount in INR : "))                                           # input from user money in INR : int

details = list(zip(time_zone, time, currency, language, currency_rate))     # zip function to group the items and placing values inside a list 
# print(l)
country_details = dict(zip(country, details))       # use of zip function and placing inside a Dictionary (Key : country_name, value : tuple(time_zone, time, currency, language, currency_rate))
# for k in country:
#     for v in l:
#         country_details[k] = v 
#         l.remove(v)
#         break
# print(country_details)
countries(country_name,country_details,inr)     # function call to display the country details





#=======================i/p======================================
# Enter country name from (UK,USA,MEXICO,AUSTRALIA):USA                                                                                            
# Enter amount in INR:700000     

#=======================o/p======================================
# Enter country name from (UK,USA,MEXICO,AUSTRALIA):USA                                                                                            
# Enter amount in INR:700000
# Country: USA 
# Current time : 2020-02-12 18:50:12.427208 EST 
# Language: ENGLISH                                                                                                                        
# Currency Value: 71.32 INR                                                                                                                
# Equivalent Currency value for 700000 INR : 9814.918676388112 USD  



#=======================i/p======================================
# Enter country name from (UK,USA,MEXICO,AUSTRALIA) : UK                                                                                                   
# Enter amount in INR : 100000

#=======================o/p======================================
# Enter country name from (UK,USA,MEXICO,AUSTRALIA) : UK                                                                                                   
# Enter amount in INR : 100000                                                                                                                             
# Country : UK  
# Current time : 2020-02-12 23:55:05.826263 GMT
# Language : ENGLISH                                                                                                                                       
# Currency Value : 92.72                                                                                                                                   
# Equivalent currency value for 100000 INR : 1078.515962036238 POUND 



