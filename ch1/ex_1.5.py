# (define (square x) (* x x) )

# (define (sqrt x)
#     (define (good-enough? guess)
#         (< (abs (- (square guess) x)) 0.001))
#     (define (average x y)
#         (/ (+ x y) 2))
#     (define (improve guess)
#         (average guess (/ x guess)))
#     (define (sqrt-iter guess)
#         (if (good-enough? guess)
#             guess
#             (sqrt-iter (improve guess))))
#     (sqrt-iter 1.0))

# (sqrt 9)
# (sqrt (+ 100 37))
# (sqrt (+ (sqrt 2) (sqrt 3)))
# (square (sqrt 1000))


# 1 ]=> (sqrt 9)
# ;Value: 3.00009155413138

# 1 ]=> (sqrt (+ 100 37))
# ;Value: 11.704699917758145

# 1 ]=> (sqrt (+ (sqrt 2) (sqrt 3)))
# ;Value: 1.7739279023207892

# 1 ]=> (square (sqrt 1000))
# ;Value: 1000.000369924366

def square(x):
    return x * x

def good_enough(guess, x):
    return abs(square(guess) - x) < 0.001

def average(x,y):
    return (x + y)/2

def improve(guess, x):
    return average(guess, (x/guess))

def sqrt_iter(guess, x):
    if good_enough(guess,x):
        return guess
    else:
        return sqrt_iter(improve(guess,x),x)



def sqrt(x):
    return sqrt_iter(1.0, x)

print(sqrt(9))
print(sqrt(100+37))
print(sqrt(sqrt(2) + sqrt(3)))
print(square(sqrt(1000)))



