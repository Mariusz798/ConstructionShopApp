from django.test import Client
import pytest
from django.urls import reverse

from store.models import Products, Orders, Opinions, Basket, Producent, Category, BasketProduct


@pytest.mark.django_db
def test_client():
    Client()


@pytest.mark.django_db
def test_index_view_get():
    c = Client()
    url = reverse('index')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context.render_context.template.name == 'base.html'


@pytest.mark.django_db
def test_view_product_get(product):
    c = Client()
    url = reverse('product_list')
    response = c.get(url)
    pds = response.context['object_list']
    assert response.status_code == 200
    assert pds.count() == 1


@pytest.mark.django_db
def test_create_product_view_get_not_logged_in():
    c = Client()
    url = reverse('product_create')
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_create_product_view_get_logged_in(user):
    c = Client()
    c.force_login(user[0])
    url = reverse('product_create')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['form'].Meta.fields == ['name', 'producent', 'category', 'price']


@pytest.mark.django_db
def test_create_product_view_post(user, producent, category):
    c = Client()
    c.force_login(user[0])
    url = reverse('product_create')
    response = c.post(url, {'name':'narzędzie', 'producent':producent.id, 'category': category.id, 'price':2})
    assert response.status_code == 302
    assert Products.objects.count() == 1


@pytest.mark.django_db
def test_detail_product_view_get(product):
    c = Client()
    url = reverse('product_detail', args=(product.id,))
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['object'] == product


@pytest.mark.django_db
def test_modify_product_view_get_not_logged_in(product):
    c = Client()
    url = reverse('product_modify', args=(product.id,))
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_modify_product_view_get_logged_in(user, product):
    c = Client()
    c.force_login(user[0])
    url = reverse('product_modify', args=(product.id,))
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['form'].fields


@pytest.mark.django_db
def test_modify_product_view_post(user, product, producent, category):
    c = Client()
    c.force_login(user[0])
    url = reverse('product_modify', args=(product.id,))
    response = c.post(url, {'name':product.name, 'producent':producent.id, 'category': category.id, 'price':15})
    assert response.status_code == 302


@pytest.mark.django_db
def test_delete_product_view_get_not_logged_in(product):
    c = Client()
    url = reverse('product_delete', args=(product.id,))
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_delete_product_view_get_logged_in(user, product):
    c = Client()
    c.force_login(user[0])
    url = reverse('product_delete', args=(product.id,))
    response = c.get(url)
    assert response.status_code == 200
    assert response.context.render_context.template.name == 'confirm_delete.html'


@pytest.mark.django_db
def test_delete_product_view_post(user, product):
    c = Client()
    c.force_login(user[0])
    url = reverse('product_delete', args=(product.id,))
    response = c.post(url)
    assert response.status_code == 302
    assert Products.objects.count() == 0



@pytest.mark.django_db
def test_view_producent_get(producent):
    c = Client()
    url = reverse('producent_list')
    response = c.get(url)
    pts = response.context['object_list']
    assert response.status_code == 200
    assert pts.count() == 1


@pytest.mark.django_db
def test_create_producent_get_not_logged_in():
    c = Client()
    url = reverse('producent_create')
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_create_producent_get_logged_in(user):
    c = Client()
    c.force_login(user[0])
    url = reverse('producent_create')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['form'].Meta.model.__name__ == 'Producent'


@pytest.mark.django_db
def test_create_producent_post(user):
    c = Client()
    c.force_login(user[0])
    url = reverse('producent_create')
    response = c.post(url, {'name':'Producent2021'})
    assert response.status_code == 302
    assert Producent.objects.count() == 1


@pytest.mark.django_db
def test_modify_producent_get_not_logged_in(producent):
    c = Client()
    url = reverse('producent_modify', args=(producent.id,))
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_modify_producent_view_get_logged_in(user, producent):
    c = Client()
    c.force_login(user[0])
    url = reverse('producent_modify', args=(producent.id,))
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['object'] == producent


