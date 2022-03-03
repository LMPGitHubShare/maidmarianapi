import urllib.request
import json

enpoints = "https://maidmarian.azurewebsites.net"

def createaccount(name, password, apikey):
    return urllib.request.urlopen(enpoints + "/Api/CreateAccount?accountId=" + name +"&password="+ password + "&apiKey=" + apikey, data={}).read()

def getaccount(name, password, apikey):
    return json.loads(urllib.request.urlopen(enpoints + "/Api/GetAccount?accountId=" + name +"&password="+ password + "&apiKey=" + apikey, data={}).read())

def buy(name, ticker, fraction, password, apikey):
    return json.loads(urllib.request.urlopen(enpoints + "/Api/Buy?accountId=" + name + "&symbole=" + ticker + "&fraction=" + fraction +"&password="+ password + "&apiKey=" + apikey, data={}).read())

def sell(name, stockid, password, apikey):
    return json.loads(urllib.request.urlopen(enpoints + "/Api/Sell?accountId=" + name + "&stockId=" + stockid  +"&password="+ password + "&apiKey=" + apikey, data={}).read())
    
def stocksummary(ticker, apikey):
    return json.loads(urllib.request.urlopen(enpoints + "/Api/GetStockSummary?symbole=" + ticker + "&apiKey=" + apikey, data={}).read())