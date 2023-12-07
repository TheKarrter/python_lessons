#2) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for X in [True,False]:
    for Y in [True,False]:
        for Z in [True,False]:
            if (not(X or Y or Z)) == ((not(X) and not(Y) and not(Z))):
                # print('X = ', X ,'\tY = ' , Y , '\tZ = ' , Z ,'\tis ' , '\tTrue')
                print(f"X = {X} \tY = {Y} \tZ = {Z} \tis \tTrue")
            else:
                # print('X = ', X ,'\tY = ' , Y , '\tZ = ' , Z ,'\tis ' , '\tFalse')
                print(f"X = {X} \tY = {Y} \tZ = {Z} \tis \tFalse")