# Electronic Resistor Calculator

This is a Python-based graphical calculator that calculates the resistance of an electronic resistor using the color code method. The calculator supports resistors from 3 bands to 6 bands, and it is built using the `Tkinter` module for the graphical user interface (GUI).

## Features
- Supports resistor calculation for 3, 4, 5, and 6 band resistors.
- GUI interface for easy input of resistor bands using Tkinter.
- Shows the exact resistance value along with the tolerance and temperature coefficient (for 6-band resistors).
  
## Technologies Used
- **Python**: The core language for the project.
- **Tkinter**: For creating the graphical user interface.

## Prerequisites
Make sure you have Python 3.x installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/resistor-calculator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd resistor-calculator
    ```

3. Install the necessary dependencies (if any):
    Tkinter comes pre-installed with most Python distributions. However, if needed:
    ```bash
    pip install tk
    ```

4. Run the program:
    ```bash
    python resistor_calculator.py
    ```

## Usage

1. After running the script, a GUI will open where you can select the color bands of the resistor using drop-down menus.
2. The program will calculate and display the resistor's value, tolerance, and temperature coefficient (for 6-band resistors).

### Example:

- A 4-band resistor with the color bands **Red**, **Violet**, **Yellow**, and **Gold** will have the following value:
    - Resistance: `27 kΩ`
    - Tolerance: `±5%`

## Project Structure

```bash
resistor-calculator/
│
├── resistor_calculator.py  # Main Python script with the GUI and logic
├── README.md               # This README file
└── LICENSE                 # License information
