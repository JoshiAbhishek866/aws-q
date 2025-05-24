# Chess Game

A graphical chess implementation with an elegant UI built using PyGame and python-chess.

![Chess Game Screenshot](https://example.com/chess_screenshot.png)

## Features

- **Professional UI**: Elegant chessboard with cream and forest green squares on a dark background
- **Custom Chess Pieces**: Visually distinct pieces with professional design
- **Human vs AI Gameplay**: Play against a computer opponent making random valid moves
- **Legal Move Validation**: Complete chess rules enforced by python-chess library
- **Interactive Elements**:
  - Piece selection highlighting
  - Valid move indicators (dots for empty squares, rings for captures)
  - Last move highlighting
  - Game state tracking
- **Game Status Display**: Shows whose turn it is, check/checkmate status, and game results
- **Board Coordinates**: Standard chess notation (a-h, 1-8) displayed around the board

## Requirements

- Python 3.x
- PyGame
- python-chess

## Installation

1. Clone or download this repository
2. Install the required packages:

```bash
pip install pygame python-chess
```

3. Run the game:

```bash
python3 chess_gui.py
```

## How to Play

1. **Starting the Game**: Run `python3 chess_gui.py` to launch the game
2. **Making Moves**:
   - Click on a white piece to select it
   - Valid moves will be highlighted
   - Click on a destination square to move the piece
3. **AI Response**: The AI will automatically make its move after yours
4. **Game End**: The game will detect checkmate, stalemate, or insufficient material

## Controls

- **Left Mouse Click**: Select and move pieces
- **Mouse Hover**: View piece information
- **Close Window**: Quit the game

## Game Rules

- You play as white pieces
- The AI plays as black pieces
- Standard chess rules apply:
  - Pawns move forward one square (or two on first move) and capture diagonally
  - Rooks move horizontally and vertically
  - Knights move in an L-shape
  - Bishops move diagonally
  - Queens move horizontally, vertically, and diagonally
  - Kings move one square in any direction
  - Special moves like castling and en passant are supported

## Project Structure

- `chess_gui.py`: Main game file with the chess implementation
- `generate_pieces.py`: Script to generate custom chess piece images
- `pieces/`: Directory containing chess piece images
- `README.md`: This documentation file

## Customization

You can customize the game by modifying:

- Board colors in the `chess_gui.py` file (LIGHT_SQUARE, DARK_SQUARE constants)
- Piece designs in the `generate_pieces.py` file
- Board size by changing the WIDTH and HEIGHT constants

## Credits

- Chess logic: [python-chess](https://python-chess.readthedocs.io/)
- Graphics: PyGame
- Piece designs: Custom implementation

## License

This project is available under the MIT License.

## Future Improvements

- Implement AI with different difficulty levels
- Add sound effects
- Add menu system
- Add game history and replay functionality
- Add time controls
- Add multiplayer support
