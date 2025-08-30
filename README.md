# Kata TDD: Simulador del Juego Dudo Chileno

## Contexto
El Dudo es un juego tradicional chileno que se juega con dados en "cachos". Su tarea es implementar un simulador que maneje la lógica central del juego usando TDD. Como parece haber tantas variantes de reglas como jugadores, vamos a usar las reglas de la siguiente página: https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho

## Objetivos
- Aplicar TDD con Python3 y pytest y pytest-mock
- Usar mocking cuando sea apropiado
- Diseñar clases con responsabilidades claras
- Manejar lógica de juego compleja paso a paso
- Introducción a CI con GitHub Actions 


### Mocking Requerido
- **Generador de números aleatorios**: Para hacer pruebas deterministas
- **Aislamiento de las pruebas**: Mocks para aislar las diferentes partes de la lógica de negocio (excluyendo las clases orientadas a orquestaciones que pueden no hacer mocking)

###  Ejemplo de estructura
Aquí hay un ejemplo de estructura de proyecto que podría obtener y que le puede ayudar. Evidentemente, con el TDD podría obtener una estructura emergente diferente (más archivos fuente o algunos ausentes), pero debe respetar la organización del código en varios archivos dentro de /src y /tests.
En cualquier caso, hagan sus estructuras de a poquito a medida que avanzan con el TDD.


```
src/
├── juego/
│   ├── dado.py
│   ├── cacho.py
│   ├── validador_apuesta.py
│   ├── contador_pintas.py
│   ├── arbitro_ronda.py
│   └── gestor_partida.py
├── servicios/
│   └── generador_aleatorio.py
tests/
├── test_dado.py
├── test_cacho.py
├── test_validador_apuesta.py
├── test_contador_pintas.py
├── test_arbitro_ronda.py
└── test_gestor_partida.py
```

## Entregables
1. Código fuente con cobertura de pruebas > 90%
2. Todas las pruebas deben pasar
3. Implementación que siga principios SOLID
4. Historial de commits en el formato descrito
5. README con instrucciones de ejecución
6. Una GitHub Action que ejecute sus tests (¡Verde por el último commit!)



