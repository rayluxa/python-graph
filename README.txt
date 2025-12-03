📌 NT Zero Application – Python Tkinter + Matplotlib

This project was created as part of a university assignment.
The task was to build a simple Python GUI application that:

accepts two numerical inputs (N and T)

generates N random numbers in the range 1–200

replaces every T-th number with 0

displays the modified output

draws a bar graph of the resulting values

includes a graphical user interface (GUI) using Tkinter

can be converted into an .exe application

🚀 How the program works
1️⃣ Input

The user enters:

N — amount of numbers to generate

T — interval for replacing numbers with zero

2️⃣ Processing

The program generates a list of N random integers (1–200).

Every T-th element is replaced with 0.

3️⃣ Output

The resulting sequence is shown in a text window.

A bar chart is generated using Matplotlib and embedded into Tkinter.

📁 Project Structure
project-folder/
├── main.py           # main application script
├── README.txt        # documentation
└── .gitignore        # ignored files for Git

🛠 Technologies Used

Python 3.x

Tkinter — GUI framework

Matplotlib — graph rendering library

Random — number generation

PyInstaller — for building the .exe file

▶️ How to run
Run from Python:
python main.py

Build .exe (optional):
pyinstaller --onefile --noconsole main.py


The executable will appear in the dist/ folder.

📌 Author

Illia Zueiv
TUKE – Faculty of Manufacturing Technologies
Study program: Smart Technologies in Industry