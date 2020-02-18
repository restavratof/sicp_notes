# ;; Recursion
# (define (fr n)
#     (if (< n 3)
#         n
#         (+ (fr (- n 1))
#             (fr (- n 2))
#             (fr (- n 3)
#         )
#     )
# ))
#


def fi_recur(n):
    if n < 3:
        return n
    else:
        return fi_recur(n-1) + fi_recur(n-2) + fi_recur(n-3)

print(' --- RECURSION:')
print(fi_recur(2))
print(fi_recur(3))
print(fi_recur(4))
print(fi_recur(5))
print(fi_recur(6))


#-------------------------------------------------------------
# ;; Iteration
# (define (f-iter n step result result2 result3)
#     (if (= step n) result)
#     (if (< step n)
#             result
#             (f-iter
#                 n
#                 (+ step 1)
#                 (+
#                     (if (< n 3) step )
#                     result2
#                     result3
#                 )
#                 result
#                 result2
#             )
#     )
# )
#
# (define (fi n)
#     (f-iter n 1 0 0 0))
#
# (fr 2)            ;Value: 2
# (fr 3)            ;Value: 3
# (fr 4)            ;Value: 6
# (fr 5)            ;Value: 11
# (fr 6)            ;Value: 20


def fi_iter(n,step,result,result2,result3):
    if step == n:
        return result
    else:
        if step < n:
            return result
        else:
            if n < 3:
                tmp = step + result2 + result3
            else:
                tmp = result2 + result3

            return fi_iter(n, (step+1), tmp, result, result2)


def fi_it(n):
    return fi_iter(n,1,0,0,0)


print(' --- ITERATION:')
print(fi_it(2))
print(fi_it(3))
print(fi_it(4))
print(fi_it(5))
print(fi_it(6))

