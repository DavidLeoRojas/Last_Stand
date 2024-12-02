import sys

import pygame
import random

from lineasespera.LineaEspera import LineasEspera
from caminatas.CaminataH import CaminataH
from caminatas.CaminataHVD import CaminataHVD

from controls import move_player, move_player_with_joystick
from classes.constants import WIDTH, HEIGHT, FPS, SHOOT_DELAY
from functions import show_game_over, music_background
from menu import show_menu, animate_screen

from classes.player import Player
from classes.bullets import Bullet
from classes.refill import BulletRefill, HealthRefill, DoubleRefill, ExtraScore
from classes.explosives import Explosives, Explosives2, Hole
from classes.explosions import Explosion, Explosion2
from classes.enemies import Enemy1, Enemy2
from classes.bosses import Boss1, Boss2, Boss3

from Disparo_Montecarlo import DisparoMontecarloClass
from PowerUp_Markov import PowerUpMarkovClass

disparos = DisparoMontecarloClass()
poderes = PowerUpMarkovClass()

pygame.init()
music_background()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption("Last Stand")
clock = pygame.time.Clock()


def main():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('game_sounds/game.mp3')
    pygame.mixer.music.play(-1)
    animate_screen()


explosions = pygame.sprite.Group()
explosions2 = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy1_group = pygame.sprite.Group()
enemy2_group = pygame.sprite.Group()
boss1_group = pygame.sprite.Group()
boss2_group = pygame.sprite.Group()
boss3_group = pygame.sprite.Group()
bullet_refill_group = pygame.sprite.Group()
health_refill_group = pygame.sprite.Group()
double_refill_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()
meteor2_group = pygame.sprite.Group()
extra_score_group = pygame.sprite.Group()
black_hole_group = pygame.sprite.Group()
enemy2_bullets = pygame.sprite.Group()

boss1_bullets = pygame.sprite.Group()
boss2_bullets = pygame.sprite.Group()
boss3_bullets = pygame.sprite.Group()

boss1_health = 75
boss1_health_bar_rect = pygame.Rect(0, 0, 75, 5)
boss1_spawned = False

boss2_health = 100
boss2_health_bar_rect = pygame.Rect(0, 0, 100, 5)
boss2_spawned = False

boss3_health = 150
boss3_health_bar_rect = pygame.Rect(0, 0, 150, 5)
boss3_spawned = False

bg_y_shift = -HEIGHT
background_img = pygame.image.load('images/bg/background.jpg').convert()
background_img2 = pygame.image.load('images/bg/background2.jpg').convert()
background_img3 = pygame.image.load('images/bg/background3.jpg').convert()
background_img4 = pygame.image.load('images/bg/background4.jpg').convert()
background_top = background_img.copy()
current_image = background_img
new_background_activated = False

explosion_images = [pygame.image.load(
    f"images/explosion/explosion{i}.png") for i in range(8)]
explosion2_images = [pygame.image.load(
    f"images/explosion2/explosion{i}.png") for i in range(18)]
explosion3_images = [pygame.image.load(
    f"images/explosion3/explosion{i}.png") for i in range(18)]



# Establecer las imágenes de la animación para cada dirección de movimiento
enemy1_walk_left = [
    pygame.image.load('images/enemy/enemy1_left1.png').convert_alpha()
]
enemy1_walk_right = [
    pygame.image.load('images/enemy/enemy1_right1.png').convert_alpha()
]
enemy1_walk_back = [
    pygame.image.load('images/enemy/enemy1_back1.png').convert_alpha()
]
enemy1_walk_down = [
    pygame.image.load('images/enemy/enemy1_down1.png').convert_alpha()
]

# Diccionario que mapea las direcciones a las listas de imágenes correspondientes
enemy1_walk_images = {
    "left": enemy1_walk_left,
    "right": enemy1_walk_right,
    "up": enemy1_walk_back,
    "down": enemy1_walk_down
}


# Establecer las imágenes de la animación para cada dirección de movimiento
enemy2_walk_left = [
    pygame.image.load('images/enemy/enemy2_left1.png').convert_alpha()
]
enemy2_walk_right = [
    pygame.image.load('images/enemy/enemy2_right1.png').convert_alpha()
]
enemy2_walk_back = [
    pygame.image.load('images/enemy/enemy2_back1.png').convert_alpha()
]
enemy2_walk_down = [
    pygame.image.load('images/enemy/enemy2_down1.png').convert_alpha()
]

