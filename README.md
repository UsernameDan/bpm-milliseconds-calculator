# BPM to Milliseconds Calculator

A comprehensive Python tkinter application that converts beats per minute (BPM) to milliseconds and calculates precise timing for musical arrangements, with support for time signatures and beat positioning.

## Features

- **Time Signature Calculator** - Calculate exact millisecond positions for specific bars and beats
- Convert BPM to milliseconds for various note values
- **Real-time automatic calculation** as you type or change settings
- **Automatic font detection** for proper musical symbols (𝅝 𝅗𝅥 ♩ ♪ ♬ ♫)
- **Compact button layout** with all note values in a single row
- **Fallback support** for systems without musical fonts
- Support for all standard note values (semibreve, minim, crotchet, quaver, semiquaver, demisemiquaver)
- Calculate precise note durations in milliseconds
- Clean, user-friendly interface with intuitive button selection using proper musical terminology
- **Consistent visual styling** with blue text results in both calculators
- Input validation and error handling
- Font information display showing which font is being used

## Requirements

- Python 3.x
- tkinter (usually included with Python)

## How to Run

1. Make sure you have Python installed
2. Navigate to the project directory
3. Run the application:
   ```
   python bpm_calculator.py
   ```

## Font Support

The application automatically detects the best available font for musical symbols:

- **Preferred**: Professional music fonts (Noto Music, Bravura, MuseScore fonts)
- **Good**: Unicode fonts with musical symbol support (Arial Unicode MS, Symbola)
- **Basic**: System fonts with limited musical symbols (Segoe UI Symbol)
- **Fallback**: Simple text symbols if no Unicode support

### Getting Better Musical Fonts

For the best musical symbol display, install a dedicated music font:

**🎼 Recommended (Professional Quality):**
- **Noto Music** - Google's free musical notation font
- **Bravura** - Professional music engraving font by Steinberg  
- **MuseScore Fonts** - High-quality open-source music fonts

**📥 Installation:**

1. Run the font helper tool:
   ```
   python font_helper.py
   ```
2. Use the "Check Current Fonts" button to see what's installed
3. Use "Get Font Download Links" to access recommended musical fonts
4. After installing new fonts, restart the BPM calculator

## How to Use

### Getting Started

1. **Set BPM**: The main BPM field is prominently centered at the top (defaults to 120)
2. All calculations update automatically as you change any values

### Time Signature Calculator

1. **Set Time Signature**: Enter numerator and denominator (e.g., 4/4, 3/4, 6/8)
2. **Enter Bar Number**: Which measure you want to calculate (starts from 1)
3. **Enter Beat Number**: Which beat within that bar (can use decimals like 2.5)
2. **View Results**: See the exact millisecond position automatically calculated

### Note Value Calculator

1. **Select Note Value**: Click on the musical note buttons to choose note duration:
   - 𝅝 = Whole Note / Semibreve (if font supports it, otherwise W)
   - 𝅗𝅥 = Half Note / Minim (if font supports it, otherwise H)
   - ♩ = Quarter Note / Crotchet
   - ♪ = Eighth Note / Quaver
   - ♬ = Sixteenth Note / Semiquaver
   - ♫ = Thirty-second Note / Demisemiquaver
2. **View Duration**: See the millisecond duration for the selected note value
4. View the results:
   - Milliseconds: Duration of one note in milliseconds
   - Frequency: How many notes per second
   - Period: Duration of one note in seconds

## Example

**Default startup values** (120 BPM with crotchets):
- Note Duration: 500.00 ms

**Time Signature Example** (4/4 time at 120 BPM):
- Bar 1, Beat 1 = 0.00 ms (start of song)
- Bar 1, Beat 2 = 500.00 ms
- Bar 1, Beat 3 = 1000.00 ms
- Bar 1, Beat 4 = 1500.00 ms
- Bar 2, Beat 1 = 2000.00 ms (start of second measure)## Musical Terminology

The application uses proper British musical terminology in the button tooltips:

- **Semibreve** = Whole Note (4 beats)
- **Minim** = Half Note (2 beats)
- **Crotchet** = Quarter Note (1 beat)
- **Quaver** = Eighth Note (1/2 beat)
- **Semiquaver** = Sixteenth Note (1/4 beat)
- **Demisemiquaver** = Thirty-second Note (1/8 beat)

## Code Structure

- `BPMCalculator` class: Main application class
- `setup_ui()`: Creates the user interface
- `calculate()`: Performs the BPM to milliseconds conversion
- `get_note_multiplier()`: Returns the multiplier for different note values

## Customization

You can easily modify the application by:
- Adding more note values to the dropdown
- Changing the window size or appearance
- Adding more calculation results
- Implementing additional features like tempo markings

## Formula

The conversion formula used is:
```
milliseconds = (60 / BPM) × 1000 × note_multiplier
```

Where note_multiplier varies based on the selected note value:
- Whole Note: 4.0
- Half Note: 2.0
- Quarter Note: 1.0
- Eighth Note: 0.5
- Sixteenth Note: 0.25
- Thirty-second Note: 0.125