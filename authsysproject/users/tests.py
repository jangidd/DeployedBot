# from django.test import TestCase
# Interview Question .......................

# # Create your tests here.

def rotate_image(size, img):
    # Create a new matrix to store the rotated version
    rotated_img = [[0] * size for _ in range(size)]
    
    # Rotate columns to rows
    for col in range(size):
        for row in range(size):
            # Take the (size - 1 - col)th column and turn it into the row
            rotated_img[col][row] = img[row][size - 1 - col]
    
    # Update the original matrix with the rotated values
    for i in range(size):
        for j in range(size):
            img[i][j] = rotated_img[i][j]

# Input handling for testing the function
size = int(input().strip())
img = []
for _ in range(size):
    row = list(map(int, input().strip().split()))
    img.append(row)

# Call rotate_image and display the result
rotate_image(size, img)
for row in img:
    print(" ".join(map(str, row)))
