import pygame
import random


pygame.init()

# PYGAME VARIABLES

display_width = 1200
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))


# COLORS

black = (0, 0, 0)
white = (255, 255, 255)


# FONTS

small_font = pygame.font.SysFont('Monospace', 20)



# TEXT

add_node_text = small_font.render(str("Add Node"), False, black)






node_count = 0


# In our implementation, we will only use a single class, the BST Node class. Any BSTNode is technically also a full Binary Search Tree, with itself as the root node. Each method that traverses the tree will do so recursively.


class BSTNode(object):
    def exists(self, val):
        # ?
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)


        if self.right == None:
            return False
        return self.right.exists(val)
        
        

        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

    def __init__(self, val=None, parentx=None, parenty=None, parentval = None):
       

        self.left = None
        self.right = None
        self.val = val
        self.x = display_width/2
        self.y = 100
        self.parentx = parentx
        self.parenty = parenty
        self.parentval = parentval
        self.draw()
        
        



    def draw(self):
        
   
        if self.parentx is not None:
            if self.val > self.parentval:
                self.x = self.parentx + ((display_height/self.parenty)*8)
            elif self.val < self.parentval:
                self.x = self.parentx - ((display_height/self.parenty)*8)


            self.y = self.parenty + 50


        if self.y < 200:

            if self.parentx is not None:
                if self.val > self.parentval:
                    self.x = self.parentx + 250
                elif self.val < self.parentval:
                    self.x = self.parentx - 250

                self.y = self.parenty + 50

        elif self.y < 240:

            if self.parentx is not None:
                if self.val > self.parentval:
                    # self.x = self.parentx + ((display_height/self.parenty)*15)
                    self.x = self.parentx + 150
                elif self.val < self.parentval:
                    # self.x = self.parentx - ((display_height/self.parenty)*15)
                    self.x = self.parentx - 150

                self.y = self.parenty + 50

        elif self.y < 290:

            if self.parentx is not None:
                if self.val > self.parentval:
                    # self.x = self.parentx + ((display_height/self.parenty)*15)
                    self.x = self.parentx + 80
                elif self.val < self.parentval:
                    # self.x = self.parentx - ((display_height/self.parenty)*15)
                    self.x = self.parentx - 80

                self.y = self.parenty + 50

        elif self.y < 340:

            if self.parentx is not None:
                if self.val > self.parentval:
                    # self.x = self.parentx + ((display_height/self.parenty)*15)
                    self.x = self.parentx + 50
                elif self.val < self.parentval:
                    # self.x = self.parentx - ((display_height/self.parenty)*15)
                    self.x = self.parentx - 50

                self.y = self.parenty + 50


        pygame.draw.circle(gameDisplay, white, (self.x, self.y), 20)

        if self.parentx is not None:

            if self.x > self.parentx:
                pygame.draw.line(gameDisplay, white, (self.x, self.y), (self.parentx+15, self.parenty+7), 5)
            else:
                pygame.draw.line(gameDisplay, white, (self.x, self.y), (self.parentx-15, self.parenty+7), 5)
       
        node_value_text = small_font.render(str(self.val), False, black)

        if len(str(self.val)) == 1:
            offset = 6
        elif len(str(self.val)) == 2:
            offset = 12
        elif len(str(self.val)) == 3:
            offset = 18


        gameDisplay.blit(node_value_text, (self.x-offset, self.y-10))

    def insert(self, val):
        global node_count

        if node_count <=20:

            if self.val is None:
                self.val = val
                return

            if self.val == val:
                return

            elif val < self.val:
                if self.left:
                    self.left.insert(val)
                    return
                
                self.left = BSTNode(val, self.x, self.y, self.val)
                node_count += 1
                return
            
            elif val > self.val:

                if self.right:
                    self.right.insert(val)
                    return
                
                self.right = BSTNode(val, self.x, self.y, self.val)
                node_count += 1
                return
            
            


# CREATE TREE BEFORE MAIN GAME LOOP
        
root = BSTNode(random.randrange(0, 200))






while True:

    btn = pygame.draw.rect(gameDisplay, white, [display_width - 300, display_height - 200, 120, 50])
    gameDisplay.blit(add_node_text, (display_width - 290, display_height - 190))
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn.collidepoint(pygame.mouse.get_pos()):
                root.insert(random.randrange(0, 200))