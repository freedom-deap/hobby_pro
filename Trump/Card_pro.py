'''
祝　GitHubへのアップロード成功
カード1枚1枚を表すクラス
・suit:スペード、ハート、クラブ、ダイヤの4種類を0～3の4つの数で表す
・number:A～Kの数（文字)を表す
・例外としてジョーカーはsuit無し、数をJokerとして扱う
'''

class Card_pro:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def print_property_1(self):
        if self.suit in [0, 1, 2, 3]:
            print('このカードは'+ self.suit_to_mark_1()+'の'+str(self.number)+'です')
        else:
            print('このカードは'+str(self.number)+'です')

    def print_property_2(self):
        if self.suit in [0, 1, 2, 3]:
            print(str(self.suit_to_mark_2()) + ':'+ str(self.number))
        else:
            print(self.number)
            
    def suit_to_mark_1(self):
        if self.suit ==  0:
            return 'スペード'
        elif self.suit == 1:
            return 'ハート'
        elif self.suit == 2:
            return 'クラブ'
        elif self.suit == 3:
            return 'ダイヤ'

    def suit_to_mark_2(self):
        if self.suit ==  0:
            return '♠'
        elif self.suit == 1:
            return '♥'
        elif self.suit == 2:
            return '♣'
        elif self.suit == 3:
            return '♦'
        
if __name__ == '__main__':
    h_k = Card_pro(1,'K')
    h_k.print_property_1()
    h_k.print_property_2()
    
