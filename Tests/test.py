import sys              # import sys module
import os               # import os module
import unittest         # import unittest module
sys.path.append(os.path.dirname(os.path.dirname(__file__)))             #Append parent path to sys path
from Solution.lyst import solveRunTime                      # Import module to be tested
home = os.path.dirname(os.path.dirname(__file__))           # Get parent directory path
sys.path.append(os.path.dirname(__file__))                  # Append Test folder path to sys path


class TestRandomTime(unittest.TestCase):
    """Test case to test random time not close to boundaries
    """

    def test_solver(self):
        """Check the expected an actual  result of the test case
        Args:
            None
        Returns:
            Pass if all assert statements pass and
            Fail if one of the assert statements fails
        """
        result = solveRunTime('16:10', '{}/tests/cron_test.txt'.format(home))
        self.assertEqual(result[0][0:5], '23:59')
        self.assertEqual(result[0][6:9], 'tod')
        self.assertEqual(result[1][0:5], '16:45')
        self.assertEqual(result[1][6:9], 'tod')
        self.assertEqual(result[2][0:5], '16:10')
        self.assertEqual(result[2][6:9], 'tod')
        self.assertEqual(result[3][0:5], '19:00')
        self.assertEqual(result[3][6:9], 'tod')
        self.assertEqual(result[4][0:5], '00:00')
        self.assertEqual(result[4][6:9], 'tom')
        self.assertEqual(result[5][0:5], '16:59')
        self.assertEqual(result[5][6:9], 'tod')
        self.assertEqual(result[6][0:5], '16:10')
        self.assertEqual(result[6][6:9], 'tod')
        self.assertEqual(result[7][0:5], '23:00')
        self.assertEqual(result[7][6:9], 'tod')

class TestMinuteBeforeMidnight(unittest.TestCase):
    """Test case to test what will happen if the time entered
        is a minute before midnight
    """
    def test_solver(self):
        """Check the expected an actual  result of the test case
        Args:
            None
        Returns:
            Pass if all assert statements pass and
            Fail if one of the assert statements fails
        """
        result = solveRunTime('23:59', '{}/tests/cron_test.txt'.format(home))
        self.assertEqual(result[0][0:5], '23:59')
        self.assertEqual(result[0][6:9], 'tod')
        self.assertEqual(result[1][0:5], '00:45')
        self.assertEqual(result[1][6:9], 'tom')
        self.assertEqual(result[2][0:5], '23:59')
        self.assertEqual(result[2][6:9], 'tod')
        self.assertEqual(result[3][0:5], '19:00')
        self.assertEqual(result[3][6:9], 'tom')
        self.assertEqual(result[4][0:5], '00:00')
        self.assertEqual(result[4][6:9], 'tom')
        self.assertEqual(result[5][0:5], '23:59')
        self.assertEqual(result[5][6:9], 'tod')
        self.assertEqual(result[6][0:5], '23:59')
        self.assertEqual(result[6][6:9], 'tod')
        self.assertEqual(result[7][0:5], '23:59')
        self.assertEqual(result[7][6:9], 'tod')
class TestMidnight(unittest.TestCase):
    """Test case to test what will happen if the time entered is
        at midnight
    """
    def test_solver(self):
        """Check the expected an actual  result of the test case
        Args:
            None
        Returns:
            Pass if all assert statements pass and
            Fail if one of the assert statements fails
        """
        result = solveRunTime('00:00', '{}/tests/cron_test.txt'.format(home))
        self.assertEqual(result[0][0:5], '23:59')
        self.assertEqual(result[0][6:9], 'tod')
        self.assertEqual(result[1][0:5], '00:45')
        self.assertEqual(result[1][6:9], 'tod')
        self.assertEqual(result[2][0:5], '00:00')
        self.assertEqual(result[2][6:9], 'tod')
        self.assertEqual(result[3][0:5], '19:00')
        self.assertEqual(result[3][6:9], 'tod')
        self.assertEqual(result[4][0:5], '00:00')
        self.assertEqual(result[4][6:9], 'tod')
        self.assertEqual(result[5][0:5], '00:59')
        self.assertEqual(result[5][6:9], 'tod')
        self.assertEqual(result[6][0:5], '00:00')
        self.assertEqual(result[6][6:9], 'tod')
        self.assertEqual(result[7][0:5], '23:00')
        self.assertEqual(result[7][6:9], 'tod')
class TestMinuteAfterMidnight(unittest.TestCase):
    """Test case to test what will happen if the time entered is
        just after midnnight
    """
    def test_solver(self):
        """Check the expected an actual  result of the test case
        Args:
            None
        Returns:
            Pass if all assert statements pass and
            Fail if one of the assert statements fails
        """
        result = solveRunTime('00:01', '{}/tests/cron_test.txt'.format(home))
        self.assertEqual(result[0][0:5], '23:59')
        self.assertEqual(result[0][6:9], 'tod')
        self.assertEqual(result[1][0:5], '00:45')
        self.assertEqual(result[1][6:9], 'tod')
        self.assertEqual(result[2][0:5], '00:01')
        self.assertEqual(result[2][6:9], 'tod')
        self.assertEqual(result[3][0:5], '19:00')
        self.assertEqual(result[3][6:9], 'tod')
        self.assertEqual(result[4][0:5], '00:00')
        self.assertEqual(result[4][6:9], 'tom')
        self.assertEqual(result[5][0:5], '00:59')
        self.assertEqual(result[5][6:9], 'tod')
        self.assertEqual(result[6][0:5], '00:01')
        self.assertEqual(result[6][6:9], 'tod')
        self.assertEqual(result[7][0:5], '23:00')
        self.assertEqual(result[7][6:9], 'tod')
if __name__ == '__main__':
    unittest.main()
