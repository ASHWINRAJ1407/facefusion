# analysis.py
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model # type: ignore

# Path to the "captured images" folder
captured_images_folder = './captured_images/'  # Update as needed

# Load the trained CNN model
cnn_model = load_model('facefusion_cnn_model.h5')

def load_images_from_folder(folder_path):
    images = []
    image_files = os.listdir(folder_path)
    
    for img_file in image_files:
        img_path = os.path.join(folder_path, img_file)
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            # Resize the image to 48x48 pixels
            image = cv2.resize(image, (48, 48))
            # Normalize pixel values (0-255 to 0-1)
            image = image / 255.0
            images.append(image)
    
    # Convert to NumPy array and reshape for CNN input
    images = np.array(images).reshape(len(images), 48, 48, 1)
    return images

def classify_images(cnn_model, images):
    # Predict the class (engaged/not engaged)
    predictions = cnn_model.predict(images)
    # Convert probabilities to class labels (0 or 1)
    predicted_labels = np.argmax(predictions, axis=1)  # 1 = engaged, 0 = not engaged
    return predicted_labels

def calculate_engagement_percentage(predicted_labels):
    engaged_count = np.sum(predicted_labels == 1)
    total_count = len(predicted_labels)
    engagement_percentage = (engaged_count / total_count) * 100
    return engagement_percentage

def get_engagement_result():
    # Load images from the "captured images" folder
    new_images = load_images_from_folder(captured_images_folder)
    
    if len(new_images) > 0:
        # Classify the images
        predicted_labels = classify_images(cnn_model, new_images)
        # Calculate the engagement percentage
        engagement_percentage = calculate_engagement_percentage(predicted_labels)
        return engagement_percentage
    else:
        return 0  # Return 0 if no images found
engagement_percentage = get_engagement_result()
print(f"Percentage of students classified as engaged: {engagement_percentage:.2f}%")