import re
from collections import defaultdict

class GccParser:
    def __init__(self, build_log):
        self.build_log = build_log
        # some legacy modules drop the column number so the 3rd group is optional
        self.gcc_regex = re.compile(r"^(.*?):(\d+):(?:\d+:)?\s*(error|warning):\s*(.*)")

    def parse(self):
        compiler_flags = defaultdict(list)
        
        with open(self.build_log, 'r') as f:
            for line in f:
                match = self.gcc_regex.match(line.strip())
                if match:
                    module_src, line_num, severity, details = match.groups()
                    compiler_flags[module_src].append({
                        'line': line_num,
                        'level': severity,
                        'details': details
                    })
        return compiler_flags
