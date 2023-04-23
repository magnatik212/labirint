from pygame import*
win_width = 700
class GameSprite(sprite.Sprite):
    def __init__(self,picture,x,y,w,h):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image,player_x,player_y,size_x,size_y,playe_x_speed,player_y_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.x_speed = playe_x_speed
        self.y_speed = player_y_speed
    def update(self):
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
            platforms_touched = sprite.spritecollide(self,barriers, False)
            if self.x_speed > 0:
                for p in platforms_touched:
                    self.rect.left = max(self.rect.left, p.rect.right)
        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed <0:
            self.rect.y += self.y_speed
            platforms_touched = sprite.spritecollide(self,barriers,False)
            if self.y_speed > 0:
                for p in platforms_touched:
                    self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        if self.rect.x <= 420: #w1.wall_x + w1.wall_width
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width,win_height))
back = (119,210,223)
w1 = GameSprite ('stena.png',win_width / 2 - win_width / 3, win_height / 2,300,50)
w2 = GameSprite ('stena.png',370,100,50,400)
barriers = sprite.Group()
barriers.add(w1)
barriers.add(w2)
packman = Player('hero.jpg',5, win_height - 80, 80, 80, 0, 0)
final = GameSprite
final = GameSprite("pelmen.png",win_width -85,win_height -100,80,80)
monster1 = Enemy('fox.png.',500,150,80,80,5)
monsters = sprite.Group()
monsters.add(monster1)
run = True
finish = False
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                    packman.x_speed = 5
            elif e.key == K_UP:
                    packman.y_speed = -5
            elif e.key == K_DOWN:
                    packman.y_speed = 5
            elif e.key == K_SPACE:
                packman.fire()

        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
       
        
    if finish != True:
        window.fill(back)  
        monster1.reset()
        w1.reset()
        w2.reset()
        monster1.update()
        packman.reset()
        final.reset()
        packman.update()
        if sprite.spritecollide(packman,monsters,False):
            finish = True
            img = image.load('game.over.png')
            window.fill((255,255,255))
            window.blit(transform.scale(img,(win_width, win_height)), (0,0))
        if sprite.collide_rect(packman, final):
                finish = True
                win=image.load('won2.png')
                window.fill ((250,250,250))
                window.blit(transform.scale(win,(win_width,win_height)),(0,0))
    time.delay(50)
    display.update()