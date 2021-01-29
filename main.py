import NormalForm as NF

if __name__ == '__main__':
    #input number of all productions
    product_numbers = int(input('Enter number of productions:'))
    product = []
    #receiving productions
    for i in range(product_numbers):
        product.append(str(input()))
    print(product)
    #class grammar
    grammar1 = NF.NormalForm(product, product_numbers)

    #print(sel)
    #grammar1.remove_lambda()
    #grammar1.remove_unit()
    grammar1.remove_useless()

    #print(grammar1.productions[1][1])



