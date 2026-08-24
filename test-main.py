from main import clima

def test_clima():
    assert clima(50) == "Helando"
def test_clima_frio():
    assert clima(50) == "Frio"
def test_clima_fresco():
    assert clima(15) == "Fresco"
def test_clima_caluroso():
    assert clima(25) == "Caluroso"
def test_clima_caliente():
    assert clima(35) == "Caliente"