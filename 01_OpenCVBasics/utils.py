from matplotlib import pyplot as plt
import cv2

def image_stats(image):
    return image.shape

#For displaying in Jupyter Notebook we use matplotlib
def display_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.show()