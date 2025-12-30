# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from linter.core import ConsoleChecker

def main():
    parser = argparse.ArgumentParser(description="Console.log Leftover Checker")
    parser.add_argument("path", help="Directory or file to scan (defaults to current dir)", nargs='?', default=".")
    parser.add_argument("--ignore-warn-error", action="store_true", help="Ignore console.warn and console.error calls")

    args = parser.parse_args()
    path = os.path.abspath(args.path)
    
    issues = []
    
    if os.path.isfile(path):
        issues = ConsoleChecker.scan_file(path)
    elif os.path.isdir(path):
        issues = ConsoleChecker.scan_directory(path)
    else:
        print(f"Error: Path '{path}' not found.")
        sys.exit(1)
    
    # Filter issues calls if requested
    if args.ignore_warn_error:
        issues = [i for i in issues if i['type'] not in ['warn', 'error']]
        
    if not issues:
        print("Clean! No console logs found.")
        sys.exit(0)
        
    print(f"Found {len(issues)} console calls:\n")
    for issue in issues:
        print(f"[{issue['file']}:{issue['line']}] {issue['msg']}")
        
    sys.exit(1)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
