```python
import unittest
from custom_pc_builder_module.controllers.main import changeLanguage

class TestMultiLanguageSupport(unittest.TestCase):

    def setUp(self):
        self.languages = ['English', 'Spanish', 'French', 'German', 'Chinese']

    def test_change_language(self):
        for language in self.languages:
            result = changeLanguage(language)
            self.assertEqual(result, f"Language changed to {language}")

if __name__ == '__main__':
    unittest.main()
```