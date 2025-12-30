# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import os

class ConsoleChecker:
    # Matches console.log, console.debug, console.info, console.warn, console.error
    CONSOLE_PATTERN = re.compile(r'console\.(log|debug|info|warn|error|trace|table)\(')

    @staticmethod
    def scan_file(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    # Simple check. Might flag comments.
                    # Advanced would strip comments first.
                    match = ConsoleChecker.CONSOLE_PATTERN.search(line)
                    if match:
                        issues.append({
                            'line': line_num,
                            'file': filepath,
                            'type': match.group(1),
                            'msg': f'Found console.{match.group(1)} usage'
                        })
        except Exception:
            pass
            
        return issues

    @staticmethod
    def scan_directory(directory, extensions=None):
        if extensions is None:
            extensions = ['.js', '.jsx', '.ts', '.tsx', '.vue', '.html', '.svelte']
            
        all_issues = []
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            if 'dist' in dirs: dirs.remove('dist')
            if 'build' in dirs: dirs.remove('build')
            
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in extensions:
                    path = os.path.join(root, file)
                    issues = ConsoleChecker.scan_file(path)
                    all_issues.extend(issues)
                    
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
