import unittest
import unlucky_numbers


class TestUnluckyNumbers(unittest.TestCase):
    test_unlucky_numbers = {
        3: 'test unlucky number three',
        5: 'test unlucky number five',
    }

    def test_contains_unlucky_number(self):
        self.assertTrue(unlucky_numbers.contains_unlucky_number(3, self.test_unlucky_numbers))
        self.assertTrue(unlucky_numbers.contains_unlucky_number(5, self.test_unlucky_numbers))
        self.assertTrue(unlucky_numbers.contains_unlucky_number(33, self.test_unlucky_numbers))
        self.assertTrue(unlucky_numbers.contains_unlucky_number(31313, self.test_unlucky_numbers))
        self.assertTrue(unlucky_numbers.contains_unlucky_number(11333, self.test_unlucky_numbers))

        self.assertFalse(unlucky_numbers.contains_unlucky_number(11133, self.test_unlucky_numbers))
        self.assertFalse(unlucky_numbers.contains_unlucky_number(13131, self.test_unlucky_numbers))

    def test_get_lucky_base_case(self):
        test_unlucky_numbers = {}
        n = unlucky_numbers.get_lucky(unlucky_numbers=test_unlucky_numbers)
        for i in xrange(100):
            self.assertEquals(n.next(), i)

    def test_get_lucky(self):
        n_lucky_numbers = 10
        n = unlucky_numbers.get_lucky(unlucky_numbers=self.test_unlucky_numbers)
        lucky_numbers = [n.next() for i in xrange(n_lucky_numbers)]
        correct_lucky_numbers = set(xrange(n_lucky_numbers + len(self.test_unlucky_numbers))) - set(self.test_unlucky_numbers.keys())
        self.assertEquals(set(lucky_numbers), correct_lucky_numbers)

    def test_get_lucky_with_explanation(self):
        n_lucky_numbers = 10
        n = unlucky_numbers.get_lucky(with_explanation=True, unlucky_numbers=self.test_unlucky_numbers)
        lucky_numbers_with_explanation = [n.next() for i in xrange(n_lucky_numbers)]
        for number, explanation in lucky_numbers_with_explanation:
            if (number - 1) in self.test_unlucky_numbers:
                self.assertEquals(explanation, {number - 1: self.test_unlucky_numbers[number - 1]})
            else:
                self.assertEquals(explanation, {})
        lucky_numbers = [number[0] for number in lucky_numbers_with_explanation]
        correct_lucky_numbers = set(xrange(n_lucky_numbers + len(self.test_unlucky_numbers))) - set(self.test_unlucky_numbers.keys())
        self.assertEquals(set(lucky_numbers), correct_lucky_numbers)


if __name__ == '__main__':
    unittest.main()
