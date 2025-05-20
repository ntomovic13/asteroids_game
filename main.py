import pygame
from constants import *
from player import Player
from asteroidfield import *
from shot import Shot
import sys



def main():
    score = 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Asteroids")

    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)    
    asteroidfield = AsteroidField()

    dt = 0
    
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")    

    

    while True:   
        font = pygame.font.SysFont(None, 30)
        text = font.render(f"Score: {score}", True, "white")
        text_rect = text.get_rect(center=(90,50))    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)


        for ast in asteroids:
            if player.collision(ast):
                sys.exit(f"Game over!\nYour score is: {score}")   
            for bul in shots:
                if ast.collision(bul):
                    score += ast.split()
                    bul.kill()
        
        screen.fill("black")
        screen.blit(text, text_rect)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()