"""Module to represent a chess set, and individual pieces."""

from utils.spritesheet import SpriteSheet


class ChessSet:
    """Represents a set of chess pieces.
    Each piece is an object of the Piece class.
    """

    def __init__(self, chess_game):
        """Initialize attributes to represent the overall set of pieces."""

        self.chess_game = chess_game
        self.pieces = []
        self._load_pieces()

    def _load_pieces(self):
        """Builds the overall set:
        - Loads images from the sprite sheet.
        - Creates a Piece object, and sets appropriate attributes
          for that piece.
        - Adds each piece to the list self.pieces.
        """
        filename = 'images/chess_pieces.bmp'
        piece_ss = SpriteSheet(filename)

        # Load all piece images.
        piece_images = piece_ss.load_grid_images(2, 6, x_margin=64,
                x_padding=72, y_margin=68, y_padding=48)

        # Create a Piece for each image.
        colors = ['black', 'white']
        names = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

        piece_num = 0
        for color in colors:
            for name in names:
                piece = Piece(self.chess_game)
                piece.name = name
                piece.color = color
                piece.image = piece_images[piece_num]
                self.pieces.append(piece)

                piece_num += 1


class Piece:
    """Represents a chess piece."""

    def __init__(self, chess_game):
        """Initialize attributes to represent a ches piece."""
        super().__init__()

        self.image = None
        self.name = ''
        self.color = ''

        self.screen = chess_game.screen

        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        """Draw the piece at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)
