
import pygame
pygame.init()
  
# Creating window
gameWindow = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Event Handling")
  
  
exit_game = False
game_over = False
  
# Creating a game loop
check = 1
while True:
    
    for event in pygame.event.get():  # For Loop
        if event.type == pygame.QUIT:
            pygame.quit()
  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")
            elif event.key == pygame.K_LEFT:
                print("You have pressed left arrow key")
    if check:
        check = 0
        print("checkkk")
    else :
        print("not check")
  
