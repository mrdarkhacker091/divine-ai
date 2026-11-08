from pathlib import Path
import random
import re

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
OUTPUT_DIR = ROOT / "data" / "processed"

SEED = 42
VALIDATION_RATIO = 0.05
MIN_LINE_LENGTH = 10


def clean_text(text):
    text = text.replace("\ufeff", "")
    text = text.replace("\x00", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    files = list(RAW_DIR.glob("*.txt"))

    if not files:
        print("No .txt training files found in data/raw/")
        return

    lines = []

    for file in files:
        print(f"Reading: {file.name}")

        with file.open("r", encoding="utf-8", errors="replace") as f:
            for line in f:
                cleaned = clean_text(line)

                if len(cleaned) >= MIN_LINE_LENGTH:
                    lines.append(cleaned)

    # Remove duplicates while preserving order.
    lines = list(dict.fromkeys(lines))

    if len(lines) < 20:
        print("Not enough text yet. Add more training text.")
        return

    random.Random(SEED).shuffle(lines)

    validation_count = max(
        1, int(len(lines) * VALIDATION_RATIO)
    )

    validation = lines[:validation_count]
    training = lines[validation_count:]

    (OUTPUT_DIR / "train.txt").write_text(
        "\n".join(training) + "\n",
        encoding="utf-8"
    )

    (OUTPUT_DIR / "validation.txt").write_text(
        "\n".join(validation) + "\n",
        encoding="utf-8"
    )

    print("\nData preparation complete.")
    print(f"Total unique lines: {len(lines)}")
    print(f"Training lines: {len(training)}")
    print(f"Validation lines: {len(validation)}")


if __name__ == "__main__":
    main()
