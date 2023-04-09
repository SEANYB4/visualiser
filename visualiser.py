import pygame
import random
import time

# ---------------------------------------------------------------------------
# INITIALSATIONS

pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()

# VARIABLES

display_width = 1200
display_height = 800
FPS = 5
global_loop = True

# COLORS
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
list_color = "#7986cb"

background_color = "#00bcd4"
menu_button_color = "#D5B8F7"
speed_button_color = "#DDD888"
display_color = "#b3e0e5"
# ------------------------------------------------------------------------------

# MODES

sort_mode = False
glossary_mode = False
binary_tree_mode = False
graph_mode = False
red_black_mode = False

main_menu_btn_width = 250
main_menu_btn_x = (display_width/2)-(main_menu_btn_width/2)

main_menu_sorting_btn = None
main_menu_exit_btn = None
main_menu_glossary_btn = None
main_menu_BST_btn = None
main_menu_graph_btn = None
main_menu_red_black_trees_btn = None

# -------------------------------------------------------------------------------

# FONTS
# System Font
tiny_font = pygame.font.SysFont('Monospace', 15)
small_font = pygame.font.SysFont('Monospace', 20)
medium_font = pygame.font.SysFont('Monospace', 30)
large_font = pygame.font.SysFont('Monospace', 50)
redo_sort_text = small_font.render('Sort again', False, black)

number_text = small_font.render('0', False, black)

current_idx = 0
comparison_idx = None

# --------------------------------------------------------------------------------
# TEXT

# bubble sort text
bubble_sort_algorithm = tiny_font.render("def bubble_sort(arr):", False, black)
bubble_sort_algorithm_line1 = tiny_font.render("    n = len(arr)", False, black)
bubble_sort_algorithm_line2 = tiny_font.render("    for i in range(n):", False, black)
bubble_sort_algorithm_line3 = tiny_font.render("        for j in range(0, n-i-1): ", False, black)
bubble_sort_algorithm_line4 = tiny_font.render("            if arr[j] > arr[j+1]: ", False, black)
bubble_sort_algorithm_line5 = tiny_font.render("            arr[j], arr[j+1] = arr[j+1], arr[j]", False, black)

# insertion sort text
insertion_sort_algorithm = tiny_font.render("def insertion_sort(arr):", False, black)
insertion_sort_algorithm_line1 = tiny_font.render("    for i in range(1, len(arr)):", False, black)
insertion_sort_algorithm_line2 = tiny_font.render("    key = arr[i]", False, black)
insertion_sort_algorithm_line3 = tiny_font.render("    j = i-1: ", False, black)
insertion_sort_algorithm_line4 = tiny_font.render("    while j >= 0 and key < arr[j] :: ", False, black)
insertion_sort_algorithm_line5 = tiny_font.render("            arr[j + 1] = arr[j]", False, black)
insertion_sort_algorithm_line6 = tiny_font.render("            j -= 1", False, black)
insertion_sort_algorithm_line7 = tiny_font.render("    arr[j + 1] = key", False, black)


# GRAPH SECTION TEXT

graph_display_text_1 = tiny_font.render("....", False, white)


# BST SECTION TEXT

bst_display_text_1 = tiny_font.render("....", False, white)


# GLOSSARY TEXT ---------------------------------------------------------------

binary_tree_text1 = tiny_font.render("Binary Tree is defined as a tree data", False, white)
binary_tree_text2 = tiny_font.render(" structure where each node has at most 2 children.", False, white)
binary_tree_text3 = tiny_font.render("Since each element in a binary tree can have only 2 children, ", False, white)
binary_tree_text4 = tiny_font.render(" we typically name them the left and right child.", False, white)
binary_tree_text5 = tiny_font.render(".....", False, white)


rb_tree_text1 = tiny_font.render("A red-black tree is a kind of self-balancing binary search tree. ", False, white)
rb_tree_text2 = tiny_font.render("Each node stores an extra bit, which we will call the color, red or black.", False, white)
rb_tree_text3 = tiny_font.render("The color ensures that the tree remains approximately balanced during insertions and deletions.", False, white)
rb_tree_text4 = tiny_font.render("When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties that", False, white)
rb_tree_text5 = tiny_font.render(" constrain how unbalanced the tree can become in the worst case.", False, white)
rb_tree_text6 = tiny_font.render("Red black trees always have worst-case O(log(n)) insertions, deletions", False, white)
rb_tree_text7 = tiny_font.render(", lookups and rearrangements.", False, white)


bubble_sort_text1 = tiny_font.render(str("Bubble Sort is the simplest sorting algorithm   "), False, white)
bubble_sort_text2 = tiny_font.render(str("that works by repeatedly swapping the adjacent"), False, white)
bubble_sort_text3 = tiny_font.render(str("elements if they are in the wrong order."), False, white)
bubble_sort_text4 = tiny_font.render(str(" This algorithm is not suitable for large data sets as its "), False, white)
bubble_sort_text5 = tiny_font.render(str("average and worst-case time complexity is quite high."), False, white)

