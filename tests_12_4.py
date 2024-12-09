# Домашнее задание по теме "Логирование"

# Задача "Логирование бегунов":

import logging
import unittest

import rt_with_exceptions


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log',
                    encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            walk = rt_with_exceptions.Runner('walk', -5)
            for i in range(10):
                walk.walk()
            self.assertEqual(walk.distance, 50)
            logging.info(f'"test_walk" выполнен успешно', exc_info=True)
        except ValueError:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            run = rt_with_exceptions.Runner(123)
            for i in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
            logging.info(f'"test_walk" выполнен успешно', exc_info=True)
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner", exc_info=True)



if __name__ == '__main__':
    main()
