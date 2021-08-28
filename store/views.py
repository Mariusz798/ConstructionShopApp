from datetime import datetime, timedelta
from random import randint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from store.forms import CreateOrderForm, CreateOpinionForm
from store.models import Products, Category, Producent, Orders, Opinions, Basket, BasketProduct


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')


# ==============================================================


class ProductView(ListView):
    model = Products
    template_name = 'product_list.html'

    def get_queryset(self):
        return Products.objects.all()


class CreateProductView(LoginRequiredMixin, CreateView):
    model = Products
    fields = ['name', 'producent', 'category', 'price']
    success_url = reverse_lazy('product_list')
    template_name = 'form.html'


class DetailProductView(DetailView):
    model = Products
    template_name = 'detail_product_view.html'


class ModifyProductView(LoginRequiredMixin, UpdateView):
    model = Products
    fields = ['name', 'producent', 'category', 'price']
    template_name = 'form.html'
    success_url = reverse_lazy('product_list')


class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Products
    success_url = reverse_lazy('product_list')
    template_name = 'confirm_delete.html'


# ==============================================================


class ProducentView(ListView):
    model = Producent
    paginate_by = 36
    template_name = 'producent_list.html'

    def get_queryset(self):
        return Producent.objects.all()


class ProducentDetailView(LoginRequiredMixin, UpdateView):
    model = Producent
    fields = ['name']
    template_name = 'form.html'
    success_url = reverse_lazy('producent_list')


class CreateProducentView(LoginRequiredMixin, CreateView):
    model = Producent
    fields = ['name']
    success_url = reverse_lazy('producent_list')
    template_name = 'form.html'


# ==============================================================


class CategoryView(ListView):
    model = Category
    template_name = 'category_list.html'

    def get_queryset(self):
        return Category.objects.all()


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('category_list')
    template_name = 'form.html'


class ModifyCategoryView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']
    template_name = 'form.html'
    success_url = reverse_lazy('category_list')


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    template_name = 'confirm_delete.html'


# ==============================================================


class OrderView(LoginRequiredMixin, View):
    def get(self, request):
            object_list = Orders.objects.filter(username=request.user)
            if len(object_list) > 0:
                return render(request, 'order_list.html', {'object_list': object_list})
            else:
                return render(request, 'empty_order.html')


def set_order_number():
    numbers = []
    number = randint(11, 999999999)
    if number not in numbers:
        numbers.append(number)
        return number
    else:
        while number not in numbers:
            number = randint(11, 999999999)
        numbers.append(number)
        return number


class CreateOrderView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateOrderForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_number = set_order_number()
            order.username = request.user
            order.date_delivery = datetime.today() + timedelta(10)
            order.save()
            form.save_m2m()
            return redirect('order_list')
        return render(request, 'form.html', {'form': form})


class DetailOrderView(LoginRequiredMixin, DetailView):
    model = Orders
    template_name = 'detail_order_view.html'

# ==============================================================


class OpinionView(ListView):
    model = Opinions
    template_name = 'opinions_list.html'

    def get_queryset(self):
        return Opinions.objects.all()


class CreateOpinionView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateOpinionForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CreateOpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.username = request.user
            opinion.save()
            return redirect('opinion_list')
        return render(request, 'form.html', {'form': form})


# ==============================================================


class AddProductToBasket(LoginRequiredMixin, View):
    def post(self, request):
        try:
            b = Basket.objects.get(user=request.user)
            q = request.POST.get('ilosc')
            p = Products.objects.get(pk=request.POST.get('product_id'))
            bp = BasketProduct(basket=b, product=p, quantity=q)
            bp.save()
            return redirect('basket_list')
        except:
            b = Basket.objects.create(user=request.user)
            q = request.POST.get('ilosc')
            p = Products.objects.get(pk=request.POST.get('product_id'))
            bp = BasketProduct(basket=b, product=p, quantity=q)
            bp.save()
            return redirect('basket_list')


class BasketView(LoginRequiredMixin, View):
    def get(self, request):
        # try:
        my_basket = Basket.objects.get(user=request.user)
        object_list = BasketProduct.objects.filter(basket=my_basket)
        return render(request, 'basket_list.html', {'object_list':object_list})
        # except:
            # return render(request, 'empty_basket.html')


class DeleteBasketProductView(LoginRequiredMixin, DeleteView):
    model = BasketProduct
    success_url = reverse_lazy('basket_list')
    template_name = 'confirm_delete.html'