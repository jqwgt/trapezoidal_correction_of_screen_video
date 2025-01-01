import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import time


def perspective_transform(img, pts1, width=1920, height=1080):
    """透视变换函数"""
    pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (width, height))
    return result, matrix


def capture_screen():
    """捕获屏幕内容"""
    screen = np.array(ImageGrab.grab())
    return cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)


# 全局变量
points = []
transform_matrix = None


def mouse_callback(event, x, y, flags, param):
    global points, transform_matrix
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])
        temp_img = capture_screen()
        cv2.circle(temp_img, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('Original', temp_img)

        if len(points) == 4:
            pts1 = np.float32(points)
            _, transform_matrix = perspective_transform(temp_img, pts1)


def main():
    cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('Original', mouse_callback)

    while True:
        # 捕获当前屏幕
        current_frame = capture_screen()
        cv2.imshow('Original', current_frame)

        # 如果已经有了变换矩阵，则进行实时透视变换
        if transform_matrix is not None:
            result = cv2.warpPerspective(current_frame, transform_matrix, (1920, 1080))
            cv2.imshow('Result', result)

        # 按ESC退出
        if cv2.waitKey(1) == 27:
            break

        # 控制刷新率
        time.sleep(1 / 30)  # 约30FPS

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()