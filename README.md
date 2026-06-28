# BatchForge 🚀

**The Ultimate Windows Automation & Batch Script Manager**

![BatchForge Banner](https://raw.githubusercontent.com/annamalai2912/batchforge/main/landing_page/logo.png)

BatchForge is a powerful, lightweight Windows desktop application built with Python and PyQt6. It provides a centralized hub to write, organize, and safely execute your automation tasks. Whether you're a sysadmin, a developer, or just someone looking to automate daily PC tasks, BatchForge brings a modern UI/UX to classic Windows batch automation.

---

## 🌟 Key Features

- **Categorized Library:** Instantly organize your `.bat` and `.cmd` scripts into a beautiful, searchable tree structure.
- **Safe Execution Engine:** Run scripts asynchronously with real-time output. Includes robust process-tree termination to halt runaway scripts instantly.
- **Syntax Highlighting:** A custom built-in editor specifically tuned for Windows Batch commands.
- **Task Scheduling:** Seamlessly bridges into the Windows Task Scheduler to automate backups and cleanups with zero friction.
- **Built-In Script Collection:** Comes pre-loaded with over 30 incredibly useful, safe scripts ranging from system diagnostics to auto-extractors and focus modes.
- **First-Run Interactive Tour:** A welcome wizard guides you through the application's core features upon your first launch.
- **Learning Resources:** Built-in PDF guides and external links to help you master batch scripting.

---

## 📸 Screenshots

### The Script Library & Editor
![Script Library & Editor](https://raw.githubusercontent.com/annamalai2912/batchforge/main/screenshots/home.png)
*Browse your categorized scripts and edit them with syntax highlighting.*

### Collection Browser
![Collection Browser](https://raw.githubusercontent.com/annamalai2912/batchforge/main/screenshots/browser.png)
*Built-in script browser to access all the features of the application.*


---

## 📥 Installation

1. **Download the Installer:**
   Navigate to the [Releases](https://github.com/annamalai2912/BatchForge/releases/latest) page and download `BatchForge_Setup.exe`.
   
   > **Note on Windows SmartScreen:** Because this is a new open-source tool, Windows Defender might show a "Windows protected your PC" warning when running the installer. Simply click **"More info"** and then **"Run anyway"** to proceed safely.

2. **Run the Installer:**
   Follow the simple installation wizard to set up the application securely on your system.
3. **Launch:**
   Open BatchForge from your Start Menu or Desktop shortcut!

---

## 🛠️ Building from Source

If you want to contribute or build the application from source, follow these steps:

1. **Clone the Repository:**
   ```cmd
   git clone https://github.com/annamalai2912/BatchForge.git
   cd BatchForge
   ```

2. **Install Dependencies:**
   Make sure you have Python 3.10+ installed.
   ```cmd
   pip install -r requirements.txt
   pip install pyinstaller fpdf
   ```

3. **Build the Executable:**
   ```cmd
   pyinstaller batchforge.spec
   ```

4. **Build the Installer (Requires NSIS):**
   ```cmd
   python build_installer.py
   ```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
Feel free to check the [issues page](https://github.com/annamalai2912/BatchForge/issues) if you want to contribute.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

---

**Built with ❤️ by Annamalai K M**
