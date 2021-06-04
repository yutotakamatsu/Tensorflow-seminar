import cv2

def mosaic(img, rect, size):
    # モザイクをかける領域を取得
    # 関数に投げられたrectをx1, y1, x2, y2に入力する．
    (#) = rect
    # x1とx2を減算することでモザイクする矩形の幅を取得する
    w = x2 - x1
    # y2とy1を減算することでモザイクする矩形の高さを取得する
    h = y2 - y1
    # 画像のモザイクをする位置を決定する
    i_rect = img[#]
    # モザイク処理のため一度縮小して拡大する
    i_small = cv2.resize(i_rect, ( size, size))
    i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)
    # 画像にモザイク画像を重ねる
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2