insertion_sort_text1 = tiny_font.render(str("insertion"), False, white)
insertion_sort_text2 = tiny_font.render(str("insertion"), False, white)
insertion_sort_text3 = tiny_font.render(str("insertion"), False, white)
insertion_sort_text4 = tiny_font.render(str("insertion"), False, white)
insertion_sort_text5 = tiny_font.render(str("Insertion"), False, white)

graph_text1 = tiny_font.render(str("graphs"), False, white)
graph_text2 = tiny_font.render(str("graphs"), False, white)
graph_text3 = tiny_font.render(str("graphs"), False, white)
graph_text4 = tiny_font.render(str("graphs"), False, white)
graph_text5 = tiny_font.render(str("graphs"), False, white)

merge_sort_text1 = tiny_font.render(str("merge"), False, white)
merge_sort_text2 = tiny_font.render(str("merge"), False, white)
merge_sort_text3 = tiny_font.render(str("merge"), False, white)
merge_sort_text4 = tiny_font.render(str("merge"), False, white)
merge_sort_text5 = tiny_font.render(str("merge"), False, white)

quick_sort_text1 = tiny_font.render(str("quick"), False, white)
quick_sort_text2 = tiny_font.render(str("quick"), False, white)
quick_sort_text3 = tiny_font.render(str("quick"), False, white)
quick_sort_text4 = tiny_font.render(str("quick"), False, white)
quick_sort_text5 = tiny_font.render(str("quick"), False, white)
# --------------------------------------------------------------------------------
# IMAGES

# OTACON
img1 = pygame.image.load('OTACON.png')
scaled_image = pygame.transform.scale(img1, (100, 100))
img2 = pygame.image.load('24224.png')
scaled_image2 = pygame.transform.scale(img2, (100, 100))
image = scaled_image



# TITLE

title_image = pygame.image.load('test2.png')
scaled_title = pygame.transform.scale(title_image, (400, 200))



# ---------------------------------------------------------------------------------

# BUTTONS FOR COLLIDEPOINTS
sort_button1 = None
sort_button2 = None
sort_button3 = None
sort_button4 = None
speed_button1 = None
speed_button2 = None
speed_button3 = None
main_menu_btn = None
redo_sort_button = None

# glossary btns for collide point

binary_tree_btn = None
bubble_sort_btn = None
graphs_btn = None
insertion_sort_btn = None
merge_sort_btn = None
quick_sort_btn = None

pygame.display.set_icon(img2)

# -----------------------------------------------------------------------------
# SOUNDS

# music
# pygame.mixer.music.load('main_theme.mp3')
# pygame.mixer.music.play(-1)

# sounds
loaded_sound = pygame.mixer.Sound('Loaded.mp3')
btn_click_sound = pygame.mixer.Sound('btn_click.mp3')
algo_step_sound = pygame.mixer.Sound('algo_step.mp3')

# ----------------------------------------------------------------------------------
# GENERAL

block_size = 50
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Visualiser")
game_exit = True
algorithm = "insertion"
speed = 0.01

glossary_screen_text1 = medium_font.render(str("...."), False, white)
glossary_screen_text2 = medium_font.render(str("...."), False, white)
glossary_screen_text3 = medium_font.render(str("...."), False, white)
glossary_screen_text4 = medium_font.render(str("...."), False, white)
glossary_screen_text5 = medium_font.render(str("...."), False, white)

node_count = 0


# main menu animation
main_menu_line_x = 0
main_menu_line_y = 0


line_1_y = 300
line_2_x = 500

cities = ['Glasgow', 'Manchester', 'London', 'Edinburgh', 'NewCastle', 'York', 'Liverpool', 'Leeds', 'Reading', 'Aberdeen', 'Stirling', 'Durham', 'Birmingham', 'Blackpool', 'Cardiff', 'Dublin', 'Perth', 'Dundee', 'South Hampton', 'Bristol']




def print_tree(node, lines, level=0):
    if node.val != 0:
        print_tree(node.right, lines, level + 1)
        lines.append(
            "-" * 4 * level + "> " + str(node.val) + " " + ("r" if node.red else "b")
        )
        print_tree(node.left, lines, level + 1)



# -----------------------------------------------------------------------------
# CLASSES

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

        global bst_display_text_1

        bst_display_text_1 = tiny_font.render(str("Adding node with value " + str(self.val) + '.'), False, white)
        pygame.draw.rect(gameDisplay, black, [0, 0, display_width, 60])
        gameDisplay.blit(bst_display_text_1, (50, 30))
        
        if self.parentx is not None:
            if self.val > self.parentval:
                self.x = self.parentx + ((display_height/self.parenty)*8)
            elif self.val < self.parentval:
                self.x = self.parentx - ((display_height/self.parenty)*8)
            self.y = self.parenty + 50


        # X COORDINATES FOR LEVEL 1
        if self.y < 200:

            if self.parentx is not None:
                if self.val > self.parentval:
                    self.x = self.parentx + 250
                elif self.val < self.parentval:
                    self.x = self.parentx - 250

                self.y = self.parenty + 50

        # X COORDINATES FOR LEVEL 2
        elif self.y < 240:

            if self.parentx is not None:
                if self.val > self.parentval:
                    # self.x = self.parentx + ((display_height/self.parenty)*15)
                    self.x = self.parentx + 150
                elif self.val < self.parentval:
                    # self.x = self.parentx - ((display_height/self.parenty)*15)
                    self.x = self.parentx - 150

                self.y = self.parenty + 50

        # X COORDINATES FOR LEVEL 3
        elif self.y < 290:

            if self.parentx is not None:
                if self.val > self.parentval:
                    # self.x = self.parentx + ((display_height/self.parenty)*15)
                    self.x = self.parentx + 80
                elif self.val < self.parentval:
                    # self.x = self.parentx - ((display_height/self.parenty)*15)
                    self.x = self.parentx - 80

                self.y = self.parenty + 50


        # X COORDINATES FOR LEVEL 4
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
            

