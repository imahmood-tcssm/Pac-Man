from processing import *
import random
# test change
# [(3, 9), (3, 7)]

board = [["w", "w", "w", "w", "w", "w", "w", "w", "w"],
         ["w", "P", "p", "p", "P", "p", "p", "P", "w"],
         ["w", "p", "w", "p", "p", "p", "w", "p", "w"],
         ["w", "p", "w", "p", "p", "p", "w", "p", "w"],
         ["w", "p", "w", "w", "pl", "w", "w", "p", "w"],
         ["w", "p", "w", "w", "p", "w", "w", "p", "w"],
         ["w", "p", "p", "p", "p", "p", "p", "p", "w"],
         ["w", "p", "w", "w", "b", "w", "w", "p", "w"],
         ["w", "p", "w", " ", "blinky", " ", "w", "p", "w"],
         [" ", "P", "w", "inky", "pinky", "clyde", "w", "P", " "],
         ["w", "p", "w", " ", " ", " ", "w", "p", "w"],
         ["w", "p", "w", "w", "w", "w", "w", "p", "w"],
         ["w", "p", "p", "p", "p", "p", "p", "p", "w"],
         ["w", "p", "w", "w", "p", "w", "w", "p", "w"],
         ["w", "p", "w", "w", "p", "w", "w", "p", "w"],
         ["w", "p", "w", "p", "p", "p", "w", "p", "w"],
         ["w", "p", "w", "p", "p", "p", "w", "p", "w"],
         ["w", "P", "p", "p", "P", "p", "p", "P", "w"],
         ["w", "w", "w", "w", "w", "w", "w", "w", "w"]]
         
img0 = None
img1 = None
img2 = None
img3 = None
img4 = None
plRow = 4
plCol = 4
clydeRow = 10
clydeCol = 6
clydeDir = "l"
clydeCur = " "
pinkyRow = 10
pinkyCol = 5
pinkyDir = "u"
pinkyCur = " "
inkyRow = 10
inkyCol = 4
inkyDir = "r"
inkyCur = " "
blinkyRow = 9
blinkyCol = 5
blinkyDir = "u"
blinkyCur = " "
score = 0
start = 0
ghosts = {}
game = {}
super_time = 10
game_over = False
super_begin = 0

def setup():
  global img0, img1, img2, img3, img4, img5, img6, updateGhostCoords
  size(700, 550)
  img0 = loadImage("pm.png")
  img1 = loadImage("inky.png")
  img2 = loadImage("blinky.png")
  img3 = loadImage("clyde.png")
  img4 = loadImage("pinky.png")
  img5 = loadImage("cap.png")
  img6 = loadImage("vul.gif")
  class Ghost:
    def __init__(self, col, row, dirn, behind, img, name):
      self.col = col
      self.row = row
      self.dirn = dirn
      self.behind = behind
      self.bLoc = (col, row)
      self.img = img
      self.vulnerable = img6
      self.backHome = img5
      self.cur = img
      self.mode = "n"
      self.x = 0
      self.y = 0
      # print ("setup")
  ghosts['blinky'] = Ghost(4, 8, "n", " ", img2, "blinky")
  ghosts['pinky'] = Ghost(4, 9, "n", " ", img4, "pinky")
  ghosts['inky'] = Ghost(3, 9, "e", " ", img1, "inky")
  ghosts['clyde'] = Ghost(5, 9, "w", " ", img3, "clyde")
  game["isSuper"] = False
  def updateGhostCoords(ghost):
    global ghosts
    print ('ran')
    def getXCoord(ghost):
      print ('getting X coords')
      return 78 * (ghosts[ghost].col) + 39
    def getYCoord(ghost):
      print('get Y coords')
      return 28 * (ghosts[ghost].row) + 14
    ghosts[ghost].x = getXCoord(ghost)
    ghosts[ghost].y = getYCoord(ghost)
    print("got coordinates")
    print("row: ", ghosts[ghost].row, "col: ", ghosts[ghost].col)
    print(ghost, ghosts[ghost].x, ghosts[ghost].y)

