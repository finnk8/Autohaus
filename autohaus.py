import random
class Auto:
    def __init__(self, marke, modell, preis, besitzer):
        self.marke = marke
        self.modell = modell
        self.id = None
        self.tuev = None
        self.preis = preis
        self.besitzer = besitzer
        self.autohaus = None

    def update(self, **kwargs):
        pass 

Markt = []
r = random.SystemRandom()
for i in range(25):
    Markt.append(Auto('Audi', 'TT', r.randint(4000,26000), 'Tom'))

class Autohaus:
    def __init__(self, name, standort):
        self.name = name
        self.standort = standort
        self.kontostand = 0
        self.autos = [Auto('Audi', 'TT', 10000, 'Henry')]
        self.verkaefer = {}
        self.ankaefer = {}

    def verkauf(self, auto: Auto):
        self.kontostand += auto.preis
        autos = self.autos
        autos.remove(myautohaus.autos[0])
        Markt.append(auto)
    
    def ankauf(self, auto: Auto):
        self.kontostand -= auto.preis
        autos = self.autos
        Markt.remove(auto)
        autos.append(auto)

myautohaus = Autohaus("Autohaus - Klusmann","Hamburg")

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def autohaus():
    return render_template('index.html', autohaus=myautohaus, markt=Markt)

if "__main__" == __name__:
    app.run(debug=True)