# RB TREES

class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None
        self.x = None
        self.y = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        


        if parent == None:
            self.root = new_node
            new_node.x = display_width/2
            new_node.y = 100

        elif new_node.val < parent.val:
            parent.left = new_node
            new_node.x = parent.x - ((display_height/new_node.parent.y)*15)
            new_node.y = parent.y + 50
        else:
            parent.right = new_node
            new_node.x = parent.x + ((display_height/new_node.parent.y)*15)
            new_node.y = parent.y + 50





        # Fix the tree
        self.fix_insert(new_node)
        gameDisplay.fill(background_color)
        draw_rb_menu()
        self.draw_tree(self.root)
                
        pygame.display.update()

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)



        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
    


    def draw_tree(self, current):

    
        if (current is None) or current == self.nil:
            return
        
        

        # choose color
        color = black
        if current.red:
            color = red

        # draw connections
        if current.right is not None and current.right != self.nil:
            pygame.draw.line(gameDisplay, black, (current.x, current.y), (current.right.x, current.right.y), 5)

        if current.left is not None and current.left != self.nil:
            pygame.draw.line(gameDisplay, black, (current.x, current.y), (current.left.x, current.left.y), 5)
        
        # draw circle
        pygame.draw.circle(gameDisplay, color, (current.x, current.y), 20)

        # draw value
        node_val = tiny_font.render(str(current.val), False, white)
        gameDisplay.blit(node_val, (current.x, current.y))

        # if (current.left is not None) and (current.left is not self.nil):
        self.draw_tree(current.left)

        # if (current.right is not None) and (current.left is not self.nil):
        self.draw_tree(current.right)



    def move_nodes_after_left_rotation(self, x, y):

        if x == None:
            return
        else:
            self.move_nodes_down_left_rotation(x)
            
        if y == None:
            return
        else:
            
            self.move_nodes_up_left_rotation(y, first_rotation=True)



    def move_nodes_up_left_rotation(self, y, first_rotation=False):
        if y == None:
            return
        
        if y.parent is not None:
            if y is not self.root:
                y.y = y.parent.y + 50
            if y.val > y.parent.val:
                y.x = y.parent.x + ((display_height/y.parent.y)*15)
            else:
                y.x = y.parent.x - ((display_height/y.parent.y)*15)
        self.move_nodes_up_left_rotation(y.right)
        if first_rotation == False:
            self.move_nodes_up_left_rotation(y.left)
    
    def move_nodes_down_left_rotation(self, x):
        if x == None:
            return
        
        if x.parent is not None:
            if x is not self.root:
                x.y = x.parent.y + 50
            if x.val > x.parent.val:
                x.x = x.parent.x + ((display_height/x.parent.y)*15)
            else:
                x.x = x.parent.x - ((display_height/x.parent.y)*15)
        self.move_nodes_down_left_rotation(x.left)
        self.move_nodes_down_left_rotation(x.right)


    def move_nodes_up_right_rotation(self, y, first_rotation=False):
        if y == None:
            return
        
        if y.parent is not None:
            if y is not self.root:
                y.y = y.parent.y + 50
            if y.val > y.parent.val:   
                y.x = y.parent.x + ((display_height/y.parent.y)*15)
            else:
                y.x = y.parent.x - ((display_height/y.parent.y)*15)


        self.move_nodes_up_right_rotation(y.left)
        if first_rotation == False:
            self.move_nodes_up_right_rotation(y.right)
    
    def move_nodes_down_right_rotation(self, x):
        if x == None:
            return
        if x.parent is not None:
            if x is not self.root:
                x.y = x.parent.y + 50
            if x.val > x.parent.val:     
                x.x = x.parent.x + ((display_height/x.parent.y)*15)
            else:
                x.x = x.parent.x - ((display_height/x.parent.y)*15)
        self.move_nodes_down_right_rotation(x.right)
        self.move_nodes_down_right_rotation(x.left)

    def move_nodes_after_right_rotation(self, x, y):

        if x == None:
            return
        else:
            self.move_nodes_down_right_rotation(x)
            
        if y == None:
            return
        else:
            
            self.move_nodes_up_right_rotation(y, first_rotation=True)
            
        
        
        


    # rotate left at node x
    def rotate_left(self, x):
        print('rotate left' + str(x.val))
        y = x.right
        # switch coordinates
        y.x = x.x
        y.y = y.y
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
            
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        
        x.parent = y
        self.move_nodes_after_left_rotation(x, y)


