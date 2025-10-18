import cv2
import numpy as np
def apply_color_filter(image,filter_type):
    filtered_type = image.copy()
    if filter_type == "red_tint":
        filtered_type[ :, :, 1] = 0
        filtered_type[ :, :, 0] = 0
    elif filter_type == "blue_tint":
        filtered_type[ :, :, 1] = 0
        filtered_type[ :, :, 2] = 0
    elif filter_type == "green_tint":
        filtered_type[ :, :, 0] = 0
        filtered_type[ :, :, 2] = 0
    elif filter_type == "increase_red":
        filtered_type[ :, :, 2] = cv2.add(filtered_type[ :, :, 2],50)
    elif filter_type == "decrease_blue":
        filtered_type[ :, :, 0] = cv2.subtract(filtered_type[ :, :, 0],50)
    return filtered_type
image_path = "ground.png"
image = cv2.imread(image_path)
if image is None:
    print("Error image not found")
else:
    filter_type = "original"
    print("Press the following keys to apply the filters")
    print("r - red_tint")
    print("b - blue_tint")
    print("g - green_tint")
    print("i - increase_red")
    print("d - decrease_blue")
    print("q - quit")
    while True:
        filtered_type = apply_color_filter(image, filter_type)
        cv2.imshow('fILTERD IMAGE ,', filtered_type)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b') :
            filter_type = "blue_tint"
        elif key == ord('g') :
            filter_type = "green_tint"
        elif key == ord('i') :
            filter_type = "increase_red"
        elif key == ord('d') :
            filter_type = "decrease_blue"
        elif key == ord('q') :
            print("Exiting.....")
            break
        else:
            print("Invalid key pls press , r or b,g,i,d,q")

    cv2.destroyAllWindows()      





