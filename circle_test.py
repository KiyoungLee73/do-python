import turtle as t

# n = int(input())
n = 60
t.shape('turtle')
t.speed('fastest')
# t.color('red')
# t.begin_fill()

for i in range(n):
    t.circle(120)
    t.right(360/n)

# t.end_fill()

t.mainloop()
