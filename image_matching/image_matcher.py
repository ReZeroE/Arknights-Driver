import cv2
import os
import numpy as np
import imutils

MATCH_THRESHOLD = 0.8

class ImageMatcher:
    def match_image(self, original_image_name, template_name):
        MAIN_IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'screenshots/{original_image_name}')
        TEMPLATE_IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'templates/{template_name}')

        # Read the main image
        img_rgb = cv2.imread(MAIN_IMAGE_PATH)

        # Convert to grayscale
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        # Read the template
        template = cv2.imread(TEMPLATE_IMAGE_PATH,0)

        # Store width and height of template in w and h
        w, h = template.shape[::-1]
        found = None
        found_list = []

        max_acc = 0
        ct = 0
        for scale in np.linspace(0.01, 10.0, 100)[::-1]:
            # resize the image according to the scale, and keep track of the ratio of the resizing
            resized = imutils.resize(img_gray, width = int(img_gray.shape[1] * scale))
            r = img_gray.shape[1] / float(resized.shape[1])
            edged = cv2.Canny(resized, 50, 200)
            
            # cv2.imshow("Image", edged)
            # cv2.waitKey(0)

            try:
                result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
            except:
                continue

            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

            # (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
            # (endX, endY) = (int((maxLoc[0] + w) * r), int((maxLoc[1] + h) * r))

            # # draw a bounding box around the detected result and display the image
            # cv2.rectangle(img_rgb, (startX, startY), (endX, endY), (0, 0, 255), 2)
            # cv2.imshow("Image", img_rgb)
            # key = cv2.waitKey(3000)#pauses for 3 seconds before fetching next image
            # if key == 27:#if ESC is pressed, exit loop
            #     cv2.destroyAllWindows()

            print(f"[{ct}] -> Acc: {maxVal}")
            ct += 1
            if maxVal > max_acc:
                found = (maxVal, maxLoc, r)
                max_acc = maxVal

            found_list.append((maxVal, maxLoc, r))

            # end loop (template larger than original image)
            if resized.shape[0] < h or resized.shape[1] < w: break

        if found == None:
            return False

        # compute the (x, y) coordinates of the bounding box based on the resized ratio
        (_, maxLoc, r) = found
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + w) * r), int((maxLoc[1] + h) * r))

        # draw a bounding box around the detected result and display the image
        cv2.rectangle(img_rgb, (startX, startY), (endX, endY), (0, 0, 0), 2)
        cv2.imshow("Image", img_rgb)
        cv2.waitKey(0)

        i = input('Coninue Drawing? [y/n]')
        if i.lower() != 'y': exit(0)

        for f in found_list:
            (_, maxLoc, r) = f
            (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
            (endX, endY) = (int((maxLoc[0] + w) * r), int((maxLoc[1] + h) * r))
            cv2.rectangle(img_rgb, (startX, startY), (endX, endY), (0, 0, 255), 1)

        cv2.imshow("Image", img_rgb)
        cv2.waitKey(0)

        return True


if __name__ == "__main__":
    im = ImageMatcher()
    print(im.match_image("name.png", 'temp.png'))