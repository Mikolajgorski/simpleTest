import dzialania

fail = " działa niepoprawnie"

def dodawanie():
    funkcja = "suma()"
    assert dzialania.suma(27, 3) == 30, funkcja+fail
    assert dzialania.suma(20, 30) == 50, funkcja+fail

def odejmowanie():
    funkcja = "roznica()"
    assert dzialania.roznica(27, 3) == 24, funkcja+fail
    assert dzialania.roznica(71, 25) == 46, funkcja+fail

def mnozenie():
    funkcja = "iloczyn()"
    assert dzialania.iloczyn(27, 3) == 81, funkcja+fail
    assert dzialania.iloczyn(120, 130) == 15600, funkcja+fail

def dzielenie():
    funkcja = "iloraz()"
    assert dzialania.iloraz(27, 3) == 9, funkcja+fail
    assert dzialania.iloraz(100, 5) == 20, funkcja+fail

def potegowanie():
    funkcja = "potega()"
    assert dzialania.potega(27, 3) == 19683, funkcja+fail
    assert dzialania.potega(7, 3) == 343, funkcja+fail

def pierwiastkowanie():
    funkcja = "pierwiastek()"
    assert dzialania.pierwiastek(27, 3) == 3, funkcja+fail
    assert dzialania.pierwiastek(125, 3) == 5, funkcja+fail