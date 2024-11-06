import cv2

img_path = "C:Data\\animal.jpg"

# Mouse callback function
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the BGR pixel value at the clicked position
        pixel_value = img[y, x]
        b, g, r = pixel_value
        pixel_text = f" (   {x},{y}) - BGR: ({b},{g},{r})"
        
        # Display the pixel value on the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, pixel_text, (x, y), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        
        print(pixel_text)
        
        # Draw a circle at the clicked position
        cv2.circle(img, (x, y), 20, (255, 0, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button down at ({x}, {y})")
        cv2.circle(img, (x, y), 20, (0, 255, 0), -1)
    elif event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse move at ({x}, {y})")

# Load the image
img = cv2.imread(img_path)

# Resize the image to fit within the window
img = cv2.resize(img, (400, 400))

cv2.namedWindow('image')
cv2.setMouseCallback('image', onMouse)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):  # Exit on 'q' key
        break

cv2.destroyAllWindows()
