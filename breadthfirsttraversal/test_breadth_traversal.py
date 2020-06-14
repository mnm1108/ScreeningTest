import unittest
import unittest.mock
import io
import breadthfirsttraversal as br

class TestBreadthTraversal(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        br.traverse_breadth_first(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_1(self):
        root = br.Node(2)
        root.left = br.Node(4)
        root.right = br.Node(6)
        root.left.left = br.Node(8)
        root.left.right = br.Node(10)
        self.assert_stdout(root, '2\n4\n6\n8\n10\n')

    def test_2(self):
        root = br.Node(10)
        root.left = br.Node(20)
        root.right = br.Node(30)
        root.left.left = br.Node(40)
        root.left.right = br.Node(50)
        self.assert_stdout(root, '10\n20\n30\n40\n50\n')
