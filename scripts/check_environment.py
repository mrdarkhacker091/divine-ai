import sys
import platform
import os

print("=" * 45)
print("       DIVINE AI ENVIRONMENT CHECK")
print("=" * 45)

print("Python:", sys.version.split()[0])
print("Platform:", platform.platform())
print("Architecture:", platform.machine())
print("Operating system:", platform.system())

print("\nProject directories:")

directories = [
    "data/raw",
    "data/processed",
    "tokenizer",
    "src",
    "checkpoints",
    "notebooks",
    "api",
    "logs",
    "scripts"
]

for directory in directories:
    status = "OK" if os.path.isdir(directory) else "MISSING"
    print(f"[{status}] {directory}")

print("\nDivine AI environment check completed.")
