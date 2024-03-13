import cv2


def resize_image(input_image_path, output_image_path, width=None, height=None):
    # Read the image
    image = cv2.imread(input_image_path)

    # Determine the new dimensions
    if width is None and height is None:
        raise ValueError("Both width and height cannot be None.")
    elif width is None:
        aspect_ratio = height / float(image.shape[0])
        new_width = int(image.shape[1] * aspect_ratio)
        new_height = height
    elif height is None:
        aspect_ratio = width / float(image.shape[1])
        new_width = width
        new_height = int(image.shape[0] * aspect_ratio)
    else:
        new_width = width
        new_height = height

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Write the resized image to disk
    cv2.imwrite(output_image_path, resized_image)
    print("Image resized successfully.")


# Example usage:
input_image_path = "Yash_Photo.jpg"
output_image_path = "Yash_Photo2.jpg"
new_width = 400
new_height = 300
resize_image(input_image_path, output_image_path, new_width, new_height)
