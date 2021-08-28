from datetime import datetime

from django.contrib.auth.models import User
import pytest

from store.models import Products, Producent, Category, Orders, PayMethod, Opinions, Basket, BasketProduct


@pytest.fixture
def user():
    users = []
    for x in range(1,2):
        u = User()
        u.username = f'user{x}'
        u.set_password = 'haslo'
        u.save()
        users.append(u)
    return users


@pytest.fixture
def producent():
    p = Producent()
    p.name = 'Producent_1'
    p.save()
    return p


@pytest.fixture
def category():
    c = Category()
    c.name = f'Narzędzia'
    c.save()
    return c


@pytest.fixture
def product(producent, category):
    p = Products()
    p.name=f'Produkt_1'
    p.producent_id=producent.id
    p.category_id=category.id
    p.price=10
    p.save()
    return p


@pytest.fixture
def order(user, product, payment):
    o = Orders()
    o.order_number = 12345
    o.username = user[0]
    o.if_delivery = True
    o.date_delivery = datetime.today()
    o.payment_method = payment
    o.save()
    o.product.add(product)
    return o


@pytest.fixture
def payment():
    pm = PayMethod()
    pm.name = 'gotówka'
    pm.save()
    return pm


@pytest.fixture
def opinion(user, product):
    o = Opinions()
    o.username = user[0]
    o.product = product
    o.date = datetime.today()
    o.text = 'Treść opini'
    o.save()
    return o


@pytest.fixture
def basket(user, product):
    b = Basket.objects.create(user=user[0])
    return b

@pytest.fixture
def basket_products(basket, product):
    bps = []
    for x in range(1,3):
        bp = BasketProduct(basket=basket, product=product, quantity=1)
        bp.save()
        bps.append(bp)
    return bps