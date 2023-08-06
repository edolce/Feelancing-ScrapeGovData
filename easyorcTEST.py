import easyocr
import cv2

def perform_ocr(image_path):
    # Initialize the OCR reader with the desired language(s)
    reader = easyocr.Reader(['en'])

    # Read the image using OpenCV
    img_cv2 = cv2.imread(image_path)

    # Perform OCR on the image
    result = reader.readtext(img_cv2)


    # Process the OCR result
    for detection in result:
        text = detection[1]  # Extract the detected text
        confidence = detection[2]  # Extract the confidence score of the detection
        print(f"Detected Text: {text}, Confidence: {confidence:.2f}")

if __name__ == '__main__':
    image_path = 'image.jpeg'  # Replace with the path to your image file
    perform_ocr(image_path)