import unittest
import main as m

class Behavior(unittest.TestCase):
    def test_behavior(self):
        self.assertEqual(m.content_key({'a':1,'b':2}),m.content_key({'b':2,'a':1}))
        self.assertNotEqual(m.content_key({'a':1}),m.content_key({'a':2}))
