# Genetic-Algorithm for Graph Coloring Problem
This repo contains the program and report document about the implementation in Python of a Genetic Algorithm to solve the graph coloring problem.

### Developed by Damián García
The information in this document is in Spanish since I'm from Mexico and the project was for my Artificial Intelligence Techniques Class

## INTRODUCCIÓN
En este reporte se presenta el proyecto final para la materia de Técnicas de Inteligencia Artificial, el cuál consiste en seleccionar uno de los tres ejercicios del documento visto en clase llamado Algoritmos Genéticos (Ejercicios) e implementar un RGA, es decir, un algoritmo genético bidimensional para darle solución al ejercicio escogido. Para el proyecto final escogí el ejercicio número 3 del documento, el cuál se describirá a detalle a continuación, pero en resumen es el problema del coloreo de un grafo conexo y no dirigido de n vértices. Para la implementación de este proyecto, se usó el lenguaje de programación Python en su versión 3.8.5 y el IDE Visual Studio Code.

## DESARROLLO
### DESCRIPCIÓN DEL EJERCICIO
EJERCICIO3: Proponer un Algoritmo Genético Bidimensional para realizar el coloreo de un grafo no dirigido, conexo no pesado, con 3 colores diferentes. Este problema requiere mucho tiempo para obtenerse una solución, en especial cuando la cantidad de vértices es grande (superior a 20 vértices, donde se requieren varios días o semanas de cómputo). (Sugerencia: use un arreglo de n elementos para representar cada vértice, y en cada elemento puede ir uno de 3 posibles colores).

### COLOREO DE UN GRAFO
El problema del coloreo de un grafo consiste en, dado un grafo G conexo, unidireccional y no pesado de n vértices y m aristas, asignar un color a cada vértice del grafo de tal forma que ningún vértice adyacente tenga el mismo color. Para este ejercicio se pide que los colores a usar sean solo 3, sin embargo, hay otras versiones del problema del coloreo del grafo en el que se tiene que optimizar el número de colores que se usan para colorear los vértices de un grafo. Para efectos prácticos y de este ejercicio, se trabajará únicamente con los 3 colores que pide el ejercicio. Un ejemplo que ilustra lo comentado anteriormente se muestra a continuación:
![Grafo](img/img1.png)

