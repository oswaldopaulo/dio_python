X = int(input())
Y = int(input())
if (Y > X):
    for i in range(X, Y):
          if (i%5==3) or (i%5==2):
            print(i)
else:
    for i in range(Y,X):

        if (i%5==3) or (i%5==2):
            print(i)