import cv2
import os

def is_blurry(image_path, threshold=100):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.Laplacian(gray, cv2.CV_64F).var()
    print(blur)
    return blur < threshold

def remove_blurry_images(folder_path, threshold=110):
    blurry_images = []
    count = 0
    for folder in os.listdir(folder_path):
        class_path = os.path.join(folder_path, folder)
        if not os.path.isdir(class_path):
            continue
        for filename in os.listdir(class_path):
            if not filename.endswith(('.png', '.jpg', '.jpeg')):
                continue
            count += 1
            image_path = os.path.join(class_path, filename)
            if is_blurry(image_path, threshold):
                blurry_images.append(filename)
                os.remove(image_path)
    print(count)
    print(len(blurry_images))

folder_path = 'data'
blurry_images_removed = remove_blurry_images(folder_path, threshold=180)
is_blurry('data/sadness/160519156_1d48dd1827_b_face.png')