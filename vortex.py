import turtle as t

t.shape('arrow')
t.speed('fastest')

for i in range(300):
    t.forward(i)
    t.right(91)

t.mainloop()
