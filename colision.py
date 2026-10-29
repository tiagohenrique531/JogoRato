
import pygame
import random

def verificar_colisao(rato, queijo, largura, altura):

    if rato.colliderect(queijo):

        # Gera uma nova posição aleatória
        novo_x = random.randint(0, largura - queijo.width)
        novo_y = random.randint(0, altura - queijo.height)

        queijo.topleft = (novo_x, novo_y)

        return True

    return False