# HAK        
        self.root.y = 100
        self.root.left.x = 200
        self.root.right.x = 1000
        self.root.right.left.x = 900
        self.root.right.right.x = 1100
        self.root.left.left.x = 100
        self.root.left.right.x = 300

    # rotate right at node x
    def rotate_right(self, x):
        print('rotate right' + str(x.val))
        y = x.left
        y.x = x.x
        y.y = y.y
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        
        x.parent = y
        self.move_nodes_after_right_rotation(x, y)

# HAK

        self.root.y = 100
        self.root.left.x = 200
        self.root.right.x = 1000
        self.root.right.left.x = 900
        self.root.right.right.x = 1100
        self.root.left.left.x = 100
        self.root.left.right.x = 300

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return "\n".join(lines)


     

#  GRAPH

class Graph:
    def __init__(self):
        self.graph = {}
        self.cords = {}
        self.draw()
    
    def add_edge(self, u, v):
        global graph_display_text_1
        graph_display_text_1 = tiny_font.render(str("Adding edge bewteen " + str(u) + ' and ' + str(v) + '.'), False, white)
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = set()
            
            self.cords[u] = (random.randrange(100, display_width-100), random.randrange(100, display_height-100))
            self.graph[u].add(v)

        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = set()
            
            self.cords[v] = (random.randrange(100, display_width-100), random.randrange(100, display_height-100))
            self.graph[v].add(u)

        self.draw()


    def draw(self):

        gameDisplay.fill(background_color)

        pygame.draw.rect(gameDisplay, black, [0, 0, display_width, 60])
        gameDisplay.blit(graph_display_text_1, (50, 30))

        for i in self.cords:
            for j in self.graph[i]:
                pygame.draw.line(gameDisplay, black, (self.cords[i][0], self.cords[i][1]), (self.cords[j][0], self.cords[j][1]), 5)
            
        for i in self.cords:
            pygame.draw.circle(gameDisplay, white, (self.cords[i][0], self.cords[i][1]), 30)

            node_text = tiny_font.render(str(i), False, black)
            gameDisplay.blit(node_text, (self.cords[i][0]-30, self.cords[i][1]-10))

            



        # BUTTONS

            add_node_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 600, 150, 50])
            add_node_text = small_font.render(str("Add Node"), False, black)
            gameDisplay.blit(add_node_text, (display_width-165, 610))

            graph_exit_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 700, 150, 50])
            main_menu_text = small_font.render(str("Main menu"), False, black)
            gameDisplay.blit(main_menu_text, (display_width-165, 710))



        pygame.display.update()











# -------------------------------------------------------------------------------
# FUNCTIONS

# SORTING

# QUICKSORT

def quicksort(nums, low, high):

    if low < high:
        nums, p = partition(nums, low, high)
        draw_list(nums)
        time.sleep(speed)
        nums = quicksort(nums, low, p-1)
        nums = quicksort(nums, p+1, high)
    return nums


def partition(nums, low, high):
    global current_idx
    global comparison_idx
    pivot = nums[high]
    comparison_idx = pivot
    i = low
    j = low
    while j < high:
        current_idx = j
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            draw_list(nums)
            time.sleep(speed)
            i += 1
        j += 1

    nums[i], nums[high] = nums[high], nums[i]
    draw_list(nums)
    time.sleep(speed)
    return nums, i


#  INSERTION SORT

def insertion_sort(nums):
    global current_idx
    global comparison_idx
    for i in range(0, len(nums)):
        current_idx = i
        j = 0
        draw_list(nums)
        time.sleep(speed)

        while j < i:
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
            comparison_idx = j
            draw_list(nums)
            time.sleep(speed)
                
    return nums


# BUBBLE SORT

def bubble_sort(nums):
    global current_idx
    global comparison_idx
    sorting = True
    while sorting:
        sorting = False
        for i in range(1, len(nums)):
            time.sleep(speed)
            current_idx = i
            comparison_idx = (i-1)
            draw_list(nums)
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                sorting = True
    draw_list(nums)
    
    return nums


# MERGE SORT

def mergesort(nums):
    if len(nums) < 2:
        return nums
    else:
        mid = len(nums) // 2
        first = mergesort(nums[:mid])
        second = mergesort(nums[mid:])
        return merge(first, second)
    
def merge(first, second):
    final = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1

    return final

        


# FUNCTION FOR DRAWING THE CURRENT STATE OF THE LIST TO BE SORTED

