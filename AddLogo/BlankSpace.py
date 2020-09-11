import cv2


class BlankSpace:
    @staticmethod
    def findPosition(image_path, logo_path):
        logo_size = cv2.imread(logo_path).shape[:2]
        img = cv2.imread(image_path)
        img_size = img.shape
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, gray = cv2.threshold(gray, 240, 255, 0)
        gray = cv2.rectangle(gray, (0, 0), (img_size[1], img_size[0]), 255)
        contours, hier = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            rect_size = (x+w - x, y+h - y)
            print(rect_size)
            if logo_size[1] < rect_size[0] < img_size[1] and logo_size[0] < rect_size[1] < img_size[0]:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 20)
                # return [int((2 * x + w - logo_size[1])/2), int((2 * y + h - logo_size[0])/2)]
        cv2.imshow('aaa', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return [0, 0]


print(BlankSpace.findPosition(
    'C:/Users/fltrade/Desktop/adsfasf/B Audi Q7 15- (1).jpg',
    'C:/Users/fltrade/Desktop/Z4L Logo Concept.png'))
