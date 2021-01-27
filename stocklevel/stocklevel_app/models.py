from django.db import models


class Component(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa materiału wyjściowego')
    measure = models.CharField(max_length=8, choices=(('kg', 'kg'), ('l', 'l')), verbose_name='Jednostka miary')

    def __str__(self):
        return self.name


class Recipient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa odbiorcy gotowego produktu')

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa dostawcy')
    comment = models.TextField(null=True, verbose_name='Uwagi')
    component = models.ManyToManyField(Component, verbose_name='Materiał wyjściowy dostarczany przez dostawcę')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa produktu')
    production_start = models.DateField(verbose_name='Rozpoczęcie produkcji')
    production_finish = models.DateField(verbose_name='Zakończenie produkcji')
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, verbose_name='Odbiorca produktu')

    def __str__(self):
        return self.name


class WarehouseEntry(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    amount = models.FloatField(verbose_name='Ilość')
    # measure = models.CharField(choices=(('kg', 'kg'), ('l', 'l')))  powiązać z Component
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supplier_series_number = models.CharField(max_length=100, verbose_name='Numer serii producenta')
    delivery_date = models.DateField(auto_now_add=True)
    # czy data ma się sama uzupełniać?
    warehouse_series_number = models.CharField(max_length=100, verbose_name='Numer magazynowy')
    laboratory_series_number = models.CharField(max_length=100, null=True, verbose_name='Numer serii po badaniu')
    use_by_date = models.DateField('Termin przydatności')

    def __str__(self):
        return self.warehouse_series_number


class WarehouseRelease(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True)
    amount = models.FloatField(verbose_name='Ilość')
    # measure = models.CharField(max_length=8, choices=(('kg', 'kg'), ('l', 'l')), verbose_name='Jednostka miary')
    purpose = models.CharField(max_length=24, choices=(('badania', 'badania'),
                                                       ('produkcja', 'produkcja'),
                                                       ('usunięcie', 'usunięcie')),
                               verbose_name='Cel wydania materiału')
    release_date = models.DateField(auto_now_add=True, verbose_name='Data wydania materiału')
    # czy wypełniać automatycznie?

    def __str__(self):
        return self.component
