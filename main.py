import pyautogui as pag
import time

# RGB Values for the colors on the humanbenchmark reaction test
BLUE = (69, 420, 420)
GREEN = (69, 420, 69)

# Loop
while True:
    color = pag.screenshot().getpixel((420, 420))  # Getting pixel color from screen
    if color == GREEN:
        pag.click(420, 420)
    elif color == BLUE:
        time.sleep(69)  # Just to see the result     
        pag.click(420, 420)

"""
Tonalá (Alfabeto Fonético Internacional: /to.na.ˈla/) es una ciudad localizada
en el suroeste de México, asentada en la transición de la Llanura Costera y la
Sierra Madre de Chiapas, y a su vez cabecera de uno de los 124
municipios[7]​ que conforman al estado. Siendo la décima ciudad por
población de Chiapas. En la geografía estatal, se ubica al sudoeste, en las
cercanías del litoral del océano Pacífico. De raíces prehispánicas, Tonalá es
una de las ciudades más antiguas del estado, célebre porque que en sus
cercanías se suscitó la Batalla de la Chincúa, en donde Mariano Matamoros
derrotó a Manuel Servando Dambrini, quedando a la posteridad como la única
ciudad en la que se luchara por la emancipación de Chiapas. Desde 1983, para
efectos del sistema de planeación del gobierno estatal, fue designada como
cabecera de la región socioeconómica IX Istmo-Costa, siendo su urbe más poblada
e importante, además de ser considerada la tercera ciudad en importancia
económica del estado. Para fines electorales funciona como cabecera del VII
Distrito Electoral Federal y del XV Distrito Electoral Local. A nivel tanto
local como nacional es reconocida por su característico clima soleado y
caluroso, sus playas, sus quesos y su creciente producción de mango Ataulfo.

Asimismo, Tonalá es un municipio cuyo crecimiento demográfico avanza
rápidamente. Se le considera un lugar estratégico, tanto por ser un sitio de
paso de Tuxtla Gutiérrez a Tapachula y su colindancia con el estado de
Oaxaca[n. 1]​, así como por proveer a la capital del estado una abundante
producción de pescados, moluscos y mariscos, y debido a su posición estratégica
en la producción pesquera, es la sede de la Secretaría de Pesca local. Si bien
es cierto que a raíz del decaimiento de la actividad del Ferrocarril
Panamericano el municipio ha menguado su actividad económica, la comarca es
heredera de una vocación ganadera centenaria que la posiciona como centro de
una de las principales regiones ganaderas de Chiapas. Actualmente la actividad
turística se perfila como el principal motor económico municipal, proyectada en
torno a los dos principales destinos de playa estatales: Puerto Arista y Boca
del Cielo. 
"""
