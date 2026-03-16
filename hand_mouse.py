import cv2
import mediapipe as mp
import pyautogui
import math
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

camera = cv2.VideoCapture(0)

x1 = y1 = x2 = y2 = 0
click_done = False

while True:
    _, image = camera.read()
    image = cv2.flip(image, 1)

    image_height, image_width, _ = image.shape

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_image)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(image, hand)

            for id, lm in enumerate(hand.landmark):

                x = int(lm.x * image_width)
                y = int(lm.y * image_height)

                if id == 8:
                    mouse_x = int(screen_width / image_width * x)
                    mouse_y = int(screen_height / image_height * y)

                    pyautogui.moveTo(mouse_x, mouse_y)

                    x1, y1 = x, y
                    cv2.circle(image, (x, y), 10, (0, 255, 255), -1)

                if id == 4:
                    x2, y2 = x, y
                    cv2.circle(image, (x, y), 10, (0, 255, 255), -1)

            distance = math.hypot(x2 - x1, y2 - y1)

            if distance < 35 and not click_done:
                pyautogui.click()
                click_done = True
                time.sleep(0.2)

            if distance > 45:
                click_done = False

    cv2.imshow("Hand Mouse Control", image)

    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()