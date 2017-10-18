import pygame
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    def image(self):
        image = pygame.image.load("l.jpg")
        screen.blit(image,1350,1198)
