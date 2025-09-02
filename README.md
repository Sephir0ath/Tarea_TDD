# Kata TDD: Simulador del Juego Dudo Chileno

## Contexto

El Dudo es un juego tradicional chileno que se juega con dados en "cachos". Su tarea es implementar un simulador que maneje la lógica central del juego usando TDD. Como parece haber tantas variantes de reglas como jugadores, vamos a usar las reglas de la siguiente página: https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho

## Pasos de ejecución y compilación
### Clonar el repositorio:
```bash
git clone "https://github.com/Sephir0ath/Tarea_TDD.git"
```

### Instalación de requerimientos:
Dentro de la carpeta que se genera en el repositorio, se ejecuta el siguiente comando:
```bash
 pip install -r requirements.txt
```
### Ejecución de tests
Para ejecutar los tests, después de instalar las dependencias con pip o equivalente, pueden usar:
```bash
pytest
o
python3 -m pytest
```

###  Coverage 
Para ejecutar el coverage del proyecto se debe ejecutar:
```bash
 python -m pytest --cov=src --cov-report=term-missing
```
Existe la alternativa de que se deba usar otros comandos similares como:
```bash
pytest --cov=src --cov-report=term-missing
o
 python3 -m pytest --cov=src --cov-report=term-missing
```

Se adjunta de todas maneras el coverage del proyecto:
<p align="center">
  <img src="https://github.com/Sephir0ath/Tarea_TDD/blob/main/coverage.png" alt="Imagen del coverage" width="400">
</p>

## Contribuyentes ✨
* [Juan Felipe Raysz Muñoz](https://github.com/Sephir0ath)
* [Tomás Alejandro Gutierrez Bizama](https://github.com/TomasGutierrez777)
* [Matías Ignacio Figueroa Vasquez](https://github.com/Matfigueroa20)
