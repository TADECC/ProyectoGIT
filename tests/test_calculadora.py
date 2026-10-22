# test_calculadora.py

from src.calculadora import sumar
from src.calculadora import restar
from src.calculadora import multiplicar

def test_suma():
    assert sumar(2, 3) == 5

def test_resta():
    assert restar(10, 2) == 8

def test_multiplicacion():
    assert multiplicar(4, 5) == 20
