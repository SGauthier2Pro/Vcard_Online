from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from portfolio.models.portfolio import Portfolio
from portfolio.forms import portfolioform


@login_required
def index(request):
    portfolios = Portfolio.objects.filter(
        Q(user=request.user)
    )

    return render(request,
                  'portfolio/portfolios_index.html',
                  context={'portfolios': portfolios}
                  )


@login_required
def create_portfolio(request):
    portfolio_form = portfolioform.PortfolioForm(request.user)
    if request.method == 'POST':
        portfolio_form = portfolioform.PortfolioForm(request.user, request.POST)
        if portfolio_form.is_valid():
            portfolio_to_save = portfolio_form.save(commit=False)
            portfolio_to_save.user = request.user
            portfolio_to_save.save()
            return redirect('portfolio:portfolio_home')
    return render(request,
                  'portfolio/create_portfolio.html',
                  context={'portfolio_form': portfolio_form}
                  )


@login_required
def edit_portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio,
                                  id=portfolio_id)
    edit_form = portfolioform.PortfolioForm(user=request.user, instance=portfolio)
    if request.method == 'POST':
        edit_form = portfolioform.PortfolioForm(user=request.user,
                                                data=request.POST,
                                                instance=portfolio)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('portfolio:portfolio_home')
    context = {
        'portfolio': portfolio,
        'edit_form': edit_form,
    }
    return render(request,
                  'portfolio/edit_portfolio.html',
                  context=context)


@login_required
def delete_portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    delete_form = portfolioform.DeletePortfolioForm()
    if request.method == 'POST':
        delete_form = portfolioform.DeletePortfolioForm(request.POST)
        if delete_form.is_valid():
            portfolio.delete()
            return redirect('portfolio:portfolio_home')
    context = {
        'portfolio': portfolio,
        'delete_form': delete_form,
    }
    return render(request,
                  'portfolio/delete_portfolio.html',
                  context=context)


@login_required
def set_portfolio_visible(request, portfolio_id):
    portfolios = Portfolio.objects.filter(
        Q(user=request.user)
    )
    for portfolio_to_check in portfolios:
        if portfolio_to_check.id == portfolio_id:
            portfolio_to_check.is_visible = True
            portfolio_to_check.save()
        else:
            portfolio_to_check.is_visible = False
            portfolio_to_check.save()

    return redirect('portfolio:portfolio_home')
