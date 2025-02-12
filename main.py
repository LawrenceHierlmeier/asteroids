import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    if pygame.get_init() == False:
        pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock() 
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing Game")
                return
        screen.fill((0,0,0))
        


        updatable.update(dt)
        for unit in drawable:
            unit.draw(screen) 




        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.tick(60)/1000
        #print(dt)

    


if __name__ == "__main__":
    main()