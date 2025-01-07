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
