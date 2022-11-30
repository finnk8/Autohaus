import random
import datetime

class Auto:
    def __init__(self, marke, modell, lakierung, preis, besitzer):
        self.marke = marke
        self.modell = modell
        self.lakierung = lakierung
        self.id = None
        self.tuev = None
        self.naechster_tuev = None
        self.schaeden_liste = []
        self.preis = preis
        self.besitzer = besitzer
        self.autohaus = None

    def umlakieren(self, farbe):
        self.lakierung = str(farbe)

    def set_tuev(self):
        self.tuev = datetime.date.today() + datetime.timedelta(weeks=104)

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
r = random.SystemRandom()
for i in range(25):
    Markt.append(Auto('Audi', 'TT', 'rot', r.randint(4000,26000), 'Tom'))

class Autohaus:
    def __init__(self, name, standort):
        self.name = name
        self.standort = standort
        self.kontostand = 0
        self.autos = [Auto('Audi', 'TT', 'blau', 10000, 'Henry')]
        self.verkaefer = {}
        self.ankaefer = {}

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
        Markt.remove(auto)

myautohaus = Autohaus("Autohaus - Finn und Tore","Hamburg")

from flask import Flask, render_template, redirect, url_for

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

if __name__ == '__main__':
    app.run(debug=True)