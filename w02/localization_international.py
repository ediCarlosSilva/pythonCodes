# 1. Import the locale library
import locale

# 2. Here you have the values you want to format (you can set any value)
money_value = 1245.60

# 3. This part is specific to the output language you want
# In this case, the variables are set to the Brazilian culture
currency_symbol = 'R$'
locale_value = 'pt_BR.UTF-8'

# 4. Set the locale parameters and convert the value 
locale.setlocale(locale.LC_ALL, locale_value)
money_formatted = locale.currency(money_value, grouping=True, symbol=currency_symbol)

# 5. Optionally, print to check the results
print(money_formatted)

# You can set the result to be in any language you want, like Spain which uses Euros
currency_symbol = '€'
locale_value = 'es_ES.UTF-8'

# Or Ghana that uses Ghanaian Cedi and many others
currency_symbol = 'GHS'
locale_value = 'en_GH.UTF-8'