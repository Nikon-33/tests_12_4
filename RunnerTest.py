import unittest
import unittest as ut
import rt_with_exceptions as rt
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                    format="%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | Строка: %(lineno)d | %(message)s",
                    encoding='utf-8')

class RunnerTest(ut.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runner = rt.Runner("Ilya", -5)
            for i in range(10):
                runner.walk()
            logging.info(f'"test_walk" выполнен успешно')
            self.assertEqual(runner.distance, 50)
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: %s', e)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = rt.Runner("Ilya")
            for i in range(10):
                runner.run()
            logging.info(f'"test_run" выполнен успешно')
            self.assertEqual(runner.distance, 100)
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: %s', e)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = rt.Runner("Ilya")
        runner2 = rt.Runner("Dima")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    ut.main()