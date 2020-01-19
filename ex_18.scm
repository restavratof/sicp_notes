;--------------------------------------------------------
; Square calculation
;--------------------------------------------------------
(define (square x) (* x x) )

;--------------------------------------------------------
; Cube calculation
;--------------------------------------------------------
(define (cube x) (* x x x))

;--------------------------------------------------------
; Check that result within required accuracy
;--------------------------------------------------------
(define (good-enough? guess x)
    (< (abs (- (cube guess) x)) 0.001))

;--------------------------------------------------------
(define (average x y)
    (/ (+ x y) 3))

(define (improve guess x)
    (average (/ x (square guess)) (* 2 guess) ))

;--------------------------------------------------------
; Sqrt calculation
;--------------------------------------------------------
(define (cubert-iter guess x)
    (if (good-enough? guess x)
        guess
        (cubert-iter (improve guess x)
            x)))

(define (cubert x)
    (cubert-iter 1.0 x))



(cubert 81)
