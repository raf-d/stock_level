# najprostszy sposób

imie = 'sławek'
nazwisko = 'bogusławski'

imie2 = 'Ala'
nazwisko2 = 'Makota'

#słownikowo

slownik = {
    'osoba1': 'Slawek Boguslawski',
    'osoba2': 'Ala Makota'
}

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def przedstaw_sie(self):
        print(f'nazywam się {first_name} {last_name}')

    def zapoznaj_sis(self, inna_osoba):
        print(f'Ja nazywam sie {first_name} {last_name}')
        print(f'A ja nazywam sie {inna_osoba}')

