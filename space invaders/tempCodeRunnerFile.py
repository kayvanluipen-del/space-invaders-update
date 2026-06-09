 key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]and yellow.x - VEL >0:
            yellow.x -= VEL
        if key_pressed[pygame.K_s]and yellow.y + VEL <550:
            yellow.y += VEL
        if key_pressed[pygame.K_d]and yellow.x + VEL <390:
            yellow.x += VEL
        if key_pressed[pygame.K_w]and yellow.y - VEL >0:
            yellow.y -= VEL
        if key_pressed[pygame.K_LEFT]and red.x - VEL >0:
            red.x -= VEL
        if key_pressed[pygame.K_DOWN]and red.y + VEL <550:
            red.y += VEL
        if key_pressed[pygame.K_RIGHT]and red.x + VEL <390:
            red.x += VEL
        if key_pressed[pygame.K_UP]and red.y - VEL >0:
            red.y -= VEL