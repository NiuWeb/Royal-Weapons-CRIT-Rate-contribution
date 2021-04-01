import numpy as np

# Polynomial regressions
class Regression:
    def __init__(self, x, y, n = 3):
        # Generate polynomial regression
        self.__fit = np.polyfit(x, y, n)
        # Generate polynomial function from regression
        self.__p = np.poly1d(self.__fit)
    
    # Poly function string (ax^n+...+z)
    def __str__(self):
        p = []
        n = 0
        for i in self.__fit[::-1]:
            p.append(str(i) + ('*x^' + str(n) if n > 0 else ""))
            n += 1

        return '+'.join(p[::-1])
    
    # Evaluate polynomial function
    def eval(self, x):
        return self.__p(x)
    # Get the list of coefficients
    @property
    def poly(self):
        return self.__fit
    