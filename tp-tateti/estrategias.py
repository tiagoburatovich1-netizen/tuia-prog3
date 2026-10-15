"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def minimax_max(problema, estado: List[List[str]]) -> float:
    """
    Función auxiliar para el jugador MAX en el algoritmo minimax.
    Entrada:
        problema: Instancia de la clase Tateti
        estado: Estado actual del tablero  
    Salida:
        float: Valor de utilidad del estado
    """
    if problema.test_terminal(estado):
        return problema.utilidad(estado)
    
    v = float('-inf')
    for accion in problema.acciones(estado):
        v = max(v, minimax_min(problema, problema.resultado(estado, accion)))
    return v

def minimax_min(problema, estado: List[List[str]]) -> float:
    """
    Función auxiliar para el jugador MIN en el algoritmo minimax.
    Entrada:
        problema: Instancia de la clase Tateti
        estado: Estado actual del tablero   
    Salida:
        float: Valor de utilidad del estado
    """
    if problema.test_terminal(estado):
        return problema.utilidad(estado)
    
    v = float('inf')
    for accion in problema.acciones(estado):
        v = min(v, minimax_max(problema, problema.resultado(estado, accion)))
    return v



def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """
    if tateti.jugador(estado) == JUGADOR_MAX:
        sucs = {
            accion: minimax_min(tateti, tateti.resultado(estado, accion))
            for accion in tateti.acciones(estado)
        }
        return max(sucs, key=sucs.get)  # Elige la acción con el valor máximo

    if tateti.jugador(estado) == JUGADOR_MIN:
        sucs = {
            accion: minimax_max(tateti, tateti.resultado(estado, accion))
            for accion in tateti.acciones(estado)
        }
        return min(sucs, key=sucs.get)  # Elige la acción con el valor mínimo

