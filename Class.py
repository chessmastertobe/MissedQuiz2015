
from Check_Function import *

class Hand:

   def __init__(self, hand):
       self.hand = hand
       self.rank = value(self.hand)

   def get_rank(self):
       return self.rank


