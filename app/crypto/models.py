from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=25,default=None)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10,decimal_places=4,default=0)
    volume = models.IntegerField(default=0)
    img = models.ImageField(upload_to='crypto_img')

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class PortfolioItem(models.Model):
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=6,max_digits=20)

    def currency_price(self):
        return self.amount * self.currency.price

    @staticmethod
    def total_money(portfolio_item):
        sum = 0
        for item in portfolio_item:
            sum += item.currency_price()
        return sum