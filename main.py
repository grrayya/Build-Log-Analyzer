import sys
from parser import GccParser
from reporter import ConsoleDump

def main():
    target_log = sys.argv[1]
    
    parser = GccParser(target_log)
    build_faults = parser.parse()
    
    out = ConsoleDump(build_faults)
    out.to_stdout()

if __name__ == "__main__":
    main()
