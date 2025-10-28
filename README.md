# 🐍 Snake Game

**Proyecto académico desarrollado para aplicar los conocimientos de la materia Estructura de Datos.**

## Descripción general
Este proyecto implementa el clásico juego de Snake, en el cual el jugador controla una serpiente que crece al comer manzanas, evitando chocar contra sí misma o las paredes.
El objetivo principal es aplicar conceptos de estructuras de datos y lógica de movimiento en 2D.

Existen dos versiones del juego, con diferentes formas de contar los movimientos:

Snake 1. los movimientos se cuentan cada que se presiona una tecla.
Snake 2. Los movimientos se cuentan cada que el cuerpo avanza un cuadrado.

## Características del juego

🍎 Manzana aleatoria:
Se genera en posiciones aleatorias del tablero, nunca sobre el cuerpo de la serpiente.

🔁 Reaparición de manzanas:
Después de comer una, la siguiente aparece de forma aleatoria entre 1 y 10 movimientos después.

⚡ Aumento progresivo de velocidad:
Con cada manzana, la serpiente se mueve más rápido, hasta un límite para conservar la jugabilidad.

💥 Condiciones de derrota:
El jugador pierde si la serpiente colisiona con su cuerpo o una pared.

## Objetivos de este juego
- Implementar estructuras de datos dinámicas (listas, colas, o matrices).
- Aplicar lógica de colisiones y generación aleatoria controlada.
- Practicar control de eventos, temporizadores y renderizado básico en Python.

## Cómo ejecutar

1. Clona este repositorio:
```bash
git clone https://github.com/Jcastanour/Snake-Game.git
cd Snake-Game
```

2. Ejecuta la versión que desees:
```bash
python SnakeGame.py
```
o
```bash
python SnakeGame2.0.py
```

## Tablero

![TABLERO2 0](https://github.com/Jcastanour/Snake-Game/assets/125745152/5dde6601-a1cf-42d9-8a85-14831db70105)

Partida en juego

![image](https://github.com/Jcastanour/Snake-Game/assets/125745152/34070846-d112-4328-8859-5e8cb5904e66)

Game over

![FONDOgameover](https://github.com/Jcastanour/Snake-Game/assets/125745152/65057eb8-fbce-483a-b380-bcb17555f5f8)


