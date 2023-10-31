from celery import shared_task
from .models import Currency
import requests
from .key import KEY

@shared_task
def update_price():
    API_KEY = KEY

    # Получаем полный список криптовалют и их символов из CoinMarketCap API
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '100',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    if response.status_code == 200:
        cryptocurrencies = data['data']
        for crypto in cryptocurrencies:
            symbol = crypto['symbol']
            price = crypto['quote']['USD']['price']
            volume_24h = crypto['quote']['USD']['volume_24h']

            if Currency.objects.filter(symbol=symbol).exists():
                Currency.objects.filter(symbol=symbol).update(price=price, volume=volume_24h)
        print('Все обновлено')
    else:
        print('Ошибка при получении данных:', data['status']['error_message'])

