# (define (square x) (* x x) )
#
# (define (cube x) (* x x x))
#
# (define (cubert x)
#     (define (good-enough? guess)
#         (< (abs (- (cube guess) x)) 0.001))
#     (define (average x y)
#         (/ (+ x y) 3))
#     (define (improve guess)
#         (average (/ x (square guess)) (* 2 guess) ))
#     (define (cubert-iter guess)
#         (if (good-enough? guess)
#             guess
#             (cubert-iter (improve guess))))
#     (cubert-iter 1.0))
#
#
#
# (cubert 27)
# ;Value: 3.0000005410641766
#
# (cubert 205379)
# ;Value: 59.00000002829254


def square(x):
    return x * x

def cube(x):
    return x*x*x

def good_enough(guess, x):
    return abs(cube(guess) - x) < 0.001

def average(x,y):
    return (x + y)/3

def improve(guess, x):
    return average((x/square(guess)), (2*guess))

def cubert_iter(guess, x):
    if good_enough(guess,x):
        return guess
    else:
        return cubert_iter(improve(guess,x),x)



def cubert(x):
    return cubert_iter(1.0, x)


print(cubert(27))
print(cubert(205379))