def draw_list(list_for_sort):
    gameDisplay.fill(background_color)
    gameDisplay.blit(image, (display_width-200, 50))
    for i in range(len(list_for_sort)):
      color = list_color
      if i == current_idx:
          color = green
      elif i == comparison_idx:
          color = blue
      height = (list_for_sort[i]*10)
      pygame.draw.rect(gameDisplay, color, [(i*80)+20, display_height-height, block_size, height])
      color = black
      if i == current_idx:
          color = green
      elif i == comparison_idx:
          color = blue
      number_text = large_font.render(str(list_for_sort[i]), False, color)
      gameDisplay.blit(number_text, (((i*80)-5)+20, 300))
      
      display_algorithm()
      pygame.display.update()

def draw_sort_menu():

    global sort_button1, sort_button2, sort_button3, sort_button4, speed_button1, speed_button2, speed_button3, main_menu_btn

    pygame.draw.rect(gameDisplay, display_color, [display_width-210, 160, 200, 600])

    sort_button1 = pygame.draw.rect(gameDisplay, menu_button_color, [display_width - 200, 200, 180, 50])
    sort_button2 = pygame.draw.rect(gameDisplay, menu_button_color, [display_width - 200, 260, 180, 50])
    sort_button3 = pygame.draw.rect(gameDisplay, menu_button_color, [display_width - 200, 320, 180, 50])
    sort_button4 = pygame.draw.rect(gameDisplay, menu_button_color, [display_width - 200, 380, 180, 50])


    speed_button1 = pygame.draw.rect(gameDisplay, speed_button_color, [display_width - 200, 500, 180, 50])
    speed_button2 = pygame.draw.rect(gameDisplay, speed_button_color, [display_width - 200, 560, 180, 50])
    speed_button3 = pygame.draw.rect(gameDisplay, speed_button_color, [display_width - 200, 620, 180, 50])

    main_menu_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width - 200, 700, 180, 50])

    algorithm_text = medium_font.render(str("Algorithm:"), False, black)
    speed_text1 = medium_font.render(str("Visualiser"), False, black)
    speed_text2 = medium_font.render(str("Speed:"), False, black)

    insertion_sort_text = small_font.render(str("Insertion Sort"), False, black)
    bubble_sort_text = small_font.render(str("Bubble Sort"), False, black)
    quicksort_text = small_font.render(str("Quicksort Sort"), False, black)
    merge_sort_text = small_font.render(str("Merge Sort"), False, black)

    speed_button1_text = small_font.render(str("Slow"), False, black)
    speed_button2_text = small_font.render(str("Medium"), False, black)
    speed_button3_text = small_font.render(str("Fast"), False, black)

    main_menu_text = small_font.render(str("Main Menu"), False, black)

    #  BLIT TEXT TO SCREEN

    gameDisplay.blit(algorithm_text, (display_width-200, 160))

    gameDisplay.blit(insertion_sort_text, (display_width-200, 200))
    gameDisplay.blit(bubble_sort_text, (display_width-200, 260))
    gameDisplay.blit(quicksort_text, (display_width-200, 320))
    gameDisplay.blit(merge_sort_text, (display_width-200, 380))

    gameDisplay.blit(speed_text1, (display_width-200, 440))
    gameDisplay.blit(speed_text2, (display_width-200, 460))

    gameDisplay.blit(speed_button1_text, (display_width-200, 500))
    gameDisplay.blit(speed_button2_text, (display_width-200, 560))
    gameDisplay.blit(speed_button3_text, (display_width-200, 620))

    gameDisplay.blit(main_menu_text, (display_width-200, 700))

    
#  REDO SORT

def redo_sort(list_for_sort):
    global image, redo_sort_button
    display_algorithm()
    image = scaled_image
    list_for_sort = [random.randrange(0, 40) for i in range(0, 10)]
    draw_list(list_for_sort)
    
    if algorithm == "insertion":
        list_for_sort = insertion_sort(list_for_sort)
    elif algorithm == "bubble":
        list_for_sort = bubble_sort(list_for_sort)
    elif algorithm == "quicksort":
        list_for_sort = quicksort(list_for_sort, 0, len(list_for_sort)-1)
    elif algorithm == "mergesort":
        list_for_sort = mergesort(list_for_sort)

    
    image = scaled_image2
    draw_list(list_for_sort)
    redo_sort_button = pygame.draw.rect(gameDisplay, menu_button_color, [560, 50, 170, 170])
    gameDisplay.blit(redo_sort_text,(570, 60))



