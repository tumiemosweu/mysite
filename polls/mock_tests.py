from django.test import TestCase
from unittest.mock import patch, Mock
from .models import MockingExample

import polls


# Create your tests here.
class ExampleTestCase(MockingExample, TestCase):

    @patch('polls.models.Choice')
    def test_mock_example(self, choiceMock):
        polls.models.Choice()
        assert choiceMock is polls.models.Choice
        assert choiceMock.called

    @patch('polls.models.MockingExample.example')
    def test_example_method_call(self, exampleMock):
        self.example_call()
        exampleMock.assert_called_once_with()

    """test that name_in_page calls get_page"""
    @patch('polls.models.MockingExample._get_page')
    def test_name_in_page_calls_get_page(self, getpageMock):
        url = Mock()
        name = 'Tumie'
        self.name_in_page(url, name)
        getpageMock.assert_called_once_with(url)

# ???
    """mock page content with name and assert name is in the content"""
    @patch('polls.models.MockingExample._get_page')
    def test_name_in_page(self, getpageMock):
        url = Mock()
        getpageMock.return_value = Mock(
            content='Text that contains {} in it'.format('Tumie'))
        self.assertTrue(self.name_in_page(url, 'Tumie'))

    @patch('polls.models.MockingExample._get_page')
    def test_name_in_page_not(self, getpageMock):
        url = Mock()
        self.assertFalse(self.name_in_page(url, 'Tumie'))

    @patch('polls.models.MockingExample._get_page')
    def test_name_in_page_closes_response(self, getpageMock):
        resp = Mock()
        url = Mock()
        getpageMock.return_value = resp
        self.name_in_page(url, 'Tumie')
        resp.close.assert_called_once_with()
