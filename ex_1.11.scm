;; Recursion
(display "------------------------------\n")
(display "Recursion:\n")
(define (fr n)
    (if (< n 3) 
        n
        (+ (fr (- n 1)) 
            (fr (- n 2)) 
            (fr (- n 3)
        ) 
    )
))

(display "2:\n")
(fr 2)
(display "3:\n")
(fr 3)
(display "4:\n")
(fr 4)
(display "5:\n")
(fr 5)
(display "6:\n")
(fr 6)


;; Iteration
(display "------------------------------\n")
(display "Iteration:\n")
(define (f-iter n step result result2 result3)
    (if (= step n) result)
    (if (< step n)
            result
            (f-iter 
                n 
                (+ step 1) 
                (+ 
                    (if (< n 3) step ) 
                    result2 
                    result3
                ) 
                result 
                result2
            )
    )
)

(define (fi n)
    (f-iter n 1 0 0 0))


(display "2:\n")
(fr 2)
(display "3:\n")
(fr 3)
(display "4:\n")
(fr 4)
(display "5:\n")
(fr 5)
(display "6:\n")
(fr 6)
