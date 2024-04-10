class Auto:
    def __init__(self, model, rv, vyrobce, obsah, barva, cena):
        self.model = model
        self.rv = rv
        self.vyrobce = vyrobce
        self.obsah = obsah
        self.barva = barva
        self.cena = cena
    def zadej_parametr(self, model, rv, vyrobce, obsah, barva, cena):
        self.model = model
        self.rv = rv
        self.vyrobce = vyrobce
        self.obsah = obsah
        self.barva = barva
        self.cena = cena

    def input_data(self):
            self.model = input("zadej model vozu: ")
            self.rv = int(input("zadej rok výroby vozu: "))
            self.vyrobce = input("zadej výrobce vozu: ")
            self.obsah = float(input("zadej obsah motoru vozu: "))
            self.barva = input("zadej barvu vozu: ")
            self.cena = float(input("zadej cenu vozu: "))
    def output_data(self):
            print("model vozu:", self.model)
            print("rok výroby:", self.rv)
            print("výrobce:", self.vyrobce)
            print("obsah motoru:", self.obsah)
            print("barva:", self.barva)
            print("cena:", self.cena)
    def get_model(self):
        return self.model
    def get_year(self):
        return self.rv
    def get_manufacturer(self):
        return self.vyrobce
    def get_engine_capacity(self):
        return self.obsah
    def get_color(self):
        return self.barva
    def get_price(self):
        return self.cena


auto = Auto("", 0, "", 0.0, "", 0.0)
auto.input_data()
auto.output_data()


