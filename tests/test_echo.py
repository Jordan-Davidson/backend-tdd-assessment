#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        self.assertIsNotNone(echo.to_upper)
        self.assertEqual(echo.to_upper('hello!'), 'HELLO!')
        self.assertEqual(echo.to_upper('WHAT?'), 'WHAT?')

    def test_lower(self):
        self.assertIsNotNone(echo.to_lower)
        self.assertEqual(echo.to_lower('HELLO!'), 'hello!')
        self.assertEqual(echo.to_lower('what?'), 'what?')

    def test_title(self):
        self.assertIsNotNone(echo.to_title)
        self.assertEqual(echo.to_title('hello there'), 'Hello There')
        self.assertEqual(echo.to_title('Hey'), 'Hey')


if __name__ == '__main__':
    unittest.main()
