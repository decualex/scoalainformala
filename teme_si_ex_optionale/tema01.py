# my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# my_list.sort()
# print(my_list)
# my_list.sort(reverse = True)
# print(my_list)
# lista_impare = [7, 9, 3, 1, 5]
# res = lista_impare
# print("Lista separata impare : " + str(res))
# lista_pare = [8, 2, 4, 10, 6]
# res = lista_pare
# print("Lista separata pare : " + str(res))
# lista_mult_trei = [3, 6, 9]
# res = lista_mult_trei
# print("Lista separata mult. lui 3 : " + str(res))
def get_sum(a, b, c, d, e, f, g) :
    return a + b + c * [e + f + g]




my_sum = get_sum
print(my_sum)



def plus(a, b):
    return a + b



class Summation(object):
    def sum(self, a, b):
        self.contents = a + b
        return self.contents