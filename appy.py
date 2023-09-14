#!/usr/bin/env python3
import os

# Define your buttons and their corresponding URLs
buttons = [
    {"label": "google", "url": "https://google.com"},
    {"label": "yahoo", "url": "https://yahoo.com"},
    # Add more buttons as needed
]

def main():
    while True:
        os.system("clear")  # Clear the terminal screen

        # Display the text art
        print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           TERMINAL APP            ┃
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
""")

        # Display buttons
        for idx, button in enumerate(buttons, start=1):
            print(f"   {idx}. {button['label']}")

        print("""
┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
┃ Use arrow keys to navigate, Enter  ┃
┃ to open a link, or Ctrl+C to exit. ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")

        # Get user input
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(buttons):
                url = buttons[choice - 1]["url"]
                os.system(f"firefox {url} &")
        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
