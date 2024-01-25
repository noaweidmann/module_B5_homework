def greet():
   print("~~~~~~~~~~~~~~~~~")
   print("Добро пожаловать")
   print("     В игру     ")
   print("Крестики - нолики")
   print("~~~~~~~~~~~~~~~~~")

def show():
   print()
   print("     |  0  |  1  |  2  |")
   print("------------------------")
   for i, row in enumerate(field):
      row_str = f"  {i} | {'  |  '.join(row)} | "
      print(row_str)
      print("------------------------")
   print()

def ask():
   while True:
      answer = input("Ваш ход: ").split()
      if len(answer) != 2:
         print("Введите две координаты!")
         continue

      x, y = answer
      if not(x.isdigit()) or not(y.isdigit()):
         print("Введите ЧИСЛА!")
         continue

      x, y = int(x), int(y)
      if 0 > x > 2 or 0 > y > 2:
         print("Координаты вне диапазона!")
         continue

      if field[x][y] != " ":
         print("Клетка занята!")
         continue

      return x, y

def win():
   win_variants = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
   for variants in win_variants:
      symbols = []
      for v in variants:
         symbols.append(field[v[0]][v[1]])
      if symbols == ["X", "X", "X"]:
         print("Выиграл Х!")
         return True
      if symbols == ["O", "O", "O"]:
         print("Выиграл О!")
         return True
   return False

greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
   count += 1
   show()
   if count % 2 == 1:
      print("Ход Х")
   else:
      print("Ход О")

   x,y = ask()
   if count % 2 == 1:
      field[x][y] = "X"
   else:
      field[x][y] = "O"

   if win():
      break

   if count == 9:
      print("Ничья!")
      break



