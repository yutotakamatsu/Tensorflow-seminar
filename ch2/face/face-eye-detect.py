import matplotlib.pyplot as plt
import cv2

# カスケードファイルを指定して検出器を作成 --- (*1)
cascade_face_file = "haarcascade_frontalface_alt.xml"
cascade_eye_file = "haarcascade_eye.xml"
cascade_face = cv2.CascadeClassifier(cascade_face_file)
cascade_eye = cv2.CascadeClassifier(cascade_eye_file)

# 画像の読み込んでグレイスケールに変換する --- (*2)
img = cv2.imread("girl.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 顔認識を実行 --- (*3)
face_list = cascade_face.detectMultiScale(img_gray, minSize=(150,150))
# 結果を確認 --- (*4)
if len(face_list) == 0:
    print("失敗")
    quit()
# 認識した部分に印をつける --- (*5)
for (x,y,w,h) in face_list:
    print("顔の座標=", x, y, w, h)
    print(f'顔座標の大きさ＝{x + w}')
    red = (0, 0, 255)
    cv2.rectangle(img, (x, y), (x+w, y+h), red, thickness=20)
    face_img = img_gray[y:y+h, x:x+w]

cv2.imshow('img',face_img)
cv2.waitKey(0)

# 認識した顔画像の中に目があるか判定しよう
eye_list = cascade_eye.detectMultiScale(＃)
# 結果の確認
if len(eye_list) == 0:
    print("失敗")
    quit()
# 認識した部分に印をつける（顔認識でやったように認識した部分に印をつけよう）
for (ex,ey,ew,eh) in eye_list:
    print("目の座標＝", ex, ey, ew, eh)
    print(f'目の大きさ＝{ex + ew}')
    if ex + ew >= 200:
        green = (0, 255, 0)
        cv2.rectangle(img, (＃,＃), (＃, ＃), green, thickness=20)

#画像を出力
cv2.imwrite("face-detect.png", img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
