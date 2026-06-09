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
        
        x = 0
        y = 0
        if key_lst[pg.K_UP]: #上矢印キーが押されたら
            y -= 1#上に移動
        if key_lst[pg.K_DOWN]: #下矢印キーが押されたら
            y += 1#下に移動
        if key_lst[pg.K_LEFT]: #左矢印キーが押されたら
            x -= 1#左に移動
        if key_lst[pg.K_RIGHT]: #右矢印キーが押されたら
            x += 2 #右に移動　#演習1: 風に流されるため、より強い力で前に進む
        kt_rct.move_ip(x, y) #演習2:　move_ipを一回だけ使用
            
        x = tmr%3200
        kt_rct.move_ip(-1, 0) #演習1: こうかとんが風に流されるようにする
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