import os
from time import localtime, strftime
from typing import Dict, List


class ListxService:
    def __init__(self, path: str) -> None:

        if not os.path.isdir(path) and not os.path.isfile(path):
            raise ValueError("Invalid path")

        self.path = path + "/"

    def _get_items(self) -> Dict[int, str]:
        if os.path.isfile(self.path):
            return {os.path.getsize(self.path): self.path}

        return {
            os.path.getsize(self.path + directory): directory
            for directory in os.listdir(self.path)
        }

    def _order_items(self) -> List[str]:
        return [item for _, item in sorted(self._get_items().items())]

    def _get_formated_items(self) -> List[Dict[str, str]]:
        return [
            {
                "size": f"{os.path.getsize(self.path + directory)}",
                "name": f"{directory}",
                "is_file": f"{os.path.isfile(self.path + directory)}",
                "modified": f"{strftime('%c', localtime(os.path.getmtime(self.path + directory)))}",
            }
            for directory in self._order_items()
        ]

    def get_path_size(self) -> int:
        return os.path.getsize(self.path)

    def get_path_items(self) -> List[Dict[str, str]]:
        return self._get_formated_items()
