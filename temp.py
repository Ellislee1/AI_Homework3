from src.board2 import Board
from src.actor import Actor
import numpy as np

p1 = Actor(1, True)
p2 = Actor(2, True)

b = Board(np.zeros((4,4)),p1,[p1,p2],3)

while not b.is_terminal and not b.is_draw:
    move = b.turn.get_move(b)
    b = b.move(move)
    b.print()

b.print()
print(b._eval(p1))

