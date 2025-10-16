#!/usr/bin/env python3
"""
Font Installer Helper for Musical Symbols
This script helps you download and install fonts with better musical symbol support
"""

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import os


def open_font_download_links():
    """Open browser tabs with musical font download links"""
    fonts_info = [
        ("Noto Music", "Google's dedicated musical notation font (RECOMMENDED)", "https://fonts.google.com/noto/specimen/Noto+Music"),
        ("Bravura", "Professional music engraving font by Steinberg", "https://www.smufl.org/fonts/"),
        ("MuseScore Fonts", "High-quality music notation fonts", "https://github.com/musescore/MuseScore/tree/master/fonts"),
        ("Segoe UI Symbol", "Already installed on Windows 10/11 (basic support)", None),
        ("Symbola Font", "Comprehensive Unicode font", "https://fontlibrary.org/en/font/symbola"),
        ("DejaVu Sans", "Cross-platform Unicode font", "https://dejavu-fonts.github.io/"),
    ]
    
    message = "Recommended Musical Font Downloads:\n\n"
    message += "⭐ BEST OPTIONS for proper musical notation:\n\n"
    for name, description, url in fonts_info[:3]:
        message += f"• {name}: {description}\n"
        if url:
            message += f"  Download: {url}\n"
        message += "\n"
    
    message += "📋 Other Options:\n\n"
    for name, description, url in fonts_info[3:]:
        message += f"• {name}: {description}\n"
        if url:
            message += f"  Download: {url}\n"
        message += "\n"
    
    # Show info dialog
    messagebox.showinfo("Musical Fonts - Recommendations", message)
    
    # Open download pages for recommended fonts
    recommended_urls = [
        "https://fonts.google.com/noto/specimen/Noto+Music",
        "https://www.smufl.org/fonts/",
        "https://github.com/musescore/MuseScore/tree/master/fonts"
    ]
    
    for url in recommended_urls:
        webbrowser.open(url)


def check_current_fonts():
    """Check what fonts are currently available"""
    import tkinter.font as font
    available_fonts = list(font.families())
    
    musical_fonts = [
        "Noto Music",
        "Bravura", 
        "Petaluma",
        "MuseJazz",
        "Leland",
        "Sebastian",
        "Opus",
        "Maestro",
        "Musical Symbols",
        "Symbola",
        "DejaVu Sans",
        "Apple Symbols",
        "Arial Unicode MS",
        "Segoe UI Symbol"
    ]
    
    found_fonts = []
    missing_fonts = []
    
    for music_font in musical_fonts:
        if music_font in available_fonts:
            found_fonts.append(music_font)
        else:
            missing_fonts.append(music_font)
    
    message = "INSTALLED MUSICAL FONTS:\n"
    for font_name in found_fonts:
        message += f"✓ {font_name}\n"
    
    message += "\nMISSING FONTS:\n"
    for font_name in missing_fonts:
        message += f"✗ {font_name}\n"
    
    messagebox.showinfo("Font Check Results", message)


def main():
    """Main function for the font helper"""
    root = tk.Tk()
    root.title("Musical Font Helper")
    root.geometry("300x200")
    
    frame = ttk.Frame(root, padding="20")
    frame.pack(fill=tk.BOTH, expand=True)
    
    ttk.Label(frame, text="Musical Font Helper", font=("Arial", 14, "bold")).pack(pady=10)
    
    ttk.Button(frame, text="Check Current Fonts", 
               command=check_current_fonts).pack(pady=5, fill=tk.X)
    
    ttk.Button(frame, text="Get Font Download Links", 
               command=open_font_download_links).pack(pady=5, fill=tk.X)
    
    ttk.Label(frame, text="\nNote: After installing new fonts,\nrestart the BPM calculator.", 
              font=("Arial", 9), foreground="gray").pack(pady=10)
    
    root.mainloop()


if __name__ == "__main__":
    main()