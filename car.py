
import pygame

class Rato:
    def __init__(self, x, y):
        self.imagem = pygame.image.load(
            "imagens/rato.png"
        ).convert_alpha()

        self.imagem = pygame.transform.scale(
            self.imagem, (60, 60)
        )

        self.rect = self.imagem.get_rect(topleft=(x, y))
        self.velocidade = 5

    def movimentar(self, teclas, largura, altura):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade

        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade

        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidade

        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidade

        # Impede o rato de sair da tela
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(largura, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(altura, self.rect.bottom)

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)