def draw():
  global start, game_over
  background(0)
  # print (ghosts)
  if frameCount - super_begin > 450:
    # print("here")
    stopSuper()
  now = millis()
  def check():
    for ghost in ghosts:
      if ghosts[ghost].behind == "pl":
        if ghosts[ghost].bLoc != (plCol, plRow):
          ghosts[ghost].behind = " "
  check()
  if abs(now - start) > 500:
    # print("ran")
    start = now
    # if game["isSuper"]:
    #   run_away()
    # else:
    move_ghosts()
    
  y = 0
  for row in board:
    x = 0
    for el in row:
      if el == "w":
        fill(0, 0, 255)
        rect(x, y, 78, 28)
      elif el == "p":
        fill(255, 255, 0)
        ellipse(x + 36, y + 16, 15, 15)
      elif el == "P":
        fill(255, 255, 0)
        fill(255, 0, 0)
        fill(255, 255, 0)
        ellipse(x + 36, y + 16, 22, 22)
      elif el == "pl":
        image(img0, x + 22, y + 2, 28, 28)
      elif el == "inky":
        if ghosts["inky"].mode == "c":
          image(img5, ghosts['inky'].x, ghosts['inky'].y, 35, 35)
        else:
          image(ghosts["inky"].cur, x + 25, y + -1, 38, 38)
      elif el == "pinky":
        if ghosts["pinky"].mode == "c":
          image(img5, ghosts['pinky'].x, ghosts['pinky'].y, 35, 35)
        else:
          image(ghosts["pinky"].cur, x + 23, y + -1, 31, 31)
      elif el == "clyde":
        if ghosts['clyde'].mode == "c":
          image(img5, ghosts['clyde'].x, ghosts['clyde'].y, 35, 35)
        else:
          image(ghosts["clyde"].cur, x + 25, y + -3, 32, 32)
      elif el == "blinky":
        if ghosts["blinky"].mode == "c":
          image(img5, ghosts["blinky"].x, ghosts['blinky'].y, 35, 35)
        else:
          image(ghosts["blinky"].cur, x + 20, y + -3, 37, 37)
      x += 78
    y += 28
  if game_over == True:
    fill(255, 255, 255)
    textSize(50)
    text("GAME OVER", 200, 280)
    exit()
  fill(255, 255, 255)
  textSize(20)
  text(str(score), 32, 20)

def goSuper():
  global super_begin
  super_begin = frameCount
  game["isSuper"] = True
  for ghost in ghosts:
    ghosts[ghost].cur = img6
    ghosts[ghost].mode = "v"
  
def stopSuper():
    game["isSuper"] = False
    for ghost in ghosts:
      ghosts[ghost].cur = ghosts[ghost].img
      ghosts[ghost].mode = "n"

def keyPressed():
  global plRow, plCol, score, game
  if keyCode == UP:
    if plRow != 0 and (board[plRow - 1][plCol] != "w" and board[plRow - 1][plCol] != "b"):
      #valid move
      if (game["isSuper"]) and ( board[plRow -1][plCol] not in ["p", "P", " ", "b", "pl"]  ): # is a ghost
        # hit ghost
        ghosts[board[plRow -1][plCol]].cur = img5
        ghosts[board[plRow -1][plCol]].mode = "c"
        updateGhostCoords(board[plRow -1][plCol])

      if board[plRow -1][plCol] == "P":
        goSuper()
      board[plRow][plCol] = " "
      plRow -= 1
      if board[plRow][plCol] == "p":
        score += 50
      board[plRow][plCol] = "pl"
  if keyCode == DOWN: 
    if board[plRow + 1][plCol] != "b" and plRow != 0 and (board[plRow + 1][plCol] != "w" and board[plRow + 1][plCol] != "b"):
      board[plRow][plCol] = " "
      plRow += 1
      if board[plRow][plCol] == "p":
        score += 50
      if board[plRow][plCol] == "P":
        goSuper()
      board[plRow][plCol] = "pl"
      if (game["isSuper"]) and ( board[plRow +1][plCol] not in ["p", "P", " ", "b", "pl", "w"] ):
        ghosts[board[plRow + 1][plCol]].cur = img5
        ghosts[board[plRow + 1][plCol]].mode = "c"
        updateGhostCoords(board[plRow +1][plCol])
  if keyCode == RIGHT: 
    try:
      if board[plRow][plCol + 1] != "w":
        board[plRow][plCol] = " "
        plCol += 1
        if board[plRow][plCol] == "p":
          score += 50
        if board[plRow][plCol] == "P":
          goSuper()
        board[plRow][plCol] = "pl"
      if (game["isSuper"]) and ( board[plRow][plCol] not in ["p", "P", " ", "b", "pl", "w"] ):
        # print ("here")
        ghosts[board[plRow][plCol + 1]].cur = img5
        ghosts[board[plRow][plCol + 1]].mode = "c"
        updateGhostCoords(board[plRow][plCol +1])
    except:
      board[plRow][plCol] = " "
      plCol = 0
      if board[plRow][plCol] == "p":
        score += 50
      board[plRow][plCol] = "pl"
      if (game["isSuper"]) and ( board[plRow][plCol + 1] not in ["p", "P", " ", "b", "pl", "W"] ):
        ghosts[board[plRow][plCol + 1]].cur = img5
        ghosts[board[plRow][plCol + 1]].mode = "c"
        updateGhostCoords(board[plRow][plCol +1])
  if keyCode == LEFT: 
    try:
      if board[plRow][plCol - 1] != "w":
      # no wall
        if board[plRow][plCol] == "p":
          score += 50
        if board[plRow][plCol - 1] == "P":
          goSuper()
        board[plRow][plCol] = " "
        plCol -= 1
        if (game["isSuper"]) and ( board[plRow][plCol] not in ["p", "P", " ", "b", "pl", "w"] ):
          # print ("here")
          ghosts[board[plRow][plCol]].cur = img5
          ghosts[board[plRow][plCol]].mode = "c"
          updateGhostCoords(board[plRow][plCol -1])
          # print ("after")
        board[plRow][plCol] = "pl"
    except:
      # wall
      board[plRow][plCol] = " "
      plCol = 8
      if board[plRow][plCol] == "p":
        score += 50
      board[plRow][plCol] = "pl"
      if (game["isSuper"]) and ( board[plRow][plCol - 1] not in ["p", "P", " ", "b", "pl", "w"]):
        ghosts[board[plRow][plCol - 1]].cur = img5
        ghosts[board[plRow][plCol - 1]].mode = "c"
        updateGhostCoords(board[plRow][plCol -1])

