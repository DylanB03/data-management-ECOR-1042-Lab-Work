ECOR 1042 - Lab 6: Student Data Analysis
Date: April 2025
Software Name/Version: Student Data Analysis v1.0
Contact Information: Team Leader: Cameron MacGillivray, Email: cameronmacgillivray@cmail.carleton.ca

DESCRIPTION
    This software, fully made with Python, allows the user to load, filter, sort and analyse
student data. There are two ways to interface with the software, using either a batch form
of user interface (UI) or a more intuitive text UI. This way, a user can load their choice
of student data from a CSV file, then processes with the outlined capabilities, including
creation of histograms and graphical curve fit.

DEPENDENCIES
    - Python 3.13
    - NumPy (used for polynomial fitting)
    - Matplotlib (for plotting histograms)

    Note: these libraries must be installed before running the project files, at least for the curve fit,
    histograms and either of the UIs.

INSTALLATION

    1. Download all the files in the project, including load_data.py, sort.py, curve_fit.py, histogram.py,
     text_UI.py and batch_UI.py, and well as this README, from the gradescope or place this project is obtained.
    2. All files must be in the same directory so that UI files can call the needed modules.
    3. Ensure the most recent version of Python is installed, as well as the two required libraries.

USAGE
    Video Instructions: For simplest instructions, please following included video instructions for use of Text UI
    as well as Batch UI. For a brief text summary, see the instructions below.

    1. Text UI:
        Run text_UI.py in the terminal or in your IDE of choice. There will be a presented menu with options to
        perform any one of the capabilities of the software. The only initial choice possible at first will be to
        load the data of choice, likely something comparable to the student-test.csv file provided by this project's
        requirements. The instructions are clear within the running UI software. When prompted to choose a file,
        enter just the file's name and extension, then press enter to confirm the entry. Once data is successfully loaded,
        a success message will indicate "Data Loaded Successfully" or similar. Once data is loaded, additional
        capabilities become possible. Following this, all commands can be used to sort by data category of choice
        create a histogram, curve fit graph or exit the program. Again, certain parameters of choice will be required,
        which the user can enter typed, then simply press "ENTER".

    2. Batch UI:
        Run the batch_UI.py in the terminal or IDE of choice. There will be a prompt to enter the name of a batch file
        that should contain the batch commands. As opposed to the Text UI process, all loading, data processing, sorting
        and other capabilities must all be contained within the batch file containing commands and parameters when
        needed for some commands.

CREDITS
    Team T-051
    - Chloe Ouellette: histogram functions
    - Dylan Butz: curve fit functions,
    - Arman Rahmani: batch UI,
    - Cameron MacGillivray - text UI,
    - All contributors: loading various data in load_data.py and various sorting functions in sort.py

LICENSE
    MIT License

    Copyright (c) [2025] [Cameron MacGillivray, Arman Rahmani, Dylan Butz, Chloe Ouellette]

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

