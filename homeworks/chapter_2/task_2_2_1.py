def product(a, b):
    if a < 0:
        a *= -1
    elif b < 0:
        b *= -1
    result = a * b
    print("Product of", a, "and", b, "equals", result)
    return result


def pre_product(a,b):
    product_result = product(a,b)
    if a < 0 or b < 0:
        product_result *= -1
        print('\nNo, the right answer is:')
        print("Product of", a, "and", b, "equals", product_result)
        return product_result
    return product_result
a, b = int(input()), int(input())
pre_product(a, b)
