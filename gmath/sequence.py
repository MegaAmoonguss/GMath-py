import sympy
from gmath import Polynomial


class Sequence:
    """
    A class to model sequences.
    """
    n = sympy.symbols('n')

    def __init__(self, terms):
        """
        Initialize Sequence object by figuring out what kind of sequence the terms are a part of
        and the equation for the nth term.
        """
        if len(terms) > 1 and terms[1:] == terms[:-1]:
            self.type = "constant"
            self.equation = str(terms[0])
        elif is_arithmetic(terms):
            self.type = "arithmetic"
            self.equation = terms[0] + (Sequence.n - 1) * (terms[1] - terms[0])
        elif is_geometric(terms):
            self.type = "geometric"
            d = terms[1] / terms[0]
            if int(d) == d:
                d = int(d)
            self.equation = terms[0] * d**(Sequence.n - 1)
        elif is_quadratic(terms):
            self.type = "quadratic"
            p = Polynomial(points=((1, terms[0]), (2, terms[1]), (3, terms[2])))
            seq_coeffs = [int(c) for c in p.coeffs if int(c) == c]
            self.equation = seq_coeffs[0] * Sequence.n**2 + seq_coeffs[1] * Sequence.n + seq_coeffs[2]
        else:
            self.type = None
            self.equation = None
    
    def get_term(self, n):
        """
        Return the nth value of the sequence. Starts at index 0.
        """
        if self.type is None:
            raise ValueError("No sequence found")
        elif self.type == "constant":
            if int(self.equation) == float(self.equation):
                return int(self.equation)
            return float(self.equation)

        retval = self.equation.subs(Sequence.n, n)
        if retval == int(retval):
            return int(retval)
        return retval


def is_arithmetic(terms):
    """
    Checks if given terms make up an arithmetic sequence. Length of terms must be at least 3.
    """
    if len(terms) < 3:
        return False
    
    d = terms[1] - terms[0]
    for i in range(2, len(terms)):
        if terms[i] - terms[i - 1] != d:
            return False
    return True


def is_geometric(terms):
    """
    Checks if given terms make up a geometric sequence. Length of terms must be at least 3.
    """
    if len(terms) < 3:
        return False
    
    d = terms[1] / terms[0]
    for i in range(2, len(terms)):
        if terms[i] / terms[i - 1] != d:
            return False
    return True


def is_quadratic(terms):
    """
    Checks if given terms make up a quadratic sequence. Length of terms must be at least 4.
    """
    if len(terms) < 4:
        return False
    
    if is_arithmetic(terms):
        return False
    
    diffs = []
    for i in range(1, len(terms)):
        diffs.append(terms[i] - terms[i - 1])
    
    d = diffs[1] - diffs[0]
    for i in range(2, len(diffs)):
        if diffs[i] - diffs[i - 1] != d:
            return False
    return True
