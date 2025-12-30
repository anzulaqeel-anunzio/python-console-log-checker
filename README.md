# Console.log Leftover Checker

A linter ensuring production code is free of debugging `console.log` statements. Supports JavaScript, TypeScript, Vue, React, and Svelte files.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Broad Support**: Detects `log`, `debug`, `info`, `trace`, `table`.
*   **Smart Filtering**: Option to ignore `console.warn` and `console.error` which may be legitimate.
*   **File Extension Aware**: Automatically scans `.js`, `.ts`, `.jsx`, `.tsx`, `.vue`, `.svelte`.

## Usage

```bash
python run_checker.py [path] [options]
```

### Options

*   `--ignore-warn-error`: Allow `console.warn` and `console.error` calls.

### Examples

**1. Scan Project**
```bash
python run_checker.py src/
```

**2. Strict Check (Everything)**
```bash
python run_checker.py src/
```

**3. Production Check (Allow errors)**
```bash
python run_checker.py src/ --ignore-warn-error
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
