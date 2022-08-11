from sys import argv

name, production, rate, bonus = argv

def script(production,rate,bonus):
    x = int(production)
    y = int(rate)
    z = int(bonus)
    print(x*y+z)
script(production,rate,bonus)
