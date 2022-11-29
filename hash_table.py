class HashTable:
    def __init__(self):
        self.length = 4
        self.__keys = [] + [None] * self.length
        self.__values = [] + [None] * self.length

    def __getitem__(self, item):
        try:
            index = self.__keys.index(item)
            return self.__values[index]
        except ValueError:
            raise ValueError(item)


    def __setitem__(self, key, value):
        filled_places = self.__size()
        if filled_places == self.length:
            self.__resize()
        if key in self.__keys:
            key_index = self.__keys.index(key)
            self.__values[key_index] = value
            return
        index = self.__get_index(key)
        self.__keys[index] = key
        self.__values[index] = value

    def __get_index(self, key):
        if isinstance(key, int) or isinstance(key, float):
            return self.__set_values(0)
        index = sum([ord(el) for el in key]) % self.length
        return self.__set_values(index)

    def __set_values(self, index):
        if index == self.length:
            index = 0
        if self.__keys[index] == None:
            return index
        return self.__set_values(index + 1)

    def __size(self):
        return len([el for el in self.__keys if el != None])

    def __resize(self):
        self.__keys += [None] * self.length
        self.__values += [None] * self.length
        self.length *= 2

    def get(self, key, default=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return default

    def __len__(self):
        return self.length

    def add(self, key, value):
        self[key] = value

    def clear(self):
        self.__keys = [None] * self.length
        self.__values = [None] * self.length

    def keys(self):
        return self.__keys

    def values(self):
        return self.__values

    def items(self):
        return [(self._HashTable__keys[el], self._HashTable__values[el]) for el in range(len(self._HashTable__keys)) if not self._HashTable__keys[el] == None]


    def __str__(self):
        lst = [f"{self._HashTable__keys[el]}: {self._HashTable__values[el]}"for el in range(len(self._HashTable__keys)) if not self._HashTable__keys[el] == None]
        return "{" + ", ".join(lst) + "}"





