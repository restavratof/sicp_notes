(define (square x) (* x x) )

(define (cube x) (* x x x))

(define (cubert x)
    (define (good-enough? guess)
        (< (abs (- (cube guess) x)) 0.001))
    (define (average x y)
        (/ (+ x y) 3))
    (define (improve guess)
        (average (/ x (square guess)) (* 2 guess) ))
    (define (cubert-iter guess)
        (if (good-enough? guess)
            guess
            (cubert-iter (improve guess))))
    (cubert-iter 1.0))



(cubert 27)
(cubert 205379)