@pytest.mark.django_db
def test_modify_producent_view_post(user, producent):
    c = Client()
    c.force_login(user[0])
    url = reverse('producent_modify', args=(producent.id,))
    response = c.post(url, {'name':'Producent2021'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_category_get(category):
    c = Client()
    url = reverse('category_list')
    response = c.get(url)
    cts = response.context['object_list']
    assert response.status_code == 200
    assert cts.count() == 1


@pytest.mark.django_db
def test_create_category_get_not_logged_in():
    c = Client()
    url = reverse('category_create')
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_create_category_get_logged_in(user):
    c = Client()
    c.force_login(user[0])
    url = reverse('category_create')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['form'].Meta.model.__name__ == 'Category'


@pytest.mark.django_db
def test_create_category_post(user):
    c = Client()
    c.force_login(user[0])
    url = reverse('category_create')
    response = c.post(url, {'name':'kategoria2021'})
    assert response.status_code == 302
    assert Category.objects.count() == 1


@pytest.mark.django_db
def test_modify_category_view_get_not_logged_in(category):
    c = Client()
    url = reverse('category_modify', args=(category.id,))
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_modify_category_view_get_logged_in(user, category):
    c = Client()
    c.force_login(user[0])
    url = reverse('category_modify', args=(category.id,))
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['object'] == category


@pytest.mark.django_db
def test_modify_category_view_post(user, category):
    c = Client()
    c.force_login(user[0])
    url = reverse('category_modify', args=(category.id,))
    response = c.post(url, {'name':'Kategoria2021'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_delete_category_view_get_not_logged_in(category):
    c = Client()
    url = reverse('category_delete', args=(category.id,))
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_delete_category_view_get_logged_in(user, category):
    c = Client()
    c.force_login(user[0])
    url = reverse('category_delete', args=(category.id,))
    response = c.get(url)
    assert response.status_code == 200
    assert response.context.render_context.template.name == 'confirm_delete.html'


@pytest.mark.django_db
def test_delete_category_view_post(user, category):
    c = Client()
    c.force_login(user[0])
    url = reverse('category_delete', args=(category.id,))
    response = c.post(url)
    assert response.status_code == 302
    assert Category.objects.count() == 0


@pytest.mark.django_db
def test_order_view_get_not_logged_in():
    c = Client()
    url = reverse('order_list')
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_order_view_get_logged_in(user, order):
    c = Client()
    c.force_login(user[0])
    url = reverse('order_list')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == 1


@pytest.mark.django_db
def test_create_order_view_get_not_logged_in():
    c = Client()
    url = reverse('order_create')
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_create_order_view_get_logged_in(user):
    c = Client()
    c.force_login(user[0])
    url = reverse('order_create')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['form'].__class__.__name__ == 'CreateOrderForm'


@pytest.mark.django_db
def test_create_order_view_post(user, product, payment):
    c = Client()
    c.force_login(user[0])
    url = reverse('order_create')
    response = c.post(url, {'product': product.id, 'if_delivery': True, 'payment_method': payment.id})
    assert response.status_code == 302
    assert Orders.objects.count() == 1


@pytest.mark.django_db
def test_detail_order_view_get_not_logged_in(order):
    c = Client()
    url = reverse('order_detail', args=(order.id,))
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_detail_order_view_get_logged_in(user, order):
    c = Client()
    c.force_login(user[0])
    url = reverse('order_detail', args=(order.id,))
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['object'] == order


@pytest.mark.django_db
def test_opinion_view_get(opinion):
    c = Client()
    url = reverse('opinion_list')
    response = c.get(url)
    ops = response.context['object_list']
    assert response.status_code == 200
    assert ops.count() == 1


@pytest.mark.django_db
def test_create_opinion_view_get_not_logged_in():
    c = Client()
    url = reverse('opinion_create')
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_create_opinion_view_get_logged_in(user):
    c = Client()
    c.force_login(user[0])
    url = reverse('opinion_create')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['form'].__class__.__name__ == 'CreateOpinionForm'


@pytest.mark.django_db
def test_create_opinion_view_post(user, product):
    c = Client()
    c.force_login(user[0])
    url = reverse('opinion_create')
    response = c.post(url, {'product':product.id, 'text':'Jakaś opinia'})
    assert response.status_code == 302
    assert Opinions.objects.count() == 1


@pytest.mark.django_db
def test_basket_products_view_get_not_logged_in():
    c = Client()
    url = reverse('basket_list')
    response = c.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_basket_products_view_get_logged_in(user, basket_products):
    c = Client()
    c.force_login(user[0])
    url = reverse('basket_list')
    response = c.get(url)
    products = response.context['object_list']
    assert response.status_code == 200
    assert products.count() == len(basket_products)


@pytest.mark.django_db
def test_add_product_to_basket_post(user, product, basket):
    c = Client()
    c.force_login(user[0])
    url = reverse('add_to_basket')
    response = c.post(url, {'product_id':product.id, 'ilosc':1})
    assert response.status_code == 302
    assert Basket.objects.count() == 1


@pytest.mark.django_db
def test_delete_product_in_basket_view_get_logged_in(user, basket_products):
    c = Client()
    c.force_login(user[0])
    url = reverse('basket_delete', args=(basket_products[0].id,))
    response = c.get(url)
    assert response.status_code == 200
    assert response.context.render_context.template.name == 'confirm_delete.html'


@pytest.mark.django_db
def test_delete_product_in_basket_post(user, basket_products):
    c = Client()
    c.force_login(user[0])
    url = reverse('basket_delete', args=(basket_products[0].id,))
    response = c.post(url)
    assert response.status_code == 302
    assert BasketProduct.objects.count() == 1