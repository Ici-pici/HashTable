from unittest import TestCase, main
from hash_table_workshop.hash_table import HashTable


class HashTableTests(TestCase):
    def setUp(self) -> None:
        self.example = HashTable()

    def test_constructor_elements(self):
        self.assertEqual([None, None, None, None], self.example._HashTable__keys)
        self.assertEqual([None, None, None, None], self.example._HashTable__values)

    def test_set_item_dunder_method_with_sting_key(self):
        self.example['Name'] = 5
        passed = True if "Name" in self.example._HashTable__keys and 5 in self.example._HashTable__values else False
        self.assertTrue(passed)

    def test_set_item_dunder_method_with_integer_key(self):
        self.example[6] = 5
        passed = True if 6 in self.example._HashTable__keys and 5 in self.example._HashTable__values else False
        self.assertTrue(passed)

    def test_correct_indexes_for_both_lists(self):
        self.example['Name'] = 5
        key_index = self.example._HashTable__keys.index("Name")
        value_index = self.example._HashTable__values.index(5)
        passed = True if key_index == value_index else False
        self.assertTrue(passed)

    def test_size_method(self):
        self.example['Name'] = 5
        res = self.example._HashTable__size()
        self.assertEqual(1, res)

        self.example['age'] = 5
        res = self.example._HashTable__size()
        self.assertEqual(2, res)

    def test_for_unique_keys_with_string_keys(self):
        self.example['Name'] = 5
        self.example['Name'] = 5
        res = self.example._HashTable__size()
        self.assertEqual(1, res)

    def test_for_unique_keys_with_integer_keys(self):
        self.example[6] = 5
        self.example[6] = 5
        res = self.example._HashTable__size()
        self.assertEqual(1, res)

    def test_resize_method(self):
        self.example['Name'] = 5
        self.example['Age'] = 6
        self.example['Gender'] = 'Male'
        self.example['Hair'] = 'Brown'
        self.example['Nails'] = 'Long'
        self.assertEqual(8, self.example.length)
        self.assertEqual(['Hair', 'Name', 'Age', 'Gender', None, None, None, 'Nails'], self.example._HashTable__keys)
        self.assertEqual(['Brown', 5, 6, 'Male', None, None, None, 'Long'], self.example._HashTable__values)

    def test_get_item_dunder_method_raises(self):
        table = HashTable()
        with self.assertRaises(ValueError) as ex:
            print(table["Name"])
        self.assertEqual("Name", str(ex.exception))

    def test_get_item_dunder_method_returning_correct_value(self):
        self.example['Name'] = 5
        res = self.example['Name']
        self.assertEqual(5, res)

    def test_get_method_with_non_existing_key_with_default_message(self):
        res = self.example.get("Name")
        self.assertEqual(None, res)

    def test_get_method_with_non_valid_key_with_custom_message(self):
        res = self.example.get("Name", 'SomeMessage')
        self.assertEqual('SomeMessage', res)

    def test_get_method_with_valid_key(self):
        self.example['Name'] = 5
        res = self.example.get("Name")
        self.assertEqual(5, res)

    def test_len_dunder_method_without_resizing(self):
        res = len(self.example)
        self.assertEqual(4, res)

    def test_len_dunder_method_with_resizing(self):
        self.example._HashTable__resize()
        res = len(self.example)
        self.assertEqual(8, res)

    def test_add_method(self):
        self.example.add("Name", "SomeName")
        name_registered = True if 'Name' in self.example._HashTable__keys else False
        value_registered = True if 'SomeName' in self.example._HashTable__values else False
        passed = True if name_registered and value_registered else False
        self.assertTrue(passed)

    def test_clear_method(self):
        self.example['Name'] = 5
        self.example['Age'] = 6
        self.example['Gender'] = 'Male'
        self.example.clear()
        self.assertEqual([None, None, None, None], self.example._HashTable__keys)
        self.assertEqual([None, None, None, None], self.example._HashTable__values)

    def test_keys_method_return(self):
        self.example['Name'] = 5
        self.example['Age'] = 6
        self.example['Gender'] = 'Male'
        res = self.example.keys()
        self.assertEqual([None, 'Name', 'Age', 'Gender'], res)

    def test_values_method_return(self):
        self.example['Name'] = 5
        self.example['Age'] = 6
        self.example['Gender'] = 'Male'
        res = self.example.values()
        self.assertEqual([None, 5, 6, 'Male'], res)

    def test_items_method_return(self):
        self.example['Name'] = 5
        self.example['Age'] = 6
        res = self.example.items()
        self.assertEqual([('Name', 5), ('Age', 6)], res)

    def test_str_dunder_method_return(self):
        self.example['Name'] = 5
        self.assertEqual("{Name: 5}", str(self.example))




if __name__ == "__main__":
    main()