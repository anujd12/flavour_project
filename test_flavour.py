import unittest
from flavour import transpile
class TranspilerTests(unittest.TestCase):
    def test_keywords(self):
        self.assertIn("if x:",transpile("agar x:\n    likho(x)\n"))
    def test_strings_comments_substrings(self):
        src='agarbatti = "agar"; # warna\nagar True:\n    likho("likho")\n'
        out=transpile(src)
        self.assertIn('agarbatti = "agar"; # warna',out)
        self.assertIn("if True:",out)
    def test_function_and_range(self):
        src="banao add(a, b):\n    bhejo a + b\nhar i mein range(3):\n    likho(i)\n"
        out=transpile(src,"hinglish")
        self.assertIn("def add",out); self.assertIn("for i in range",out)
    def test_dialects(self):
        self.assertIn("if",transpile("lowkey fr:\n    spill(1)","genz"))
    def test_bad_dialect(self):
        with self.assertRaises(ValueError): transpile("x=1","not-a-dialect")
if __name__=="__main__": unittest.main()
