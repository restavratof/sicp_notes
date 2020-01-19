(define (square x) (* x x) )

(square 5)

(square 6)

(define (good-enough? guess x)
    (< (abs (- (square guess) x)) 0.001))

(define (average x y)
    (/ (+ x y) 2))

(define (improve guess x)
    (average guess (/ x guess)))

(define (sqrt-iter guess x)
    (if (good-enough? guess x)
        guess
        (sqrt-iter (improve guess x)
            x)))

(define (good-enough? guess x)
    (< (abs (- (square guess) x)) 0.001))

(sqrt 9)

(sqrt (+ 100 37))

(sqrt (+ (sqrt 2) (sqrt 3)))

(square (sqrt 1000))