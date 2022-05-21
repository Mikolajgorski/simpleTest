import dzialania

def dodawanieOrazOdejmowanie():
    failMsg = "Test integracyjny dodawanie oraz odejmowania nie powiódł się"
    assert dzialania.roznica(dzialania.suma(27,27), dzialania.roznica(27, 3)) == 30, failMsg
    assert dzialania.roznica(dzialania.roznica(3,7), dzialania.suma(32, 17)) == -53, failMsg
    assert dzialania.suma(dzialania.suma(27,-27), dzialania.roznica(-27, -27)) == 0, failMsg

def mnozenieOrazDzielenie():
    failMsg = "Test integracyjny mnożenia oraz dzielenia nie powiódł się"
    assert dzialania.iloczyn(dzialania.iloczyn(3,3), dzialania.iloraz(27,3)) == 81, failMsg
    assert dzialania.iloraz(dzialania.iloczyn(-3,3), dzialania.iloraz(-3,3)) == 81, failMsg
    assert dzialania.iloczyn(dzialania.iloczyn(3,3), dzialania.iloraz(27,3)) == 81, failMsg

def potegaOrazPierwiastek():
    failMsg = "Test integracyjny potegowania oraz pierwiastkowania nie powiódł się"
    assert dzialania.pierwiastek(dzialania.potega(2,2), dzialania.pierwiastek(16,4)) == 2, failMsg