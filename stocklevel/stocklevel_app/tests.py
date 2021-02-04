from django.test import TestCase, Client
import pytest
from stocklevel_app.models import Product, Component, Supplier, Recipient, WarehouseFlows


# dodanie nowego materiału wyjściowego
@pytest.mark.django_db
def test_component_add(client_with_authorised_user):
    response = client_with_authorised_user.post('/add-component/', {'name': 'skladnik1',
                                               'measure': 'l',
                                               'stock_level': '60'
                                               })
    assert response.status_code == 302
    assert Component.objects.filter(name='skladnik1')


# próba dodania nowego materiału wyjściowego bez uprawnień
@pytest.mark.django_db
def test_component_add_without_permission(client, unauthorised_user):
    client.force_login(unauthorised_user)
    response = client.post('/add-component/', {'name': 'skladnik1',
                                               'measure': 'l',
                                               'stock_level': '60'
                                               })
    assert response.status_code == 403  # odmowa dostępu
    assert len(Component.objects.filter(name='skladnik1')) == 0


# dodanie nowego odbiorcy
@pytest.mark.django_db
def test_recipient_add(client_with_authorised_user):
    response = client_with_authorised_user.post('/add-recipient/', {'name': 'klient1'})
    assert Recipient.objects.filter(name='klient1')


# dodanie nowego dostawcy
@pytest.mark.django_db
def test_supplier_add(client_with_authorised_user, component_add):
    response = client_with_authorised_user.post('/add-supplier/', {'name': 'dostawca1',
                                              'comment': 'komentarz',
                                              'component': component_add.id,
                                              'category': 'n'
                                              })
    assert Supplier.objects.filter(name='dostawca1')


# dodanie nowego produktu końcowego
@pytest.mark.django_db
def test_product_add(client_with_authorised_user, recipient_add):
    response = client_with_authorised_user.post('/add-product/', {'name': 'produkt1',
                                             'production_start': '2021-02-02',
                                             'production_finish': '2021-02-03',
                                             'recipient': recipient_add.id
                                             })
    assert Product.objects.filter(name='produkt1')


# dodanie nowej dostawy do magazynu
@pytest.mark.django_db
def test_warehouseentry_add(client_with_authorised_user, component_add, supplier_add):
    response = client_with_authorised_user.post('/add-warehouse-entry/', {'component': component_add.id,
                                                     'series_amount': '60',
                                                     'supplier': supplier_add.id,
                                                     'supplier_series_number': 'num1',
                                                     'delivery_date': '2021-02-02',
                                                     'warehouse_series_number': 'war1',
                                                     'use_by_date': '2021-02-03'
                                                     })
    assert WarehouseFlows.objects.filter(warehouse_series_number='war1')


# dodanie numeru badań laboratoryjnych
@pytest.mark.django_db
def test_warehouseentry_lab(client_with_authorised_user, warehouseentry_add):
    response = client_with_authorised_user.post(f'/add-laboratory-number/{warehouseentry_add.id}/',
                           {'laboratory_series_number': 'lab1',
                            'laboratory_series_date': '2021-02-02'
                            })
    assert WarehouseFlows.objects.filter(laboratory_series_number='lab1')


# wydanie materiału z magazynu
@pytest.mark.django_db
def test_warehouse_release(client_with_authorised_user, warehouseentry_add):
    response = client_with_authorised_user.post(f'/add-warehouse-release/{warehouseentry_add.id}/',
                           {'component': warehouseentry_add.component.id,
                            'series_amount': warehouseentry_add.series_amount,
                            'release_date': '2021-02-02',
                            'release_purpose': 'produkcja',
                            'release_amount': '10'
                            })
    print(response.content)
    assert WarehouseFlows.objects.filter(release_date='2021-02-02')


# próba wydania materiału z magazynu w ilości większej niż dostarczono
@pytest.mark.django_db
def test_warehouse_release_with_to_much_amount(client_with_authorised_user, warehouseentry_add):
    response = client_with_authorised_user.post(f'/add-warehouse-release/{warehouseentry_add.id}/',
                            {'component': warehouseentry_add.component.id,
                             'series_amount': warehouseentry_add.series_amount,
                             'release_date': '2021-02-02',
                             'release_purpose': 'produkcja',
                             'release_amount': '70'
                             })
    assert response.status_code == 200
    assert len(WarehouseFlows.objects.filter(release_date='2021-02-02')) == 0
