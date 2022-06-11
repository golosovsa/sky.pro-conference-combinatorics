import itertools


class AppPage:
    def __init__(self):

        self.slide2 = {"seq": "123", "permutations": itertools.permutations("123")}

        self.slide3 = {"seq": "123", "permutations": itertools.permutations("123", 2)}

        self.slide4 = {"seq": "123", "product": itertools.product("123", repeat=2)}

        self.slide5 = {"seq": "123", "combinations": itertools.combinations("123", 2)}

        self.slide6 = {"seq": "123", "combinations_with_replacement": itertools.combinations_with_replacement("123", 2)}

