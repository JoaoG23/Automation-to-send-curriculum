import pytest
import os
from src.utils.logging.log_manager.log_manager import write_to_log  # Adjust based on your actual path
from src.utils.move_to_file.move_to_file import move_to_file  # Adjust based on your actual path

def test_move_to_file(mocker):
    # Mock os.rename
    mock_rename = mocker.patch('os.rename')
    # Mock write_to_log
    mock_write_to_log = mocker.patch('src.utils.logging.log_manager.log_manager.write_to_log')
    
    source = "test_source.txt"
    destination = "test_destination.txt"
    
    # Call the function
    move_to_file(source, destination)
    
    # Assertions to verify the mocks were called correctly
    mock_rename.assert_called_once_with(source, destination)
    mock_write_to_log.assert_called_once_with(f"File moved from {source} to {destination}")

def test_move_to_file_file_not_found(mocker):
    # Mock os.rename to raise a FileNotFoundError
    mock_rename = mocker.patch('os.rename', side_effect=FileNotFoundError)
    
    source = "non_existent_file.txt"
    destination = "any_destination.txt"
    
    # Test if the FileNotFoundError is raised
    with pytest.raises(FileNotFoundError):
        move_to_file(source, destination)
