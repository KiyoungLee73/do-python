import turtle as t

n = int(input())
t.shape('turtle')
t.color('red')
t.begin_fill()

for i in range(n):
    t.forward(100)
    t.right(360/n)

t.end_fill()

t.mainloop()
