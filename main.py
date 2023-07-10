import pygame
import sys

#CONSTANTS
SCREEN = SCREEN_WIDTH ,SCREEN_HEIGHT= 480, 720
FPS = 60
WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 20)

def main():
    pygame.init()

    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h

    #TODO: res işini sonra hallet.
    if width >= height:
        win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
    else:
        win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

    clock = pygame.time.Clock()
    #TODO: image load işini başka modüle taşı.
    ingame_bg_image = pygame.image.load("./Assets/bg.jpg")
    ingame_bg_image = pygame.transform.scale(ingame_bg_image, pygame.display.get_window_size())
    is_game_running = True
    while is_game_running:
        ######EVENT LISTEN######
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_game_running = False
        #######################

        clock.tick(FPS)
        print(clock.get_fps())
        
        #arka planı ekranı çiz
        win.blit(ingame_bg_image, (0,0))

        pygame.display.update()
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()