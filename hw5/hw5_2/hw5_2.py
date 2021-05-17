import unittest
from game import TicTacToe


class TestGameWinner(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_row(self):
        print("Unit Test Row 1")
        self.game.board = ['X', 'X', 'X', '0', ' ', '0', '0', ' ', ' ']
        self.game.print_board()
        self.assertTrue(self.game.winner(0, 'X'))
        print("Unit Test Row 2")
        self.game.board = [' ', '0', '0', 'X', 'X', 'X', '0', ' ', ' ']
        self.game.print_board()
        self.assertTrue(self.game.winner(4, 'X'))
        print("Unit Test Row 3")
        self.game.board = ['X', 'X', ' ', 'X', ' ', ' ', '0', '0', '0']
        self.game.print_board()
        self.assertTrue(self.game.winner(8, '0'))
        print("Unit Test Row 4")
        self.game.board = ['X', 'X', ' ', 'X', ' ', ' ', '', '0', '0']
        self.game.print_board()
        self.assertFalse(self.game.winner(8, '0'))
        self.assertFalse(self.game.winner(0, 'X'))

    def test_column(self):
        print("Unit Test Column 1")
        self.game.board = ['X', 'X', '0', 'X', '0', 'X', 'X', '0', '0']
        self.game.print_board()
        self.assertTrue(self.game.winner(0, 'X'))
        print("Unit Test Column 2")
        self.game.board = [' ', 'X', '0', 'X', 'X', 'X', '0', 'X', ' ']
        self.game.print_board()
        self.assertTrue(self.game.winner(4, 'X'))
        print("Unit Test Column 3")
        self.game.board = ['X', 'X', '0', 'X', ' ', '0', '0', 'X', '0']
        self.game.print_board()
        self.assertTrue(self.game.winner(8, '0'))
        print("Unit Test Column 4")
        self.game.board = ['X', 'X', '', 'X', ' ', '0', '0', 'X', '0']
        self.game.print_board()
        self.assertFalse(self.game.winner(8, '0'))
        self.assertFalse(self.game.winner(0, 'X'))

    def test_diagonal(self):
        print("Unit Test Diagonal 1")
        self.game.board = ['X', '0', '0', '0', 'X', '0', '0', '0', 'X']
        self.game.print_board()
        self.assertTrue(self.game.winner(0, 'X'))
        print("Unit Test Diagonal 2")
        self.game.board = ['X', 'X', '0', 'X', '0', 'X', '0', 'X', 'X']
        self.game.print_board()
        self.assertTrue(self.game.winner(8, '0'))
        print("Unit Test Diagonal 3")
        self.game.board = ['X', '0', '0', 'X', '', 'X', '0', '0', 'X']
        self.game.print_board()
        self.assertFalse(self.game.winner(8, 'X'))
        self.assertFalse(self.game.winner(6, '0'))


if __name__ == '__main__':
    unittest.main()
