import cv2
path = 'numpy.jpg'
image = cv2.imread(path)
window_name = 'Image'
center_coordinates = (150, 60)
radius = 20
color = (255, 0, 0)
thickness = 2
image = cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()