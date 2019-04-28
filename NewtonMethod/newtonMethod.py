#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sympy

class Newton:
    def __init__(self,equation):
        self.__error = 1000
        self.__x_value = 0
        self.__n = 0
        self.__equation = equation
    def getError(self):
        return self.__error
    def getN(self):
        return self.__n
    def getX(self):
        return self.__x_value
    def setEquation(self,new_eq):
        self.__equation = new_eq
    def Module(self,value):
        if value < 0:
            value = -value
        return value
    def solveEq(self,x_value,max_iterations,tolerance):
        self.__x_value = x_value
        derivate_f = sympy.diff(self.__equation,x)
        f_value = self.__equation.subs(x,self.__x_value)
        self.__error = self.Module(f_value)
        out = True
        while (self.__error > tolerance):
            self.__n += 1
            if self.__n > max_iterations:
                out = False
                break
            self.__x_value = self.__x_value - f_value / derivate_f.subs(x,self.__x_value)
            f_value = self.__equation.subs(x,self.__x_value)
            self.__error = self.Module(f_value)
        return out
    def __str__(self):
        return "x = {:12f}\nAproximation error = {:12f}\n{:d} iterations made in total".format(self.__x_value,self.__error,self.__n) 
        
if __name__ == "__main__":
    x = sympy.symbols('x')
    equation = sympy.exp(0.2*x) - sympy.exp(-0.8*x) - 2
    solution = Newton(equation)
    for i in range(0,15):
        print("For xi = {:d}".format(i))
        DidItWorked = solution.solveEq(i,15,0.00000001)
        print(solution)
        print("Did the program finish before exceeding the iterations limit?",DidItWorked)
        print("-----------------------------------------------------")
    
    
    
    