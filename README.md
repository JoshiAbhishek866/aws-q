# Chess Game using AWS Q

A graphical chess implementation with an elegant UI built using PyGame and python-chess, using AWS Q.

![Chess Game using AWS Q](https://youtu.be/OZM6BmLVeYU)

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

## Prompts Used with AWS Q CLI
This project was prototyped with the help of AWS Q CLI for initial scaffolding and iterative improvements. Below are the prompts used during development:

-Initial Prompt

Create a Chess game using Python and PyGame. The board should be 8x8 and styled like a real chessboard with alternating light and dark square colors. Draw or use images for all standard chess pieces and display their names like "Pawn", "Rook", "Knight", "Bishop", "Queen", and "King" either on or just below each piece using readable fonts. The game should be played between a human and a basic AI. Use the `python-chess` library to validate legal moves. Implement piece selection, movement, and capturing logic. Ensure turns alternate properly between the player and the AI. The AI can make random valid moves for simplicity. Add basic UI interactions like selecting a piece and clicking to move it. Avoid implementing check/checkmate logic unless simple. Focus on functionality, clarity, and piece visibility.

-UI Enhancement Feedback

Please can you work on UI of game? Make the chessboard look more like a professional chessboard, if possible. You can do changes as per your convenience, but please take note on better Professional UI.

-Specific Refinement Request

Can you help me to make shape of pawn more proper, it looks unprofessional; also please make size of entire chessboard a little bit small, as it's not properly fitting my screen.

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