# Diccionario que mapea las direcciones a las listas de imágenes correspondientes
enemy2_walk_images = {
    "left": enemy2_walk_left,
    "right": enemy2_walk_right,
    "up": enemy2_walk_back,
    "down": enemy2_walk_down
}


# Establecer las imágenes de la animación para cada dirección de movimiento
enemy3_walk_left = [
    pygame.image.load('images/enemy/enemy3_left1.png').convert_alpha()
]
enemy3_walk_right = [
    pygame.image.load('images/enemy/enemy3_right1.png').convert_alpha()
]
enemy3_walk_back = [
    pygame.image.load('images/enemy/enemy3_back1.png').convert_alpha()
]
enemy3_walk_down = [
    pygame.image.load('images/enemy/enemy3_down1.png').convert_alpha()
]

# Diccionario que mapea las direcciones a las listas de imágenes correspondientes
enemy3_walk_images = {
    "left": enemy3_walk_left,
    "right": enemy3_walk_right,
    "up": enemy3_walk_back,
    "down": enemy3_walk_down
}

enemy1_img = [
    pygame.image.load('images/enemy/enemy2_down1.png').convert_alpha(),
    pygame.image.load('images/enemy/enemy3_down1.png').convert_alpha()
]

enemy2_img = [
    pygame.image.load('images/enemy/enemy1_down1.png').convert_alpha()
]

boss1_img = pygame.image.load('images/boss/boss1.png').convert_alpha()
boss2_img = pygame.image.load('images/boss/boss2.png').convert_alpha()
boss3_img = pygame.image.load('images/boss/boss3.png').convert_alpha()
caminata_boss1 = CaminataH()
caminata_boss2 = CaminataHVD()
caminata_boss3 = CaminataHVD()

health_refill_img = pygame.image.load(
    'images/refill/health_refill.png').convert_alpha()
bullet_refill_img = pygame.image.load(
    'images/refill/bullet_refill.png').convert_alpha()
double_refill_img = pygame.image.load(
    'images/refill/double_refill.png').convert_alpha()
extra_score_img = pygame.image.load(
    'images/refill/extra_points.png').convert_alpha()
score_coin_img = pygame.image.load(
    'images/score/score_coin.png').convert_alpha()

explosive_imgs = [
    pygame.image.load('images/explosives/explosive_1.png').convert_alpha()
]
explosive2_imgs = [
    pygame.image.load('images/explosives/explosive1_1.png').convert_alpha(),
    pygame.image.load('images/explosives/explosive1_2.png').convert_alpha()
]

hole_imgs = [
    pygame.image.load('images/hole/hole.png').convert_alpha(),
    pygame.image.load('images/hole/hole2.png').convert_alpha()
]

