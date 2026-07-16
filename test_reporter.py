import unittest
from io import StringIO
from contextlib import redirect_stdout
from reporter import ConsoleDump

class TestConsoleDump(unittest.TestCase):
    def test_clean_build_output(self):
        out_stream = StringIO()
        dump = ConsoleDump({})
        
        with redirect_stdout(out_stream):
            dump.to_stdout()
            
        self.assertEqual(out_stream.getvalue().strip(), "clean build")

    def test_fault_formatting(self):
        mock_flags = {
            'core/dsp_init.c': [{'line': '12', 'level': 'error', 'details': 'missing semicolon'}]
        }
        
        out_stream = StringIO()
        dump = ConsoleDump(mock_flags)
        
        with redirect_stdout(out_stream):
            dump.to_stdout()
            
        terminal_str = out_stream.getvalue()
        self.assertIn("[core/dsp_init.c]", terminal_str)
        self.assertIn("X L12: missing semicolon", terminal_str)

if __name__ == '__main__':
    unittest.main()
