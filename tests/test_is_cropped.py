""" 
Entire TestSuite for is_cropped. 
"""

import unittest

from main import guess_jpg, match


class TestGuessJpg(unittest.TestCase):
    """ Tests for guess_jpg """

    def test_good(self):
        try:
            guess_jpg('tests/fixtures/sample.jpg')
        except SystemExit:
            self.fail("System Exit raised.")

    def test_not_found(self):
        self.assertRaises(SystemExit, guess_jpg, 'lsjdflkdjf.jpg')

    def test_not_jpeg(self):
        self.assertRaises(SystemExit, guess_jpg, 'tests/fixtures/not_jpeg.png')


class TestMatch(unittest.TestCase):

    def test_good(self):
        self.assertEqual(
            match('tests/fixtures/sample.jpg', 'tests/fixtures/cropped.jpg'),
            u"'cropped.jpg' appears to be cropped from 'sample.jpg' at (88, 79)"
        )

    def test_no_match(self):
        self.assertEqual(
            match(
                'tests/fixtures/sample.jpg',
                'tests/fixtures/not_cropped.jpg'
            ),
            u"'not_cropped.jpg' does not appear to be cropped from 'sample.jpg'"
        )
