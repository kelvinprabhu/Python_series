# break -- keyword is used to terminate the loop
for i in range(5):
    if i == 3:
        break
    print(i,end=" ")
# continue -- it is used to skip the current iteration and continue with the next iteration
for i in range(10):
    if i == 4:
        continue
    print(i,end=" ")

# pass -- it is a null statement used as a placeholder
for i in range(5):
    if i % 2 == 0:
        pass
    else:
        print(i,end=" ")
# pass - used in function definition as a placeholder