import pygame
import random
pygame.init()

white=(255,255,255)                  //this stuff is for food color and snake color
black=(0,0,0)
red=(255,0,0)

s_width=600                                                           //height and width of snake at start
s_height=600
screen=pygame.display.set_mode((s_height,s_width))
pygame.display.set_caption("GaMe")

snake_size=10
snake_x=5
snake_y=5
game_over=False
game_end=False
fps=60                                           //fps is for speed of snake during run time
velocity_x=0
velocity_y=0
food_x=random.randint(0,s_width)
food_y=random.randint(0,s_height)
score=0
font=pygame.font.SysFont(0,30)                             //for score display
snake_list=[]
snake_length=1





def engine(screen,color,snk_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(screen,color,[x,y,snake_size,snake_size])                  // for when game start snake should be in square




def text_on_screen(text,color,x,y):
    shlok=font.render(text,True,color)
    screen.blit(shlok,[x,y])


clock=pygame.time.Clock()

while not game_end:                                                                      //for to move snake up,down,left.right
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_end=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=5
                velocity_y=0

            if event.key==pygame.K_LEFT:
                velocity_x=-5
                velocity_y=0
            if event.key==pygame.K_UP:
                velocity_y=-5
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=5
                velocity_x=0

    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y
    screen.fill(white)
    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score+=1
        print(f"score is {score*10}")
        food_x = random.randint(0, s_width)                                               //genrate food of snake randomly
        food_y = random.randint(0, s_height)
        snake_length+=5


    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)
    if len(snake_list)>snake_length:
        del snake_list[0]

    text_on_screen(f"score {score*10}",red,0,3)                                                        //score in multiple of 10
    pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(screen,black,[snake_x,snake_y,snake_size,snake_size])
    engine(screen,black,snake_list,snake_size
           )
    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()
