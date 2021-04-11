# Add Black Background While Utilizing "cv2.putText()"
import cv2
import numpy as np

# Load Image, Define Rectangle Bounds
image = cv2.imread(r'C:\Users\Bharath\Downloads\test.jpg')

# Overlay Space
(x, y, w, h) = (40, 30, 300, 60)

# Alpha, The 4th channel of The Image
alpha = 0.3
overlay = image.copy()
output = image.copy()

# Corner
cv2.rectangle(overlay, (x, x), (x + w, y + h), (0, 0, 0), -1)

# Add Text
cv2.putText(
    overlay,
    'HELLO WORLD..!',
    (x + int(w / 10), y + int(h / 1.5)),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 255, 255),
    2,
    )

# Combine Final Output
cv2.addWeighted(
    overlay,
    alpha,
    output,
    1 - alpha,
    0,
    output,
    )

# Display Results

cv2.imshow('Output', output)
cv2.waitKey(0)
