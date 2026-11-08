from pathlib import Path
import sentencepiece as spm

ROOT = Path(__file__).resolve().parents[1]

TRAIN_FILE = ROOT / "data" / "processed" / "train.txt"
OUTPUT_PREFIX = ROOT / "tokenizer" / "divine"

VOCAB_SIZE = 4000


def main():
    if not TRAIN_FILE.exists():
        raise FileNotFoundError(
            "Training data not found. Run src/prepare_data.py first."
        )

    spm.SentencePieceTrainer.train(
        input=str(TRAIN_FILE),
        model_prefix=str(OUTPUT_PREFIX),
        vocab_size=VOCAB_SIZE,
        model_type="bpe",
        character_coverage=0.9995,
        unk_id=0,
        bos_id=1,
        eos_id=2,
        pad_id=3,
        hard_vocab_limit=False,
        shuffle_input_sentence=True,
        input_sentence_size=1000000,
    )

    print("Divine AI tokenizer trained successfully.")
    print(f"Model: {OUTPUT_PREFIX}.model")
    print(f"Vocabulary: {OUTPUT_PREFIX}.vocab")


if __name__ == "__main__":
    main()
