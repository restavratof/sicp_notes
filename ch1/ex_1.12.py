# ;; Pascal triangle
# (define (pascal row col)
#     (if (or (= col 1) (= col row))
#         1
#         (+ (pascal (- row 1) (- col 1))
#             (pascal (- row 1) col)
#         )
#     )
# )
#
# (pascal 8 6)

def pascal(row,col):
    if (col == 1) or (col == row):
        return 1
    else:
        return pascal((row-1),(col-1)) + pascal((row-1),col)

print(pascal(8,6))