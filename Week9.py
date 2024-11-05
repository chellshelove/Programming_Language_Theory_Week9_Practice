def outer():
    def middle(k):
        def inner():
            global i
            i = 4
        inner()
        return i, j, k
    i = 2
    return middle(j)

i = 1
j = 3

print(outer())
print(i, j)

# 14 > 2 > 8 > 9 > 3 > 6 > 5 > 7 > 9 > 14 > 15 