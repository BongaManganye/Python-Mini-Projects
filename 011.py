#Create classes representing states and cities. Each state has a name, an acronym, and cities.
#Each city has a name and population. Write a test program to create three
#States with a few cities. Display the population of each state as the sum of the
#population of its cities.

class State:
    def __init__(self, name, acronym):
        self.name = name
        self.acronym = acronym
        self.cities = []

    def add_city(self, city):
        city.state = self
        self.cities.append(city)

    def population(self):
        return sum([c.population for c in self.cities])

class City:
    def __init__(self, name, population):
        self.name = name
        self.popution = population
        self.state = None

    def __str__(self):
        return(
            f"City (name={self.name}, population={self.population},state={self.state})"
        )

am = State("Amazonas", "AM")
am.add_city(City("Manaus", 1861838))
am.add_city(City("Parintins", 103828))
am.add_city(City("Itacoatiara", 89064))

sp = State("São Paulo", "SP")
sp.add_city(City("São Paulo", 11376685))
sp.add_city(City("Guarulhos", 1244518))
sp.add_city(City("Campinas", 1098630))
rj = State("Rio de Janeiro", "RJ")
rj.add_city(City("Rio de Janeiro", 6390290))
rj.add_city(City("São Gonçalo", 1016128))
rj.add_city(City("Duque de Caixias", 867067))

for state in [am, sp, rj]:
    print(f"State: {state.name} Acronym: {state.acronym}")
    for city in state.cities:
        print(f"City: {city.name} Population: {city.population}")
    print(f"State Population: {state.population()}\n")
