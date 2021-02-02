from django.db import models


class Component(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa materiału wyjściowego')
    measure = models.CharField(max_length=8, choices=(('kg', 'kg'), ('l', 'l')), verbose_name='Jednostka miary')
    stock_level = models.FloatField(null=True, default=0)  # dodano

    def __str__(self):
        return f'{self.name} [{self.measure}]'


class Recipient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa odbiorcy gotowego produktu')

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa dostawcy')
    comment = models.TextField(null=True, verbose_name='Uwagi')
    component = models.ManyToManyField(Component, verbose_name='Materiał wyjściowy dostarczany przez dostawcę')
    category = models.CharField(max_length=1, choices=(('a', 'a'), ('b', 'b'), ('c', 'c'),
                                                       ('d', 'd'), ('n', 'n')), default='n',
                                verbose_name='Kategoria dostawcy')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa produktu')
    production_start = models.DateField(verbose_name='Rozpoczęcie produkcji')
    production_finish = models.DateField(verbose_name='Zakończenie produkcji')
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, verbose_name='Odbiorca produktu')

    def __str__(self):
        return self.name


# upgrade modelu
class WarehouseFlows(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, verbose_name='Nazwa materiału wyjściowego')
    series_amount = models.FloatField(verbose_name='Ilość')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Dostawca materiału')
    supplier_series_number = models.CharField(max_length=100, verbose_name='Numer serii producenta')
    delivery_date = models.DateField(verbose_name='Data wpływu materiału')
    warehouse_series_number = models.CharField(max_length=100, unique=True, verbose_name='Numer magazynowy')
    use_by_date = models.DateField(verbose_name='Termin przydatności')
    laboratory_series_date = models.DateField(null=True, verbose_name='Data wykonania badania')
    laboratory_series_number = models.CharField(max_length=100, null=True, verbose_name='Numer serii po badaniu',
                                                help_text='Pole do uzupełnienia po wykonaniu badań wewnętrznych')
    release_date = models.DateField(null=True, verbose_name='Data wydania z magazynu')
    release_amount = models.FloatField(null=True, verbose_name='Wydawana ilość')
    release_purpose = models.CharField(max_length=24, null=True, choices=(('badania', 'badania'),
                                                                          ('produkcja', 'produkcja'),
                                                                          ('usunięcie', 'usunięcie')),
                                       verbose_name='Cel wydania materiału')

    def __str__(self):
        return self.warehouse_series_number
