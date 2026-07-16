import unittest
import tempfile
import os
from parser import GccParser

class TestGccParser(unittest.TestCase):
    def setUp(self):
        self.fd, self.log_path = tempfile.mkstemp()
        with os.fdopen(self.fd, 'w') as f:
            f.write("src/radio_ctrl.c:42:5: warning: implicit declaration of function 'enable_power'\n")
            f.write("src/memory_map.c:105: error: request for member 'buffer'\n")
            f.write("Linking objects...\n")

    def tearDown(self):
        os.remove(self.log_path)

    def test_extracts_warnings_and_errors(self):
        parser = GccParser(self.log_path)
        faults = parser.parse()
        
        self.assertIn('src/radio_ctrl.c', faults)
        self.assertEqual(faults['src/radio_ctrl.c'][0]['level'], 'warning')
        self.assertEqual(faults['src/memory_map.c'][0]['line'], '105')

    def test_ignores_standard_output(self):
        parser = GccParser(self.log_path)
        faults = parser.parse()
        self.assertNotIn('Linking objects...', faults)

if __name__ == '__main__':
    unittest.main()
