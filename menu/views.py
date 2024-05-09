from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import *
from .forms import OrderForm
# Create your views here.
def menu(request):
    mydishes = Dish.objects.all().values()
    template = loader.get_template('all_dishes.html')
    context = {
        'mydishes': mydishes,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mydishes = Dish.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mydishes': mydishes
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')

    # Número de visitas a esta view
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits
    }

    return HttpResponse(template.render(context))

def myOrders(request):
    orders = Order.objects.all().prefetch_related('dish')
    template = loader.get_template('orders.html')
    context = {
        'orders': orders
    }
    return HttpResponse(template.render(context, request))


def createOrder(request):
    form = OrderForm()

    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/my_orders')

    context = {
        'form': form
    }
    template = loader.get_template('order_form.html')
    return HttpResponse(template.render(context, request))

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/my_orders')

    context = {
        'form': form    
    }
    template = loader.get_template('order_form.html')
    return HttpResponse(template.render(context, request))

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/my_orders')

    context = {
        'item': order
    }
    template = loader.get_template('delete.html')
    return HttpResponse(template.render(context, request))