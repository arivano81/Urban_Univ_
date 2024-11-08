immutable_var = 5, 7, "f", "g"
# print("immutable_var: " + str(immutable_var)) # для проверки
# immutable_var [0] = "a"
# уже на этапе написания кода PyCharm выдает ошибку "Tuples don't support item assignment", за что ему спасибо!
# однако можем добавить информацию к имеющемуся кортежу
immutable_var += (1, 2, 3)
print("Immutable tuple: " + str(immutable_var))
# в отличие от кортежа в списке можно изменить значения
mutable_list = [1, 2, "b", "f", "Classefied"]
mutable_list[0] = "a"
print("Mutable list: " + str(mutable_list))
