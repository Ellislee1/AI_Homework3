import unittest

from src.environment import Environment as Env
from src.player import Player


class EnvironmentTests(unittest.TestCase):

    def test_check_horizontal(self):
        p1 = Player('X', False)
        p2 = Player('O', False)
        shape = 3
        to_win = 3
        env = Env(p1, p2, shape, to_win)
        env.place(0,0,p1)
        env.place(1,0,p1)
        env.place(2,0,p1)
        print(env.grid)
        print("\n\n")
        self.assertTrue(env.checkOver([2,0],1))

    def test_check_vertical(self):
        p1 = Player('X', False)
        p2 = Player('O', False)
        shape = 3
        to_win = 3
        env = Env(p1, p2, shape, to_win)
        env.place(2,1,p1)
        env.place(2,2,p1)
        env.place(2,0,p1)
        print(env.grid)
        print("\n\n")
        self.assertTrue(env.checkOver([2,0],1))

    def test_check_diagonal(self):
        p1 = Player('X', False)
        p2 = Player('O', False)
        shape = 3
        to_win = 3
        env = Env(p1, p2, shape, to_win)
        env.place(0,2,p1)
        env.place(1,1,p1)
        env.place(2,0,p1)
        print(env.grid)
        print("\n\n")
        self.assertTrue(env.checkOver([2,0],1))
    
    def test_check_inversediagonal(self):
        p1 = Player('X', False)
        p2 = Player('O', False)
        shape = 3
        to_win = 3
        env = Env(p1, p2, shape, to_win)
        env.place(0,0,p1)
        env.place(1,1,p1)
        env.place(2,2,p1)
        print(env.grid)
        print("\n\n")
        self.assertTrue(env.checkOver([2,2],1))




if __name__ == "__main__":
    unittest.main()