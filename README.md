# GOPH 547
*Semester:* W2026
*Instructor:* B. Karchewski
*Author(s):* <Matthew Davidson>
######################################################################
Lab 0A and 0B
Includes examples using Numpy arrays and Matplotlib for
visulization for part 0A.
For part 0B there is a driver script that shows NumPy array operations and image processing through using Matplotlib.
######################################################################
1.) Downloading the Repository
 Clone this to your local machine by using:
----------------------------------------------------------------------
git clone https://github.com/MudkipTheGr8/goph547-w2026-lab00-stMD
----------------------------------------------------------------------
cd goph547-w2026-lab00-stMD
----------------------------------------------------------------------
######################################################################
2.) Setting Up the Virtual Environment/ Installing the Package
A Virtual Environment in Windows:
----------------------------------------------------------------------
python -m venv venv
----------------------------------------------------------------------
venv\Scripts\activate
----------------------------------------------------------------------

Installing Packages (note: Pillow is needed for importing Image):
----------------------------------------------------------------------
pip install numpy matplotlib pillow
----------------------------------------------------------------------

Installing the goph547lab00 package: (From the repository root directory):
----------------------------------------------------------------------
pip install -e.
----------------------------------------------------------------------
######################################################################
3.) Description of driver.py

The script follows these tasks listed below:
- Creates arrays of ones and NaNs
- Generates a column vector of odd numbers and comuptes its sum
- Defines matricies and performs:
    - element-wise multiplication
    - matrix multiplication
    - cross products

- Loads an RGB image (rock_canyon.jpg)
- Converts the image to grayscale
- Crops a smaller grayscale part that only has a rock pillar
- Computes mean RGB values:
    - averaged over the y direction and plotted against the x
    - averaged over the x direction and plotted against the y
- Makes and saves a summary plot of mean RGB values
######################################################################
4.) Running the Code/ Expected Outcomes

There needs to be an image file (rock_canyon.jpg) for the code to function properly.

From the repository root put the following in the terminal to run the script:

python examples/driver.py

The expected outcomes are:
- Printed NumPy arrays and numerical results in the terminal
- Figures being displayed:
    - RGB image (canyon) (with shape of array)
    - grayscale image (with shape of array)
    - cropped grayscale image (with shape of array)
    - 2 panel plot with mean RGB values v.s. x and y coordinates.
######################################################################
