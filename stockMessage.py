from nsetools import Nse
from twilio.rest import Client

client = Client("XXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXX")
nse = Nse()





stocks = {
            "itc" : 287.95,
    "suzlon"   : 19.5,"idfcbank":55.4
    }

#stock name and quantity of stocks     
qty = {
        "itc" : 7,
        "suzlon"   : 50,"idfcbank":20
    }
    
    
stock1      = nse.get_quote('itc')
stock1Close = stock1['closePrice']
    

stock2      = nse.get_quote('suzlon')
stock2Close = stock2['closePrice']
    
    
stock3      = nse.get_quote('IDFCBANK')
stock3Close = stock3['closePrice']
    
    ### SBIN
    #stock4      = nse.get_quote('SBIN')
    #stock4Close = stock4['closePrice']
actual_value=((stocks['itc']*qty['itc'])+(stocks['suzlon']*qty['suzlon'])+(stocks['idfcbank']*qty['idfcbank']))
current_value = (stock1Close * qty['itc']) + (stock2Close * qty['suzlon'])+(stock3Close*qty['idfcbank'])
losses=actual_value-current_value
if(actual_value<current_value):
    print("profit")
    print(stock1Close)
    print(stock2Close)
    print(stock3Close)
    print(actual_value-current_value)
    print(actual_value)
    print(current_value)
    print(losses)
    losses=actual_value-current_value
    client.messages.create(to="+919738666329", 
                               from_="+1 206-202-8553 ", 
                               body="loss"+str(losses)
                               +"current value"+str(current_value)+" SUZLON="+str(stock1Close)+" ITC="+str(stock2Close)+" IDFCBANK="+str(stock3Close))
else:
    profit=current_value-actual_value
    client.messages.create(to="+919738666329", 
                               from_="+1 206-202-8553", 
                               body="Profit"+str(profit)
                               +"current value"+str(current_value)+" SUZLON="+str(stock1Close)+" ITC="+str(stock2Close)+" IDFCBANK="+str(stock3Close))
    print("loss")
    print(stock1Close)
    print(stock2Close)
    print(stock3Close)
    print(actual_value-current_value)
    print(actual_value)
    print(current_value)
    print(losses)
    
   
