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

main_menu_btn_width = 250
main_menu_btn_x = (display_width/2)-(main_menu_btn_width/2)

main_menu_sorting_btn = None
main_menu_exit_btn = None
main_menu_glossary_btn = None
main_menu_BST_btn = None
main_menu_graph_btn = None

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


# GLOSSARY TEXT ---------------------------------------------------------------

binary_tree_text1 = tiny_font.render("Binary Tree is defined as a tree data", False, white)
binary_tree_text2 = tiny_font.render(" structure where each node has at most 2 children.", False, white)
binary_tree_text3 = tiny_font.render("Since each element in a binary tree can have only 2 children, ", False, white)
binary_tree_text4 = tiny_font.render(" we typically name them the left and right child.", False, white)
binary_tree_text5 = tiny_font.render(".....", False, white)

bubble_sort_text1 = tiny_font.render(str("Bubbles"), False, white)
bubble_sort_text2 = tiny_font.render(str("Bubbles"), False, white)
bubble_sort_text3 = tiny_font.render(str("Bubbles"), False, white)
bubble_sort_text4 = tiny_font.render(str("Bubbles"), False, white)
bubble_sort_text5 = tiny_font.render(str("Bubbles"), False, white)

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

# --------------------------------------------------------------------------------
# IMAGES

# OTACON
img1 = pygame.image.load('OTACON.png')
scaled_image = pygame.transform.scale(img1, (100, 100))
img2 = pygame.image.load('24224.png')
scaled_image2 = pygame.transform.scale(img2, (100, 100))
image = scaled_image

# BUTTONS FOR COLLIDEPOINTS
sort_button1 = None
sort_button2 = None
sort_button3 = None
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
pygame.display.set_caption("Computer Bestiary")
game_exit = True
algorithm = "insertion"
speed = 0.01

glossary_screen_text1 = medium_font.render(str("...."), False, white)
glossary_screen_text2 = medium_font.render(str("...."), False, white)
glossary_screen_text3 = medium_font.render(str("...."), False, white)
glossary_screen_text4 = medium_font.render(str("...."), False, white)
glossary_screen_text5 = medium_font.render(str("...."), False, white)

node_count = 0

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



# FUNCTION FOR DRAWING THE CURRENT STATE OF THE LIST TO BE SORTED

def draw_list(list_for_sort):
    gameDisplay.fill(background_color)
    for i in range(len(list_for_sort)):
      color = list_color
      if i == current_idx:
          color = green
      elif i == comparison_idx:
          color = blue
      height = (list_for_sort[i]*10)
      pygame.draw.rect(gameDisplay, color, [(i*80), display_height-height, block_size, height])
      color = black
      if i == current_idx:
          color = green
      elif i == comparison_idx:
          color = blue
      number_text = large_font.render(str(list_for_sort[i]), False, color)
      gameDisplay.blit(number_text, ((i*80)+15, 40))
      gameDisplay.blit(image, (display_width-200, 50))
      display_algorithm()
      pygame.display.update()

def draw_menu():

    global sort_button1, sort_button2, sort_button3, speed_button1, speed_button2, speed_button3, main_menu_btn

    pygame.draw.rect(gameDisplay, display_color, [display_width-210, 160, 200, 600])

    sort_button1 = pygame.draw.rect(gameDisplay, menu_button_color, [display_width - 200, 200, 180, 50])
    sort_button2 = pygame.draw.rect(gameDisplay, menu_button_color, [display_width - 200, 260, 180, 50])
    sort_button3 = pygame.draw.rect(gameDisplay, menu_button_color, [display_width - 200, 320, 180, 50])
    
    speed_button1 = pygame.draw.rect(gameDisplay, speed_button_color, [display_width - 200, 400, 180, 50])
    speed_button2 = pygame.draw.rect(gameDisplay, speed_button_color, [display_width - 200, 460, 180, 50])
    speed_button3 = pygame.draw.rect(gameDisplay, speed_button_color, [display_width - 200, 520, 180, 50])

    main_menu_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width - 200, 700, 180, 50])

    algorithm_text = medium_font.render(str("Algorithm:"), False, black)
    speed_text = medium_font.render(str("Speed:"), False, black)

    insertion_sort_text = small_font.render(str("Insertion Sort"), False, black)
    bubble_sort_text = small_font.render(str("Bubble Sort"), False, black)
    quicksort_text = small_font.render(str("Quicksort Sort"), False, black)

    speed_button1_text = small_font.render(str("Slow"), False, black)
    speed_button2_text = small_font.render(str("Medium"), False, black)
    speed_button3_text = small_font.render(str("Fast"), False, black)

    main_menu_text = small_font.render(str("Main Menu"), False, black)

    #  BLIT TEXT TO SCREEN

    gameDisplay.blit(algorithm_text, (display_width-200, 160))

    gameDisplay.blit(insertion_sort_text, (display_width-200, 200))
    gameDisplay.blit(bubble_sort_text, (display_width-200, 260))
    gameDisplay.blit(quicksort_text, (display_width-200, 320))

    gameDisplay.blit(speed_text, (display_width-200, 360))

    gameDisplay.blit(speed_button1_text, (display_width-200, 400))
    gameDisplay.blit(speed_button2_text, (display_width-200, 460))
    gameDisplay.blit(speed_button3_text, (display_width-200, 520))

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

    
    image = scaled_image2
    draw_list(list_for_sort)
    redo_sort_button = pygame.draw.rect(gameDisplay, menu_button_color, [20, 410, 300, 40])
    gameDisplay.blit(redo_sort_text,(30, 415))



