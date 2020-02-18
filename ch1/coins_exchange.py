#
# (define (first-denomination kind-of-coins)
#     (cond ((= kind-of-coins 1) 1)
#         ((= kind-of-coins 2) 5)
#         ((= kind-of-coins 3) 10)
#         ((= kind-of-coins 4) 25)
#         ((= kind-of-coins 5) 50)))
#
#
# (define (cc amount kind-of-coins)
#     (cond ((= amount 0) 1)
#         ((or (< amount 0) (= kind-of-coins 0)) 0)
#         (else (+ (cc amount
#                     (- kind-of-coins 1))
#                 (cc (- amount (first-denomination kind-of-coins))
#                      kind-of-coins)))))
#
#
# (define (count-change amount)
#     (cc amount 5))
#
#
#
# (count-change 100)    ; Value: 292


def first_denom(kind_of_coins):
    if kind_of_coins == 1:
        return 1
    elif kind_of_coins == 2:
        return 5
    elif kind_of_coins == 3:
        return 10
    elif kind_of_coins == 4:
        return 25
    elif kind_of_coins == 5:
        return 50


def cc(amount, kind):
    if amount == 0:
        return 1
    elif (amount < 0) or (kind == 0):
        return 0
    else:
        return cc(amount, (kind - 1)) + cc((amount - first_denom(kind)),kind)


def count_change(amount):
    return cc(amount,5)


print(count_change(100))