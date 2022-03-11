def extendCoeffList(coeffs, n):
    # Metoda, która przy dodawaniu wielomianów powoduje, że do tego o mniejszej ilości
    # współczynników nadpisywane są "zera"
    newcoeffs = []
    for i in range(n):
        newcoeffs.append(0)
    for i in range(0, len(coeffs)):
        newcoeffs.append(coeffs[i])
    return newcoeffs


class Polynomial:
    # Klasa reprezentująca wielomiany postaci a1x^n + a2*x^(n-1) + ... + an*x^0
    # Atrybut __coeffs - lista zawierająca kolejne współczynniki wielomianu w kolejności
    # od najwyższej potęgi do najniższej

    def __init__(self, coeffs):
        # Metoda inicjalizująca obiekt wielomianu. Argumentem jest lista współczynników
        self.__coeffs = coeffs

    def getCoeffs(self):
        # Metoda zwracająca wartość atrybutu __coeffs (czyli listę współczynników)
        return self.__coeffs

    def setCoeffs(self, coeffs):
        # Metoda nadająca atrybutowi __coeffs wartość w postaci listy współczynników
        self.__coeffs = coeffs

    def __add__(self, other):
        # Metoda dodająca wielomiany (do obiektu self podstawia sumę wielomianów self i other)
        # Dodawanie wielomianów polega na obliczeniu sum współczynników stojących przy tych samych potęgach
        coeffs1 = self.getCoeffs()
        coeffs2 = other.getCoeffs()
        if len(coeffs1) > len(coeffs2):
            n = len(coeffs1) - len(coeffs2)
            coeffs = extendCoeffList(coeffs2, n)
        if len(coeffs1) < len(coeffs2):
            n = len(coeffs2) - len(coeffs1)
            coeffs = extendCoeffList(coeffs1, n)
        for i in range(0, len(coeffs1)):
            coeffs[i] = coeffs[i] + coeffs1[i]
        d = Polynomial(coeffs)
        return d

    def derivative(self):
        # Metoda obliczająca pochodną wielomianu self. Wynikiem jest wielomian stopnia niższego o 1.
        # Metoda zwraca wielomian będący pochodną wielomianu self.
        coeffs = self.getCoeffs()
        dercoeffs = []
        exponent = len(coeffs) - 1
        for i in range(0, len(coeffs)-1):
            dercoeffs.append(coeffs[i] * exponent)
            exponent -= 1
        if len(dercoeffs) == 0:
            dercoeffs = [0]
        d = Polynomial(dercoeffs)
        return d

    def __str__(self):
        # Metoda przedstawiajaca wielomian w czytelnej potaci
        res = ""
        coeffs = self.getCoeffs()
        exponent = len(coeffs) - 1
        for i in range(0, len(coeffs)):
            res = res + str(coeffs[i])
            if i < len(coeffs)-1:
                res = res + "x"
                if exponent > 1:
                    res = res + "^" + str(exponent)
                res = res + " + "
            exponent -= 1
        return res


w = Polynomial([2,7,9,-2,8])
print("Your polynomial coefficients are: ", w.getCoeffs())
print("Your polynomial is: ", w.__str__())
d = w.derivative()
print("Your derivative of the polynomial is: ", d.__str__())
s = w.__add__(d)
print("Your sum of polynomials is: ", s.__str__())
s = d.__add__(w)
print("Your sum of polynomials is: ", s.__str__())
