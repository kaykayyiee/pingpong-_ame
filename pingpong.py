from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80 :
            self.rect.y += self.speed
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis_balll.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

skor_1 = 0
skor_2 = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        text = font.render("player 1: " + str(skor_1), 1, (0, 0, 0,))
        window.blit(text, (10, 20))

        text_lose = font.render("player 2: " + str(skor_2), 1, (0, 0, 0))
        window.blit(text_lose, (10, 50))
        racket1.update_1()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1                                                                                                                                                
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0: #kondisi ketika player 2 menang
            skor_2 += 1
            ball.rect.x = win_width // 2 - ball.rect.width // 2
            ball.rect.y = win_height // 2 - ball.rect.height // 2
            speed_x *= -1
            speed_y *= 1
            
        if ball.rect.x > win_width: #kondisi ketika player 1 menang
            skor_1 += 1
            ball.rect.y = win_width // 2 - ball.rect.width // 2
            ball.rect.x = win_height // 2 - ball.rect.height // 2
            speed_y *= -1
            speed_x *= 1
            
        if skor_1 >= 5:
            finish - True
            window.blit(lose2, (200, 200))
            game_over = True
        if skor_2 >= 5:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True


        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)