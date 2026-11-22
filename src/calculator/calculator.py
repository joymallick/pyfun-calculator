class Calculator:
    """
    Singleton Calculator instance performs basic calculations on numbers.

    Numbers can be given in various forms: as int, float, double or as string
    numbers, e.g. "123" or "1.600" or as Latin numbers "X", as single digit
    words: "three" (English, 3), "cinco" (Spanish, 5), "семь" (Russian, 7),
    "X" (Latin, 10) or "三" (Chinese, sān 3).

    See: https://sgra64.github.io/py-fun.github.io/src.calculator.html.
    """

    def add(_self, a, b):
        """
        Add two numbers.

        Args:
            a: the base number.
            b: the number to add.

        Returns:
            The sum of both numbers.

        Raises:
            ValueError: If an input number is not valid or not understood.
        """
        return as_num(a) + as_num(b)
    
    def sub(_self, a, b):
        """
        Subtract two numbers.

        Args:
            a: the base number.
            b: the number to subtract.

        Returns:
            The subtration of both numbers.

        Raises:
            ValueError: If an input number is not valid or not understood.
        """
        return as_num(a) - as_num(b)
    
    def mul(_self, a, b):
        """
        Multiply two numbers.

        Args:
            a: the base number.
            b: the number to multiply.

        Returns:
            The product of both numbers.

        Raises:
            ValueError: If an input number is not valid or not understood.
        """
        return as_num(a) * as_num(b)
    
    def div(_self, a, b):
        """
        Divide two numbers.

        Args:
            a: the base number.
            b: the number to divide.

        Returns:
            The division of both numbers.

        Raises:
            ValueError: If an input number is not valid or not understood.
            ZeroDivisionError: If a division by 0 is attempted.
        """
        try:
            return as_num(a) / as_num(b)
        except ZeroDivisionError:
            print("Cannot divide by zero, return infinity.")
            return float('inf')
        
    
    def factorize(_self, n):
        """
        Factorize number into prime factors.

        Args:
            n: the number to factorize into prime factors.

        Returns:
            The list of prime factors.

        Raises:
            ValueError: If an input number is not valid, not understood or negative.
        """
        return factorize(as_num(n))
        

    _instance = None

    def __init__(self):
        pass

    # Singleton pattern by overloading the new operator, see
    # https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    
def as_num(arg):
    return 0 if arg==None else \
        arg if isinstance(arg, (int, float)) else \
        _str_val(arg.strip()) if isinstance(arg, str) else \
        _complex_val(arg) if isinstance(arg, complex) else 0
_numbers = {
    "zero": 0,
    "one": 1 , "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6 , "seven": 7, "eight": 8, "nine": 9, "ten": 10,

    # no 'zero' in latin numbers
    "i": 1 , "ii": 2, "iii": 3, "iv": 4, "v": 5,
    "vi": 6 , "vii": 7, "viii": 8, "ix": 9, "x": 10,

    "null": 0,
    "eins": 1 , "zwei": 2, "drei": 3, "vier": 4, "fünf": 5, "fuenf": 5,
    "sechs": 6 , "sieben": 7, "acht": 8, "neun": 9, "zehn": 10,

    "cero": 0,
    "uno": 1 , "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,

    "ноль": 0,
    "один": 1 , "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,

    "零": 0,
    "一": 1 , "二": 2, "三": 3, "四": 4, "五": 5,
    "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
}

def _str_val(arg):
    try:
        return int(arg)
    except ValueError:
        try:
            return float(arg)
        except ValueError:
            try:
                return _numbers[arg]
            except KeyError:
                try:
                    return _numbers[arg.lower()]
                except KeyError:
                    print(f'Cannot convert \"{arg}\" to number, 0 used')
                    return 0

def _complex_val(arg):
    return 0

def factorize(n):
    
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors