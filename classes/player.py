import pygame
from .constants import WIDTH, HEIGHT

class Player:

    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 100, 100)
        self.speed = 10
        self.image = pygame.image.load('images/Player/down1.png').convert_alpha()
        self.original_image = self.image.copy()
        self.direction = 'down'

        # Imágenes para movimiento hacia la izquierda
        self.images_left = [pygame.image.load(f'images/Player/left{i}.png').convert_alpha() for i in range(1, 3)]
        self.index_left = 0

        # Imágenes para movimiento hacia la derecha
        self.images_right = [pygame.image.load(f'images/Player/right{i}.png').convert_alpha() for i in range(1, 3)]
        self.index_right = 0

        # Imágenes para movimiento hacia arriba
        self.images_up = [pygame.image.load(f'images/Player/up{i}.png').convert_alpha() for i in range(1, 3)]
        self.index_up = 0

        # Imágenes para movimiento hacia abajo
        self.images_down = [pygame.image.load(f'images/Player/down{i}.png').convert_alpha() for i in range(1, 3)]
        self.index_down = 0

        # Imágenes para disparo
        self.shoot_images_right = [pygame.image.load(f'images/Player/shoot_right.png').convert_alpha()]
        self.shoot_images_left = [pygame.image.load(f'images/Player/shoot_left.png').convert_alpha()]
        self.shoot_images_up = [pygame.image.load(f'images/Player/shoot_up.png').convert_alpha()]
        self.shoot_images_down = [pygame.image.load(f'images/Player/shoot_down.png').convert_alpha()]

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = 'left'
            # Incrementa el índice para la siguiente imagen
            self.index_left = (self.index_left + 1) % len(self.images_left)
            # Cambio de imagen para animación
            self.image = self.images_left[self.index_left]

    def move_right(self):
        if self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.direction = 'right'
            # Cambio de imagen para animación
            self.index_right = (self.index_right + 1) % len(self.images_right)
            self.image = self.images_right[self.index_right]

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed
            self.direction = 'up'
            # Cambio de imagen para animación
            self.index_up = (self.index_up + 1) % len(self.images_up)
            self.image = self.images_up[self.index_up]

    def move_down(self):
        if self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
            self.direction = 'down'
            # Cambio de imagen para animación
            self.index_down = (self.index_down + 1) % len(self.images_down)
            self.image = self.images_down[self.index_down]

    def move_up_left(self):
        if self.rect.top > 0 and self.rect.left > 0:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
            self.direction = 'up_left'

    def move_up_right(self):
        if self.rect.top > 0 and self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.rect.y -= self.speed
            self.direction = 'up_right'

    def move_down_left(self):
        if self.rect.bottom < HEIGHT and self.rect.left > 0:
            self.rect.x -= self.speed
            self.rect.y += self.speed
            self.direction = 'down_left'

    def move_down_right(self):
        if self.rect.bottom < HEIGHT and self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.rect.y += self.speed
            self.direction = 'down_right'

    def stop(self):
        pass

    def stop_left(self):
        self.index_left = 0
        self.image = self.images_left[self.index_left]

    def stop_right(self):
        self.index_right = 0
        self.image = self.images_right[self.index_right]

    def stop_up(self):
        self.index_up = 0
        self.image = self.images_up[self.index_up]

    def stop_down(self):
        self.index_down = 0
        self.image = self.images_down[self.index_down]

    def shoot(self):
        if self.direction == 'right':
            self.image = self.shoot_images_right[0]
        elif self.direction == 'left':
            self.image = self.shoot_images_left[0]
        elif self.direction == 'up':
            self.image = self.shoot_images_up[0]
        elif self.direction == 'down':
            self.image = self.shoot_images_down[0]

    def reset_image(self):
        self.image = self.original_image.copy()
