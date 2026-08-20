import time
def clima(temperatura):
    if temperatura < 0:
        return "Helando"
    elif 0 <= temperatura < 10:
        return "Frio"
    elif 10 <= temperatura < 20:
        return "Fresco"
    elif 20 <= temperatura < 30:
        return "Caluroso"
    else:
        return "Caliente"