def move_ghosts():
  global ghosts, board, get_possibles, move_ghost, move_captured
  game_over()
  # print(ghosts["pinky"].dirn)
  def get_possibles(ghost):
    possibles = []
    if ghosts[ghost].col == 0:
      if board[9][1] in ["P", " ", "pl"]:
        possibles.append((9, 1))
      if board[9][8] in ["P", " ", "pl"]:
        possibles.append((9, 8))
    elif ghosts[ghost].col == 8:
      if board[9][7] in ["P", " ", "pl"]:
        possibles.append((9, 7))
      if board[9][0] in ["P", " ", "pl"]:
        possibles.append((9, 0))
    else:
      # above 
      if board[ghosts[ghost].row -1][ghosts[ghost].col] in ["P", " ", "pl", "p", "b"]:
        possibles.append(((ghosts[ghost].row -1), ghosts[ghost].col))
      # below
      if board[ghosts[ghost].row +1][ghosts[ghost].col] in ["P", " ", "pl", "p", "b"]:
        possibles.append(((ghosts[ghost].row +1), ghosts[ghost].col))
      # right
      if board[ghosts[ghost].row][ghosts[ghost].col +1] in ["P", " ", "pl", "p", "b"]:
        possibles.append((ghosts[ghost].row, (ghosts[ghost].col +1)))
      # left
      if board[ghosts[ghost].row][ghosts[ghost].col -1] in ["P", " ", "pl", "p", "b"]:
        possibles.append((ghosts[ghost].row, (ghosts[ghost].col -1)))
      
    return possibles
  def get_previous(ghost):
    previous = (ghosts[ghost].row, ghosts[ghost].col)
    if ghosts[ghost].dirn == "n":
      previous = ((ghosts[ghost].row +1), ghosts[ghost].col)
    if ghosts[ghost].dirn == "w":
      previous = (ghosts[ghost].row, (ghosts[ghost].col +1))
    if ghosts[ghost].dirn == "s":
      previous = ((ghosts[ghost].row -1), ghosts[ghost].col)
    if ghosts[ghost].dirn == "e":
      previous = (ghosts[ghost].row, (ghosts[ghost].col -1))
    return previous
    
  def get_dirn(ghost, location):
    global board
    prev_row = ghosts[ghost].row
    prev_col = ghosts[ghost].col
    new_row = location[0]
    new_col = location[1]
    if new_row > prev_row:
      return "s"
    elif new_row < prev_row:
      return "n"
    elif new_col > prev_col:
      try:
        a = board[new_row][new_col]
      except:
          return "e"
    elif new_col < prev_col:
      try:
        b = board[new_row][new_col]
      except:
        return "w"
    else:
      return ghosts[ghost].dirn
      
  def move_captured(ghost):
    pass
    # logic for captured code
    

  def move_ghost(ghost, location):
    behind = ghosts[ghost].behind
    if board[ghosts[ghost].row][ghosts[ghost].col] != "pl":
      board[ghosts[ghost].row][ghosts[ghost].col] = ghosts[ghost].behind
    elif board[ghosts[ghost].row] == plRow and board[ghosts[ghost].col] == plCol:
      board[ghosts[ghost].row][ghosts[ghost].col] = "pl"
    ghosts[ghost].behind = board[location[0]][location[1]]
    ghosts[ghost].bLoc = (location[1], location[0])
    ghosts[ghost].dirn = get_dirn(ghost, location)
    ghosts[ghost].row = location[0]
    ghosts[ghost].col = location[1]
    board[location[0]][location[1]] = ghost
  

  for ghost in ghosts:
    if ghosts[ghost].mode == "c":
      move_ghost(ghost, (8, 4)) # row, column
      #TODO change pic and behavior at base
    else:
      # print(ghosts[ghost].cur)
      possibles = get_possibles(ghost)
      if len(possibles) == 1:
        move_ghost(ghost, possibles[0])
      if len(possibles) > 1:
        if get_previous(ghost) in possibles:
          possibles.remove(get_previous(ghost))
        move_ghost(ghost, possibles[random.randint(0, len(possibles) -1)])
  
def game_over():
  global game_over
  for ghost in ghosts:
    # print ("GAME OVER")
    if ghosts[ghost].row == plRow and ghosts[ghost].col == plCol and game["isSuper"] != True:
      # text("GAME OVER", 250, 100)
      game_over = True
      
# TODO captured + captured score
# move_ghosts()
run()


