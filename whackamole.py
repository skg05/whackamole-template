import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        def draw_grid():
            for i in range(32,640,32):
                pygame.draw.line(screen,"black",(i,0),(i,512))
            for i in range(32,512,32):
                pygame.draw.line(screen, "black", (0, i), (640, i))

        running = True
        draw_grid()
        screen.fill("light green")
        draw_grid()
        mole_x = random.randrange(0, 20)
        mole_y = random.randrange(0, 16)
        screen.blit(mole_image, mole_image.get_rect(topleft=((mole_x * 32)+3, (mole_y * 32)+1)))
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    print(x,y)
                    row = x//32
                    col = y//32
                    print(row,col)
                    if mole_x == row and mole_y == col:
                        mole_x = random.randrange(0, 20)
                        mole_y = random.randrange(0, 16)
                        screen.fill("light green")
                        draw_grid()
                        screen.blit(mole_image, mole_image.get_rect(topleft=((mole_x * 32) + 3, (mole_y * 32) + 1)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
