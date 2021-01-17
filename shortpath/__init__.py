""" Short Path
"""
from typing import Union

import os.path
from pathlib import Path


def shortpath(p: Union[Path, str]) -> str:
    if isinstance(p, str):
        p = Path(p)

    new_path = []
    for i in p.parts[0:-1]:
        new_path.append(i[0])
    new_path.append(p.parts[-1])

    return os.path.join(*new_path)