def display_main_menu():
    global main_menu_sorting_btn, main_menu_exit_btn, main_menu_glossary_btn, main_menu_BST_btn, main_menu_graph_btn, main_menu_line_x, main_menu_line_y, main_menu_red_black_trees_btn, line_1_y, line_2_x

    gameDisplay.fill(background_color)


    
    if main_menu_line_x <= display_width:
        main_menu_line_x += 10
    else:
        main_menu_line_x = 0
        line_1_y = random.randrange(10, display_height - 100)


    if main_menu_line_y <= display_height:
        main_menu_line_y += 10
    else:
        main_menu_line_y = 0
        line_2_x = random.randrange(10, display_width-100)
    

    

    pygame.draw.line(gameDisplay, white, (0, line_1_y), (main_menu_line_x, line_1_y), 10)
    pygame.draw.line(gameDisplay, white, (line_2_x, 0), (line_2_x, main_menu_line_y), 10)

    # BLIT IMAGE
    gameDisplay.blit(image, (display_width-200, 50))
    gameDisplay.blit(scaled_title, (display_width/2, 20))

    main_menu_sorting_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 200, main_menu_btn_width, 50])
    main_menu_exit_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 700, main_menu_btn_width, 50])
    main_menu_glossary_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 600, main_menu_btn_width, 50])
    main_menu_BST_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 300, main_menu_btn_width, 50])
    main_menu_graph_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 500, main_menu_btn_width, 50])
    main_menu_red_black_trees_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 400, main_menu_btn_width, 50])

    main_menu_title_text = large_font.render(str("Main Menu"), False, black)
    sorting_text = small_font.render(str("Sorting Algorithms"), False, black)
    glossary_text = small_font.render(str("Glossary"), False, black)
    exit_text = small_font.render(str("Exit"), False, black)
    bst_text = small_font.render(str("Binary Trees"), False, black)
    graph_text = small_font.render(str("Graphs"), False, black)
    rbt_text = small_font.render(str("Red Black Trees"), False, black)
    
    gameDisplay.blit(main_menu_title_text, ((display_width/2)-135, 80))
    gameDisplay.blit(sorting_text, (main_menu_btn_x + 10, 212))
    gameDisplay.blit(graph_text, (main_menu_btn_x + 10, 512))
    gameDisplay.blit(glossary_text, (main_menu_btn_x + 10, 612))
    gameDisplay.blit(bst_text, (main_menu_btn_x + 10, 312))
    gameDisplay.blit(rbt_text, (main_menu_btn_x + 10, 412))
    gameDisplay.blit(exit_text, (main_menu_btn_x + 10, 712))
    
    pygame.display.update()

def display_algorithm():

    pygame.draw.rect(gameDisplay, display_color, [20, 50, 500, 170])

    if algorithm == "bubble":
            gameDisplay.blit(bubble_sort_algorithm, (30, 60))
            gameDisplay.blit(bubble_sort_algorithm_line1, (30, 80))
            gameDisplay.blit(bubble_sort_algorithm_line2, (30, 100))
            gameDisplay.blit(bubble_sort_algorithm_line3, (30, 120))
            gameDisplay.blit(bubble_sort_algorithm_line4, (30, 140))
            gameDisplay.blit(bubble_sort_algorithm_line5, (30, 160))

    elif algorithm == "insertion":

            gameDisplay.blit(insertion_sort_algorithm, (30, 60))
            gameDisplay.blit(insertion_sort_algorithm_line1, (30, 80))
            gameDisplay.blit(insertion_sort_algorithm_line2, (30, 100))
            gameDisplay.blit(insertion_sort_algorithm_line3, (30, 120))
            gameDisplay.blit(insertion_sort_algorithm_line4, (30, 140))
            gameDisplay.blit(insertion_sort_algorithm_line5, (30, 160))
            gameDisplay.blit(insertion_sort_algorithm_line6, (30, 180))
            gameDisplay.blit(insertion_sort_algorithm_line7, (30, 200))


def draw_glossary_buttons():

    global binary_tree_btn, bubble_sort_btn, graphs_btn, insertion_sort_btn, merge_sort_btn, quick_sort_btn
    
    gameDisplay.blit(image, (display_width-200, 50))
    
    # BINARY TREES

    binary_tree_btn = pygame.draw.rect(gameDisplay, green, [170, 50, 120, 120])
    binary_tree_label = small_font.render("Binary", False, black)
    binary_tree_label2 = small_font.render("Tree", False, black)
    gameDisplay.blit(binary_tree_label, (180, 70))
    gameDisplay.blit(binary_tree_label2, (180, 90))


    # BUBBLE SORT

    bubble_sort_btn = pygame.draw.rect(gameDisplay, green, [370, 50, 120, 120])
    bubble_sort_label1 = small_font.render("Bubble", False, black)
    bubble_sort_label2 = small_font.render("Sort", False, black)
    
    gameDisplay.blit(bubble_sort_label1, (380, 70))
    gameDisplay.blit(bubble_sort_label2, (380, 90))
    

    # GRAPHS

    graphs_btn = pygame.draw.rect(gameDisplay, green, [570, 50, 120, 120])
    graphs_label = small_font.render("Graphs", False, black)
    gameDisplay.blit(graphs_label, (580, 70))
    
    # insertion_sort

    insertion_sort_btn = pygame.draw.rect(gameDisplay, green, [770, 50, 120, 120])
    insertion_sort_label1 = small_font.render("Insertion", False, black)
    insertion_sort_label2 = small_font.render("Sort", False, black)
    gameDisplay.blit(insertion_sort_label1, (780, 70))
    gameDisplay.blit(insertion_sort_label2, (780, 90))


    # merge sort

    merge_sort_btn = pygame.draw.rect(gameDisplay, green, [170, 630, 120, 120])
    merge_sort_label1 = small_font.render("Merge", False, black)
    merge_sort_label2 = small_font.render("Sort", False, black)
    gameDisplay.blit(merge_sort_label1, [180, 650])
    gameDisplay.blit(merge_sort_label2, [180, 670])


    # insertion sort

    quick_sort_btn = pygame.draw.rect(gameDisplay, green, [370, 630, 120, 120])
    quick_sort_label1 = small_font.render("Quick", False, black)
    quick_sort_label2 = small_font.render("Sort", False, black)
    gameDisplay.blit(quick_sort_label1, [380, 650])
    gameDisplay.blit(quick_sort_label2, [380, 670])




