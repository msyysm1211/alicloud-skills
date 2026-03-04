import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


class TestGuardsCLI(unittest.TestCase):
    def test_frontmatter_checker_fails_without_description(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            skill = root / "skills" / "demo" / "demo-skill"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    name: demo-skill
                    ---

                    # Demo
                    """
                ),
                encoding="utf-8",
            )
            proc = subprocess.run(
                ["python3", "scripts/guards/check_frontmatter.py", "--root", str(root / "skills")],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("missing required frontmatter", proc.stdout)

    def test_antipattern_checker_detects_reset_hard(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            skill = root / "skills" / "demo" / "danger"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    name: danger
                    description: Use when testing.
                    ---

                    # Danger

                    ```bash
                    git reset --hard
                    ```
                    """
                ),
                encoding="utf-8",
            )
            proc = subprocess.run(
                ["python3", "scripts/guards/check_antipatterns.py", "--root", str(root / "skills")],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("Anti-pattern check FAILED", proc.stdout)


if __name__ == "__main__":
    unittest.main()
