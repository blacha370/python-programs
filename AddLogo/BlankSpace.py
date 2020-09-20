import cv2
import numpy as np


class BlankSpace:
    @staticmethod
    def findPosition(image_path, logo_path):
        logo_size = cv2.imread(logo_path).shape[:2]
        img = cv2.imread(image_path)
        img_size = img.shape
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, gray = cv2.threshold(gray, 240, 255, 0)
        gray = cv2.bitwise_not(gray)
        contours, hier = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        biggest_contour = list()
        print(logo_size[0] * logo_size[1])
        for cnt in contours:
            if cv2.contourArea(cnt) > logo_size[0] * logo_size[1]:
                biggest_contour.append(cnt)
                print(cv2.contourArea(cnt))
        for cnt in biggest_contour:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            im = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
        cv2.imshow('aaa', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
