from time import localtime, strftime
from typing import Dict, Generator, Iterator, List, Union
from pathlib import Path


class ListxService:
    def __init__(self, path: str) -> None:
        self.path = Path(path)

        if not self.path.is_dir() and not self.path.is_file():
            raise ValueError("Invalid path")

        self.path_stat = self.path.stat()

    def _get_items(self) -> Dict[int, Path]:
        if self.path.is_file():
            return {self.path_stat.st_size: self.path}

        return {
            directory.stat().st_size: directory
            for directory in self.path.iterdir()
        }

    def _order_items(self) -> List[Path]:
        return [item for _, item in sorted(self._get_items().items())]

    def _get_formated_items(self) -> Iterator[Dict[str, Union[str, int]]]:
        for directory in self._order_items():
            dir_stat = directory.stat()
            yield {
                "name": directory.name,
                "path": str(directory),
                "is_file": directory.is_file(),
                "size": dir_stat.st_size,
                "modified": strftime("%Y-%m-%d %H:%M:%S", localtime(dir_stat.st_mtime)),
            }

    def get_path_size(self) -> int:
        return self.path_stat.st_size

    def get_path_items(self) -> Iterator[Dict[str, Union[str, int]]]:
        return self._get_formated_items()
