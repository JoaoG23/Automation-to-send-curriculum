import os
import unittest
from unittest.mock import MagicMock, patch

from send_emails.add_attachment_resume.add_attachment_resume import add_attachment_resume


class TestAddAttachmentResume(unittest.TestCase):

    @patch('selenium.webdriver.Chrome')
    @patch('selenium.webdriver.support.ui.WebDriverWait.until')
    def test_add_attachment_resume(self, mock_until, mock_driver):
        os.environ['PATH_WHERE_RESUMES'] = '/caminho/para/curriculos/'
        
        mock_element = MagicMock()
        mock_until.return_value = mock_element
        
        add_attachment_resume(mock_driver, 'java')
        
        expected_path = "/caminho/para/curriculos/\\joao-guilherme-desenvolvedor-java.pdf"
        mock_element.send_keys.assert_called_once_with(expected_path)
        
        add_attachment_resume(mock_driver, 'frontend')
        expected_path = "/caminho/para/curriculos/\\joao-guilherme-desenvolvedor-frontend.pdf"
        mock_element.send_keys.assert_called_with(expected_path)

if __name__ == '__main__':
    unittest.main()