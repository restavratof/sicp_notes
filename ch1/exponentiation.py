#;; -----------------------------------------
#;; Recursion
# (define (exp b n)
#     (if (= n 0)
#         1
#         (* b (exp b (- n 1)))))
#
#;; -----------------------------------------
# ;; Iteration
# (define (expt-iter b counter product)
#     (if (= counter 0)
#         product
#         (expt-iter b
#             (- counter 1)
#             (* b product))))
#
# (define (expt b n)
#     (expt-iter b n 1))
#
#;; -----------------------------------------
# ;; Fast
# (define (even? n)
#     (= (remainder n 2) 0))
#
# (define (fast-expt b n)
#     (cond ((= n 0) 1)
#         ((even? n) (square (fast-expt b (/ n 2))))
#         (else (* b (fast-expt b (- n 1))))))
#;; -----------------------------------------

def exp(num,n):
    if n == 0:
        return 1
    else:
        return num * exp(num, (n-1))


print(' Recursion:')
print(exp(2,3))


def exp_iter(num, counter, product):
    if counter == 0:
        return product
    else:
        return exp_iter(num, (counter-1), (num * product))


def expi(num,n):
    return exp_iter(num, n, 1)


print(' Iteration:')
print(expi(2,3))

def square(x):
    return x*x

def even(n):
    return (n % 2) == 0


def fast_exp(num, n):
    if n == 0:
        return 1
    elif even(n):
        return square(fast_exp(num,(n/2)))
    else:
        return num * fast_exp(num, (n-1))


print('Fast recursion:')
print(fast_exp(2,3))



import time
start_time = time.time()
print(exp(2,500))
print("1:  %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(expi(2,500))
print("2:  %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(exp(2,500))
print("3:  %s seconds ---" % (time.time() - start_time))

