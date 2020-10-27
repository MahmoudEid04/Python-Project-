def eraseTable(tab):
   for i in range(0, 3):
       for j in range(0, 3):
           tab[i][j] = '-'
  
def verifyWin(tab):
  
   if testDraw(tab):
       print("It is a draw")
       return True
   elif testRows(tab)=='X' or testCols(tab)=='X' or testDiags(tab)=='X':
       print("Player X has won!")
       return True
   elif testRows(tab)=='O' or testCols(tab)=='O' or testDiags(tab)=='O':
       print("Player O has won!")
       return True
      
   return False 


def testRows(tab):
   for List in tab:
       c = 0
       for ch in List:
           if ch == 'X':
               c = c+1
       if c==3:
           return 'X'
          
   for List in tab:
       c = 0
       for ch in List:
           if ch == 'O':
               c = c+1
       if c==3:
           return 'O'
          
   return '-' 
  
  
def testCols(tab):

   for i in range(0, 3):
       c = 0
       for j in range(0, 3):
           if tab[j][i] == 'X':
               c = c+1
       if c==3:
           return 'X'
          
   for i in range(0, 3):
       c = 0
       for j in range(0, 3):
           if tab[j][i] == 'O':
               c = c+1
       if c==3:
           return 'O'
  
   return '-' 
  
def testDiags(tab):

   if (tab[0][0]=='X' and tab[1][1]=='X' and tab[2][2]=='X') or (tab[0][2]=='X' and tab[1][1]=='X' and tab[2][0]=='X'):
       return 'X'
   elif (tab[0][0]=='O' and tab[1][1]=='O' and tab[2][2]=='O') or (tab[0][2]=='O' and tab[1][1]=='O' and tab[2][0]=='O'):
       return 'O'
  
   return '-' 
  
  
def testDraw(tab):

   for List in tab:
       for ch in List:
           if ch == '-':
               
               return False
   return True
  


def displayTable (tab):

   print(" ", end="")
   col = 0
   while col < len(tab):
       print(col, end=" ")
       col += 1
   print()
   row = 0
   while row < len(tab):
       print(row, end="")
       col = 0
       while col < len(tab[row]):
           print(" ",tab[row][col], end="")
           col += 1
       print()
       row += 1

def play (tab, player):
   facts = False
   while not facts:
       place = [-1,-1] 
       while not((0 <= place[0] < len(tab)) and (0 <= place[1] < len(tab))):
           print ("player ",player, end="")
           print(", Provide the row and column from 0 to", (len(tab)-1), ": ")
           place[0] = int(input("Row: ")) 
           place[1] = int(input("Column: "))
          
           if tab[place[0]][place[1]] != '-':
               print("the position", place[0], place[1], "is busy")
               facts = False
           else:
               facts = True
            
               tab[place[0]][place[1]] = player
      
      

table = [['-','-','-'],['-','-','-'],['-','-','-']] 
  
Answer = input("Start a game (O or N): ");
while Answer == 'o' or Answer == 'O':
   eraseTable(table) 
   winner = False 
   while not winner:
       displayTable(table)
       play(table,'X') 
       winner = verifyWin(table) 
       if not winner:
           displayTable(table) 
           play(table,'O') 
           winner = verifyWin(table) 
      
   displayTable(table)
   Answer = input("Start a game (O or N): ") 
