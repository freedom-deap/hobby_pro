from Card_pro import Card_pro

face_and_A = ['A', 'J', 'Q', 'K']
numb_o_sh = int(13)
numb_o_su = int(4)
    
class Trump_pro:
    def __init__(self):
        self.deck = []
        for i in range(numb_o_su):
            for j in range(numb_o_sh):
                if j == 0:
                    self.deck.append(Card_pro(i, face_and_A[0]))
                elif j == 10:
                    self.deck.append(Card_pro(i, face_and_A[1]))
                elif j == 11:
                    self.deck.append(Card_pro(i, face_and_A[2]))
                elif j == 12:
                    self.deck.append(Card_pro(i, face_and_A[3]))
                else:
                    self.deck.append(Card_pro(i, j))
        self.deck.append(Card_pro('', 'Joker'))
                    
if __name__ == '__main__':
    Trump = Trump_pro()
    Trump.deck[12].print_property_2()
    Trump.deck[25].print_property_2()
    Trump.deck[38].print_property_2()
    Trump.deck[51].print_property_2()
