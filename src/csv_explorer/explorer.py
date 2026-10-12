import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Explore a CSV file: summary stats + charts.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python explorer.py data.csv
    python explorer.py data.csv --output charts/
    python explorer.py data.csv --encoding latin-1
        """,
    )
    parser.add_argument("csv_path", help="Path to the CSV file to explore")
    parser.add_argument(
        "--output",
        "-o",
        default="output",
        help="Directory to save chart images",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Encoding used when reading the CSV (default: utf-8)",
    )
    return parser.parse_args()


def load_csv(path: Path, encoding: str) -> pd.DataFrame:
    if not path.is_file():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    try:
        return pd.read_csv(path, encoding=encoding)
    except UnicodeDecodeError:
        print(
            f"Error: could not decode file with encoding {encoding!r}. "
            "Try --encoding (e.g. latin-1).",
            file=sys.stderr,
        )
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: CSV file is empty: {path}", file=sys.stderr)
        sys.exit(1)


def print_summary(df: pd.DataFrame) -> None:
    print(f"\nRows: {len(df):,}  |  Columns: {len(df.columns)}")
    print("\n--- Column types ---")
    print(df.dtypes.to_string())
    missing = df.isna().sum()
    if missing.any():
        print("\n--- Missing values ---")
        print(missing[missing > 0].to_string())
    else:
        print("\nNo missing values.")
    numeric = df.select_dtypes(include="number")
    if not numeric.empty:
        print("\n--- Numeric summary ---")
        print(numeric.describe().to_string())
    else:
        print("\nNo numeric columns found for statistical summary.")


def save_charts(df: pd.DataFrame, output_dir: Path) -> None:
    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        print("\nNo numeric columns; skipping charts.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    for col in numeric.columns:
        values = numeric[col].dropna()
        if values.empty:
            continue
        fig, ax = plt.subplots()
        ax.hist(values, bins="auto", edgecolor="black", alpha=0.75)
        ax.set_title(f"Distribution of {col}")
        ax.set_xlabel(col)
        ax.set_ylabel("Frequency")
        safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in str(col))
        fig.savefig(output_dir / f"{safe_name}_hist.png", bbox_inches="tight")
        plt.close(fig)

    print(f"\nSaved {len(numeric.columns)} chart(s) to {output_dir.resolve()}")


def main() -> None:
    args = parse_args()
    df = load_csv(Path(args.csv_path), args.encoding)
    print_summary(df)
    save_charts(df, Path(args.output))


if __name__ == "__main__":
    main()
