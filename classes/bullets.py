import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.direction = direction
        self.speed = 10

        # Selecciona la imagen correcta según la dirección
        if self.direction == 'up':
            self.image = pygame.image.load('images/bullets/up.png').convert_alpha()
        elif self.direction == 'down':
            self.image = pygame.image.load('images/bullets/down.png').convert_alpha()
        elif self.direction == 'left':
            self.image = pygame.image.load('images/bullets/left.png').convert_alpha()
        elif self.direction == 'right':
            self.image = pygame.image.load('images/bullets/right.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/shoot.mp3')
        self.shoot_sound.set_volume(0.4)
        self.shoot_sound.play()

    def update(self):
        if self.direction == 'up':
            self.rect.move_ip(0, -self.speed)
        elif self.direction == 'down':
            self.rect.move_ip(0, self.speed)
        elif self.direction == 'left':
            self.rect.move_ip(-self.speed, 0)
        elif self.direction == 'right':
            self.rect.move_ip(self.speed, 0)
        elif self.direction == 'up_left':
            self.rect.move_ip(-self.speed, -self.speed)
        elif self.direction == 'up_right':
            self.rect.move_ip(self.speed, -self.speed)
        elif self.direction == 'down_left':
            self.rect.move_ip(-self.speed, self.speed)
        elif self.direction == 'down_right':
            self.rect.move_ip(self.speed, self.speed)

        # Eliminar la bala si se sale de la pantalla
        if (self.rect.top <= 0 or self.rect.bottom >= pygame.display.get_surface().get_height() or
            self.rect.left <= 0 or self.rect.right >= pygame.display.get_surface().get_width()):
            self.kill()
