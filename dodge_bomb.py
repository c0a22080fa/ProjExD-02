import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}



def bound_1(rect: pg.rect) -> tuple[bool, bool]:
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right: 
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:
        tate = False
    return yoko, tate

def main():
    bd_imgs = []  # 大きさのリストを作成
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    for r in range(1, 11):  #　追加課題2
        bd_img = pg.Surface((20*r, 20*r))
        pg.draw.circle(bd_img, (255, 0, 0), (10*r, 10*r), 10*r)
        bd_img.set_colorkey((0,0,0))
        bd_imgs.append(bd_img)
    bd_img = bd_imgs[0]  # 初期の大きさリストを0に設定
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bd_rct = bd_img.get_rect()
    bd_rct.center = x, y  #xとyをrandomに生成
    vx, vy = +5, +5
    clock = pg.time.Clock()
    tmr = 0 

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0
        if kk_rct.colliderect(bd_rct):
            print("ゲームオーバー")
            return 
        
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv[0], sum_mv[1])

        if bound_1(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bd_rct.move_ip(vx, vy)
        yoko, tate =bound_1(bd_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bd_img, bd_rct)
        
        tmr += 1
        key_lst = pg.key.get_pressed()
        
        
        bd_img = bd_imgs[min(tmr//500, 9)] # 爆弾の大きさを更新
        
        pg.display.update()
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()