class A:
    pass


class B(A):
    pass


class C(A, B):
    pass

# Ошибка в данном коде вызвана одновременным наследованием родительского класса A и
# его дочернего класса B, python не может определить методы какого класса использовать, поэтому поднимает ошибку
