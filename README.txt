📌 NT Zero Application – Python Tkinter + Matplotlib

This project was created as part of a university assignment.
The task was to build a simple Python GUI application that:

accepts two numerical inputs (N and T),

generates N random numbers in the range 1–200,

replaces every T-th number with 0,

displays the modified sequence,

draws a bar graph of the resulting values,

uses a graphical user interface (GUI) with Tkinter,

can be converted into an .exe application.

🚀 How the program works
1️⃣ Input

The user enters:

N – how many numbers to generate,

T – interval for replacing numbers with zero (every T-th element becomes 0).

2️⃣ Processing

The program generates a list of N random integers in the range 1–200.

Every T-th element (T, 2T, 3T, …) is replaced with 0.

3️⃣ Output

The resulting sequence is displayed in a text window.

A bar chart is generated using Matplotlib and embedded into the Tkinter window.

📁 Project structure
project-folder/
├── main.py      # main application script (Python source)
├── main.exe     # built executable (PyInstaller)
├── README.txt   # documentation
└── .gitignore   # Git ignore rules

🛠 Technologies used

Python 3.x

Tkinter – GUI framework

Matplotlib – graph rendering library

random – number generation

PyInstaller – building the .exe file

▶️ How to run
Run from Python (source code)
python main.py

Run compiled executable

Double-click main.exe in the project folder
(no Python installation required on the target machine).

Build .exe from source (optional)

If you want to rebuild the executable:

pyinstaller --onefile --noconsole main.py


The new executable will appear in the dist/ folder.

📌 Author

Illia Zueiv
TUKE – Faculty of Manufacturing Technologies
Study program: Smart Technologies in Industry