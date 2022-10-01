import os
from pathlib import Path
import json


def results_to_json(
    results_dictionary,
    file=__file__,
    ):
    os.makedirs("results", exist_ok=True)
    filepath = os.path.join("results", Path(file).name.replace(".py", ".json"))
    with open(filepath, 'w') as fp:
        json.dump(results_dictionary, fp, indent=4, sort_keys=True, default=str)
