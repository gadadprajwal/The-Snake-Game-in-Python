import sys, pygame, time, random
print(pygame.init())
check_errors = pygame.init()   #values for checking errors #(6,0)

#Checking for initializing error
if check_errors[1]>0:
    print("Had {0} initializing errors, exiting.".format(check_errors[1]))
    sys.exit(-1)
else:
    print("PyGame succesfully initiallized")


#Lets create a surface
play_surface = pygame.display.set_mode((720,460)) #Accepts a tuple of the resolution
pygame.display.set_caption("Prajwal's Snake Game")  #Display the name of your game on the window
#time.sleep(5)

#Colours
red = pygame.Color(255,0,0) #(R,G,B) #gameover
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0)#score
white = pygame.Color(255,255,255)#background
brown = pygame.Color(165,42,42)#food

#frames per second controller
fps_controller = pygame.time.Clock()

#Snake features
snake_pos = [100,50]
snake_body = [[100,50],[90,50],[80,50]]

#Random placement of food
food_pos = [random.randrange(1,72)*10, random.randrange(1,46)*10] #Multiple of 10
food_spwan = True
score = 0
direction = 'RIGHT'
changeto = direction



def show_score(choice=1):
    s_font = pygame.font.SysFont('monaco', 24)
    s_surface = s_font.render("Score: {0}".format(score), True, black)
    s_rectange = s_surface.get_rect()
    if choice == 1:
        s_rectange.midtop = (80, 10)
    else:
        s_rectange.midtop = (360, 120)
    play_surface.blit(s_surface, s_rectange)


#Gameover function
def gameover():
    my_font =  pygame.font.SysFont('monaco',72)
    gameover_surface = my_font.render("Gamer Over",True,red)
    gameover_rectange = gameover_surface.get_rect()
    gameover_rectange.midtop = (360, 15)
    play_surface.blit(gameover_surface,gameover_rectange)
    pygame.display.flip() #For updating the values
    show_score(123)
    time.sleep(4)
    pygame.quit() #For the game window
    sys.exit() #For console

#Events:- Hit, Duration, Release time period, etc.

#Main Logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                changeto = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                changeto = "LEFT"
            if event.key == pygame.K_UP or event.key == ord("w"):
                changeto = "UP"
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                changeto = "DOWN"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))



    #Validation of directions
    if changeto == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeto == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if changeto == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeto == "DOWN" and not direction == "UP":
        direction = "DOWN"


    #Update the position of the snake
    if direction == "RIGHT":
        snake_pos[0]+=10
    if direction == "LEFT":
        snake_pos[0]-=10
    if direction == "UP":
        snake_pos[1]-=10
    if direction == "DOWN":
        snake_pos[1]+=10


    #Snake Body
    snake_body.insert(0,list(snake_pos))
    if snake_pos[0]==food_pos[0] and snake_pos[1]==food_pos[1]:
        score+=1
        food_spwan = False
    else:
        snake_body.pop()

    if food_spwan == False:
        food_pos = [[random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]]
    food_spwan = True

    play_surface.fill(white)

    #Draw Snake
    for pos in snake_body:
        pygame.draw.rect(play_surface, green, pygame.Rect(pos[0], pos[1],10,10))

    pygame.draw.rect(play_surface, brown, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    #Bound
    if snake_pos[0] > 720 or snake_pos[0]<0:
        gameover()
    if snake_pos[1] > 460 or snake_pos[1]<0:
        gameover()

     #Self Eating
    for blocks in snake_body[1:]:
        if (snake_pos[0]==blocks[0] and snake_pos[1] == blocks[1]):
            gameover()



    show_score()
    pygame.display.update()
    fps_controller.tick(21)





