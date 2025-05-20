import pygame
from constants import *
from player import Player
from asteroidfield import *
from shot import Shot
import sys



def main():
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
        font1 = pygame.font.SysFont(None, 35)

        #scoring
        score_text = font.render(f"Score: {player.score}", True, "white")
        score_text_rect = score_text.get_rect(center=(90,50))

        #lifes
        life_text = font.render(f"Lifes: {player.lifes}", True, "red")
        life_text_rect = life_text.get_rect(center=(1200,50))   

        #interactive
        int_text1 = font1.render("Be carefull!", True, "green")
        int_text2 = font1.render("This is your last chance!", True, "red")
        int_text1_rect = int_text1.get_rect(center=(640,20))
        int_text2_rect = int_text1.get_rect(center=(560,20))

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for ast in asteroids:
            if player.collision(ast):
                if player.lifes == 1:
                    sys.exit(f"Game over!\nYour score is: {player.score}")
                else:
                    player.timer -= PLAYER_SHOT_COOLDOWN
                    player.get_damage()
                    for i in asteroids:
                        i.kill()

            for bul in shots:
                if ast.collision(bul):
                    player.score += ast.split()
                    bul.kill()
        
        screen.fill("black")
        screen.blit(score_text, score_text_rect)
        screen.blit(life_text, life_text_rect)
        if player.lifes == 2:
            screen.blit(int_text1, int_text1_rect)
        if player.lifes == 1:
            screen.blit(int_text2, int_text2_rect)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()