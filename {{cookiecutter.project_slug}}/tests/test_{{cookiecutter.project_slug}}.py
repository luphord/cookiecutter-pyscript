import unittest

from {{cookiecutter.project_slug}} import parser


class Test{{cookiecutter.project_slug}}(unittest.TestCase):

    def test_argument_parsing(self):
        args = parser.parse_args([])
        self.assertEqual(args.version, False)
        args = parser.parse_args(['--version'])
        self.assertEqual(args.version, True)
