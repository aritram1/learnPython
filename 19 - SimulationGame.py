import time

class player:
    def __init__(self,name):
        self.name = name
        self.life = 100
        self.turn = True
        self.weapons = []
    def loadweapon(self, name):
        self.weapons.append(weapon(name))
    def play(self, other):
        self.life = self.life - 10
        for weapon in self.weapons:
            weapon.ammo = weapon.ammo - 10
        self.turn = not self.turn
        other.turn = not other.turn
        print('{0} has life {1} and weapon {2}'.format(self.name, self.life, self.weapons))
        
class weapon:
    def __init__(self, name):
        self.name = name
        self.ammo = 100
    def fire(self):
        print(self.name, 'firing..')
        self.ammo = self.ammo - 10
        print('{0} has ammo {1}'.format(self.name, self.ammo))
    def __repr__(self):
        return self.name

class board:
    def __init__(self):
       pass
    def addplayers(self, players):
        self.players = players

class game:
    def __init__(self):
        #spawn players
        self.player1 = player('player1')
        self.player2 = player('player2')
        
        #spawn weapons
        self.player1.loadweapon('Maverick')
        self.player2.loadweapon('B43')

    def play(self):
        self.player1.play()
        time.sleep(0.5)
        self.player2.play()

    def start(self):
        print('starting the game...enter the number of moves')
        n = input()
        for _ in range(n):
            self.player1.play()
            time.sleep(0.5)
            self.player2.play()

game = game()
game.start()
