#Generate single samples from each font size 5-10
# Working example for generating and saving perfect z
#changed stroke to generate fat z shapes


import cv2


import numpy as np
import random
import os
import time
num = 0
# Create a blank white image of size 250x250
image = np.ones((250, 250, 3), dtype=np.uint8) * 255

# Set the font face to Times New Roman
font_face = cv2.FONT_HERSHEY_SIMPLEX
font_size = random.uniform(5, 10)
font_size = 5
while True:
    # Generate a random font size between 1 and 10 (inclusive)

    print(font_size)

    # Get the size of the letter 'Z' using the selected font and font size
    (z_width, z_height), _ = cv2.getTextSize('Z', font_face, font_size, 2)

    # Calculate the position to place the letter 'Z' at the center of the image
    x = int((image.shape[1] - z_width) / 2)
    y = int((image.shape[0] + z_height) / 2)

    # Draw the letter 'Z' on the image with the chosen font, font size, and position
    cv2.putText(image, 'Z', (x, y), font_face, font_size, (0, 0, 0), 2)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Count the number of black pixels (pixels with value 0)
    num_black_pixels = np.count_nonzero(gray_image == 0)

    # Display the generated image
    cv2.imshow("Generated Image", image)
    cv2.waitKey(100)  # Display for 1 second

    output_folder = 'generated_Z'

    # Create the folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Save the modified image in the specified folder
    output_path = os.path.join(output_folder, f'output_image{num}.jpg')
    cv2.imwrite(output_path, image)
    num +=1

    # Clear the image for the next iteration
    image.fill(255)

    # Print the number of black pixels in the image
    print("Number of black pixels:", num_black_pixels)
    font_size += 1
    if font_size == 11:
        break


