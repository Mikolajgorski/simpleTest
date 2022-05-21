import jednostkowe as testJednostkowy
import integracyjne as testIntegracyjny

def main():

    # # testy jednostkowe
    testJednostkowy.dodawanie()
    testJednostkowy.odejmowanie()
    testJednostkowy.mnozenie()
    testJednostkowy.dzielenie()
    testJednostkowy.potegowanie()
    testJednostkowy.pierwiastkowanie()

    # # testy integracyjne
    testIntegracyjny.dodawanieOrazOdejmowanie()
    testIntegracyjny.mnozenieOrazDzielenie()
    testIntegracyjny.potegaOrazPierwiastek()

if __name__=="__main__":
    main()