from libs.openexchange import OpenExchangeClient

APP_ID = '887ff597291d4629a06f82ac1ed5a035'

client = OpenExchangeClient(APP_ID)

usd_amount = 100
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
print(f'USD {usd_amount} = GBP {gbp_amount:.2f}')
