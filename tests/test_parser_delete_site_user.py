import sys
import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.delete_site_users_parser import DeleteSiteUsersParser


class DeleteUsersParserTest(unittest.TestCase):
    csv = ("testname", "testpassword", "test", "test", "test", "test")

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=(argparse.Namespace(
                                                 username="test",
                                                 password="testpass",
                                                 server="http://test")))
    def test_delete_user_parser(self, mock_args):
        with mock.patch('builtins.open', mock.mock_open(read_data='test')):
            sys.argv = ["test_csv.csv", "test", "test1", "test2"]
            csv_lines, args = DeleteSiteUsersParser.delete_site_users_parser()
            args_from_command = vars(args)
            args_from_mock = vars(mock_args.return_value)
            self.assertEqual(args_from_command, args_from_mock)

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=(argparse.Namespace()))
    def test_delete_user_parser_missing_arguments(self, mock_args):
        with mock.patch('builtins.open', mock.mock_open(read_data='test')):
            sys.argv = ["test_csv.csv", "test", "test1", "test2"]
            csv_lines, args = DeleteSiteUsersParser.delete_site_users_parser()
            args_from_command = vars(args)
            args_from_mock = vars(mock_args.return_value)
            self.assertEqual(args_from_command, args_from_mock)

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=(argparse.Namespace()))
    def test_delete_user_parser_missing_arguments_(self, mock_args):
        with mock.patch('builtins.open', mock.mock_open(read_data='test')):
            sys.argv = ["test_csv.csv", "test", "test1", "test2"]
            csv_lines, args = DeleteSiteUsersParser.delete_site_users_parser()
            args_from_command = vars(args)
            args_from_mock = vars(mock_args.return_value)
            self.assertEqual(args_from_command, args_from_mock)