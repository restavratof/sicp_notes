# ----- SCHEME
# (define (A x y)
#     (cond   ((= y 0) 0)
#             ((= x 0) (* 2 y))
#             ((= y 1) 2)
#             (else
#                 (A (- x 1) (A x (- y 1)) )
#             )
#     )
# )
#
# (A 1 2)
# (A 1 4)
# (A 1 10)
# (A 2 3)
# (A 2 4)
# (A 3 3)
#
# ; output
# ;$1 = 4
# ;$2 = 16
# ;$3 = 1024
# ;$4 = 16
# ;$5 = 65536
# ;$6 = 65536
#

def ackerman(x,y):
    if y == 0:
        return 0
    elif x == 0:
        return 2*y
    elif y == 1:
        return 2
    else:
        return ackerman((x-1), (ackerman(x,(y-1))))

print(ackerman(1,2))
print(ackerman(1,4))
print(ackerman(1,10))
print(ackerman(2,3))
print(ackerman(2,4))
print(ackerman(3,3))