import requests
import json
from BOT.Config import *

class APIException(Exception):
    pass
class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        if quote==base:
            raise APIException("Вы ввели одинаковые валюты")
        try:
            quote_value=keys[quote]
        except KeyError:
            raise APIException("Наш конвертор не поддерживает данную валюту")
        try:
            base_value=keys[base]
        except KeyError:
            raise APIException("Наш конвертор не поддерживает данную валюту")
        try:
            amount=float(amount)
        except ValueError:
            raise APIException("Количество валюты должно быть числом")
        r = requests.get(
            f"https://api.currencyapi.com/v3/latest?apikey=0GvxycvPgnjchvll8tDJcyXeIV20380nILebHu63&currencies={quote_value}&base_currency={base_value}")
        text = json.loads(r.content)
        new_price = text['data'][quote_value]['value'] * amount
        new_price = round(new_price, 3)
        return new_price