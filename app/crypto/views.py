from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from crypto.models import Currency,PortfolioItem,Portfolio
from crypto.form import PorfolioItemsForm
class IndexView(View):
    template_name = 'app/index.html'

    def get(self,request):
        return render(request,self.template_name)

class CurrencyListView(View):
    template_name = 'app/currencylist.html'

    def get(self,request):
        context = {
            'currency_list':Currency.objects.all(),
        }
        return render(request,self.template_name,context)
@method_decorator(login_required, name='dispatch')
class PortfolioView(View):
    template_name = 'app/portfolio.html'

    def get(self,request):
        user = request.user
        portfolio_items = PortfolioItem.objects.filter(portfolio__user=user)
        total_money = PortfolioItem.total_money(list(portfolio_items))
        form = PorfolioItemsForm()
        context = {
            'portfolio_items':portfolio_items,
            'total_money':total_money,
            'form':form
        }
        return render(request,self.template_name,context)
    def post(self,request):
        form = PorfolioItemsForm(data = request.POST)
        if form.is_valid():
            currency = form.cleaned_data['currency']
            amount = form.cleaned_data['amount']
            user_portfolio, created = Portfolio.objects.get_or_create(user = request.user)

            existing_item = PortfolioItem.objects.filter(portfolio=user_portfolio, currency=currency).first()

            if existing_item:
                existing_item.amount += amount
                existing_item.save()
            else:
                PortfolioItem.objects.create(portfolio=user_portfolio, currency=currency, amount=amount)
        return redirect('profile')

