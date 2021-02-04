import pytest
import django.test
from django.contrib.auth.models import User, Permission
from stocklevel_app.models import Product, Component, Supplier, Recipient, WarehouseFlows


@pytest.fixture
def client():
    return django.test.Client()


@pytest.fixture
def unauthorised_user():
    unauth_user = User.objects.create_user('Rafal')
    return unauth_user


@pytest.fixture
def authorised_user():
    auth_user = User.objects.create_user('Rafal')
    perm = Permission.objects.filter(codename__in=['add_recipient',
                                                   'add_component',
                                                   'add_supplier',
                                                   'add_product',
                                                   'add_warehouseflows',
                                                   'change_warehouseflows'
                                                   ])
    auth_user.user_permissions.set(perm)
    return auth_user


@pytest.fixture
def client_with_authorised_user(authorised_user):
    client = django.test.Client()
    client.force_login(authorised_user)
    return client


@pytest.fixture
def test_component():
    component = Component.objects.create(name='skladnik_testowy', measure='l')
    return component


@pytest.fixture
def recipient_add(client, authorised_user):
    client.force_login(authorised_user)
    response = client.post('/add-recipient/', {'name': 'klient1'})
    return Recipient.objects.get(name='klient1')


@pytest.fixture
def component_add(client, authorised_user):
    client.force_login(authorised_user)
    response = client.post('/add-component/', {'name': 'skladnik1',
                                               'measure': 'l',
                                               'stock_level': '60'
                                               })
    return Component.objects.get(name='skladnik1')


@pytest.fixture
def supplier_add(client, authorised_user, component_add):
    client.force_login(authorised_user)
    response = client.post('/add-supplier/', {'name': 'dostawca1',
                                              'comment': 'komentarz',
                                              'component': component_add.id,
                                              'category': 'n'
                                              })
    return Supplier.objects.get(name='dostawca1')


@pytest.fixture
def warehouseentry_add(client, authorised_user, component_add, supplier_add):
    client.force_login(authorised_user)
    response = client.post('/add-warehouse-entry/', {'component': component_add.id,
                                                     'series_amount': '60',
                                                     'supplier': supplier_add.id,
                                                     'supplier_series_number': 'num1',
                                                     'delivery_date': '2021-02-02',
                                                     'warehouse_series_number': 'war1',
                                                     'use_by_date': '2021-02-03'
                                                     })
    return WarehouseFlows.objects.get(warehouse_series_number='war1')
