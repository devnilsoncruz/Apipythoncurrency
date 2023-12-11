import requests

def take_price():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    
    request_data = request.json()
    
    dolar_price = request_data['USDBRL']['bid']
    euro_price = request_data['EURBRL']['bid']
    btc_price = request_data['BTCBRL']['bid']
    
    text =f'''
    
    Dólar:{dolar_price}
    Euro:{euro_price}
    BTC:{btc_price}'''
    
    print(text)
    take_price()