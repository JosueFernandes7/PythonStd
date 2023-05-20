def expression_matter(a, b, c):
#    p1 = a + b + c
#    p2 = a + b * c
#    p3 = (a + b) * c
#    p4 = a * b * c
#    p5 = a * b + c
#    p6 = a * (b + c)
#    return max(p1,p2,p3,p4,p5,p6)

    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))

print(expression_matter(5, 6, 1))
