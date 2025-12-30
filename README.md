# Niko’s File Organizer — Emerald Edition 💚

A modern desktop **file organization tool** built with **Python** and **CustomTkinter**.  
This application scans a selected directory and automatically sorts files into clean, categorized folders based on file type — all through a sleek, emerald-themed GUI.

---

## ✨ Features

- 📁 **Automatic File Sorting**
- 🧠 **Smart File Type Detection**
- ⚡ **Multithreaded Processing** (UI never freezes)
- 📊 **Live Progress Bar**
- 📝 **Real-time Status Logs**
- 🟢 **Custom Emerald-Themed Interface**
- 🛡️ **Duplicate File Protection**
- ❌ Skips hidden/system files

---

## 🗂️ File Categories

Files are automatically sorted into the following folders:

| Category | File Types |
|--------|-----------|
| Images | `.jpg`, `.png`, `.gif`, `.svg`, `.webp`, etc. |
| Documents | `.pdf`, `.docx`, `.txt`, `.csv`, `.xlsx`, `.md` |
| Videos | `.mp4`, `.mov`, `.avi`, `.mkv` |
| Music | `.mp3`, `.wav`, `.flac`, `.m4a` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Code | `.py`, `.js`, `.html`, `.css`, `.cpp`, `.java`, `.json` |
| Executables | `.exe`, `.msi`, `.dmg`, `.sh` |
| Others | Files that don’t match any category |

---

## 🖥️ Interface Preview

- Emerald green accent colors  
- Fixedsys & Consolas fonts  
- Dark mode UI  
- Terminal-style logging panel  

---

## 🚀 How It Works

1. Launch the application
2. Click **“SELECT YOUR TARGETTED DIRECTORY”**
3. Choose a folder you want to organize
4. The app:
   - Scans all files
   - Creates folders automatically
   - Moves files based on extension
   - Renames duplicates safely
5. Done. Clean directory.

---

## 🔧 Installation

### Requirements
- Python **3.9+**
- Windows / macOS / Linux

### Install Dependencies
```bash
pip install customtkinter
