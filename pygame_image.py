import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True , False)
    kt_img = pg.image.load("fig/3.png") #練習３：こうかとんSurfaceの作成
    kt_img = pg.transform.flip(kt_img, True, False)
    kt_rct = kt_img.get_rect() #練習10-1:こうかとんRectの取得
    kt_rct.center = 300, 200 #練習10-2: こうかとんRectの中心属性を設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        key_lst = pg.key.get_pressed() #練習10-3: 全てのキーの押下状態の取得
        if key_lst[pg.K_UP]: #上矢印キーが押されたら
            kt_rct.move_ip((0, -1)) #上に移動
        if key_lst[pg.K_DOWN]: #下矢印キーが押されたら
            kt_rct.move_ip((0, +1)) #下に移動
        if key_lst[pg.K_LEFT]: #左矢印キーが押されたら
            kt_rct.move_ip((-1, 0)) #左に移動
        if key_lst[pg.K_RIGHT]: #右矢印キーが押されたら
            kt_rct.move_ip((1, 0)) #右に移動
            
        x = tmr%3200
        screen.blit(bg_img, [-x, 0]) #練習５：背景画像を右から左へ
        screen.blit(bg_img2, [-x+1600, 0]) #練習７：２枚目のSurface
        screen.blit(bg_img, [-x+3200, 0]) #練習９：３枚目の背景画像の描画
        screen.blit(kt_img, kt_rct) #練習４：こうかとんSurfaceを描画する
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()