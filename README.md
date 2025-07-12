🏆 Automatic Certificate Name Generator

This Python program automates the process of generating personalized certificates using data from an Excel file. It reads names from the names column and overlays them onto a given certificate image.
📌 Features

Read names from an Excel sheet (.xlsx) using pandas
Automatically overlay each name on a certificate image
Customize font, size, position (x, y), and image
Folder Structure

certificate_generator/
├── input.xlsx           # Excel file with a column named 'names'
├── ss.png               # Template certificate image (replace as needed)
├── YourFont.ttf         # Font file used for printing names (optional)
├── output/              # Auto-created folder to store generated certificates
└── certificator_automator.py              # Main script to run the program

📦 Requirements

  Python 3.x
  pandas
  PIL (Pillow)

Install dependencies using:

    pip install pandas pillow

 How to Use:
Edit the Excel Sheet:
    Add all recipient names under the column named names in input.xlsx.
Replace Certificate Template:
    Rename your certificate image to ss.png or update the filename in the script.
Set Coordinates and Font:
    In certificate_automator.py, adjust:

x, y = 100, 200   # Position to print the name
font_path = "YourFont.ttf"
font_size = 60

Run the Script:

    python certificate_automator.py

🖼️ Example Output

Each name from the Excel sheet will be printed onto the certificate template like this:

(Replace with actual preview if available)
🔧 Troubleshooting
Font Not Found:
    Download your preferred .ttf font, place it in the project folder, and update the font_path.
Text Misaligned:
    Adjust x and y coordinates to properly position the text on your certificate.

📃 License

This project is open-source and free to use for educational and personal purposes.
