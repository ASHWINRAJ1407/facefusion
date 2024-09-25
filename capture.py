import cv2
import os
import time

# Create a folder to save the captured images
output_dir = 'captured_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Function to capture 5 images
def capture_images():
    count = 0
    while count < 5:
        # Read a frame from the webcam
        ret, frame = cap.read()

        if ret:
            # Save the image with a unique name
            image_path = os.path.join(output_dir, f"student_image_{int(time.time())}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Captured: {image_path}")
            count += 1
            
            # Show the frame (optional)
            cv2.imshow('Webcam', frame)
            
            # Wait for 1 second before capturing the next image
            time.sleep(1)
        else:
            print("Error: Failed to capture image.")
            break

# Capture images every 10 seconds, periodically
try:
    while True:
        print("Capturing 5 images...")
        capture_images()
        print("Waiting for 10 seconds...")
        time.sleep(10)  # Wait for 10 seconds before capturing again

        # If you want to break the loop with a key press, uncomment the following:
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

except KeyboardInterrupt:
    print("Program terminated by user.")

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
