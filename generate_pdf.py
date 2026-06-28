from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Batch Scripting Beginner's Guide", ln=1, align='C')
pdf.ln(10)

pdf.set_font("Arial", size=12)

content = """
Welcome to the Batch Scripting Beginner's Guide!

1. What is a Batch Script?
A batch file is a script file in DOS, OS/2 and Microsoft Windows. It consists of a series of commands to be executed by the command-line interpreter, stored in a plain text file.

2. Basic Commands
- echo: Prints out text. (e.g. echo Hello World)
- @echo off: Hides the command from printing before execution.
- pause: Halts execution and waits for the user to press a key.
- rem or :: : Used for adding comments to your script.

3. Variables
To set a variable, use:
set myVar=Hello

To use a variable, wrap it in percent signs:
echo %myVar%

4. Conditionals (IF statements)
if "%myVar%"=="Hello" (
    echo The variable is Hello!
) else (
    echo The variable is something else!
)

5. Loops (FOR loop)
for %%a in (1 2 3 4 5) do (
    echo %%a
)

6. Resources to Learn More
- SS64 (ss64.com/nt/)
- Microsoft Docs (learn.microsoft.com/en-us/windows-server/administration/windows-commands/)
- Tutorialspoint Batch Script Tutorial

BatchForge allows you to test these scripts safely using its built-in Execution Engine.
"""

# write multi-line text
pdf.multi_cell(0, 8, content)
pdf.output("Batch_Scripting_Guide.pdf")
print("PDF generated successfully.")
