import pygame
import os
pygame.font.init()

screen = pygame.display.set_mode((900,600))
WIDTH = 900
HEIGHT = 600
WHITE = (255,255,255)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
black = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
yellowspaceship = pygame.image.load(os.path.join("images","yellow.png"))
yellowship = pygame.transform.rotate(pygame.transform.scale(yellowspaceship,(50,50)),90)
redspaceship = pygame.image.load(os.path.join("images","red.png"))
redship = pygame.transform.rotate(pygame.transform.scale(redspaceship,(50,50)),270)
spacebg = pygame.transform.scale(pygame.image.load(os.path.join("images","bg.png")),(WIDTH,HEIGHT))
border = pygame.Rect(440,0,20,600)
HEALTH_FONT = pygame.font.SysFont("comicsans",40)
WINNER_FONT = pygame.font.SysFont("comicsans",100)


def draw_window(red,yellow,red_bullets,yellow_bullets):
    screen.fill(WHITE)
    screen.blit(spacebg,(0,0))
    screen.blit(yellowship,(yellow.x,yellow.y))
    screen.blit(redship,(red.x,red.y))
    pygame.draw.rect(screen,black,border)
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health),1,WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health),1,WHITE)
    screen.blit(red_health_text,(850,50))
    screen.blit(yellow_health_text,(50,50))

    for bullet in red_bullets:
        pygame.draw.rect(screen, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(screen, YELLOW, bullet)
    
    pygame.display.update()


def main():
    red = pygame.Rect(700,300,50 ,50)
    yellow = pygame.Rect(100,300, 50 ,50)
    clock = pygame.time.Clock()
    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()
        draw_window(red,yellow)
    pygame.quit()


            
def yellow_handle_movement(keys_pressed, yellow):
    if key_pressed[pygame.K_a]and yellow.x - VEL >0:
        yellow.x -= VEL
    if key_pressed[pygame.K_s]and yellow.y + VEL <550:
        yellow.y += VEL
    if key_pressed[pygame.K_d]and yellow.x + VEL <390:
        yellow.x += VEL
    if key_pressed[pygame.K_w]and yellow.y - VEL >0:
        yellow.y -= VEL

def red_handle_movement(keys_pressed, red):
    if key_pressed[pygame.K_LEFT]and red.x - VEL >460:
        red.x -= VEL
    if key_pressed[pygame.K_DOWN]and red.y + VEL <550:
        red.y += VEL
    if key_pressed[pygame.K_RIGHT]and red.x + VEL <850:
        red.x += VEL
    if key_pressed[pygame.K_UP]and red.y - VEL >0:
        red.y -= VEL

def handle_bullets(red_bullets,yellow_bullets,red,yellow):
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x <0:
            red_bullets.remove(bullet)
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x <0:
            yellow_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    screen.blit(draw_text,(450,400))
    pygame.display.update()
    pygame.time.delay(5000)



main()




if __name__ == "__main__":
    main()