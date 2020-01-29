;; Recursion
(define (fr n)
    (if (< n 3) 
        n
        (+ (fr (- n 1)) 
            (fr (- n 2)) 
            (fr (- n 3)
        ) 
    )
)))

(fr 2)
(fr 3)
(fr 4)
(fr 5)
(fr 6)

;;------------------------------------------------
;; Iteration
(define (f-iter result n)
    (if (< n 3) 
        (+ result n)
        (+
            (f-iter result (- n 1))
            (f-iter result (- n 2))
            (f-iter result (- n 3))
        )
    ))


(define (fi n)
    (f-iter 0 n))

(fi 2)
(fi 3)
(fi 4)
(fi 5)
(fi 6)
