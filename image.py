import cv2

# Load the image
img = cv2.imread(r'C:\Users\DELL\OneDrive\1.jpeg')

# Convert the image to grayscale
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_gray = 255 - gray_scale

# Apply a Gaussian blur to the inverted image
blur = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

# Blend the grayscale image with the blurred image using a color dodge blend mode
sketch = cv2.divide(gray_scale, 255 - blur, scale=256)

cv2.imshow('Sketch', sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
