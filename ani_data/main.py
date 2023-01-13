#animation testing
from engine import game_engine_80123 as game_engine
import pygame, os, animation
file_dir = os.getcwd()
#create window
w, h = 600, 400
window = game_engine.window.define("Animation", w, h)

#variables
run = True
clock = pygame.time.Clock()
scale = 1
sprite_speed = 2

#lists
#display
display = []
background = game_engine.properties_object("bg", f"{file_dir}/textures/background.webp", 0, 0, w, h, False)
display += [background]
#display_sprite
display_sprite = []

#jim - player 1
standingPlayer = pygame.image.load(f"{file_dir}/textures/jim/standing.png")
jim = game_engine.properties_object("player", standingPlayer, 300, 300, 64 * scale, 64 * scale, True)

#billy - player 2
billy = game_engine.properties_object("enemy", f"{file_dir}/textures/billy/L1E.png", 400, 300, 64 * scale, 64 * scale, True)
display_sprite += [jim, billy]

def main():
    #player 1 control
    if keys[pygame.K_a]: 
        #if player hits the border move the camera, this will set the player back by 1 pixel to move the player again by another 1 pixel
        if game_engine.player.left(jim, sprite_speed, 10):         
            game_engine.camera.moveCamera(-sprite_speed, 0)
            game_engine.player.left(jim, sprite_speed, 10)
        game_engine.player.animate(jim, animation.animationsLeftPlayer, 5)

    elif keys[pygame.K_d]:
        if game_engine.player.right(jim, sprite_speed, w - (10 + jim.width)):
            game_engine.camera.moveCamera(sprite_speed, 0)
            game_engine.player.right(jim, sprite_speed, w - (10 + jim.width))
        game_engine.player.animate(jim, animation.animationsRightPlayer, 5)

    """elif keys[pygame.K_s]:
        game_engine.player.down(jim, 2, h - (10 + jim.height))
    elif keys[pygame.K_w]:
        game_engine.player.up(jim, 2, 10)"""
     
    #player 2 control
    if keys[pygame.K_LEFT]:
        game_engine.player.left(billy, sprite_speed, 10)
        game_engine.player.animate(billy, animation.animationsLeftEnemy, 5)
    elif keys[pygame.K_RIGHT]:
        game_engine.player.right(billy, sprite_speed, w - (10 + billy.width))
        game_engine.player.animate(billy, animation.animationsRightEnemy, 5)

    if game_engine.frames >= jim.animationTime:                     #if the players animation time is lower than the frames passed, then change to standing still
        jim.texture = game_engine.properties_object.reload_texture(standingPlayer, 64 * scale, 64 * scale)

    #camera control - controls the camera around
    if keys[pygame.K_j]:
        game_engine.camera.moveCamera(-1, 0)
    elif keys[pygame.K_l]:
        game_engine.camera.moveCamera(1, 0)
    elif keys[pygame.K_i]:
        game_engine.camera.moveCamera(0, -1)
    elif keys[pygame.K_k]:
        game_engine.camera.moveCamera(0, 1)

while run:
    #keyboard and exit button, main code -----------------------------
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    main()
    game_engine.counter.update()
    game_engine.window.update(window, display, display_sprite, None, None, clock, 1)
    clock.tick(60)

pygame.quit()