# GAME = "Maze Runner" 

from grid import generate_maze

import pygame as p
import math as m
p.init()

ratio,L,running = 9/16,2300,True
l = int(L * ratio)





screen = p.display.set_mode((L,l))
p.display.set_caption("Maze Runner")

# maze_griding System !
maze_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
g_L,g_l = 30,30
#maze_grid = generate_maze(g_L,g_l)

for i in range(30):
    for j in range(30):
        if maze_grid[i][j] == 0 and (i == 0 or i == 29 or j == 0 or j == 29):
            maze_grid[i][j]=1
#for row in maze_grid:
#    print(row)
# End of maze_griding System !

tile_size = l // g_L
maze_grid_x = (L-(tile_size*g_l))//2
maze_grid_y = 0

skin = p.image.load('ghst.jpg').convert_alpha()

w_skin = skin.get_width()
h_skin = skin.get_height()

k_w = tile_size/ w_skin
k_h = tile_size/ h_skin

skin = p.transform.scale(skin,(w_skin *k_w, h_skin * k_h))

w_skin, h_skin = skin.get_size()

def draw_maze_grid(screen,maze_grid,g_l,g_L):
    for i in range(g_L):
        for j in range(g_l):
            tile = maze_grid[i][j]
            color = (0,0,0)
            if tile == 0 :
                color = (255,255,255)
            elif tile == 2 :
                color = (200,100,200)
            else :
                color = (0,0,0)
            p.draw.rect(screen,color,(maze_grid_x + j*tile_size,maze_grid_y + i*tile_size,tile_size,tile_size))

def is_blocked(px, py):
    col = int((px - maze_grid_x) // tile_size)
    row = int((py - maze_grid_y) // tile_size)

    if row < 0 or col < 0 or row >= g_L or col >= g_l:
        return True  # hors map = mur

    return maze_grid[row][col] == 1

hitbox_offset_x = h_skin * 0.120 + tile_size/4.5
hitbox_offset_y = w_skin * 0.120 + tile_size * 0.15
hitbox_w = w_skin * 0.4
hitbox_h = h_skin * 0.6

def init_player_on_grid(maze_grid, maze_grid_x, maze_grid_y, tile_size, skin_w, skin_h):
    for i, row in enumerate(maze_grid):
        for j, cell in enumerate(row):
            if cell == 0:  # case libre
                # On centre la hitbox du joueur sur cette case
                x = maze_grid_x + j * tile_size + (tile_size - skin_w)/2
                y = maze_grid_y + i * tile_size + (tile_size - skin_h)/2
                return x, y
    return 0, 0  # fallback

# Position initiale centrée sur la case libre
x_skin, y_skin = init_player_on_grid(maze_grid, maze_grid_x, maze_grid_y, tile_size, w_skin, h_skin)




def collide(x, y):
    points = [
        (x + hitbox_offset_x, y + hitbox_offset_y),
        (x + hitbox_offset_x + hitbox_w - 1, y + hitbox_offset_y),
        (x + hitbox_offset_x, y + hitbox_offset_y + hitbox_h - 1),
        (x + hitbox_offset_x + hitbox_w - 1, y + hitbox_offset_y + hitbox_h - 1)
    ]
    for px, py in points:
        if is_blocked(px, py):
            return True
    return False

clock = p.time.Clock()
speed = tile_size/12

while running:

    clock.tick(120)

    keys = p.key.get_pressed()
    dx,dy = 0,0

    print("collide initial:", collide(x_skin, y_skin))


    if keys[p.K_z]:
        dy-= speed
        #img = pygame.transform.scale(img,(img.get_width() * coef, img.get_height() * coef))
        #coef *= 0.9
    if keys[p.K_s]:
        dy += speed
        #img = pygame.transform.scale(img,(img.get_width() * coef, img.get_height() * coef))
        #coef *= 1.01
    if keys[p.K_q]:
        dx -= speed
    if keys[p.K_d]:
        dx += speed

    # dx, dy calculés avec le clavier
    if not collide(x_skin+dx, y_skin):
        x_skin += dx

    if not collide(x_skin, y_skin+dy):
        y_skin += dy


    screen.fill((25,12,61))
    draw_maze_grid(screen,maze_grid,g_l,g_L)
    screen.blit(skin,(x_skin, y_skin))

###___#___#___#___###


    hitbox_rect = p.Rect( x_skin + hitbox_offset_x, y_skin + hitbox_offset_y, hitbox_w, hitbox_h )
    p.draw.rect(screen, (5, 250, 0), hitbox_rect, 2)  # 2 = épaisseur du trait


###___#___#___#___###



    p.display.flip()

    for event in p.event.get() :
        if event.type == p.QUIT :
            running = False

p.quit()



# important pour les collisions : hitbox du joueur = 3/4 des pixels de son image png !

