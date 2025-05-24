import pygame
import os
import math

# Initialize pygame
pygame.init()

# Constants
PIECE_SIZE = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (220, 220, 220)
DARK_GRAY = (80, 80, 80)
GOLD = (212, 175, 55)
SILVER = (192, 192, 192)

def create_piece_image(piece_char, output_dir):
    """Create a more professional looking image for a chess piece."""
    surface = pygame.Surface((PIECE_SIZE, PIECE_SIZE), pygame.SRCALPHA)
    
    # Determine piece color and type
    is_white = piece_char.isupper()
    piece_type = piece_char.upper()
    
    # Base colors
    piece_color = WHITE if is_white else BLACK
    outline_color = BLACK if is_white else LIGHT_GRAY
    highlight_color = SILVER if is_white else GOLD
    
    # Draw piece based on type
    if piece_type == 'P':  # Pawn
        draw_pawn(surface, piece_color, outline_color, highlight_color)
    elif piece_type == 'R':  # Rook
        draw_rook(surface, piece_color, outline_color, highlight_color)
    elif piece_type == 'N':  # Knight
        draw_knight(surface, piece_color, outline_color, highlight_color)
    elif piece_type == 'B':  # Bishop
        draw_bishop(surface, piece_color, outline_color, highlight_color)
    elif piece_type == 'Q':  # Queen
        draw_queen(surface, piece_color, outline_color, highlight_color)
    elif piece_type == 'K':  # King
        draw_king(surface, piece_color, outline_color, highlight_color)
    
    # Save the image
    output_path = os.path.join(output_dir, f'{piece_char}.png')
    pygame.image.save(surface, output_path)
    print(f"Created {output_path}")

def draw_pawn(surface, color, outline, highlight):
    """Draw a more professional pawn piece."""
    # Base
    pygame.draw.ellipse(surface, color, (25, 70, 50, 20))
    pygame.draw.ellipse(surface, outline, (25, 70, 50, 20), 2)
    
    # Stem/body
    pygame.draw.polygon(surface, color, [(40, 70), (35, 40), (50, 35), (65, 40), (60, 70)])
    pygame.draw.polygon(surface, outline, [(40, 70), (35, 40), (50, 35), (65, 40), (60, 70)], 2)
    
    # Head
    pygame.draw.circle(surface, color, (50, 25), 15)
    pygame.draw.circle(surface, outline, (50, 25), 15, 2)
    
    # Highlight
    pygame.draw.arc(surface, highlight, (40, 20, 20, 15), math.pi/4, math.pi, 2)

def draw_rook(surface, color, outline, highlight):
    """Draw a rook piece."""
    # Base
    pygame.draw.rect(surface, color, (20, 65, 60, 20))
    pygame.draw.rect(surface, outline, (20, 65, 60, 20), 2)
    
    # Body
    pygame.draw.rect(surface, color, (30, 35, 40, 30))
    pygame.draw.rect(surface, outline, (30, 35, 40, 30), 2)
    
    # Top
    pygame.draw.rect(surface, color, (20, 25, 60, 10))
    pygame.draw.rect(surface, outline, (20, 25, 60, 10), 2)
    
    # Battlements
    for i in range(3):
        x = 25 + i*25
        pygame.draw.rect(surface, color, (x, 15, 10, 10))
        pygame.draw.rect(surface, outline, (x, 15, 10, 10), 2)
    
    # Highlight
    pygame.draw.line(surface, highlight, (35, 40), (65, 40), 2)

def draw_knight(surface, color, outline, highlight):
    """Draw a knight piece."""
    # Base
    pygame.draw.ellipse(surface, color, (25, 65, 50, 25))
    pygame.draw.ellipse(surface, outline, (25, 65, 50, 25), 2)
    
    # Body
    points = [(40, 65), (35, 40), (45, 25), (60, 15), (70, 25), (65, 40), (60, 65)]
    pygame.draw.polygon(surface, color, points)
    pygame.draw.polygon(surface, outline, points, 2)
    
    # Eye
    pygame.draw.circle(surface, outline, (55, 25), 3)
    
    # Mane
    pygame.draw.arc(surface, highlight, (45, 20, 20, 30), math.pi/2, 3*math.pi/2, 3)

def draw_bishop(surface, color, outline, highlight):
    """Draw a bishop piece."""
    # Base
    pygame.draw.ellipse(surface, color, (25, 65, 50, 25))
    pygame.draw.ellipse(surface, outline, (25, 65, 50, 25), 2)
    
    # Body
    pygame.draw.polygon(surface, color, [(40, 65), (35, 35), (50, 15), (65, 35), (60, 65)])
    pygame.draw.polygon(surface, outline, [(40, 65), (35, 35), (50, 15), (65, 35), (60, 65)], 2)
    
    # Slit
    pygame.draw.line(surface, outline, (50, 25), (50, 45), 2)
    
    # Highlight
    pygame.draw.arc(surface, highlight, (40, 20, 20, 20), math.pi/4, math.pi, 2)

def draw_queen(surface, color, outline, highlight):
    """Draw a queen piece."""
    # Base
    pygame.draw.ellipse(surface, color, (20, 65, 60, 25))
    pygame.draw.ellipse(surface, outline, (20, 65, 60, 25), 2)
    
    # Body
    pygame.draw.polygon(surface, color, [(35, 65), (30, 35), (50, 20), (70, 35), (65, 65)])
    pygame.draw.polygon(surface, outline, [(35, 65), (30, 35), (50, 20), (70, 35), (65, 65)], 2)
    
    # Crown
    for i in range(5):
        x = 30 + i*10
        pygame.draw.circle(surface, color, (x, 20), 5)
        pygame.draw.circle(surface, outline, (x, 20), 5, 1)
    
    # Highlight
    pygame.draw.arc(surface, highlight, (35, 30, 30, 20), math.pi/4, math.pi, 2)

def draw_king(surface, color, outline, highlight):
    """Draw a king piece."""
    # Base
    pygame.draw.ellipse(surface, color, (20, 65, 60, 25))
    pygame.draw.ellipse(surface, outline, (20, 65, 60, 25), 2)
    
    # Body
    pygame.draw.polygon(surface, color, [(35, 65), (30, 35), (50, 25), (70, 35), (65, 65)])
    pygame.draw.polygon(surface, outline, [(35, 65), (30, 35), (50, 25), (70, 35), (65, 65)], 2)
    
    # Cross
    pygame.draw.rect(surface, color, (45, 10, 10, 25))
    pygame.draw.rect(surface, outline, (45, 10, 10, 25), 2)
    pygame.draw.rect(surface, color, (35, 15, 30, 10))
    pygame.draw.rect(surface, outline, (35, 15, 30, 10), 2)
    
    # Highlight
    pygame.draw.arc(surface, highlight, (35, 30, 30, 20), math.pi/4, math.pi, 2)

def main():
    # Create pieces directory if it doesn't exist
    output_dir = 'pieces'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate all piece images
    piece_chars = ['p', 'r', 'n', 'b', 'q', 'k', 'P', 'R', 'N', 'B', 'Q', 'K']
    for piece in piece_chars:
        create_piece_image(piece, output_dir)
    
    print("All piece images generated successfully!")

if __name__ == "__main__":
    main()
