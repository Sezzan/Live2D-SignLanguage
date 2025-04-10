import cv2
import mediapipe as mp
import math
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time
import sys
import json

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# 根據兩點的座標，計算角度
def vector_2d_angle(v1, v2):
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_ = math.degrees(math.acos((v1_x*v2_x+v1_y*v2_y)/(((v1_x**2+v1_y**2)**0.5)*((v2_x**2+v2_y**2)**0.5))))
    except:
        angle_ = 180
    return angle_

# 根據傳入的 21 個節點座標，得到該手指的角度
def hand_angle(hand_):
    angle_list = []
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[2][0])),(int(hand_[0][1])-int(hand_[2][1]))),
        ((int(hand_[3][0])- int(hand_[4][0])),(int(hand_[3][1])- int(hand_[4][1])))
    )
    angle_list.append(angle_)
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])-int(hand_[6][0])),(int(hand_[0][1])- int(hand_[6][1]))),
        ((int(hand_[7][0])- int(hand_[8][0])),(int(hand_[7][1])- int(hand_[8][1])))
    )
    angle_list.append(angle_)
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[10][0])),(int(hand_[0][1])- int(hand_[10][1]))),
        ((int(hand_[11][0])- int(hand_[12][0])),(int(hand_[11][1])- int(hand_[12][1])))
    )
    angle_list.append(angle_)
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[14][0])),(int(hand_[0][1])- int(hand_[14][1]))),
        ((int(hand_[15][0])- int(hand_[16][0])),(int(hand_[15][1])- int(hand_[16][1])))
    )
    angle_list.append(angle_)
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[18][0])),(int(hand_[0][1])- int(hand_[18][1]))),
        ((int(hand_[19][0])- int(hand_[20][0])),(int(hand_[19][1])- int(hand_[20][1])))
    )
    angle_list.append(angle_)
    return angle_list

# 根據手指角度的串列內容，返回對應的手語單詞
def hand_pos(finger_angle, finger_angle_other=None):
    f1 = finger_angle[0]
    f2 = finger_angle[1]
    f3 = finger_angle[2]
    f4 = finger_angle[3]
    f5 = finger_angle[4]

    if finger_angle_other:
        fo1 = finger_angle_other[0]
        fo2 = finger_angle_other[1]
        fo3 = finger_angle_other[2]
        fo4 = finger_angle_other[3]
        fo5 = finger_angle_other[4]
        if f1<50 and f2<50 and f3<50 and f4<50 and f5<50 and fo1<50 and fo2<50 and fo3<50 and fo4<50 and fo5<50:
            return '讀書'
        elif f1>50 and f2<50 and f3<50 and f4<50 and f5<50 and fo1>50 and fo2<50 and fo3<50 and fo4<50 and fo5<50:
            return '門'
        elif f1<50 and f2>50 and f3>50 and f4>50 and f5>50 and fo1>50 and fo2<50 and fo3>50 and fo4>50 and fo5>50:
            return '血'
        elif f1>50 and f2<50 and f3<50 and f4<50 and f5>50 and fo1>50 and fo2<50 and fo3>50 and fo4>50 and fo5>50:
            return '當'
        elif f1>50 and f2<50 and f3>50 and f4>50 and f5>50 and fo1<50 and fo2<50 and fo3<50 and fo4<50 and fo5<50:
            return '表演'
        elif f1<50 and f2>50 and f3>50 and f4>50 and f5<50 and fo1<50 and fo2>50 and fo3>50 and fo4>50 and fo5<50:
            return '牛'
        elif f1<50 and f2<50 and f3>50 and f4>50 and f5>50 and fo1<50 and fo2<50 and fo3>50 and fo4>50 and fo5>50:
            return '心'
        elif f1>50 and f2<50 and f3<50 and f4>50 and f5>50 and fo1>50 and fo2<50 and fo3<50 and fo4>50 and fo5>50:
            return '相信'
        elif f1<50 and f2<50 and f3<50 and f4>50 and f5>50 and fo1<50 and fo2<50 and fo3<50 and fo4>50 and fo5<50:
            return '坦白'
        elif f1<50 and f2>50 and f3>50 and f4>50 and f5>50 and fo1<50 and fo2<50 and fo3<50 and fo4<50 and fo5<50:
            return '有名'
        elif f1>50 and f2<50 and f3>50 and f4>50 and f5>50 and fo1>50 and fo2<50 and fo3<50 and fo4>50 and fo5>50:
            return '小'
        elif f1>=50 and f2>=50 and f3<50 and f4<50 and f5<50 and fo1>=50 and fo2>=50 and fo3<50 and fo4<50 and fo5<50:
            return '銀行'
        elif f1<50 and f2>=50 and f3<50 and f4<50 and f5<50 and fo1<50 and fo2>=50 and fo3<50 and fo4<50 and fo5<50:
            return '銀行'

    if f1<50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
        return '男'
    elif f1>=50 and f2>=50 and f3<50 and f4>=50 and f5>=50:
        return '高'
    elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5<50:
        return '等'
    elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
        return '在'
    elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
        return '女'
    elif f1>=50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '我'
    elif f1>=50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return '命令'
    elif f1>=50 and f2>=50 and f3<50 and f4<50 and f5<50:
        return 'ok'
    elif f1<50 and f2>=50 and f3<50 and f4<50 and f5<50:
        return 'ok'
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5>50:
        return '川'
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5<50:
        return '是'
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5<50:
        return '有'
    elif f1<50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
        return '怎麼會'
    elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '刷牙'
    elif f1<50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return '懶惰'
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5>=50:
        return '八'
    else:
        return ''

