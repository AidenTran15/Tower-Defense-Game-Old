import pygame


class Enemy:
    imgs = []

    def __int__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = []
        self.health = 1
        self.path = [(19, 224), (177, 235), (282, 283), (526, 277), (607, 217), (641, 105), (717, 57), (796, 83), (855, 222) (973, 284), (1046, 366), (1022, 458), (894, 502), (740, 514), (580, 552), (148, 551), (85, 452), (52, 345), (1, 335)]
        self.img = None

    def draw(self, win):
        """
        Draw the enemy with the given images
        :param win: surface
        :return: None
        """ 
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0    

        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        """
        Returns if positions has hit enemy
        :param x : int
        :param y : int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        pass

    def hit(self):
        """
        Returns if an enemy has died and remove one health
        each call
        :return: Bool
        """
        self.health -= 1 
        if self.health <= 0:
            return True