# Temporizador con Alarma usando Pygame

Este proyecto es un temporizador interactivo que utiliza la biblioteca Pygame para mostrar el tiempo restante en pantalla y reproducir un sonido de alarma al finalizar.

## Requisitos

Para ejecutar este programa, necesitas:

- Python 3.x
- La biblioteca Pygame instalada: `pip install pygame`
- Un archivo de audio MP3 para la alarma llamado `Alarma de despertador.mp3` en el mismo directorio que el script.

## Uso

1. Ejecuta el programa en la terminal.
2. Ingresa los minutos y segundos que deseas para el temporizador.
3. El temporizador se mostrará en la pantalla.
4. Cuando el tiempo llegue a cero, sonará la alarma.

## Código principal

```python
import time
import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Fuente
fuente = pygame.font.Font(None, 74)

Pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Temporizador de la pantalla")

def mostrar_tiempo_restante(segundos_restantes):
    Pantalla.fill(NEGRO)
    minutos_restantes = segundos_restantes // 60
    segundos_restantes = segundos_restantes % 60
    tiempo_formateado = f"{minutos_restantes:02d}:{segundos_restantes:02d}"
    texto = fuente.render(tiempo_formateado, True, BLANCO)
    rect_texto = texto.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2))
    Pantalla.blit(texto, rect_texto)
    pygame.display.flip()

def alarma(segundos):
    tiempo_inicial = time.time()
    tiempo_transcurrido = 0

    while tiempo_transcurrido < segundos:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        segundos_restantes = int(segundos - tiempo_transcurrido)
        mostrar_tiempo_restante(segundos_restantes)
        time.sleep(1)

    # Reproducir el sonido de la alarma cuando el tiempo llegue a cero
    pygame.mixer.music.load("Alarma de despertador.mp3")
    pygame.mixer.music.play()

    # Mantener el programa activo mientras suena la alarma
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(0.1)

# Solicitar el tiempo de la alarma
minutos = int(input("Ingrese minutos: "))
segundos = int(input("Ingrese segundos: "))
segundos_totales = minutos * 60 + segundos

# Ejecutar la alarma
alarma(segundos_totales)
```

## Notas
- Puedes personalizar los colores, dimensiones de la pantalla o la fuente si lo deseas.
- checa que tengas el archivo mp3 o vere si lo dejo.

- Asta pronto... 
