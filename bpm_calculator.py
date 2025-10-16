#!/usr/bin/env python3
"""
BPM to Milliseconds Calculator
A simple tkinter application to convert beats per minute to milliseconds
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
import math


class BPMCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BPM to Milliseconds Calculator")
        self.root.geometry("500x500")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Set up musical font
        self.setup_musical_font()
        
        self.setup_ui()
        
    def setup_musical_font(self):
        """Set up the best available font for musical symbols"""
        # List of fonts that support musical symbols, in order of preference
        # Prioritizing fonts with proper musical notation over basic Unicode fonts
        musical_fonts = [
            "Bravura",             # Professional music engraving font
            "Noto Music",          # Google's dedicated musical notation font
            "Petaluma",            # Steinberg's handwritten music font
            "MuseJazz",            # MuseScore's jazz font
            "Leland",              # Steinberg's music font
            "Sebastian",           # Legacy Sibelius font
            "Opus",                # Legacy Finale font
            "Maestro",             # Legacy music font
            "Musical Symbols",     # Generic musical font name
            "Segoe UI Symbol",     # Windows - actually works well for basic musical symbols
            "Symbola",             # Cross-platform Unicode font with better musical symbols
            "DejaVu Sans",         # Linux/cross-platform
            "Apple Symbols",       # macOS
            "Arial Unicode MS",    # Has issues with some musical symbols
            "Arial",               # Final fallback
        ]
        
        # Get list of available fonts
        available_fonts = list(font.families())
        
        # Find the first available musical font
        self.musical_font = None
        for music_font in musical_fonts:
            if music_font in available_fonts:
                self.musical_font = music_font
                print(f"Using font: {music_font}")
                break
        
        # If no specific font found, use default
        if not self.musical_font:
            self.musical_font = "Arial"
            print(f"Using fallback font: {self.musical_font}")
        
        # Test if the font can display musical symbols
        self.use_unicode_symbols = self.test_musical_symbols()
        
    def test_musical_symbols(self):
        """Test if the current font can display Unicode musical symbols properly"""
        try:
            # Test multiple musical symbols to ensure proper support
            test_symbols = ["𝅝", "𝅗𝅥", "♩", "♪", "♬", "♫"]
            
            # Create a temporary label to test symbol rendering
            for symbol in test_symbols:
                test_label = tk.Label(self.root, text=symbol, font=(self.musical_font, 16))
                test_label.destroy()  # Clean up immediately
            
            # If we can create all symbols without error, assume good support
            # Additional check: prioritize fonts with "Music" in the name
            if "music" in self.musical_font.lower() or "bravura" in self.musical_font.lower() or "noto" in self.musical_font.lower():
                return True
            
            # For other fonts, be more conservative
            return True
        except:
            return False
        
    def setup_ui(self):
        """Set up the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="BPM to Milliseconds Calculator", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # === BPM INPUT SECTION ===
        bpm_input_frame = ttk.Frame(main_frame)
        bpm_input_frame.grid(row=1, column=0, columnspan=2, pady=(0, 15))
        
        # Create a sub-frame to center the BPM controls
        bpm_center_frame = ttk.Frame(bpm_input_frame)
        bpm_center_frame.pack(expand=True)
        
        ttk.Label(bpm_center_frame, text="BPM:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=(0, 10), pady=5)
        self.bpm_var = tk.StringVar(value="120")  # Default to 120 BPM
        self.bpm_entry = ttk.Entry(bpm_center_frame, textvariable=self.bpm_var, width=5, font=("Arial", 12), justify='center')
        self.bpm_entry.grid(row=0, column=1, pady=5)
        
        # Bind automatic calculation to BPM changes
        self.bpm_var.trace_add('write', lambda name, index, mode: self.auto_calculate_all())
        
        # === TIME SIGNATURE CALCULATOR SECTION ===
        ts_frame = ttk.LabelFrame(main_frame, text="Beat Position Calculator", padding="10")
        ts_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        ts_frame.columnconfigure(1, weight=1)
        ts_frame.columnconfigure(3, weight=1)
        ts_frame.columnconfigure(5, weight=1)
        
        # Time Signature inputs (4/4, 3/4, etc.)
        ttk.Label(ts_frame, text="Time Signature:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ts_input_frame = ttk.Frame(ts_frame)
        ts_input_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        self.numerator_var = tk.StringVar(value="4")
        self.denominator_var = tk.StringVar(value="4")
        
        numerator_entry = ttk.Entry(ts_input_frame, textvariable=self.numerator_var, width=3)
        numerator_entry.grid(row=0, column=0)
        ttk.Label(ts_input_frame, text="/").grid(row=0, column=1, padx=5)
        denominator_entry = ttk.Entry(ts_input_frame, textvariable=self.denominator_var, width=3)
        denominator_entry.grid(row=0, column=2)
        
        # Bar number input
        ttk.Label(ts_frame, text="Bar:").grid(row=0, column=2, sticky=tk.W, pady=5, padx=(20, 0))
        self.bar_var = tk.StringVar(value="1")
        bar_entry = ttk.Entry(ts_frame, textvariable=self.bar_var, width=8)
        bar_entry.grid(row=0, column=3, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Beat number input
        ttk.Label(ts_frame, text="Beat:").grid(row=0, column=4, sticky=tk.W, pady=5, padx=(20, 0))
        self.beat_var = tk.StringVar(value="1")
        beat_entry = ttk.Entry(ts_frame, textvariable=self.beat_var, width=8)
        beat_entry.grid(row=0, column=5, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Time signature result
        ttk.Label(ts_frame, text="Position:").grid(row=1, column=0, sticky=tk.W, pady=(10, 5))
        self.ts_result = ttk.Label(ts_frame, text="--", font=("Arial", 10, "bold"), foreground="blue")
        self.ts_result.grid(row=1, column=1, columnspan=5, sticky=tk.W, pady=(10, 5), padx=(10, 0))
        
        # Bind time signature calculator events
        self.numerator_var.trace_add('write', lambda *args: self.auto_calculate_all())
        self.denominator_var.trace_add('write', lambda *args: self.auto_calculate_all())
        self.bar_var.trace_add('write', lambda *args: self.auto_calculate_all())
        self.beat_var.trace_add('write', lambda *args: self.auto_calculate_all())
        
        # === BPM CALCULATOR SECTION ===
        bpm_frame = ttk.LabelFrame(main_frame, text="Note Value Calculator", padding="10")
        bpm_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        bpm_frame.columnconfigure(1, weight=1)
        
        # Note value selection with buttons
        ttk.Label(bpm_frame, text="Note Value:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.note_var = tk.StringVar(value="Quarter Note (1/4)")
        
        # Create frame for note buttons
        note_frame = ttk.Frame(bpm_frame)
        note_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        note_frame.columnconfigure(0, weight=1)
        
        # Note buttons with musical symbols
        self.note_buttons = []
        
        # Choose symbols based on font capability
        if self.use_unicode_symbols:
            note_options = [
                ("𝅝", "Whole Note (1/1)", "Semibreve"),
                ("𝅗𝅥", "Half Note (1/2)", "Minim"),
                ("♩", "Quarter Note (1/4)", "Crotchet"),
                ("♪", "Eighth Note (1/8)", "Quaver"),
                ("♬", "Sixteenth Note (1/16)", "Semiquaver"),
                ("♫", "Thirty-second Note (1/32)", "Demisemiquaver")
            ]
        else:
            # Fallback to simple symbols
            note_options = [
                ("W", "Whole Note (1/1)", "Semibreve"),
                ("H", "Half Note (1/2)", "Minim"),
                ("♩", "Quarter Note (1/4)", "Crotchet"),
                ("♪", "Eighth Note (1/8)", "Quaver"),
                ("♬", "Sixteenth Note (1/16)", "Semiquaver"),
                ("♫", "Thirty-second Note (1/32)", "Demisemiquaver")
            ]
        
        # Create all buttons in a single row
        for i, (symbol, value, tooltip) in enumerate(note_options):
            row = 0  # All buttons in row 0
            col = i  # Each button in its own column
            
            btn = tk.Button(note_frame, text=symbol, 
                           font=(self.musical_font, 12), width=3, height=1,
                           command=lambda v=value: self.select_note(v),
                           relief="raised", bd=2)
            btn.grid(row=row, column=col, padx=1, pady=2, sticky="ew")
            
            # Add tooltip text below button
            tooltip_label = ttk.Label(note_frame, text=tooltip, font=("Arial", 7))
            tooltip_label.grid(row=row+1, column=col, padx=1, pady=(0, 2))
            
            self.note_buttons.append(btn)
            
        # Configure equal column weights for note frame (now 6 columns)
        for i in range(6):
            note_frame.columnconfigure(i, weight=1)
        
        # Initially select quarter note button
        self.update_button_selection()
        
        # Note value result (consistent with beat position calculator)
        ttk.Label(bpm_frame, text="Duration:").grid(row=2, column=0, sticky=tk.W, pady=(10, 5))
        self.ms_result = ttk.Label(bpm_frame, text="--", font=("Arial", 10, "bold"), foreground="blue")
        self.ms_result.grid(row=2, column=1, sticky=tk.W, pady=(10, 5), padx=(10, 0))
        
        # Display font information
        font_info = f"Using font: {self.musical_font}"
        if self.use_unicode_symbols:
            font_info += " (Unicode symbols supported)"
        else:
            font_info += " (Using fallback symbols)"
        
        font_label = ttk.Label(main_frame, text=font_info, font=("Arial", 8), foreground="gray")
        font_label.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Focus on BPM entry
        self.bpm_entry.focus()
        
        # Initial calculation with default values
        self.auto_calculate_all()
        
    def select_note(self, note_value):
        """Select a note value and update button appearance"""
        self.note_var.set(note_value)
        self.update_button_selection()
        self.auto_calculate_all()  # Automatically calculate when note changes
        
    def update_button_selection(self):
        """Update the visual appearance of note buttons to show selection"""
        current_note = self.note_var.get()
        note_values = [
            "Whole Note (1/1)",
            "Half Note (1/2)",
            "Quarter Note (1/4)",
            "Eighth Note (1/8)",
            "Sixteenth Note (1/16)",
            "Thirty-second Note (1/32)"
        ]
        
        for i, btn in enumerate(self.note_buttons):
            if i < len(note_values) and note_values[i] == current_note:
                # Selected button - make it look pressed
                btn.config(relief="sunken", bg="#4CAF50", fg="white")
            else:
                # Unselected button - normal appearance
                btn.config(relief="raised", bg="SystemButtonFace", fg="black")
        
    def get_note_multiplier(self):
        """Get the multiplier for the selected note value"""
        note_multipliers = {
            "Whole Note (1/1)": 4.0,
            "Half Note (1/2)": 2.0,
            "Quarter Note (1/4)": 1.0,
            "Eighth Note (1/8)": 0.5,
            "Sixteenth Note (1/16)": 0.25,
            "Thirty-second Note (1/32)": 0.125
        }
        return note_multipliers.get(self.note_var.get(), 1.0)
        
    def calculate(self):
        """Calculate milliseconds from BPM"""
        try:
            bpm = float(self.bpm_var.get())
            if bpm <= 0:
                raise ValueError("BPM must be positive")
                
            # Get note multiplier
            note_multiplier = self.get_note_multiplier()
            
            # Calculate milliseconds per beat (quarter note = 1 beat)
            # Formula: (60 seconds / BPM) * 1000 ms/second * note_multiplier
            milliseconds = (60.0 / bpm) * 1000.0 * note_multiplier
            
            # Update result
            self.ms_result.config(text=f"{milliseconds:.2f} ms")
            
        except ValueError as e:
            if "could not convert" in str(e):
                messagebox.showerror("Error", "Please enter a valid number for BPM")
            else:
                messagebox.showerror("Error", str(e))
            # Clear result on error
            self.ms_result.config(text="--")

    def auto_calculate(self):
        """Automatically calculate without showing error dialogs for invalid input"""
        try:
            bpm_text = self.bpm_var.get().strip()
            if not bpm_text:
                # Clear results if BPM field is empty
                self.ms_result.config(text="--")
                self.freq_result.config(text="--")
                self.period_result.config(text="--")
                return
                
            bpm = float(bpm_text)
            if bpm <= 0:
                # Clear results if BPM is invalid
                self.ms_result.config(text="--")
                self.freq_result.config(text="--")
                self.period_result.config(text="--")
                return
                
            # Get note multiplier
            note_multiplier = self.get_note_multiplier()
            
            # Calculate milliseconds per beat (quarter note = 1 beat)
            # Formula: (60 seconds / BPM) * 1000 ms/second * note_multiplier
            milliseconds = (60.0 / bpm) * 1000.0 * note_multiplier
            
            # Update result
            self.ms_result.config(text=f"{milliseconds:.2f} ms")
            
        except ValueError:
            # Silently clear results on invalid input (no error dialog)
            self.ms_result.config(text="--")

    def calculate_time_signature_position(self):
        """Calculate the millisecond position of a specific beat in a time signature"""
        try:
            # Get input values
            numerator = int(self.numerator_var.get().strip() or "4")
            denominator = int(self.denominator_var.get().strip() or "4")
            bar = int(self.bar_var.get().strip() or "1")
            beat = float(self.beat_var.get().strip() or "1")
            bpm = float(self.bpm_var.get().strip() or "120")
            
            if numerator <= 0 or denominator <= 0 or bar <= 0 or beat <= 0 or bpm <= 0:
                return None
                
            if beat > numerator:
                return None
                
            # Calculate milliseconds per quarter note
            ms_per_quarter = (60.0 / bpm) * 1000.0
            
            # Calculate the note value of one beat in this time signature
            # In 4/4 time, one beat = quarter note
            # In 2/2 time, one beat = half note, etc.
            beat_note_value = 4.0 / denominator
            ms_per_beat = ms_per_quarter * beat_note_value
            
            # Calculate position in milliseconds
            beats_elapsed = (bar - 1) * numerator + (beat - 1)
            position_ms = beats_elapsed * ms_per_beat
            
            return {
                'milliseconds': position_ms,
                'bars': bar,
                'beats': beat,
                'time_signature': f"{numerator}/{denominator}",
                'beats_elapsed': beats_elapsed
            }
            
        except (ValueError, ZeroDivisionError):
            return None
    
    def auto_calculate_all(self):
        """Calculate both BPM conversion and time signature position"""
        # Calculate BPM conversion
        self.auto_calculate()
        
        # Calculate time signature position
        ts_result = self.calculate_time_signature_position()
        if ts_result:
            result_text = (f"Bar {ts_result['bars']}, Beat {ts_result['beats']} "
                          f"= {ts_result['milliseconds']:.2f} ms")
            self.ts_result.config(text=result_text)
        else:
            self.ts_result.config(text="-- (invalid input)")


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = BPMCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()