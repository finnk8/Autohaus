import random
import datetime
import names

r = random.SystemRandom()

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = r.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

class Auto:
    def __init__(self, marke, modell, lakierung, tuev, preis, besitzer):
        self.marke = marke
        self.modell = modell
        self.lakierung = lakierung
        self.id = None
        self.tuev = tuev
        self.schaeden_liste = []
        self.preis = preis
        self.besitzer = besitzer
        self.autohaus = None

    def umlakieren(self, farbe):
        self.lakierung = str(farbe)
        self.preis += int(self.preis*0.02)

    def set_tuev(self):
        self.tuev = str(datetime.date.today() + datetime.timedelta(weeks=104))
        self.preis += int(self.preis*0.02)

    def add_schaden(self, schaden):
        self.schaeden_liste.append(str(schaden))

class Tesla(Auto):
    def __init__(self, modell, preis, besitzer):
        super().__init__(modell, preis, besitzer)
        self.marke = "Tesla"
        self.akku_tausch = None

    def set_akku_tausch(self):
        self.akku_tausch = datetime.date.today()

Markt = []

auto_marken = ['Audi', 'Ford', 'Mercedes Benz', 'VW', 'Skoda', 'Fiat', 'Mini', 'Smart']
auto_modelle = ['TT', 'A3', 'Columbus', 'Cooper', 'S250', 'T40', 'Golf', 'Yeti']
auto_farbe = ['red', 'blue', 'green', 'yellow', 'white', 'black', 'grey']
tree_years_ago = datetime.date.today() - datetime.timedelta(weeks=104)
for i in range(25):
    Markt.append(Auto(str(r.choice(auto_marken)), str(r.choice(auto_modelle)), str(r.choice(auto_farbe)), random_date(tree_years_ago, datetime.date.today()), r.randint(4000,26000), str(names.get_first_name())))

class Autohaus:
    def __init__(self, name, standort):
        self.name = name
        self.standort = standort
        self.kontostand = 0
        self.autos = [Auto('Audi', 'TT', 'blau', random_date(tree_years_ago, datetime.date.today()), 10000, 'Henry')]
        self.kunden = []

    def verkauf(self, auto_id):
        auto = self.autos[auto_id]
        self.kontostand += auto.preis
        autos = self.autos
        Markt.append(auto)
        autos.remove(auto)
    
    def ankauf(self, auto_id):
        auto = Markt[auto_id]
        self.kontostand -= auto.preis
        autos = self.autos
        autos.append(auto)
        self.kunden.append(auto.besitzer)
        Markt.remove(auto)

    def auto_umlakieren(self):
        if self.kontostand-50 >= 0:
            self.kontostand -= 50
            return True
        else:
            return False

myautohaus = Autohaus("Autohaus - Finn und Tore","Hamburg")

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', autohaus=myautohaus, markt=Markt)

@app.route('/verkaufen/<id>')
def verkaufen(id):
    myautohaus.verkauf(int(id))
    return redirect(url_for('index'))

@app.route('/ankaufen/<id>')
def ankaufen(id):
    myautohaus.ankauf(int(id))
    return redirect(url_for('index'))

@app.route('/umlakieren/<id>', methods=['GET', 'POST'])
def umlakieren(id):
    auto = myautohaus.autos[int(id)]
    if myautohaus.auto_umlakieren() == True:
        auto.umlakieren(request.args.get("farbe"))
    return redirect(url_for('index'))

@app.route('/tuev_verlaengern/<id>', methods=['GET', 'POST'])
def tuev_verlaengern(id):
    auto = myautohaus.autos[int(id)]
    auto.set_tuev()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)