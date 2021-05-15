import unittest
import lesson_4.old_lessons as old

print(old.time(35425))


class TestOldLessonsTrue(unittest.TestCase):
    def test_time(self):
        self.assertEqual(old.time(35425), (9, 50, 25))

    def test_sum_max_number(self):
        self.assertEqual(old.sum_max_number([15, 2, 3, 1, 7, 5, 4, 10]), ([15, 3, 7, 10]))


class TestOldLessonsFalse(unittest.TestCase):
    def test_time(self):
        self.assertEqual(old.time(35425), (9, 40, 25))

    def test_sum_max_number(self):
        self.assertEqual(old.sum_max_number([15, 2, 3, 1, 7, 5, 4, 10]), ([15, 7, 10]))


if __name__ == "__main__":
    unittest.main()
