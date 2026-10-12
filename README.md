# CLI CSV Data Explorer

A command-line tool for quickly exploring CSV files. Load a dataset, inspect summary statistics in the terminal, and generate chart images for numeric columns—without opening a notebook or spreadsheet.

Built with **Python**, **pandas**, and **matplotlib**, with **Typer** and **Rich** available for a richer CLI experience as the project grows.

## Features

- **CSV loading** — Point the tool at any `.csv` file (optional encoding for non-UTF-8 files).
- **Summary statistics** — Row/column counts, dtypes, missing values, and descriptive stats for numeric fields.
- **Automatic charts** — Histograms and related plots for numeric columns, saved as image files.
- **Configurable output** — Choose where chart images are written (default: `output/`).

## Requirements

- Python 3.10 or newer (recommended for current dependency versions)
- Dependencies listed in [`requirements.txt`](requirements.txt)

Core libraries:

| Package     | Role                          |
|------------|--------------------------------|
| pandas     | Data loading and analysis      |
| numpy      | Numerical operations           |
| matplotlib | Chart generation               |
| typer      | CLI framework (planned/alternate entry) |
| rich       | Formatted terminal output      |

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/CLI-CSV-DATA-EXPLORER.git
   cd CLI-CSV-DATA-EXPLORER
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   ```

   Windows (PowerShell):

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   macOS / Linux:

   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the explorer against a CSV path. Example with the included sample dataset:

```bash
python src/csv_explorer/explorer.py sample_data/employees.csv
```

Save charts to a custom directory:

```bash
python src/csv_explorer/explorer.py sample_data/employees.csv --output charts/
```

If your file uses a non-UTF-8 encoding (for example Latin-1):

```bash
python src/csv_explorer/explorer.py your_data.csv --encoding latin-1
```

### CLI options

| Argument / flag | Description |
|-----------------|-------------|
| `csv_path`      | Path to the CSV file to explore (required) |
| `--output`, `-o`| Directory for saved chart images (default: `output`) |
| `--encoding`    | File encoding when reading the CSV (optional) |

Run `--help` for the full argument list:

```bash
python src/csv_explorer/explorer.py --help
```

## Sample data

[`sample_data/employees.csv`](sample_data/employees.csv) is a small employee dataset with columns such as `department`, `salary`, `age`, `years_experience`, and `performance_score`. Use it to try the tool after installation.

## Project structure

```text
CLI-CSV-DATA-EXPLORER/
├── README.md
├── requirements.txt
├── sample_data/
│   └── employees.csv
└── src/
    └── csv_explorer/
        ├── __init__.py
        ├── cli.py          # CLI entry (Typer) — extension point
        └── explorer.py     # Main explorer script
```

Generated chart images are written to the output directory you specify (for example `output/` or `charts/`). Those folders are listed in [`.gitignore`](.gitignore) so local runs are not committed by mistake.

## Contributing

1. Fork the repository and create a feature branch.
2. Make your changes and test with `sample_data/employees.csv`.
3. Open a pull request with a short description of what you changed.

## License

This project is unlicensed until you add a `LICENSE` file. On GitHub, choose a license when creating the repository or add one later from **Settings → General**.

---

Replace `YOUR_USERNAME` in the clone URL with your GitHub username after you create the remote repository.
