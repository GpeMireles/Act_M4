/// \file multi.cpp
/// \brief Este archivo contiene la implementacion de la función multi() y la función delete_arr().

#include <iostream>
#include "multi.h"

/// \brief Función para multiplicar dos enteros y devolver el resultado multiplicado por 100.
///
/// \param x El primer entero.
/// \param y El segundo entero.
/// \return Puntero a un arreglo de dos enteros. El primer elemento es el resultado de la multiplicación de x por 100, y el segundo elemento es el resultado de la multiplicación de y por 100.
int* multi(int x, int y)
{
    int*c = new int[2];
    c[0] = x*100;
    c[1] = y*100;
    return c;
}

/// \brief Función para eliminar un arreglo dinámico de enteros.
///
/// \param ptr Puntero al arreglo que se desea eliminar.
void delete_arr(int* ptr){
    delete[] ptr;
}