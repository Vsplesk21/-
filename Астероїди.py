from pygame import * 
from random import randint



def showEndWindow(window, message):
        clock = time.Clock()
        run = True
        font.init()
        text = font.Font(None, 70).render(message, True, (255, 255, 255))
        while run:
        # обробка подій
            for e in event.get():
                if e.type == QUIT:
                    run = False
            window.blit(text, (250, 250))
            display.update()
            clock.tick(60)

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, x, y, speed, size_w, size_h): 
        super().__init__() 
        self.speed = speed 
        self.player_image = transform.scale(image.load(player_image), (size_w, size_h)) 
        self.rect = self.player_image.get_rect() 
        self.rect.x = x 
        self.rect.y = y 


class Hero(GameSprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__(player_image, x, y, speed, size_w, size_h)
        self.bullets = []
    
    
    def update(self):
        keys = key.get_pressed() 
        if keys[K_a]: 
            self.rect.x -= self.speed 
        if keys[K_d]:
            self.rect.x += self.speed
        for bullet in self.bullets:
            bullet.update()

    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            bullet.draw(window)
            bullet.update()
    
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))
        
 
class Enemy(GameSprite): 
    def update(self): 
        global missEnemy
        self.rect.y += self.speed
        if self.rect.y > 550:
            self.rect.y = -100
            self.rect.x = randint(0,500)
            missEnemy += 1
    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))

mixer.init()
mixer.music.load("Лабіринт/space.ogg")
mixer.music.play()

shootsound = mixer.Sound("Лабіринт/fire.ogg")

missEnemy = 0
diedEnemy = 0

monsters = [] 
y = 0 
for i in range(15): 
    monsters.append(Enemy("Лабіринт/asteroid.png", randint(0, 700), y, 1, 50, 50)) 
    monsters.append(Enemy("Лабіринт/Граната.webp", randint(0, 700), y, 1, 50, 50))
    y -= 50 
 
hero = Hero("Лабіринт/7202313.png", 250, 440, 2, 60, 60) 
 
window = display.set_mode((700, 500)) 
clock = time.Clock() 
background = transform.scale(image.load("Лабіринт/Космос.png"), (700, 500)) 
font.init()
font1 = font.Font(None, 20)
font2 = font.Font(None, 50)
 
while True: 
    #обробка подій 
    for e in event.get(): 
        if e.type == QUIT: 
            quit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.bullets.append(Bullet("Лабіринт/bullet.png", hero.rect.centerx, hero.rect.y, 10, 5, 10))
                shootsound.play()
 
    # оновлення обєктів 
    for mon in monsters: 
        mon.update()
    hero.update() 

    text = font1.render("Кількість знищених: " + str(diedEnemy), False, (255, 255, 255))
    text2 = font1.render("Кількість пропущених: " + str(missEnemy), False,(255, 255, 255))
    text3 = font2.render("Ти програв", False,(255, 255, 255))

    # відмалювати 
    window.blit(background, (0, 0)) 
    for mon in monsters: 
        mon.draw(window)
    
    for mon in monsters:
        for bullet in hero.bullets:
            if bullet.rect.colliderect(mon.rect):
                mon.rect.x = randint(0, 500)
                mon.rect.y = -50
                hero.bullets.remove(bullet)
                diedEnemy += 1
                break

    

    for mon in monsters:
        if hero.rect.colliderect(mon.rect):
            showEndWindow(window, "Ти програв!!!")
    if missEnemy >= 3:
        showEndWindow(window, "Ти програв!!!")

    window.blit(text, (25,20))
    window.blit(text2, (25,40))



    hero.draw(window) 
    display.update() 
    clock.tick(60)