# 使用PIL繪製中文字符
def draw_chinese_text(img, text, position, font_path='simsun.ttc', font_size=50, color=(255, 255, 255)):
    font = ImageFont.truetype(font_path, font_size)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text(position, text, font=font, fill=color)
    return np.array(img_pil)

# 繪製詞彙提示
def draw_sign_prompt(img, sign_list, current_index, font_path='simsun.ttc', font_size=30):
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    y_position = img.shape[0] - 50  # 畫面底部
    x_position = 10

    for i, sign in enumerate(sign_list):
        if i < current_index:
            color = (0, 255, 0)  # 綠色：已完成
        elif i == current_index:
            color = (0, 0, 255)  # 紅色：當前詞彙
        else:
            color = (255, 255, 255)  # 白色：未完成
        font = ImageFont.truetype(font_path, font_size)
        draw.text((x_position, y_position), sign, font=font, fill=color)
        x_position += len(sign) * font_size + 10  # 根據字數調整間距

    return np.array(img_pil)

# 從命令行參數讀取詞彙列表
sign_list = []
if len(sys.argv) > 1:
    try:
        sign_list = json.loads(sys.argv[1])  # 嘗試解析 JSON 格式
    except json.JSONDecodeError:
        sign_list = sys.argv[1].split(",")  # 備用方案：以逗號分隔

# 如果沒有傳入詞彙，設置默認值
if not sign_list:
    sign_list = ["我", "讀書"]

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    w, h = 540, 310
    last_detection_time = 0
    detection_interval = 0.2
    text = ""
    current_sign_index = 0  # 當前詞彙索引
    completed = False  # 是否完成所有詞彙
    completion_time = 0  # 完成時間

    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (w, h))
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        current_time = time.time()

        # 如果尚未完成所有詞彙，繼續辨識
        if not completed:
            if current_time - last_detection_time >= detection_interval:
                results = hands.process(img2)
                if results.multi_hand_landmarks:
                    hand_angles = []
                    for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                        finger_points = []
                        for i in hand_landmarks.landmark:
                            x = i.x * w
                            y = i.y * h
                            finger_points.append((x, y))
                        if finger_points:
                            finger_angle = hand_angle(finger_points)
                            hand_angles.append(finger_angle)
                            print(f"手 {idx + 1} 的手指角度: {finger_angle}")

                    if len(hand_angles) == 1:
                        text = hand_pos(hand_angles[0])
                    elif len(hand_angles) == 2:
                        text = hand_pos(hand_angles[0], hand_angles[1])
                    else:
                        text = ''

                    if text:
                        print(f"Detected sign: {text}")
                        # 檢查是否匹配當前詞彙
                        if current_sign_index < len(sign_list) and text == sign_list[current_sign_index]:
                            current_sign_index += 1  # 匹配成功，進入下一個詞彙
                            # 如果所有詞彙都完成，記錄完成時間
                            if current_sign_index >= len(sign_list):
                                completed = True
                                completion_time = current_time
                    else:
                        text = ''
                    last_detection_time = current_time
                else:
                    text = ''
                    last_detection_time = current_time

        # 繪製手語詞彙和提示
        img = draw_chinese_text(img, text, (30, 120))
        img = draw_sign_prompt(img, sign_list, current_sign_index)

        # 如果已完成，等待 2 秒後關閉
        if completed:
            if current_time - completion_time >= 2:  # 等待 2 秒
                break

        cv2.imshow('SignLanguage', img)
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()