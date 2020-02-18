# ; Fibonacci
# ; ---  Recursion way
# (define (fib n)
#     (cond ((= n 0) 0)
#           ((= n 1) 1)
#           (else (+ (fib (- n 1 ))
#                    (fib (- n 2))))))
#
# ; ---- Iteration way
# (define (fib-iter a b count)
#     (if (= count 0)
#         b
#         (fib-iter (+ a b) a (- count 1))))
# (define (fib n)
#     (fib-iter 1 0 n))
#
#
# (fib 4)   ;Value: 3
# (fib 5)   ;Value: 5
# (fib 10)  ;Value: 55


def fib_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_r(n-1) + fib_r(n-2)

print(' Recurions:')
print(fib_r(4))
print(fib_r(5))
print(fib_r(10))


def fib_iter(a,b,count):
    if count == 0:
        return b
    else:
        return fib_iter((a+b), a, (count-1))


def fib_i(n):
    return fib_iter(1,0,n)


print(' Iteration:')
print(fib_i(4))
print(fib_i(5))
print(fib_i(10))