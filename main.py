
import pygame
import random

from car import Rato
from colision import verificar_colisao

# Inicialização
pygame.init()

# Configuração da tela
LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Rato em Busca do Queijo")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (120, 180, 100)

# Carregar queijo
queijo = pygame.image.load(
    "imagens/queijo.png"
).convert_alpha()

queijo = pygame.transform.scale(queijo, (45, 45))

# Posição inicial do queijo
queijo_rect = queijo.get_rect(
    topleft=(
        random.randint(0, LARGURA - 45),
        random.randint(0, ALTURA - 45)
    )
)

# Criar rato
rato = Rato(100, 100)

# Pontuação
pontos = 0

fonte = pygame.font.SysFont("Arial", 28)

# Controle de FPS
relogio = pygame.time.Clock()

# Loop principal
rodando = True

while rodando:

    relogio.tick(60)

    # Eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

    # Capturar teclas
    teclas = pygame.key.get_pressed()

    # Movimentar rato
    rato.movimentar(teclas, LARGURA, ALTURA)

    # Verificar colisão
    if verificar_colisao(
        rato.rect, queijo_rect, LARGURA, ALTURA
    ):
        pontos += 1

    # Desenhar cenário
    tela.fill(VERDE)

    # Desenhar queijo
    tela.blit(queijo, queijo_rect)

    # Desenhar rato
    rato.desenhar(tela)

    # Mostrar pontuação
    texto = fonte.render(
        f"Queijos: {pontos}", True, PRETO
    )

    tela.blit(texto, (10, 10))

    # Atualizar tela
    pygame.display.update()

# Encerrar
pygame.quit()
