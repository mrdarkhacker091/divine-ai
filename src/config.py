MODEL_NAME = "Divine AI"

MODEL_CONFIG = {
    "vocab_size": 4000,
    "context_length": 128,
    "embedding_dim": 128,
    "num_layers": 4,
    "num_heads": 4,
    "dropout": 0.1,
    "bias": False
}

TRAINING_CONFIG = {
    "batch_size": 16,
    "learning_rate": 0.0003,
    "epochs": 10,
    "weight_decay": 0.01,
    "seed": 42
}

LANGUAGES = [
    "English",
    "Nigerian Pidgin"
]

DEVICE_CONFIG = {
    "preferred_device": "cuda",
    "fallback_device": "cpu"
}
