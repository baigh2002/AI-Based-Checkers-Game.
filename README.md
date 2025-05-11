# 🧠 AI Checkers Game using Minimax Algorithm

A Python-based Checkers game with an AI opponent powered by the Minimax algorithm and Pygame for visuals. The AI is capable of making strategic decisions and supports custom rules like restricting crowned piece captures.

## 🎮 Features

- Player vs AI gameplay
- AI logic using Minimax algorithm with configurable depth
- Crowned (King) pieces
- Custom rule: **Only crowned pieces can capture other crowned pieces**
- Visual board with interactive mouse input
- Displays winner on screen when the game ends


## 🧠 AI Logic

The AI uses the Minimax algorithm with depth-limited recursion to simulate and evaluate future game states. The evaluation function is based on:
- Piece count advantage
- King (crowned) piece advantage

## 🧾 Rules

- Standard 8x8 Checkers rules
- White starts first
- Regular pieces can move diagonally forward
- Kings (crowned pieces) can move diagonally in both directions
- **Custom Rule**: Kings must be captured by other kings

## 🛠️ Setup Instructions

### Requirements

- Python 3.x
- Pygame

### Installation

```bash
pip install pygame