def display_main_menu():
    global main_menu_sorting_btn, main_menu_exit_btn, main_menu_glossary_btn, main_menu_BST_btn, main_menu_graph_btn

    gameDisplay.fill(background_color)

    # BLIT IMAGE
    gameDisplay.blit(image, (display_width-200, 50))

    main_menu_sorting_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 300, main_menu_btn_width, 50])
    main_menu_exit_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 700, main_menu_btn_width, 50])
    main_menu_glossary_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 600, main_menu_btn_width, 50])
    main_menu_BST_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 400, main_menu_btn_width, 50])
    main_menu_graph_btn = pygame.draw.rect(gameDisplay, menu_button_color, [main_menu_btn_x, 500, main_menu_btn_width, 50])

    main_menu_title_text = medium_font.render(str("Main Menu"), False, black)
    sorting_text = small_font.render(str("Sorting Algorithms"), False, black)
    glossary_text = small_font.render(str("Glossary"), False, black)
    exit_text = small_font.render(str("Exit"), False, black)
    bst_text = small_font.render(str("Binary Trees"), False, black)
    graph_text = small_font.render(str("Graphs"), False, black)
    
    gameDisplay.blit(main_menu_title_text, ((display_width/2)-100, 100))
    gameDisplay.blit(sorting_text, (main_menu_btn_x, 300))
    gameDisplay.blit(graph_text, (main_menu_btn_x, 500))
    gameDisplay.blit(glossary_text, (main_menu_btn_x, 600))
    gameDisplay.blit(bst_text, (main_menu_btn_x, 400))
    gameDisplay.blit(exit_text, (main_menu_btn_x, 700))
    
    pygame.display.update()

def display_algorithm():

    pygame.draw.rect(gameDisplay, display_color, [20, 170, 500, 170])

    if algorithm == "bubble":
            gameDisplay.blit(bubble_sort_algorithm, (30, 180))
            gameDisplay.blit(bubble_sort_algorithm_line1, (30, 200))
            gameDisplay.blit(bubble_sort_algorithm_line2, (30, 220))
            gameDisplay.blit(bubble_sort_algorithm_line3, (30, 240))
            gameDisplay.blit(bubble_sort_algorithm_line4, (30, 260))
            gameDisplay.blit(bubble_sort_algorithm_line5, (30, 280))

    elif algorithm == "insertion":

            gameDisplay.blit(insertion_sort_algorithm, (30, 180))
            gameDisplay.blit(insertion_sort_algorithm_line1, (30, 200))
            gameDisplay.blit(insertion_sort_algorithm_line2, (30, 220))
            gameDisplay.blit(insertion_sort_algorithm_line3, (30, 240))
            gameDisplay.blit(insertion_sort_algorithm_line4, (30, 260))
            gameDisplay.blit(insertion_sort_algorithm_line5, (30, 280))
            gameDisplay.blit(insertion_sort_algorithm_line6, (30, 300))
            gameDisplay.blit(insertion_sort_algorithm_line7, (30, 320))


def draw_glossary_buttons():

    global binary_tree_btn, bubble_sort_btn, graphs_btn, insertion_sort_btn
    
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
                        pygame.mixer.Sound.play(loaded_sound)
                        redo_sort(list_for_sort)

                    if main_menu_glossary_btn.collidepoint(pygame.mouse.get_pos()):
                        main_menu_status = False
                        glossary_mode = True
                        pygame.mixer.Sound.play(btn_click_sound)
                        pygame.mixer.Sound.play(loaded_sound)

                    if main_menu_BST_btn.collidepoint(pygame.mouse.get_pos()):
                        main_menu_status = False
                        binary_tree_mode = True
                        
                        pygame.mixer.Sound.play(btn_click_sound)
                        pygame.mixer.Sound.play(loaded_sound)

                    if main_menu_exit_btn.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.Sound.play(btn_click_sound)
                        global_loop = False
                        main_menu_status = False
                        game_exit = True
                        pygame.quit()
                        

    # GAME LOOP

    while sort_mode:

        display_algorithm()
        draw_menu()
    
        # EVENT HANDLING
            # event handling
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        loaded_sound.play()
                        redo_sort(list_for_sort)

                    if event.key == pygame.K_q:
                        game_exit == True
                        pygame.quit()

                    
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if redo_sort_button.collidepoint(pygame.mouse.get_pos()):
                        loaded_sound.play()
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
                        loaded_sound.play()
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

            add_node_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 600, 150, 50])
            add_node_text = small_font.render(str("Add Node"), False, black)
            gameDisplay.blit(add_node_text, (display_width-165, 610))

            rb_exit_btn = pygame.draw.rect(gameDisplay, menu_button_color, [display_width-170, 700, 150, 50])
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
                    if rb_exit_btn.collidepoint(pygame.mouse.get_pos()):
                        blank = True
                        node_count = 0
                        main_menu_status = True
                        binary_tree_mode = False

                    if add_node_btn.collidepoint(pygame.mouse.get_pos()):

                        root.insert(random.randrange(0, 101))


        pygame.display.update()                                 
        
pygame.quit()