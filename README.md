# HashTable
This is the classic approach to making a custom dictionary using two Lists. It is part of a workshop that I decided to join. I've also included unit tests for the code itself.

The idea of the project is a custom dictionary. The implementation is in a single class, with two private attributes that are Lists. First List represents the keys and the second the values.
"__getitem__" and "__setitem__" dunder methods are implemented, which mainly contribute to the correct syntax when we want to assign a value to a key or when we call a value by key.
I have done the hashing using a simple formula. I have fixed the problem with the matching of indexes during hashing, by using linear recursion.
I've made the Lists themselves work like arrays because they have a set length, and when that is exceeded, the length is doubled.
I have a get method that takes two values, one is the key and the other is optional and is the output that will be returned. Understandably, the output is set to None. The idea is that when we use get method, we can be sure that the program will not raise an error.
I have also implemented a __len__ dunder method that returns the total length of the arrays.
I've also done the basic keys, values, and items, along with the __srr__ dunder method that makes the object print like a real dictionary.