initial_player_pos = (WIDTH // 2, HEIGHT - 100)

score = 0
hi_score = 0
player = Player()
player_life = 2000
bullet_counter = 200

paused = False
running = True

joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

if show_menu:
    import menu
    menu.main()

is_shooting = False
last_shot_time = 0

is_shooting_animation = False

extra_points = False
power_up_time = 0
power_spawn_time = 0
power_is = False
# pasar el intervalo con máximo y mínimo
lista_lineas_espera = LineasEspera().caminar(1000,4000) #maximo y minimo en segundos
lista_final = [] # salmacena la hora del sistema + el número actual de la lista + el tiempo de carga del juego
for i in range(len(lista_lineas_espera)):
    lista_final.append((pygame.time.get_ticks() + lista_lineas_espera[i]) + 5000)# 5000 tiempo de carga del juego

while running:
    # si se supera el tiempo de aparicion de poder lo agrega - con el fin de que no todo el tiempo esten apareciendo poderes
    if pygame.time.get_ticks() >= power_spawn_time and not power_is:
        print("Mayores")
        print(pygame.time.get_ticks())
        power_is = True
        poder = poderes.obtenerSiguientePoder() # aplicacion markov
        print("Poder verdadero")
        if poder == "bullet_refill":
            bullet_refill = BulletRefill(
                random.randint(50, WIDTH - 30),
                random.randint(-HEIGHT, -30),
                bullet_refill_img,
            )
            bullet_refill_group.add(bullet_refill)
        elif poder == "health":
            health_refill = HealthRefill(
                random.randint(50, WIDTH - 30),
                random.randint(-HEIGHT, -30),
                health_refill_img,
            )
            health_refill_group.add(health_refill)
        elif poder == "double_refill":
            double_refill = DoubleRefill(
                random.randint(50, WIDTH - 30),
                random.randint(-HEIGHT, -50),
                double_refill_img,
            )
            double_refill_group.add(double_refill)
        else:
            extra_score = ExtraScore(
                random.randint(60, WIDTH - 60),
                random.randint(-HEIGHT, -40 -
                               extra_score_img.get_rect().height),
                extra_score_img,
            )
            extra_score_group.add(extra_score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not paused:
                if bullet_counter > 0 and pygame.time.get_ticks() - last_shot_time > SHOOT_DELAY:
                    last_shot_time = pygame.time.get_ticks()

                    # Cambiar la imagen del jugador al disparar
                    player.shoot()

                    # Crear y disparar la bala en la dirección actual del jugador
                    if player.direction == 'right':
                        bullet = Bullet(player.rect.right   ,
                                        player.rect.centery, player.direction)
                    elif player.direction == 'left':
                        bullet = Bullet(
                            player.rect.left, player.rect.centery, player.direction)
                    elif player.direction == 'up':
                        bullet = Bullet(player.rect.centerx,
                                        player.rect.top, player.direction)
                    elif player.direction == 'down':
                        bullet = Bullet(player.rect.centerx-40,
                                        player.rect.bottom, player.direction)

                    bullets.add(bullet)
                    bullet_counter -= 1

            elif event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.key == pygame.K_p or event.key == pygame.K_PAUSE:
                paused = not paused
            elif not paused:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_UP:
                    player.move_up()
                elif event.key == pygame.K_DOWN:
                    player.move_down()
                elif event.key == pygame.K_a:
                    player.move_up_left()
                elif event.key == pygame.K_d:
                    player.move_up_right()
                elif event.key == pygame.K_z:
                    player.move_down_left()
                elif event.key == pygame.K_x:
                    player.move_down_right()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and player.original_image is not None:
                player.image = player.original_image.copy()
                is_shooting = False
            elif not paused:
                if event.key == pygame.K_LEFT:
                    player.stop_left()
                elif event.key == pygame.K_RIGHT:
                    player.stop_right()
                elif event.key == pygame.K_UP:
                    player.stop_up()
                elif event.key == pygame.K_DOWN:
                    player.stop_down()

        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0 and not paused:
                is_shooting = True
                if bullet_counter > 0:
                    bullet = Bullet(player.rect.centerx , player.rect.top)
                    bullets.add(bullet)
                    bullet_counter -= 1
            elif event.button == 7:
                paused = not paused
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 0 and player.original_image is not None:
                is_shooting = False

    if pygame.time.get_ticks() - last_shot_time > SHOOT_DELAY and is_shooting and not paused:
        if bullet_counter > 0:
            last_shot_time = pygame.time.get_ticks()
            bullet = Bullet(player.rect.centerx , player.rect.top)
            bullets.add(bullet)
            bullet_counter -= 1

    if extra_points == True and power_up_time < pygame.time.get_ticks():  #solo verificamos si el extra de puntos esta activo y ya paso el tiempo
        extra_points = False #desactivando puntos extra
        print("Desactivar")

    if joystick:
        if not paused:
            move_player_with_joystick(joystick, player)

    if paused:
        font = pygame.font.SysFont('Comic Sans MS', 40)
        text = font.render("PAUSE", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        continue

    # Control del disparo continuo mientras se mantiene presionada la tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not paused:
        if bullet_counter > 0 and pygame.time.get_ticks() - last_shot_time > SHOOT_DELAY:
            last_shot_time = pygame.time.get_ticks()

            # Cambiar la imagen del jugador al disparar
            player.shoot()

            # Crear y disparar la bala en la dirección actual del jugador
            if player.direction == 'right':
                bullet = Bullet(player.rect.right,
                                player.rect.centery, player.direction)
            elif player.direction == 'left':
                bullet = Bullet(player.rect.left,
                                player.rect.centery, player.direction)
            elif player.direction == 'up':
                bullet = Bullet(player.rect.centerx,
                                player.rect.top, player.direction)
            elif player.direction == 'down':
                bullet = Bullet(player.rect.centerx-40,
                                player.rect.bottom, player.direction)

            bullets.add(bullet)
            bullet_counter -= 1

    if not paused:
        move_player(keys, player)

        screen.blit(current_image, (0, bg_y_shift))
        background_top_rect = background_top.get_rect(topleft=(0, bg_y_shift))
        background_top_rect.top = bg_y_shift + HEIGHT
        screen.blit(background_top, background_top_rect)

    bg_y_shift += 1
    if bg_y_shift >= 0:
        bg_y_shift = -HEIGHT

    if score > 3000:
        bg_y_shift += 2

    if score >= 3000 and not new_background_activated:
        current_image = background_img2
        background_top = background_img2.copy()
        new_background_activated = True

    if score >= 10000 and new_background_activated:
        current_image = background_img3
        background_top = background_img3.copy()

    if score >= 15000 and new_background_activated:
        current_image = background_img4
        background_top = background_img4.copy()

    if score == 0:
        current_image = background_img
        background_top = background_img.copy()
        new_background_activated = False

    screen.blit(current_image, (0, bg_y_shift))
    background_top_rect = background_top.get_rect(topleft=(0, bg_y_shift))
    background_top_rect.top = bg_y_shift + HEIGHT
    screen.blit(background_top, background_top_rect)

    if score > hi_score:
        hi_score = score
    #aplicacion linea de espera
    
    if len(lista_final) != 0 and pygame.time.get_ticks() > lista_final[0]:
        lista_final.pop(0)
        enemy_img = random.choice(enemy1_img)
        enemy_walk_images = {}  # Inicializamos un diccionario vacío para las imágenes de caminata

        # Si la imagen escogida es la primera de la lista
        if enemy_img == enemy1_img[0]:
            enemy_walk_images = enemy2_walk_images
        # Si la imagen escogida es la segunda de la lista
        elif enemy_img == enemy1_img[1]:
            enemy_walk_images = enemy3_walk_images

        enemy_object = Enemy1(
            random.randint(100, WIDTH - 50),
            random.randint(-HEIGHT, -50),
            enemy_img,
            enemy_walk_images,
        )
        enemy1_group.add(enemy_object)

    if score >= 3000 and random.randint(0, 40) == 0 and len(enemy2_group) < 2:
        enemy_img = random.choice(enemy2_img)
        enemy2_object = Enemy2(
            random.randint(200, WIDTH - 100),
            random.randint(-HEIGHT, -100),
            enemy_img,
        )
        enemy2_group.add(enemy2_object)

    if score >= 5000 and not boss1_spawned:
        pygame.mixer.Sound('game_sounds/warning.mp3').play()
        boss1_img = boss1_img
        boss1_object = Boss1(
            random.randint(200, WIDTH - 100),
            random.randint(-HEIGHT, -100),
            boss1_img,
            caminata_boss1 #aplication caminata 
        )
        boss1_group.add(boss1_object)
        boss1_spawned = True

    if score >= 10000 and not boss2_spawned:
        pygame.mixer.Sound('game_sounds/warning.mp3').play()
        boss2_img = boss2_img
        boss2_object = Boss2(
            random.randint(200, WIDTH - 100),
            random.randint(-HEIGHT, -100),
            boss2_img,
            caminata_boss2
        )
        boss2_group.add(boss2_object)
        boss2_spawned = True

    if score >= 15000 and not boss3_spawned:
        pygame.mixer.Sound('game_sounds/warning.mp3').play()
        boss3_img = boss3_img
        boss3_object = Boss3(
            random.randint(200, WIDTH - 100),
            random.randint(-HEIGHT, -100),
            boss3_img,
            caminata_boss3
        )
        boss3_group.add(boss3_object)
        boss3_spawned = True

    if score >= 500 and power_is:
        power_is = False
        print("falso")
        power_spawn_time = pygame.time.get_ticks() + 6000   #cada cuanto estimado aparece un poder 6 segundos
        print(power_spawn_time)


    if score > 3000 and random.randint(0, 100) == 0:
        meteor_img = random.choice(explosive_imgs)
        meteor_object = Explosives(
            random.randint(0, 50),
            random.randint(0, 50),
            meteor_img,
        )
        meteor_group.add(meteor_object)

    if random.randint(0, 90) == 0:
        meteor2_img = random.choice(explosive2_imgs)
        meteor2_object = Explosives2(
            random.randint(100, WIDTH - 50),
            random.randint(-HEIGHT, -50 - meteor2_img.get_rect().height),
            meteor2_img,
        )
        meteor2_group.add(meteor2_object)

    if score > 1000 and random.randint(0, 1000) == 0:
        black_hole_img = random.choice(hole_imgs)
        black_hole_object = Hole(
            random.randint(100, WIDTH - 50),
            random.randint(-HEIGHT, -50 - black_hole_img.get_rect().height),
            black_hole_img,
        )
        black_hole_group.add(black_hole_object)

    if player_life <= 0:

        screen_rect = screen.get_rect()
        image_rect = game_over_images[0].get_rect()
        image_position = (screen_rect.centerx - image_rect.width //
                          2, screen_rect.centery - image_rect.height // 2)

        for game_over_image in game_over_images:
            screen.blit(game_over_image, image_position)
            pygame.display.flip()
            pygame.time.delay(1000)  # Esperar un segundo entre cada imagen
            # Limpiar la pantalla después de mostrar cada imagen
            screen.fill((0, 0, 0))
            pygame.display.flip()

        show_game_over(score)
        boss1_spawned = False
        boss1_health = 75
        boss2_spawned = False
        boss2_health = 100
        boss3_spawned = False
        boss3_health = 150
        score = 0
        player_life = 200
        bullet_counter = 200
        player.rect.topleft = initial_player_pos
        bullets.empty()
        bullet_refill_group.empty()
        health_refill_group.empty()
        double_refill_group.empty()
        extra_score_group.empty()
        black_hole_group.empty()
        meteor_group.empty()
        meteor2_group.empty()
        enemy1_group.empty()
        enemy2_group.empty()
        boss1_group.empty()
        boss2_group.empty()
        boss3_group.empty()
        explosions.empty()
        explosions2.empty()

    for black_hole_object in black_hole_group:
        black_hole_object.update()
        black_hole_object.draw(screen)

        if black_hole_object.rect.colliderect(player.rect):
            speed = 1
            # aplications of dinamic of sistems
            # for of dinamic of systems was used for the continuos damage funcion in the tramps or monster holes
            # dinamica de sistemas incorporado para funcion de daño continuo en las trampas o agujeros de monstruos
            player_life -= 0.5 * speed
            black_hole_object.sound_effect.play()

        if score >= 5000:
            meteor2_object.speed = 2
            speed = 2
        if score >= 10000:
            meteor2_object.speed = 3
            speed = 3
        if score >= 15000:
            meteor2_object.speed = 4
            speed = 4
        if score >= 20000:
            meteor2_object.speed = 6
            speed = 6

    for bullet_refill in bullet_refill_group:

        bullet_refill.update()
        bullet_refill.draw(screen)

        if player.rect.colliderect(bullet_refill.rect):
            if bullet_counter < 200:
                bullet_counter += 50
                if bullet_counter > 200:
                    bullet_counter = 200
                bullet_refill.kill()
                bullet_refill.sound_effect.play()
            else:
                bullet_refill.kill()
                bullet_refill.sound_effect.play()

    for health_refill in health_refill_group:
        health_refill.update()
        health_refill.draw(screen)

        if player.rect.colliderect(health_refill.rect):
            if player_life < 200:
                player_life += 50
                if player_life > 200:
                    player_life = 200
                health_refill.kill()
                health_refill.sound_effect.play()
            else:
                health_refill.kill()
                health_refill.sound_effect.play()

    for extra_score in extra_score_group:
        extra_score.update()
        extra_score.draw(screen)

        if player.rect.colliderect(extra_score.rect):
            score += 40
            extra_points = True
            power_up_time = pygame.time.get_ticks() + 10000 #el poder de extra puntaje dura alrededor de 10 segundos
            extra_score.kill()
            extra_score.sound_effect.play()

        if score >= 3000:
            extra_score.speed = 2
        if score >= 10000:
            extra_score.speed = 4
        if score >= 15000:
            extra_score.speed = 6
        if score >= 20000:
            extra_score.speed = 8

    for double_refill in double_refill_group:
        double_refill.update()
        double_refill.draw(screen)
          
        if player.rect.colliderect(double_refill.rect):
            if player_life < 200:
                player_life += 50
                if player_life > 200:
                    player_life = 200
            if bullet_counter < 200:
                bullet_counter += 50
                if bullet_counter > 200:
                    bullet_counter = 200
                double_refill.kill()
                double_refill.sound_effect.play()
            else:
                double_refill.kill()
                double_refill.sound_effect.play()

    for meteor_object in meteor_group:
        meteor_object.update()
        meteor_object.draw(screen)

        if meteor_object.rect.colliderect(player.rect):
            player_life -= 10
            explosion = Explosion(meteor_object.rect.center, explosion_images)
            explosions.add(explosion)
            meteor_object.kill()
            score += 50

        bullet_collisions = pygame.sprite.spritecollide(
            meteor_object, bullets, True)
        for bullet_collision in bullet_collisions:
            explosion = Explosion(meteor_object.rect.center, explosion_images)
            explosions.add(explosion)
            meteor_object.kill()
            score += 80
            if extra_points:
                score += 20

        if score >= 3000:
            meteor_object.speed = 4
        if score >= 10000:
            meteor_object.speed = 6
        if score >= 15000:
            meteor_object.speed = 8
        if score >= 20000:
            meteor_object.speed = 10

    for meteor2_object in meteor2_group:
        meteor2_object.update()
        meteor2_object.draw(screen)

        if meteor2_object.rect.colliderect(player.rect):
            player_life -= 10
            explosion = Explosion(meteor2_object.rect.center, explosion_images)
            explosions.add(explosion)
            meteor2_object.kill()
            score += 20

        bullet_collisions = pygame.sprite.spritecollide(
            meteor2_object, bullets, True)
        for bullet_collision in bullet_collisions:
            explosion = Explosion(meteor2_object.rect.center, explosion_images)
            explosions.add(explosion)
            meteor2_object.kill()
            score += 40
            if extra_points:
                score += 20

        if score >= 3000:
            meteor2_object.speed = 4
        if score >= 10000:
            meteor2_object.speed = 6
        if score >= 15000:
            meteor2_object.speed = 8
        if score >= 20000:
            meteor2_object.speed = 10

    for enemy_object in enemy1_group:
        enemy_object.update(enemy1_group)
        enemy1_group.draw(screen)

        if enemy_object.rect.colliderect(player.rect):
            player_life -= 10
            explosion = Explosion(enemy_object.rect.center, explosion_images)
            explosions.add(explosion)
            enemy_object.kill()
            score += 20

        bullet_collisions = pygame.sprite.spritecollide(
            enemy_object, bullets, True)
        for bullet_collision in bullet_collisions:
            explosion = Explosion(enemy_object.rect.center, explosion_images)
            explosions.add(explosion)
            enemy_object.kill()
            score += 50
            if extra_points:
                score += 20

    for enemy2_object in enemy2_group:
        enemy2_object.update(enemy2_group, enemy2_bullets, player)
        enemy2_group.draw(screen)
        enemy2_bullets.update()
        enemy2_bullets.draw(screen)

        if enemy2_object.rect.colliderect(player.rect):
            player_life -= 40
            explosion2 = Explosion2(
                enemy2_object.rect.center, explosion2_images)
            explosions2.add(explosion2)
            enemy2_object.kill()
            score += 20

        bullet_collisions = pygame.sprite.spritecollide(
            enemy2_object, bullets, True)
        for bullet_collision in bullet_collisions:
            explosion2 = Explosion2(
                enemy2_object.rect.center, explosion2_images)
            explosions2.add(explosion2)
            enemy2_object.kill()
            score += 80
            if extra_points:
                score += 20
                print("Puntos extra de enemigo 2")

        for enemy2_bullet in enemy2_bullets:
            if enemy2_bullet.rect.colliderect(player.rect):
                player_life -= 10
                explosion = Explosion(player.rect.center, explosion3_images)
                explosions.add(explosion)
                enemy2_bullet.kill()

    for boss1_object in boss1_group:
        boss1_object.update(boss1_bullets, player)
        boss1_group.draw(screen)
        boss1_bullets.update()
        boss1_bullets.draw(screen)

        if boss1_object.rect.colliderect(player.rect):
            player_life -= 1

        bullet_collisions = pygame.sprite.spritecollide(
            boss1_object, bullets, True)
        for bullet_collision in bullet_collisions:
            explosion2 = Explosion(boss1_object.rect.center, explosion2_images)
            explosions2.add(explosion2)
            boss1_health -= disparos.obtenerDisparo() # aplication montecarlo
            if boss1_health <= 0:
                explosion = Explosion2(
                    boss1_object.rect.center, explosion3_images)
                explosions.add(explosion)
                boss1_object.kill()
                score += 400
                if extra_points:
                    score += 40
                   

        for boss1_bullet in boss1_bullets:
            if boss1_bullet.rect.colliderect(player.rect):
                player_life -= 20
                explosion = Explosion(player.rect.center, explosion3_images)
                explosions.add(explosion)
                boss1_bullet.kill()

        if boss1_health <= 0:
            explosion = Explosion2(boss1_object.rect.center, explosion2_images)
            explosions2.add(explosion)
            boss1_object.kill()

    if boss1_group:
        boss1_object = boss1_group.sprites()[0]
        boss1_health_bar_rect.center = (
            boss1_object.rect.centerx, boss1_object.rect.top - 5)
        pygame.draw.rect(screen, (255, 0, 0), boss1_health_bar_rect)
        pygame.draw.rect(screen, (0, 255, 0), (boss1_health_bar_rect.left,
                         boss1_health_bar_rect.top, boss1_health, boss1_health_bar_rect.height))

    for boss2_object in boss2_group:
        boss2_object.update(boss2_bullets, player)
        boss2_group.draw(screen)
        boss2_bullets.update()
        boss2_bullets.draw(screen)

        if boss2_object.rect.colliderect(player.rect):
            player_life -= 2

        bullet_collisions = pygame.sprite.spritecollide(
            boss2_object, bullets, True)
        for bullet_collision in bullet_collisions:
            explosion2 = Explosion2(
                boss2_object.rect.center, explosion2_images)
            explosions2.add(explosion2)
            boss2_health -= disparos.obtenerDisparo()
            if boss2_health <= 0:
                explosion2 = Explosion2(
                    boss2_object.rect.center, explosion3_images)
                explosions2.add(explosion2)
                boss2_object.kill()
                score += 800
                if extra_points:
                    score += 80

        for boss2_bullet in boss2_bullets:
            if boss2_bullet.rect.colliderect(player.rect):
                player_life -= 30
                explosion = Explosion(player.rect.center, explosion3_images)
                explosions.add(explosion)
                boss2_bullet.kill()

        if boss2_health <= 0:
            explosion = Explosion2(boss2_object.rect.center, explosion2_images)
            explosions2.add(explosion)
            boss2_object.kill()

    if boss2_group:
        boss2_object = boss2_group.sprites()[0]
        boss2_health_bar_rect.center = (
            boss2_object.rect.centerx, boss2_object.rect.top - 5)
        pygame.draw.rect(screen, (255, 0, 0), boss2_health_bar_rect)
        pygame.draw.rect(screen, (0, 255, 0), (boss2_health_bar_rect.left,
                         boss2_health_bar_rect.top, boss2_health, boss2_health_bar_rect.height))

    for boss3_object in boss3_group:
        boss3_object.update(boss3_bullets, player)
        boss3_group.draw(screen)
        boss3_bullets.update()
        boss3_bullets.draw(screen)

        if boss3_object.rect.colliderect(player.rect):
            player_life -= 3

        bullet_collisions = pygame.sprite.spritecollide(
            boss3_object, bullets, True)
        for bullet_collision in bullet_collisions:
            explosion2 = Explosion2(
                boss3_object.rect.center, explosion2_images)
            explosions2.add(explosion2)
            boss3_health -= disparos.obtenerDisparo()
            if boss3_health <= 0:
                explosion2 = Explosion2(
                    boss3_object.rect.center, explosion3_images)
                explosions2.add(explosion2)
                boss3_object.kill()
                score += 1000
                if extra_points:
                    score += 200

        for boss3_bullet in boss3_bullets:
            if boss3_bullet.rect.colliderect(player.rect):
                player_life -= 40
                explosion = Explosion(player.rect.center, explosion3_images)
                explosions.add(explosion)
                boss3_bullet.kill()

        if boss3_health <= 0:
            explosion = Explosion2(boss3_object.rect.center, explosion2_images)
            explosions2.add(explosion)
            boss3_object.kill()

    if boss3_group:
        boss3_object = boss3_group.sprites()[0]
        boss3_health_bar_rect.center = (
            boss3_object.rect.centerx, boss3_object.rect.top - 5)
        pygame.draw.rect(screen, (255, 0, 0), boss3_health_bar_rect)
        pygame.draw.rect(screen, (0, 255, 0), (boss3_health_bar_rect.left,
                         boss3_health_bar_rect.top, boss3_health, boss3_health_bar_rect.height))

    player_image_copy = player.image.copy()
    screen.blit(player_image_copy, player.rect)

    for explosion in explosions:
        explosion.update()
        screen.blit(explosion.image, explosion.rect)

    for explosion2 in explosions2:
        explosion2.update()
        screen.blit(explosion2.image, explosion2.rect)

    for bullet in bullets:
        bullet.update()
        screen.blit(bullet.image, bullet.rect)

        if bullet.rect.bottom < 0:
            bullet.kill()
            bullet_counter -= 1

    player_life_surface = pygame.Surface((200, 25), pygame.SRCALPHA, 32)
    player_life_surface.set_alpha(216)

    player_life_bar_width = int(player_life / 200 * 200)
    player_life_bar_width = max(0, min(player_life_bar_width, 200))

    player_life_bar = pygame.Surface(
        (player_life_bar_width, 30), pygame.SRCALPHA, 32)
    player_life_bar.set_alpha(216)

    life_bar_image = pygame.image.load("images/life_bar.png").convert_alpha()

    if player_life > 50:
        player_life_bar.fill((152, 251, 152))
    else:
        player_life_bar.fill((0, 0, 0))

    player_life_surface.blit(life_bar_image, (0, 0))
    player_life_surface.blit(player_life_bar, (35, 0))

    life_x_pos = 10
    screen.blit(player_life_surface, (life_x_pos, 10))

    bullet_counter_surface = pygame.Surface((200, 25), pygame.SRCALPHA, 32)
    bullet_counter_surface.set_alpha(216)
    bullet_counter_bar = pygame.Surface(
        ((bullet_counter / 200) * 200, 30), pygame.SRCALPHA, 32)
    bullet_counter_bar.set_alpha(216)
    bullet_bar_image = pygame.image.load(
        "images/bullet_bar.png").convert_alpha()
    if bullet_counter > 50:
        bullet_counter_bar.fill((255, 23, 23))
    else:
        bullet_counter_bar.fill((0, 0, 0))
    bullet_counter_surface.blit(bullet_bar_image, (0, 0))
    bullet_counter_surface.blit(bullet_counter_bar, (35, 0))
    bullet_x_pos = 10
    bullet_y_pos = player_life_surface.get_height() + 20
    screen.blit(bullet_counter_surface, (bullet_x_pos, bullet_y_pos))

    score_surface = pygame.font.SysFont('Comic Sans MS', 30).render(
        f'{score}', True, (238, 232, 170))
    score_image_rect = score_surface.get_rect()
    score_image_rect.x, score_image_rect.y = WIDTH - \
        score_image_rect.width - score_coin_img.get_width() - 10, 10

    screen.blit(score_coin_img, (score_image_rect.right + 5,
                score_image_rect.centery - score_coin_img.get_height()//2))
    screen.blit(score_surface, score_image_rect)

    hi_score_surface = pygame.font.SysFont('Comic Sans MS', 20).render(
        f'HI-SCORE: {hi_score}', True, (255, 255, 255))
    hi_score_surface.set_alpha(128)
    hi_score_x_pos = (screen.get_width() - hi_score_surface.get_width()) // 2
    hi_score_y_pos = 20
    screen.blit(hi_score_surface, (hi_score_x_pos, hi_score_y_pos))

    pygame.display.flip()

    clock.tick(FPS)

pygame.mixer.music.stop()
pygame.quit()
sys.exit()