def draw_rb_menu():

    global add_node_btn, red_black_exit_btn

    add_node_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 600, 150, 50])
    add_node_text = small_font.render(str("Add Node"), False, black)
    gameDisplay.blit(add_node_text, (display_width-165, 610))

    red_black_exit_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 700, 150, 50])
    main_menu_text = small_font.render(str("Main menu"), False, black)
    gameDisplay.blit(main_menu_text, (display_width-165, 710))


# INITIAL SETUP

list_for_sort = [random.randrange(0, 50) for i in range(0, 10)]


# GLOBAL LOOP

while global_loop:

    # MAIN MENU LOOP

    main_menu_status = True


    while main_menu_status:
        

        display_main_menu()
        # EVENT HANDLING
        # event handling
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if main_menu_sorting_btn.collidepoint(pygame.mouse.get_pos()):
                        main_menu_status = False
                        sort_mode = True
                        pygame.mixer.Sound.play(btn_click_sound)
                        # pygame.mixer.Sound.play(loaded_sound)
                        redo_sort(list_for_sort)

                    if main_menu_glossary_btn.collidepoint(pygame.mouse.get_pos()):
                        main_menu_status = False
                        glossary_mode = True
                        pygame.mixer.Sound.play(btn_click_sound)
                        # pygame.mixer.Sound.play(loaded_sound)

                    if main_menu_BST_btn.collidepoint(pygame.mouse.get_pos()):
                        main_menu_status = False
                        binary_tree_mode = True
                        
                        pygame.mixer.Sound.play(btn_click_sound)
                        # # pygame.mixer.Sound.play(loaded_sound)


                    if main_menu_red_black_trees_btn.collidepoint(pygame.mouse.get_pos()):
                        main_menu_status = False
                        red_black_mode = True
                        pygame.mixer.Sound.play(btn_click_sound)


                    if main_menu_graph_btn.collidepoint(pygame.mouse.get_pos()):
                        main_menu_status = False
                        graph_mode = True
                        pygame.mixer.Sound.play(btn_click_sound)


                    if main_menu_exit_btn.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(btn_click_sound)
                        global_loop = False
                        main_menu_status = False
                        game_exit = True
                        pygame.quit()
                        

    # GAME LOOP

    while sort_mode:

        display_algorithm()
        draw_sort_menu()
    
        # EVENT HANDLING
            # event handling
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # loaded_sound.play()
                        redo_sort(list_for_sort)

                    if event.key == pygame.K_q:
                        game_exit == True
                        pygame.quit()

                    
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if redo_sort_button.collidepoint(pygame.mouse.get_pos()):
                        # loaded_sound.play()
                        redo_sort(list_for_sort)

                    if sort_button1.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(btn_click_sound)
                        print("insertion click")
                        algorithm = "insertion"

                    if sort_button2.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(btn_click_sound)
                        print("bubble click")
                        algorithm = "bubble"

                    if sort_button3.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(btn_click_sound)
                        print("Quicksort click")
                        algorithm = "quicksort"

                    if sort_button4.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(btn_click_sound)
                        print("Mergesort click")
                        algorithm = "mergesort"

                    if speed_button1.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(btn_click_sound)
                        print('Slow')
                        speed = 0.3

                    if speed_button2.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(btn_click_sound)
                        print('Medium')
                        speed = 0.1
                        
                    if speed_button3.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(btn_click_sound)
                        print('Fast')
                        speed = 0.01

                    if main_menu_btn.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(btn_click_sound)
                        print("Main Menu")
                        game_exit = True
                        sort_mode = False
                        main_menu_status = True
        
        pygame.display.update()

   
    while glossary_mode:
        

        gameDisplay.fill(background_color)

        # MAIN SCREEN
        pygame.draw.rect(gameDisplay, black, [200, 200, 800, 400])
        
        draw_glossary_buttons()
        
        glossary_exit_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 700, 150, 50])

        main_menu_text = small_font.render(str("Main menu"), False, black)
        gameDisplay.blit(main_menu_text, (display_width-165, 710))


        # EVENT HANDLING
            # event handling
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # loaded_sound.play()
                        redo_sort(list_for_sort)

                    if event.key == pygame.K_q:
                        game_exit == True
                        pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
            
                    if glossary_exit_btn.collidepoint(pygame.mouse.get_pos()):
                        
                        main_menu_status = True
                        glossary_mode = False

                    if binary_tree_btn.collidepoint(pygame.mouse.get_pos()):
                        glossary_screen_text1 = binary_tree_text1
                        glossary_screen_text2 = binary_tree_text2
                        glossary_screen_text3 = binary_tree_text3
                        glossary_screen_text4 = binary_tree_text4
                        glossary_screen_text5 = binary_tree_text5


                    if bubble_sort_btn.collidepoint(pygame.mouse.get_pos()):
                        glossary_screen_text1 = bubble_sort_text1
                        glossary_screen_text2 = bubble_sort_text2
                        glossary_screen_text3 = bubble_sort_text3
                        glossary_screen_text4 = bubble_sort_text4
                        glossary_screen_text5 = bubble_sort_text5


                    if insertion_sort_btn.collidepoint(pygame.mouse.get_pos()):
                        glossary_screen_text1 = insertion_sort_text1
                        glossary_screen_text2 = insertion_sort_text2
                        glossary_screen_text3 = insertion_sort_text3
                        glossary_screen_text4 = insertion_sort_text4
                        glossary_screen_text5 = insertion_sort_text5


                    if graphs_btn.collidepoint(pygame.mouse.get_pos()):
                        glossary_screen_text1 = graph_text1
                        glossary_screen_text2 = graph_text2
                        glossary_screen_text3 = graph_text3
                        glossary_screen_text4 = graph_text4
                        glossary_screen_text5 = graph_text5


                    if merge_sort_btn.collidepoint(pygame.mouse.get_pos()):
                        glossary_screen_text1 = merge_sort_text1
                        glossary_screen_text2 = merge_sort_text2
                        glossary_screen_text3 = merge_sort_text3
                        glossary_screen_text4 = merge_sort_text4
                        glossary_screen_text5 = merge_sort_text5


                    if quick_sort_btn.collidepoint(pygame.mouse.get_pos()):
                        glossary_screen_text1 = quick_sort_text1
                        glossary_screen_text2 = quick_sort_text2
                        glossary_screen_text3 = quick_sort_text3
                        glossary_screen_text4 = quick_sort_text4
                        glossary_screen_text5 = quick_sort_text5
                            
        # TEMPORARY TEXT FOR GLOSSARY SCREEN
        
        gameDisplay.blit(glossary_screen_text1, [250, 300])
        gameDisplay.blit(glossary_screen_text2, [250, 320])
        gameDisplay.blit(glossary_screen_text3, [250, 340])                
        gameDisplay.blit(glossary_screen_text4, [250, 360])
        gameDisplay.blit(glossary_screen_text5, [250, 380])
        pygame.display.update()

    # variable for stopping the tree being drawn continuously
    blank = True

    while binary_tree_mode:
        

        if blank == True:
 
            gameDisplay.fill(background_color)
            root = BSTNode(random.randrange(0, 200))

            # BUTTONS

            draw_rb_menu()

            blank = False

        # EVENT HANDLING
            # event handling
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rb_exit_btn.collidepoint(pygame.mouse.get_pos()):
                        blank = True
                        node_count = 0
                        main_menu_status = True
                        binary_tree_mode = False

                    if add_node_btn.collidepoint(pygame.mouse.get_pos()):

                        root.insert(random.randrange(0, 101))

        pygame.display.update()
    while graph_mode:
        graph_display_text_1 = tiny_font.render(str('.....'), False, white)

        if blank == True:
 
            gameDisplay.fill(background_color)
            root = Graph()

            # BUTTONS

            add_node_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 600, 150, 50])
            add_node_text = small_font.render(str("Add Node"), False, black)
            gameDisplay.blit(add_node_text, (display_width-165, 610))

            graph_exit_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 700, 150, 50])
            main_menu_text = small_font.render(str("Main menu"), False, black)
            gameDisplay.blit(main_menu_text, (display_width-165, 710))

            blank = False

        # EVENT HANDLING
            # event handling
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if graph_exit_btn.collidepoint(pygame.mouse.get_pos()):
                        
                        main_menu_status = True
                        graph_mode = False

                    if add_node_btn.collidepoint(pygame.mouse.get_pos()):

                        root.add_edge(cities[random.randrange(0, len(cities))], cities[random.randrange(0, len(cities))])

        pygame.display.update()



    rb_tree = RBTree()
    blank = True
    while red_black_mode:

        if blank:

            gameDisplay.fill(background_color)
            
            # BUTTONS

            add_node_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 600, 150, 50])
            add_node_text = small_font.render(str("Add Node"), False, black)
            gameDisplay.blit(add_node_text, (display_width-165, 610))

            red_black_exit_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 700, 150, 50])
            main_menu_text = small_font.render(str("Main menu"), False, black)
            gameDisplay.blit(main_menu_text, (display_width-165, 710))

            blank = False

         # EVENT HANDLING
            # event handling
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if red_black_exit_btn.collidepoint(pygame.mouse.get_pos()):
                        
                        main_menu_status = True
                        red_black_mode = False
                        blank = True

                    if add_node_btn.collidepoint(pygame.mouse.get_pos()):

                        val = random.randrange(0, 200)
                        
                        rb_tree.insert(val)
                        print(rb_tree)
                        for i in range(5):
                            print('\n')


        pygame.display.update()                                 
        
pygame.quit()