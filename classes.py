class Board:
    '''



    '''
    def __init__(self):
        pass

    def build_board(self, random=True):
        pass

    def add_settlement(self, player, vertex):
        pass
    
    def add_city(self, player, vertex):
        pass
    
    def add_road(self, player, vertex):
        pass
    
class Tile:
    '''


    '''
    def __init__(self, prob, resource, number):
        self.roads = {}
        self.settlements = {}
        self.cities = {}
        

class Player:
    '''


    '''
    def __init__(self, idd):
        self.id = idd
        self.longest_road = 0
        self.num_knights = 0
        self.victory_points = 0
        self.dev_cards = []
        
    
    
