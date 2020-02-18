;; Recursion
(define (exp b n)
    (if (= n 0)
        1
        (* b (exp b (- n 1)))))

;; Iteration
(define (expt-iter b counter product)
    (if (= counter 0)
        product
        (expt-iter b 
            (- counter 1)
            (* b product))))

(define (expt b n)
    (expt-iter b n 1))


;; Fast 
(define (even? n)
    (= (remainder n 2) 0))

(define (fast-expt b n)
    (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))

