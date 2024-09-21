import unittest2
from unittest2 import mock

from move_to_file import move_to_file

class TestMoveToFile(unittest2.TestCase):
    @mock.patch('os.rename')
    def test_move_to_file_success(self, mock_rename):
        # Define source and destination
        source = "source.txt"
        destination = "destination.txt"
        
        # Call the function
        move_to_file(source, destination)

        # Check if os.rename was called with the correct arguments
        mock_rename.assert_called_once_with(source, destination)

    @mock.patch('os.rename', side_effect=OSError("File not found"))
    def test_move_to_file_failure(self, mock_rename):
        source = "nonexistent.txt"
        destination = "destination.txt"
        
        with self.assertLogs(level='INFO') as log:
            move_to_file(source, destination)
        
        self.assertIn("An error occurred: File not found", log.output[0])

if __name__ == '__main__':
    unittest2.main()
