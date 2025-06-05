# Pygame Snake Game 🐍

A classic implementation of the Snake game built using Python and the Pygame library. This project includes versions with code comments in English, Chinese (中文), and Arabic (العربية), with the Arabic version also featuring Arabic variable names.

## 🌟 Features

*   Classic Snake gameplay: control the snake to eat food and grow longer.
*   Score tracking.
*   Game over detection when the snake hits the walls or itself.
*   Option to restart the game or quit after a game over.
*   Simple, clear, and commented code, available in multiple languages for learning purposes.

## 📸 Screenshot (Placeholder)

(Consider adding a screenshot or a GIF of the game in action here!)
![Snake Game Screenshot](placeholder_snake_game.png)
*Replace `placeholder_snake_game.png` with an actual image path or URL if you have one.*

## 📋 Requirements

*   Python 3.x
*   Pygame library

## 🛠️ Installation

1.  **Clone the repository (optional):**
    ```bash
    git clone <your-repository-url>
    cd <repository-folder>
    ```
    Or simply download the Python script(s).

2.  **Install Pygame:**
    If you don't have Pygame installed, open your terminal or command prompt and run:
    ```bash
    pip install pygame
    ```
    Or, for Python 3 specific pip:
    ```bash
    pip3 install pygame
    ```

## 🚀 How to Run

Navigate to the directory where you saved the game files. Then, run the desired version of the game using Python:

*   **For the version with English comments:**
    (Assuming you have a base version named `snake_english.py` or similar)
    ```bash
    python snake_english.py
    ```

*   **For the version with Chinese comments:**
    ```bash
    python snake_chinese.py
    ```

*   **For the version with Arabic comments and variable names:**
    ```bash
    python snake_arabic.py
    ```
    *   **Note for Arabic Version:** Proper rendering of Arabic text for scores and messages within Pygame might depend on the fonts installed on your system. The code attempts to use common fonts like "Arial" or "Tahoma." If you encounter issues, you might need to install an Arabic-supporting font and modify the `pygame.font.SysFont()` calls in `snake_arabic.py` to use it explicitly (e.g., `pygame.font.Font("YourArabicFont.ttf", size)`).

## 🎮 Controls

*   **Arrow Keys (Up, Down, Left, Right):** Control the direction of the snake.
*   **Q:** Quit the game (on the "Game Over" screen).
*   **R:** Restart the game (on the "Game Over" screen).

## 📂 Project Structure (Example)

You might have the following files in your project:
