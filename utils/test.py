import os
from pathlib import Path

# check if countries.json already exists
print((Path.cwd().parent / "countries.json").is_file())