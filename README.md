<div align="center">

# python-foeppl-klammer


[![Release](https://img.shields.io/github/v/release/twihno/python-foeppl-klammer)](https://github.com/twihno/python-foeppl-klammer/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/twihno/python-foeppl-klammer/blob/main/LICENSE)
[![Test](https://github.com/twihno/python-foeppl-klammer/actions/workflows/test.yml/badge.svg)](https://github.com/twihno/python-foeppl-klammer/actions/workflows/test.yml)
[![Last Commit](https://img.shields.io/github/last-commit/twihno/python-foeppl-klammer)](https://github.com/twihno/python-foeppl-klammer/commits)
[![Open Issues](https://img.shields.io/github/issues-raw/twihno/python-foeppl-klammer)](https://github.com/twihno/python-foeppl-klammer/issues)

---


[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/twihno/python-foeppl-klammer)

</div>


Python Modul für die Verwendung von [Föppl Klammern](https://de.wikipedia.org/wiki/F%C3%B6ppl-Klammer) in Berechnungen

## Verfügbare Funktionen

### foepplklammerstandard
Funktionen für standard Python

```foeppl(var_x, grenze_a, potenz_n)```

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/1724320022637ecb47d28a280511c1b394125f2d">

```foeppl_inkl_null(var_x, grenze_a, potenz_n)```

Wie oben mit der Außnahme, dass 0 für x<=a gilt

### foepplklammernp
Funktionen für numpy arrays

```foeppl(var_x, grenze_a, potenz_n)```

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/1724320022637ecb47d28a280511c1b394125f2d">

```foeppl_inkl_null(var_x, grenze_a, potenz_n)```

Wie oben mit der Außnahme, dass 0 für x<=a gilt
