import cv2
import numpy as np

def apply_filter(image, filter_type):
    """Apply the selected color filter or edge detection."""
    
    # Create a copy to avoid changing the original image
    filtered_image = image.copy()

    # ------------------------ COLOR FILTERS ------------------------
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Green channel
        filtered_image[:, :, 2] = 0  # Blue channel

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Blue channel
        filtered_image[:, :, 2] = 0  # Red channel

    elif filter_type == "blue_tint":
        filtered_image[:, :, 0] = 0  # Green channel
        filtered_image[:, :, 1] = 0  # Red channel

    # ------------------------ SOBEL EDGE DETECTION ------------------------
    elif filter_type == "sobel":
        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Calculate Sobel gradients in X and Y directions
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

        # Convert gradients to absolute scale (uint8)
        abs_sobelx = cv2.convertScaleAbs(sobelx)
        abs_sobely = cv2.convertScaleAbs(sobely)

        # Combine both directions using bitwise OR
        combined_sobel = cv2.bitwise_or(abs_sobelx, abs_sobely)

        # Convert single-channel back to BGR for display
        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)

    # ------------------------ CANNY EDGE DETECTION ------------------------
    elif filter_type == "canny":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filtered_image


# ------------------------ MAIN PROGRAM ------------------------

# Load the image
image_path = 'restart.png'  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    filter_type = "original"  # Start with original image (no filter)

    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("g - Green Tint")
    print("b - Blue Tint")
    print("s - Sobel Edge Detection")
    print("c - Canny Edge Detection")
    print("q - Quit")

    while True:
        # Apply the selected filter
        filtered_image = apply_filter(image, filter_type)

        # Display the filtered image
        cv2.imshow("Filtered Image", filtered_image)

        # Wait for key press
        key = cv2.waitKey(0) & 0xFF

        # Change filters based on key press
        if key == ord('b'):
            filter_type = 'red_tint'
        elif key == ord('g'):
            filter_type = 'green_tint'
        elif key == ord('r'):
            filter_type = 'blue_tint'
        elif key == ord('s'):
            filter_type = 'sobel'
        elif key == ord('c'):
            filter_type = 'canny'
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! Use 'r', 'g', 'b', 's', 'c', or 'q'.")

    # Close all OpenCV windows
    cv2.destroyAllWindows()
