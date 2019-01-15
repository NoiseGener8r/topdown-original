def main():
 
    import pygame, random, time, math #Import modules
    pygame.init() #Initialize pygame
     
    # Define some colors and fonts
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    
    font = pygame.font.Font(None, 36)    # This is a font we use to draw text on the screen (size 36)
     
    # Set the width and height of the screen [width, height]
    screen_width = 1070
    screen_height = 720
    screen = pygame.display.set_mode([screen_width, screen_height]) #Create the screen
     
    pygame.display.set_caption("Awesome Laser Space Cat Samurai Warrior Jerry") #Set window title
   
    #Key input helpers
    up_pressed = False
    down_pressed = False
    left_pressed = False
    right_pressed = False
    w_pressed = False
    s_pressed = False
    a_pressed = False
    d_pressed = False
    
    
    level = 0 #Current difficulty level
    
    invinc_frames = -10 #Player invincibility frames
    
    total_items = 15 #No. total items to drop
    
    #shot_time = 1
    #pistol_timer = 25
    #mine_time = 50
    #bonus_damage = 0
     
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
################################################################################################
###########IMAGES
   
    #Backgrounds:
    
    ####MISCELLANEOUS####
    game_over_screen = pygame.image.load("game_over.png").convert() #Game Over
    game_over_screen = pygame.transform.scale(game_over_screen, [screen_width,screen_height])
    credit_page = pygame.image.load("credit_page.png").convert()           #Credits
    credit_page = pygame.transform.scale(credit_page, [screen_width,screen_height])
    background_image = pygame.image.load("Ground.png").convert()           #Game Background
    background_image = pygame.transform.scale(background_image, [screen_width, screen_height]).convert()
    
    ####INSTRUCTIONS###
    instruc_page_1 = pygame.image.load("instruc_screen_1.png").convert()   #Instructions, Page 1
    instruc_page_1 = pygame.transform.scale(instruc_page_1, [screen_width,screen_height])
    instruc_page_2 = pygame.image.load("instruc_screen_2.png").convert()   #Instructions, Page 2
    instruc_page_2 = pygame.transform.scale(instruc_page_2, [screen_width,screen_height])
    instruc_page_3 = pygame.image.load("instruc_screen_3.png").convert()   #Instructions, Page 3
    instruc_page_3 = pygame.transform.scale(instruc_page_3, [screen_width,screen_height])
      
    #Characters:
    
    ####THE PLAYER####
    init_player_image = pygame.image.load("player.png").convert()             #Initial Player Image
    init_player_image.set_colorkey(WHITE)                                     #Make transparent
    
    #Rotated player images
    player_image_up = init_player_image                                       #Defaults to UP                          
    player_image_left = pygame.transform.rotate(player_image_up, 90)          #Rotate 90 degrees, facing LEFT
    player_image_right = pygame.transform.rotate(player_image_up, -90)        #Rotate -90 (270) degrees, facing RIGHT
    player_image_down = pygame.transform.rotate(player_image_up, 180)         #Rotate 180 degrees, facing DOWN 
    
    ####THE NORMAL ENEMY####
    init_enemy_image = pygame.image.load("enemy.png").convert()               #Initial enemy image
    init_enemy_image.set_colorkey(WHITE)                                      #Make transparent
                                                                              #Make the standard enemy image
    #Rotated enemy images
    enemy_image = init_enemy_image                                            #Defaults to UP   
    enemy_left = pygame.transform.rotate(enemy_image, 90)                     #Rotate 90 degrees, facing LEFT
    enemy_right = pygame.transform.rotate(enemy_image,-90)                    #Rotate -90 (270) degrees, facing RIGHT   
    enemy_down = pygame.transform.rotate(enemy_image, 180)                    #Rotate 180 degrees, facing DOWN
    
    ####THE FAST ENEMY####
    init_fast_enemy_image = pygame.image.load("fast_enemy.png").convert()     #Initial fast enemy
    init_fast_enemy_image.set_colorkey(WHITE)                                 #Make transparent
    
    #Rotated fast enemy images
    fast_enemy_image = init_fast_enemy_image                                  #Defaults to UP            
    fast_enemy_left = pygame.transform.rotate(fast_enemy_image, 90)           #Rotate 90 degrees, facing LEFT
    fast_enemy_right = pygame.transform.rotate(fast_enemy_image,-90)          #Rotate -90 (270) degrees, facing RIGHT   
    fast_enemy_down = pygame.transform.rotate(fast_enemy_image, 180)          #Rotate 180 degrees, facing DOWN
    
    ####THE STRONG ENEMY####
    init_strong_enemy_image = pygame.image.load("strong_enemy.png").convert() #Initial strong enemy
    init_strong_enemy_image.set_colorkey(WHITE)                               #Make transparent
    
    #Rotated strong enemy images
    strong_enemy_image = init_strong_enemy_image                              #Defaults to UP  
    strong_enemy_left = pygame.transform.rotate(strong_enemy_image, 90)       #Rotate 90 degrees, facing LEFT
    strong_enemy_right = pygame.transform.rotate(strong_enemy_image, -90)     #Rotate -90 (270) degrees, facing RIGHT    
    strong_enemy_down = pygame.transform.rotate(strong_enemy_image, 180)      #Rotate 180 degrees, facing DOWN
    
    
    
    #Items
    
    ####AMMO TYPES####
    gift_ammo_image = pygame.image.load("gift_ammo.png").convert()            #'Gift Ammo', given when you run out of ammo
    gift_ammo_image.set_colorkey(WHITE)                                       #Make transparent
    
    small_ammo_image = pygame.image.load("small_ammo.png").convert()          #Small Ammo drop
    small_ammo_image.set_colorkey(WHITE)                                      #Make transparent
    
    init_ammo_image = pygame.image.load("ammo.png").convert()                 #Large Ammo drop
    init_ammo_image.set_colorkey(WHITE)                                       #Make transparent
    ammo_image = init_ammo_image                                              #Create the ammo image
    
    ####PROJECTILES####
    mine_image = pygame.image.load("mine.png").convert()                      #Weapon 3, the mine
    mine_image.set_colorkey(WHITE)                                            #Make transparent
    
    explode_image = pygame.image.load("explosion.png").convert()              #Explosion, triggered by mines
    explode_image.set_colorkey(WHITE)                                         #Make transparent 
    
    
    ammo_list = pygame.sprite.Group()
    
    
    
    
    
    
    
    init_bullet_image = pygame.image.load("bullet.png").convert()
    init_bullet_image.set_colorkey(WHITE)
    bullet_image = init_bullet_image
    
    
    init_life_image = pygame.image.load("life.png").convert()
    init_life_image.set_colorkey(WHITE)
    life_image = init_life_image
    
    
    
    all_sprites_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()
    item_list = pygame.sprite.Group()
    
    enemy_counter = 0
    timer = 0
    requirement = 50
    shot_timer = 0
    fast_health_max = 16
    reg_health_max = 20
    strong_health_max = 30
    
    # Rotated  Player Images
    
    weapon = 1
    global mine_damage, pistol_damage, chaingun_damage
    mine_damage = 10
    pistol_damage = 15
    chaingun_damage = 1 
    
    
    
    
    # Game classes
    
    class Item(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            
        
               
    
    class Life(Item):
        def __init__(self):
            super().__init__()
            
            self.image = life_image
            self.rect = self.image.get_rect()
            
        def pickedUp(self, mine_damage, pistol_damage, chaingun_damage):
            print('picked up life')
            player.lives += random.randrange(1,4)
            
        
            
            
    class SmallAmmo(Item):
        def __init__(self):
            super().__init__()
            
            self.image = small_ammo_image
            self.rect = self.image.get_rect()
            
        def pickedUp(self, mine_damage, pistol_damage, chaingun_damage):
            print('picked up ammo')
            player.ammo += 1
            
    class LargeAmmo(Item):
        def __init__(self):
            super().__init__()
            
            self.image = ammo_image
            self.rect = self.image.get_rect()
            
        def pickedUp(self, mine_damage, pistol_damage, chaingun_damage):
            print('picked up large ammo')
            player.ammo += 10 
            
    class GiftAmmo(Item):
        def __init__(self):
            super().__init__()
            
            self.image = gift_ammo_image
            self.rect = self.image.get_rect()
            
        def pickedUp(self, mine_damage, pistol_damage, chaingun_damage):
            print('picked up large ammo')
            player.ammo += 25 
            
    
    
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            
            self.image = enemy_image
            self.rect = self.image.get_rect()
            
            self.momentum_x = 1
            self.momentum_y = 1
            self.facing = 'UP'
            self.max_health = 20
            self.health = self.max_health
            
            
        def update(self):
            
            if player.rect.x < self.rect.x:
                self.facing = 'LEFT'
                self.rect.x -= self.momentum_x
                
            
            elif player.rect.x > self.rect.x:
                self.facing = 'RIGHT'
                self.rect.x += self.momentum_x
                
            
            if player.rect.y < self.rect.y:
                self.facing = 'UP'
                self.rect.y -= self.momentum_y
                
            
            if player.rect.y > self.rect.y:
                self.facing = 'DOWN'
                self.rect.y += self.momentum_y     
                
                
            if self.facing == 'DOWN':
                self.image = enemy_down
                
            if self.facing == 'UP':
                self.image = enemy_image
                
            if self.facing == 'LEFT':
                self.image = enemy_left
                
            if self.facing == 'RIGHT':
                self.image = enemy_right  
                
    class StrongEnemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            
            self.image = strong_enemy_image
            self.rect = self.image.get_rect()
            self.facing = 'UP'
            self.momentum_x = 1
            self.momentum_y = 1
            self.max_health = 45
            self.health = self.max_health
            
            
        def update(self):
            
            if player.rect.x < self.rect.x:
                self.facing = 'LEFT'
                self.rect.x -= self.momentum_x
                
            
            if player.rect.x > self.rect.x:
                self.facing = 'RIGHT'
                self.rect.x += self.momentum_x
                
            
            if player.rect.y < self.rect.y:
                self.facing = 'UP'
                self.rect.y -= self.momentum_y
                
            
            if player.rect.y >= self.rect.y:
                self.facing = 'DOWN'
                self.rect.y += self.momentum_y    
                
            if self.facing == 'DOWN':
                self.image = fast_enemy_down
                
            if self.facing == 'UP':
                self.image = fast_enemy_image
                
            if self.facing == 'LEFT':
                self.image = fast_enemy_left
                
            if self.facing == 'RIGHT':
                self.image = fast_enemy_right 
            
             
                
    class FastEnemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            
            self.image = fast_enemy_image
            self.rect = self.image.get_rect()
            self.facing = 'UP'
            self.momentum_x = 2
            self.momentum_y = 2
            self.max_health = 16
            self.health = self.max_health
            
            
        def update(self):
            
            if player.rect.x < self.rect.x:
                self.facing = 'LEFT'
                self.rect.x -= self.momentum_x
                
            
            if player.rect.x > self.rect.x:
                self.facing = 'RIGHT'
                self.rect.x += self.momentum_x
                
            
            if player.rect.y < self.rect.y:
                self.facing = 'UP'
                self.rect.y -= self.momentum_y
                
            
            if player.rect.y >= self.rect.y:
                self.facing = 'DOWN'
                self.rect.y += self.momentum_y    
                
            if self.facing == 'DOWN':
                self.image = fast_enemy_down
                
            if self.facing == 'UP':
                self.image = fast_enemy_image
                
            if self.facing == 'LEFT':
                self.image = fast_enemy_left
                
            if self.facing == 'RIGHT':
                self.image = fast_enemy_right                
            
                
    
    
    
    class Bullet(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            
            
            self.image = bullet_image
            self.rect = self.image.get_rect()
            self.momentum_x = 0
            self.momentum_y = 0
            
        def update(self):
            self.rect.x += self.momentum_x
            self.rect.y += self.momentum_y
    
    
    
    
    
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            """ Set up the player on creation .  """
            # Call the parent class (Sprite) constructor
            super().__init__()
            
            self.facing = 'UP'
            self.ammo = 100
            self.direction = ''
            self.momentum_x = 0
            self.momentum_y = 0
            self.lives = 3
            #self.damage = 1
            self.image = player_image_up
            self.rect = self.image.get_rect()
 
        def update(self):
            """ Update the player's position. """
            player.rect.x += player.momentum_x
            player.rect.y += player.momentum_y
                       
            if self.facing == 'UP':
                self.image = player_image_up
            if self.facing == 'DOWN':
                self.image = player_image_down       
                
            if self.facing == 'LEFT':
                self.image = player_image_left
            if self.facing == 'RIGHT':
                self.image = player_image_right 
                
           
                
            
            if self.rect.x > (screen_width - 30):
                self.rect.x = (screen_width - 30)
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.y > (screen_height - 30):
                self.rect.y = (screen_height - 30)
            if self.rect.y < 0:
                self.rect.y = 0
                
        
                    
    class Pistol():
        def __init__(self):
            super().__init__()
            
            self.damage = 15
            self.time = 10
            
        def shoot(self, direction):
            if self.time < 0 and player.ammo > 0:
                player.damage = self.damage
                
                pistol_bullet = Bullet()
                pistol_bullet.rect.x = player.rect.x
                pistol_bullet.rect.y = player.rect.y
                all_sprites_list.add(pistol_bullet)
                bullet_list.add(pistol_bullet)
                
                if direction == 'UP':
                    pistol_bullet.momentum_y = -5
                    
                elif direction == 'DOWN':
                    pistol_bullet.momentum_y = 5
                    
                elif direction == 'LEFT':
                    pistol_bullet.momentum_x = -5 
                    
                elif direction == 'RIGHT':
                    pistol_bullet.momentum_x = 5    
                
                player.ammo -= 1
                self.time = 25
            
                           
    
    class Chaingun():
        def __init__(self):
            super().__init__()
            
            self.damage = 10
            self.time = 1
        def shoot(self, direction):
            if self.time < 0 and player.ammo > 0:
                player.damage = self.damage
                
                chaingun_bullet = Bullet()
                chaingun_bullet.rect.x = player.rect.x
                chaingun_bullet.rect.y = player.rect.y
                all_sprites_list.add(chaingun_bullet)
                bullet_list.add(chaingun_bullet)
                
                if direction == 'UP':
                    chaingun_bullet.momentum_y = -5
                    
                elif direction == 'DOWN':
                    chaingun_bullet.momentum_y = 5
                    
                elif direction == 'LEFT':
                    chaingun_bullet.momentum_x = -5 
                    
                elif direction == 'RIGHT':
                    chaingun_bullet.momentum_x = 5  
                
                player.ammo -= 1
                self.time = 1
                
    class Mine():
        def __init__(self):
            super().__init__()
            
            self.damage = 100
            self.time = 100
        def shoot(self, direction):
            if self.time < 0 and player.ammo > 0:
                player.damage = self.damage
                
                
                
                mine_bullet = Bullet()
                mine_bullet.image = mine_image
                mine_bullet.rect.x = (player.rect.x)
                mine_bullet.rect.y = (player.rect.y)
                all_sprites_list.add(mine_bullet)
                bullet_list.add(mine_bullet)
                    
                if direction == 'UP':
                    mine_bullet.momentum_y = 0
                    
                elif direction == 'DOWN':
                    mine_bullet.momentum_y = 0
                    
                elif direction == 'LEFT':
                    mine_bullet.momentum_x = 0
                    
                elif direction == 'RIGHT':
                    mine_bullet.momentum_x = 0                
                      
                player.ammo -= 5            
                self.time = 100
                    
                     
    
    
    # Game variables
    game_over = False
    score = 0
    display_instructions = True
    instruction_page = 1   
    
    # Game functions
    
    # Create sprites
    player = Player()
    player.rect.x = screen_width / 2
    player.rect.y = screen_height / 2
    all_sprites_list.add(player)
    
    pistol = Pistol()
    chaingun = Chaingun()
    mine = Mine()
    
    # -------- Instruction Page Loop -----------
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    instruction_page += 1
                if event.key == pygame.K_LEFT:
                    instruction_page -= 1                
                if instruction_page == 4:
                    display_instructions = False
     
        # Set the screen background
        screen.fill(BLACK)
        
        if instruction_page < 1:
            screen.blit(credit_page, [0,0])
     
        if instruction_page == 1:
            # Draw instructions, page 1
            # This could also load an image created in another program.
            # That could be both easier and more flexible.
            
            screen.blit(instruc_page_1, [0,0])
     
        if instruction_page == 2:
            # Draw instructions, page 2
            
            screen.blit(instruc_page_2, [0,0])
        if instruction_page == 3:
            # Draw instructions, page 2
            
            screen.blit(instruc_page_3, [0,0])
        # Limit to 60 frames per second
        clock.tick(60)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()    
     
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over == True:
                    main()
                if event.key == pygame.K_UP:
                    w_pressed = True
                if event.key == pygame.K_DOWN:
                    s_pressed = True
                if event.key == pygame.K_LEFT:
                    a_pressed = True
                if event.key == pygame.K_RIGHT:
                    d_pressed = True
                    
                if event.key == pygame.K_w:
                    up_pressed = True
                if event.key == pygame.K_s:
                    down_pressed = True
                if event.key == pygame.K_a:
                    left_pressed = True
                if event.key == pygame.K_d:
                    right_pressed = True   
                    
                if event.key == pygame.K_1:
                    
                    weapon = 1
                    
                if event.key == pygame.K_2:
                                       
                    weapon = 2
                    
                if event.key == pygame.K_3:
                                       
                    weapon = 3
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    w_pressed = False
                if event.key == pygame.K_DOWN:
                    s_pressed = False
                if event.key == pygame.K_LEFT:
                    a_pressed = False
                if event.key == pygame.K_RIGHT:
                    d_pressed = False
                    
                if event.key == pygame.K_w:
                    up_pressed = False
                if event.key == pygame.K_a:
                    left_pressed = False
                if event.key == pygame.K_s:
                    down_pressed = False
                if event.key == pygame.K_d:
                    right_pressed = False                    
                    
                   
                
                    
                    
        if up_pressed:
            player.facing = 'UP'
            player.rect.y += -3

        if down_pressed:
            player.facing = 'DOWN'
            player.rect.y += 3
        
        if left_pressed:
            player.facing = 'LEFT'
            player.rect.x += -3
            
        if right_pressed:
            player.facing = 'RIGHT'
            player.rect.x += 3
            
        if w_pressed:
            player.facing = 'UP'
            if weapon == 1:
                
                pistol.shoot('UP')
            
            if weapon == 2:
                
                chaingun.shoot('UP')
                
            if weapon == 3:
                
                mine.shoot('UP')
                
        if a_pressed:
            player.facing = 'LEFT'
            if weapon == 1:
                
                pistol.shoot('LEFT')
            
            if weapon == 2:
                
                chaingun.shoot('LEFT')
                
            if weapon == 3:
                
                mine.shoot('LEFT')
            
        if s_pressed:
            player.facing = 'DOWN'
            if weapon == 1:
                
                pistol.shoot('DOWN')
            
            if weapon == 2:
                
                chaingun.shoot('DOWN')
                
            if weapon == 3:
                
                mine.shoot('DOWN')
            
            
        if d_pressed:
            player.facing = 'RIGHT'
            if weapon == 1:
                
                pistol.shoot('RIGHT')
            
            if weapon == 2:
                
                chaingun.shoot('RIGHT')
                
            if weapon == 3:
                
                mine.shoot('RIGHT')
                   
        all_sprites_list.update()
        
         
            
            
        # --- Screen-clearing code goes here
     
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
     
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        
        ##screen.fill(BLACK)
        screen.blit(background_image, [0, 0])
     
        # --- Drawing code should go here
        
        
        if game_over:
            # If game over is true, draw game over
            screen.blit(game_over_screen, [0,0])
            
                        
            
        else:
            if player.ammo <= 0:
                if not ammo_list:
                    ammo = GiftAmmo()
                    ammo.rect.x = random.randrange(10, screen_width-10)
                    ammo.rect.y = random.randrange(10, screen_height+10)
                    all_sprites_list.add(ammo)
                    ammo_list.add(ammo)
                    item_list.add(ammo)
            
            enemy_counter += 1
            
                
            #print(invinc_frames)
            if timer % 1000 == 0:
                level += 1
                requirement -= 1
                
                
                
                     
            #print(enemy_counter)
            if enemy_counter == requirement:
                enemy_counter = 0
                
                if level >= 10:
                    enemy = StrongEnemy()
                    fast_chance = random.randrange(0,5)
                    if fast_chance == 0:
                        enemy = FastEnemy()
                else:
                    enemy = Enemy()
                        
               
                enemy_list.add(enemy)
                all_sprites_list.add(enemy)
                enemy_door = random.randrange(0,4)
                
                if enemy_door == 0:
                    enemy.rect.x = 0
                    enemy.rect.y = screen_height/2 + random.randrange((-1 * screen_height), screen_height)
                if enemy_door == 1:
                    enemy.rect.x = screen_width/2 + random.randrange((-1 * screen_width), screen_width)
                    enemy.rect.y = 0
                if enemy_door == 2:
                    enemy.rect.x = screen_width
                    enemy.rect.y = screen_height/2 + random.randrange((-1 * screen_height), screen_height)
                if enemy_door == 3:
                    enemy.rect.x = screen_width/2 + random.randrange((-1 * screen_width), screen_width)
                    enemy.rect.y = screen_height
                    
                    
                
            for item in item_list:
                item_pickup_list = pygame.sprite.spritecollide(player, item_list, True)
                for i in item_pickup_list:
                    
                    item_list.remove(i)
                    if i in ammo_list:
                        ammo_list.remove(i)
                    
                        
                    i.pickedUp(mine_damage, pistol_damage, chaingun_damage)
                
            
                                   
            for mine_bullet in bullet_list:
                
     
                # See if it hit an enemy
                enemy_hit_list = pygame.sprite.spritecollide(mine_bullet, enemy_list, False)
                for enemy in enemy_hit_list:
                    # screen.blit(explode_image, [mine_bullet.rect.x, mine_bullet.rect.y])
                    enemy.health -= player.damage
                    damage_text_a = font.render('-' + str(player.damage), True, RED)
                    screen.blit(damage_text_a, [(random.randrange(enemy.rect.x - 4,enemy.rect.x + 4)), (enemy.rect.y - 25)])
                    #damage_text_b = font.render('-', True, RED)
                    #screen.blit(damage_text_b, [(random.randrange(enemy.rect.x - 14,enemy.rect.x - 10)), (enemy.rect.y - 25)])
                    all_sprites_list.remove(mine_bullet)
                    bullet_list.remove(mine_bullet)               
             
            for bullet in bullet_list:
                if bullet.rect.x > screen_width or bullet.rect.x < 0 or bullet.rect.y < 0 or bullet.rect.y > screen_height:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)
                    
                
                    
            
                    
                    
                # See if it hit an enemy
                enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, False)
                for enemy in enemy_hit_list:
                    
                    enemy.health -= player.damage
                    damage_text_a = font.render('-' + str(player.damage), True, RED)
                    screen.blit(damage_text_a, [(random.randrange(enemy.rect.x - 4,enemy.rect.x + 4)), (enemy.rect.y - 25)])
                    #damage_text_b = font.render('-', True, RED)
                    #screen.blit(damage_text_b, [(random.randrange(enemy.rect.x - 14,enemy.rect.x - 10)), (enemy.rect.y - 25)])
                    all_sprites_list.remove(bullet)
                    bullet_list.remove(bullet)
            for enemy in enemy_list:
                player_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
                for enemy in player_hit_list:  
                    if invinc_frames < 0:
                        invinc_frames = 25
                        player.lives -= 1
                
                if enemy.health > 0 and enemy.health < enemy.max_health:
                    health_bar = pygame.Surface([enemy.max_health, 5])
                    health_bar.fill((230,230,230))
                    screen.blit(health_bar, [enemy.rect.x - 5, enemy.rect.y + 30])                    
                    health_bar_filled = pygame.Surface([enemy.health, 5])
                    health_bar_filled.fill(RED)
                    screen.blit(health_bar_filled, [enemy.rect.x - 5, enemy.rect.y + 30])
                                      
                if enemy.health <= 0:
                    item_drop = random.randrange(0,1)
                    if item_drop == 0:
                        
                        ID = random.randrange(0, total_items)
                        
                        if ID == 0:
                            life = Life()
                            all_sprites_list.add(life)
                            item_list.add(life)
                            life.rect.x = enemy.rect.x
                            life.rect.y = enemy.rect.y 
                        else:
                            ammo_type = random.randrange(0,5)
                            if ammo_type == 0:
                                ammo = LargeAmmo()
                                ammo.rect.x = enemy.rect.x
                                ammo.rect.y = enemy.rect.y
                                all_sprites_list.add(ammo)
                                ammo_list.add(ammo)
                                item_list.add(ammo)
                            else:
                                ammo = SmallAmmo()
                                ammo.rect.x = enemy.rect.x
                                ammo.rect.y = enemy.rect.y
                                all_sprites_list.add(ammo)
                                ammo_list.add(ammo)  
                                item_list.add(ammo)
                                
                    
                        
                            
                    all_sprites_list.remove(enemy)
                    enemy_list.remove(enemy)  
                    
                                    
                    
            all_sprites_list.draw(screen)  
            level_text_b = font.render("Level: ", True, WHITE)
            level_text_a = font.render(str(level), True, WHITE)
            lives_text_a = font.render(str(player.lives), True, WHITE)
            lives_text_b = font.render("Lives: ", True, WHITE)
            ammo_text_a = font.render("Ammo: ", True, WHITE)
            ammo_text_b = font.render(str(player.ammo), True, WHITE)
            screen.blit(level_text_b, [15,15])
            screen.blit(level_text_a, [100,15])
            screen.blit(lives_text_b, [15,45])
            screen.blit(lives_text_a, [100,45])      
            screen.blit(ammo_text_a, [screen_width - 150, 15])
            screen.blit(ammo_text_b, [screen_width - 60, 15])
            
            timer += 1  
            invinc_frames -= 1
            pistol.time -= 1
            mine.time -= 1
            chaingun.time -= 1
            
            print(pistol.time)
                 
            if player.lives <= 0:
                game_over = True
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()
    
if __name__ == "__main__":
    main()
