/// \file multi.h
/// \brief Este archivo contiene la declaración de las funciones multi() y delete_arr().
#pragma once

/// \brief Función para multiplicar dos enteros por 100.
///
/// \param x El primer entero.
/// \param y El segundo entero.
/// \return Puntero a un entero que devuelve los enteros multiplicados por 100.
extern "C" int* multi(int x, int y);

/// \brief Función para eliminar un arreglo dinámico de enteros.
///
/// \param ptr Puntero al arreglo que se desea eliminar.
extern "C" void delete_arr(int* ptr);