class SuperMario:
    
    max_distance = 100
    
    def __init__(self, nickname):
        self.nickname = nickname
        self.coor = 0
        print('Welcome to the Super Mario game!')
        print('As the programmer is too lazy, you only have the ability to walk')
        print('But, hey, you can walk either to left or right ;)\n')
        print(self.__str__())
        
    def __str__(self):
        return f'{self.nickname} is now at x = {self.coor}\n'
        
    def move(self, distance):
        flag = self._check(distance)
        if not flag:
            self.coor += distance
            print('Succesful move!')
        else:
            print('You are trying to get too far!')
        
        print(self.__str__())
        
    def _check(self, distance):
        # if the new coordinate is illegal, return True
        # else, return None -> False
        if not (-SuperMario.max_distance <= self.coor + distance <=
                 SuperMario.max_distance):
            return True
        

player1 = SuperMario('Yiyi')
player1.move(100)
player1.move(-300)