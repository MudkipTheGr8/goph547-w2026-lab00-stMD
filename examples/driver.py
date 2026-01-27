import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from goph547lab00.arrays import (
    square_ones,
    )
def main():

    # Part 0A
    # test creating square array of ones
    A_np = np.ones((3,3))
    A = square_ones(3)
    print(f'A_np:\n{A_np}')
    print(f'A:\n{A}')

    # Part 0B
    # Question 1: Array of ones (3x5)
    Array_Q1 = np.ones((3,5))
    print(f'Array_Q1:\n{Array_Q1}')

    # Question 2: Array of NaN (6x3)
    Array_Q2 = np.full((6,3), np.nan)
    print(f'Array_Q2:\n{Array_Q2}')

    # Question 3: Column vector of odd numbers between 44 and 75
    Array_Q3 = np.arange(45, 76, 2).reshape(-1,1)
    print(f'Array_Q3:\n{Array_Q3}')

    # Question 4: Sum of the vector produced in Question 3
    Sum_Q4 = np.sum(Array_Q3)
    print(f'Sum_Q4: {Sum_Q4}')

    # Question 5: Array A
    A = np.array([[5,7,2],[1,-2,3],[4,4,4]])
    print(f'Array A:\n{A}')

    # Question 6: Array B in a single command
    B = np.eye(3)
    print(f'Array B:\n{B}')

    # Question 7: Element-wise multiplication of A and B
    C = A * B
    print(f'Element-wise multiplication of A and B (C):\n{C}')

    # Question 8: Matrix multiplication of A and B
    D = A @ B
    print(f'Matrix multiplication of A and B (D):\n{D}')

    # Question 9: Cross product of arrays A and B
    cross_product = np.cross(A, B)
    print(f'Cross product of A and B:\n{cross_product}')

    # Question 10: Loading rock canyon image
    rock_canyon = np.asarray(Image.open("examples/rock_canyon.jpg"))

    # Question 11: Plotting Image + Shape of the array(s)
    plt.imshow(rock_canyon)
    plt.title('Rock Canyon Image')
    plt.axis('off')
    plt.show()
    print(f'Shape of rock_canyon array: {rock_canyon.shape}')

    # Question 12: Converting to Grayscale
    rock_canyon_gray = np.asarray(Image.open("examples/rock_canyon.jpg").convert('L'))
    plt.imshow(rock_canyon_gray, cmap='gray')
    plt.title('Rock Canyon Grayscale Image')
    plt.axis('off')
    plt.show()
    print(f'Shape of rock_canyon_gray array: {rock_canyon_gray.shape}')

    # Question 13: New smaller image array
    H, W = rock_canyon_gray.shape
    small_gray_image = rock_canyon_gray[int(0.45*H):int(0.90*H), int(0.20*W):int(0.35*W)]
    plt.imshow(small_gray_image, cmap='gray')
    plt.title('Smaller Grayscale Image')
    plt.axis('off')
    plt.show()
    print(f'Shape of small_gray_image array: {small_gray_image.shape}')

    # Question 14 to 16: Subplots, x-coordinate on the horizontal axis and colour values on the vertical axis, 
    # and y-coordinate on the vertical axis and colour values on the horizontal axis

    # Splitting image into color channels
    R = rock_canyon[:, :, 0].astype(float)
    G = rock_canyon[:, :, 1].astype(float)
    B = rock_canyon[:, :, 2].astype(float)
    RGB = (R + G + B) / 3.0

    # Prepare x and y coordinates
    x = np.arange(W)
    y = np.arange(H)

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Plot mean RGB values against x and y coordinates
    # For x-coordinate (horizontal axis)
    axs[0].plot(x, np.mean(R, axis=0), color='red', label='R', linewidth = 1.0)
    axs[0].plot(x, np.mean(G, axis=0), color='green', label='G', linewidth = 1.0)
    axs[0].plot(x, np.mean(B, axis=0), color='blue', label='B', linewidth = 1.0)
    axs[0].plot(x, np.mean(RGB, axis=0), color='k', label='RGB', linewidth = 2.5)
    axs[0].set_title('Mean along the y-direction plotted along the x-coordinate')
    axs[0].set_xlabel('x-coordinate (pixels)')
    axs[0].set_ylabel('Mean Pixel Value')
    axs[0].legend()

    # For y-coordinate (vertical axis)
    axs[1].plot(np.mean(R, axis=1), y, color='red', label='R', linewidth = 1.0)
    axs[1].plot(np.mean(G, axis=1), y, color='green', label='G', linewidth = 1.0)
    axs[1].plot(np.mean(B, axis=1), y, color='blue', label='B', linewidth = 1.0)
    axs[1].plot(np.mean(RGB, axis=1), y, color='k', label='RGB', linewidth = 2.5)
    axs[1].invert_yaxis()
    axs[1].set_title('Mean along the x-direction plotted against the y-coordinate')
    axs[1].set_xlabel('Mean Pixel Value')
    axs[1].set_ylabel('y-coordinate (pixels)')
    axs[1].legend()

    # Save and show the figure
    plt.savefig('examples/rock_canyon_RGB_summary.png', dpi=200)
    plt.show()

if __name__ == '__main__':
    main()