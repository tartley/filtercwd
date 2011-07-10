
from unittest import TestCase, main

from filtercwd import transform


class TestFilterCwd(TestCase):

    def test_untouched(self):
        self.assertEqual(
            transform('/other', '/cwd', '/home'),
            '/other'
        )

    def test_cwd(self):
        self.assertEqual(
            transform('/cwd/sub', '/cwd', '/home'),
            './sub'
        )

    def test_home(self):
        self.assertEqual(
            transform('/home/sub', '/cwd', '/home'),
            '~/sub'
        )

    def test_cwd_is_inside_home(self):
        self.assertEqual(
            transform('/home/one/two', '/home/one', '/home'),
            './two'
        )

    def test_home_is_inside_cwd(self):
        self.assertEqual(
            transform('/home/mine/sub', '/home', '/home/mine'),
            '~/sub'
        )

    def test_prefer_cwd(self):
        self.assertEqual(
            transform('/home/sub', '/home', '/home'),
            './sub'
        )



if __name__ == '__main__':
    main()

