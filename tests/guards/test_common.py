import unittest

from scripts.guards._common import check_required_sections, parse_frontmatter


class TestCommon(unittest.TestCase):
    def test_parse_frontmatter(self):
        text = """---\nname: demo\ndescription: demo desc\n---\n\n# Title\n"""
        fm = parse_frontmatter(text)
        self.assertEqual(fm["name"], "demo")
        self.assertEqual(fm["description"], "demo desc")

    def test_required_sections(self):
        text = """# Title\n\n## Validation\n\n## Output And Evidence\n"""
        ok, missing = check_required_sections(text, ["Validation", "Output And Evidence"])
        self.assertTrue(ok)
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
