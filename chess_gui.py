import pygame
import chess
import random
import os
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600  # Reduced from 800x800 to 600x600
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
PIECE_SIZE = SQUARE_SIZE - 12  # Adjusted for smaller board
FONT_SIZE = 14
BORDER_SIZE = 25  # Slightly smaller border

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = (238, 238, 210)  # Cream color for light squares
DARK_SQUARE = (118, 150, 86)    # Forest green for dark squares
HIGHLIGHT = (247, 247, 105, 180)  # Semi-transparent yellow for highlighting
MOVE_HIGHLIGHT = (186, 202, 68, 180)  # Semi-transparent green for possible moves
BORDER_COLOR = (62, 39, 35)  # Dark brown for border
TEXT_COLOR = (230, 230, 230)  # Off-white for text
BACKGROUND_COLOR = (40, 40, 40)  # Dark gray for background

# Set up the display with border
screen_width = WIDTH + 2 * BORDER_SIZE
screen_height = HEIGHT + 2 * BORDER_SIZE + 60  # Extra space for status bar
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chess")

# Load fonts
try:
    font = pygame.font.Font(None, FONT_SIZE)
    title_font = pygame.font.Font(None, 28)
    coordinate_font = pygame.font.Font(None, 20)
except:
    font = pygame.font.SysFont('Arial', FONT_SIZE)
    title_font = pygame.font.SysFont('Arial', 28)
    coordinate_font = pygame.font.SysFont('Arial', 20)

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.selected_square = None
        self.valid_moves = []
        self.piece_images = {}
        self.load_piece_images()
        self.player_color = chess.WHITE  # Player plays as white
        self.ai_color = chess.BLACK      # AI plays as black
        self.current_turn = chess.WHITE  # White starts
        self.status_message = "White to move"
        self.last_move = None
        self.game_over = False
        self.game_result = ""
        
    def load_piece_images(self):
        """Load chess piece images or create colored shapes if images not available."""
        piece_chars = ['p', 'r', 'n', 'b', 'q', 'k', 'P', 'R', 'N', 'B', 'Q', 'K']
        
        # Try to load images from the pieces directory
        for piece in piece_chars:
            image_path = os.path.join('pieces', f'{piece}.png')
            try:
                if os.path.exists(image_path):
                    img = pygame.image.load(image_path)
                    self.piece_images[piece] = pygame.transform.scale(img, (PIECE_SIZE, PIECE_SIZE))
                else:
                    # Create a placeholder surface if image doesn't exist
                    self.piece_images[piece] = self.create_placeholder_piece(piece)
            except pygame.error:
                self.piece_images[piece] = self.create_placeholder_piece(piece)
    
    def create_placeholder_piece(self, piece):
        """Create a placeholder piece when images are not available."""
        surface = pygame.Surface((PIECE_SIZE, PIECE_SIZE), pygame.SRCALPHA)
        
        # Determine piece color
        is_white = piece.isupper()
        piece_color = WHITE if is_white else BLACK
        bg_color = (200, 200, 200) if is_white else (100, 100, 100)
        
        # Draw a circle as the base
        pygame.draw.circle(surface, bg_color, (PIECE_SIZE//2, PIECE_SIZE//2), PIECE_SIZE//2)
        pygame.draw.circle(surface, piece_color, (PIECE_SIZE//2, PIECE_SIZE//2), PIECE_SIZE//2 - 2)
        
        # Add the piece letter
        text = font.render(piece.upper(), True, BLACK if is_white else WHITE)
        text_rect = text.get_rect(center=(PIECE_SIZE//2, PIECE_SIZE//2))
        surface.blit(text, text_rect)
        
        return surface
    
    def get_piece_name(self, piece_char):
        """Return the full name of a piece based on its character."""
        names = {
            'p': 'Pawn', 'r': 'Rook', 'n': 'Knight', 'b': 'Bishop', 'q': 'Queen', 'k': 'King',
            'P': 'Pawn', 'R': 'Rook', 'N': 'Knight', 'B': 'Bishop', 'Q': 'Queen', 'K': 'King'
        }
        return names.get(piece_char, '')
    
    def draw_board(self):
        """Draw the chess board with pieces and coordinates."""
        # Fill background
        screen.fill(BACKGROUND_COLOR)
        
        # Draw board border
        pygame.draw.rect(screen, BORDER_COLOR, 
                         (BORDER_SIZE - 5, BORDER_SIZE - 5, 
                          WIDTH + 10, HEIGHT + 10), 5)
        
        # Draw the squares
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
                
                # Draw the square
                pygame.draw.rect(screen, color, 
                                (col * SQUARE_SIZE + BORDER_SIZE, 
                                 row * SQUARE_SIZE + BORDER_SIZE, 
                                 SQUARE_SIZE, SQUARE_SIZE))
                
                # Highlight selected square
                if self.selected_square is not None and row * BOARD_SIZE + col == self.selected_square:
                    highlight_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                    highlight_surface.fill(HIGHLIGHT)
                    screen.blit(highlight_surface, 
                               (col * SQUARE_SIZE + BORDER_SIZE, 
                                row * SQUARE_SIZE + BORDER_SIZE))
                
                # Highlight valid moves
                if row * BOARD_SIZE + col in self.valid_moves:
                    move_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                    move_surface.fill(MOVE_HIGHLIGHT)
                    screen.blit(move_surface, 
                               (col * SQUARE_SIZE + BORDER_SIZE, 
                                row * SQUARE_SIZE + BORDER_SIZE))
                    
                    # Draw a circle for empty squares or a ring for captures
                    piece = self.board.piece_at(row * BOARD_SIZE + col)
                    if piece is None:
                        # Draw a dot for empty square moves
                        pygame.draw.circle(screen, DARK_SQUARE if (row + col) % 2 == 0 else LIGHT_SQUARE,
                                          (col * SQUARE_SIZE + BORDER_SIZE + SQUARE_SIZE // 2,
                                           row * SQUARE_SIZE + BORDER_SIZE + SQUARE_SIZE // 2),
                                          SQUARE_SIZE // 8)
                    else:
                        # Draw a ring for captures
                        pygame.draw.circle(screen, (255, 0, 0, 180),
                                          (col * SQUARE_SIZE + BORDER_SIZE + SQUARE_SIZE // 2,
                                           row * SQUARE_SIZE + BORDER_SIZE + SQUARE_SIZE // 2),
                                          SQUARE_SIZE // 2 - 5, 2)
                
                # Highlight last move
                if self.last_move:
                    from_square = self.last_move.from_square
                    to_square = self.last_move.to_square
                    
                    from_row, from_col = self.square_to_coords(from_square)
                    to_row, to_col = self.square_to_coords(to_square)
                    
                    if row == from_row and col == from_col or row == to_row and col == to_col:
                        last_move_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                        last_move_surface.fill((255, 255, 0, 60))  # Very light yellow
                        screen.blit(last_move_surface, 
                                   (col * SQUARE_SIZE + BORDER_SIZE, 
                                    row * SQUARE_SIZE + BORDER_SIZE))
        
        # Draw the pieces
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                square = row * BOARD_SIZE + col
                piece = self.board.piece_at(square)
                
                if piece:
                    piece_char = piece.symbol()
                    piece_img = self.piece_images.get(piece_char)
                    
                    if piece_img:
                        # Center the piece in the square
                        x = col * SQUARE_SIZE + BORDER_SIZE + (SQUARE_SIZE - PIECE_SIZE) // 2
                        y = row * SQUARE_SIZE + BORDER_SIZE + (SQUARE_SIZE - PIECE_SIZE) // 2
                        screen.blit(piece_img, (x, y))
        
        # Draw coordinates
        for i in range(BOARD_SIZE):
            # Draw file labels (a-h)
            file_label = chr(97 + i)  # ASCII 'a' is 97
            text = coordinate_font.render(file_label, True, TEXT_COLOR)
            screen.blit(text, (BORDER_SIZE + i * SQUARE_SIZE + SQUARE_SIZE // 2 - text.get_width() // 2, 
                              HEIGHT + BORDER_SIZE + 5))
            
            # Draw rank labels (1-8)
            rank_label = str(8 - i)
            text = coordinate_font.render(rank_label, True, TEXT_COLOR)
            screen.blit(text, (BORDER_SIZE - 15, 
                              BORDER_SIZE + i * SQUARE_SIZE + SQUARE_SIZE // 2 - text.get_height() // 2))
        
        # Draw status bar
        status_rect = pygame.Rect(BORDER_SIZE, HEIGHT + BORDER_SIZE + 20, WIDTH, 25)
        status_text = title_font.render(self.status_message, True, TEXT_COLOR)
        screen.blit(status_text, (status_rect.centerx - status_text.get_width() // 2, 
                                 status_rect.centery - status_text.get_height() // 2))
        
        # Draw game title
        title_text = title_font.render("Chess", True, TEXT_COLOR)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 8))
    
    def square_to_coords(self, square):
        """Convert a chess.square (0-63) to board coordinates (row, col)."""
        return (square // BOARD_SIZE, square % BOARD_SIZE)
    
    def coords_to_square(self, row, col):
        """Convert board coordinates (row, col) to a chess.square (0-63)."""
        return row * BOARD_SIZE + col
    
    def get_square_from_pos(self, pos):
        """Convert screen position to board square."""
        x, y = pos
        x -= BORDER_SIZE
        y -= BORDER_SIZE
        
        if x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT:
            return None
            
        col = x // SQUARE_SIZE
        row = y // SQUARE_SIZE
        return self.coords_to_square(row, col)
    
    def get_valid_moves(self, square):
        """Get all valid moves for the piece at the given square."""
        valid_moves = []
        piece = self.board.piece_at(square)
        
        if piece and piece.color == self.board.turn:
            for move in self.board.legal_moves:
                if move.from_square == square:
                    valid_moves.append(move.to_square)
        
        return valid_moves
    
    def make_move(self, from_square, to_square):
        """Make a move on the board if it's valid."""
        move = chess.Move(from_square, to_square)
        
        # Check for promotion
        if self.board.piece_at(from_square) and self.board.piece_at(from_square).piece_type == chess.PAWN:
            if (to_square < 8 and self.board.piece_at(from_square).color == chess.BLACK) or \
               (to_square >= 56 and self.board.piece_at(from_square).color == chess.WHITE):
                move = chess.Move(from_square, to_square, promotion=chess.QUEEN)
        
        if move in self.board.legal_moves:
            self.board.push(move)
            self.last_move = move
            self.current_turn = not self.current_turn  # Switch turns
            
            # Update status message
            if self.board.turn == chess.WHITE:
                self.status_message = "White to move"
            else:
                self.status_message = "Black to move"
            
            # Check for game over conditions
            if self.board.is_checkmate():
                winner = "Black" if self.board.turn == chess.WHITE else "White"
                self.status_message = f"Checkmate! {winner} wins!"
                self.game_over = True
                self.game_result = f"{winner} wins by checkmate"
            elif self.board.is_stalemate():
                self.status_message = "Stalemate! Game drawn."
                self.game_over = True
                self.game_result = "Draw by stalemate"
            elif self.board.is_insufficient_material():
                self.status_message = "Insufficient material! Game drawn."
                self.game_over = True
                self.game_result = "Draw by insufficient material"
            elif self.board.is_check():
                self.status_message += " (Check!)"
            
            return True
        return False
    
    def ai_move(self):
        """Make a random valid move for the AI."""
        if self.board.turn == self.ai_color and not self.game_over:
            legal_moves = list(self.board.legal_moves)
            if legal_moves:
                move = random.choice(legal_moves)
                self.board.push(move)
                self.last_move = move
                self.current_turn = not self.current_turn  # Switch turns
                
                # Update status message
                if self.board.turn == chess.WHITE:
                    self.status_message = "White to move"
                else:
                    self.status_message = "Black to move"
                
                # Check for game over conditions
                if self.board.is_checkmate():
                    winner = "Black" if self.board.turn == chess.WHITE else "White"
                    self.status_message = f"Checkmate! {winner} wins!"
                    self.game_over = True
                    self.game_result = f"{winner} wins by checkmate"
                elif self.board.is_stalemate():
                    self.status_message = "Stalemate! Game drawn."
                    self.game_over = True
                    self.game_result = "Draw by stalemate"
                elif self.board.is_insufficient_material():
                    self.status_message = "Insufficient material! Game drawn."
                    self.game_over = True
                    self.game_result = "Draw by insufficient material"
                elif self.board.is_check():
                    self.status_message += " (Check!)"
                
                return True
        return False
    
    def handle_click(self, pos):
        """Handle mouse click on the board."""
        square = self.get_square_from_pos(pos)
        
        # If click is outside the board or game is over
        if square is None or self.game_over:
            return
        
        # If it's not the player's turn, do nothing
        if self.board.turn != self.player_color:
            return
        
        # If a square is already selected
        if self.selected_square is not None:
            # Try to make a move
            if self.make_move(self.selected_square, square):
                self.selected_square = None
                self.valid_moves = []
                
                # After player's move, make AI move
                pygame.time.delay(500)  # Small delay before AI moves
                self.ai_move()
            else:
                # If the clicked square has a piece of the player's color, select it
                piece = self.board.piece_at(square)
                if piece and piece.color == self.player_color:
                    self.selected_square = square
                    self.valid_moves = self.get_valid_moves(square)
                else:
                    # If clicked on an invalid square, deselect
                    self.selected_square = None
                    self.valid_moves = []
        else:
            # Select a square if it has a piece of the player's color
            piece = self.board.piece_at(square)
            if piece and piece.color == self.player_color:
                self.selected_square = square
                self.valid_moves = self.get_valid_moves(square)
    
    def draw_piece_info(self, pos):
        """Draw information about the piece at the given position."""
        square = self.get_square_from_pos(pos)
        if square is not None:
            piece = self.board.piece_at(square)
            if piece:
                piece_char = piece.symbol()
                piece_name = self.get_piece_name(piece_char)
                color = "White" if piece.color == chess.WHITE else "Black"
                info_text = f"{color} {piece_name}"
                
                # Update status message with piece info
                self.status_message = info_text

def main():
    game = ChessGame()
    running = True
    clock = pygame.time.Clock()
    
    # If AI starts (playing as white), make the first move
    if game.current_turn == game.ai_color:
        game.ai_move()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    game.handle_click(event.pos)
            elif event.type == pygame.MOUSEMOTION:
                # Update piece info on hover
                game.draw_piece_info(event.pos)
        
        screen.fill(BACKGROUND_COLOR)
        game.draw_board()
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
