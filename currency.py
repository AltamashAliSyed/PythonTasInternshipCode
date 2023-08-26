from forex_python.converter import CurrencyRates


print(" CURRENCY CONVERTER")

class currency_converter:
    
        
    def __init__(self,from_currency,to_currency,amount):
        self.currency = CurrencyRates()
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
    
    def conversion (self):
        
        result = self.currency.convert(self.from_currency,self.to_currency,self.amount)
        return result

        
from_currency = input(" Enter a currency :").upper()
to_currency = input(" to convert currency :").upper()
amount = float(input(" Enter a amount :"))

Convert = currency_converter(from_currency,to_currency,amount)
        
Conversion = Convert.conversion()

b = Conversion
print("Conversion :", b)
