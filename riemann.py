"""Calcular el área bajo la curva de la función f(x) = x^2 entre los puntos x = 2 y x = 5.
 Determine el área utilizando el método de Riemann con 4 subintervalos usando los datos de la derecha, izquierda y centro."""
import numpy as np

a = 2
b = 5
n = 4  # número de subintervalos
Δ_x = (b - a) / n

val_der = np.linspace(a + Δ_x, b, n)
val_izq = np.linspace(a, b - Δ_x, n)
val_med = np.linspace(a + (Δ_x / 2), b - (Δ_x / 2), n)

def f(x):
    x = x ** 2
    return x

def riemann_izq():
    integral = np.sum(Δ_x * f(val_izq))
    return integral

def riemann_der():
    integral = np.sum(Δ_x * f(val_der))
    return integral

def riemann_med():
    integral = np.sum(Δ_x * f(val_med))
    return integral

integral_der = riemann_der()
integral_izq = riemann_izq()
integral_med = riemann_med()

print("Resultados:")
print("Integral de Riemann por la derecha: ", integral_der)
print("Integral de Riemann por la izquierda: ", integral_izq)
print("Integral de Riemann por punto medio: ", integral_med)
