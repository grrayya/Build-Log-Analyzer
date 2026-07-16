class ConsoleDump:
    def __init__(self, flags):
        self.flags = flags

    def to_stdout(self):
        if not self.flags:
            print("clean build")
            return

        for module, issues in self.flags.items():
            print(f"\n[{module}]")
            
            for issue in issues:
                marker = "X" if issue['level'] == "error" else "!"
                print(f"  {marker} L{issue['line']}: {issue['details']}")
