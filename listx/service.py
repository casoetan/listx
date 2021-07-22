import os
from time import localtime, strftime
from typing import Dict, Iterator, List, Tuple, Union
from pathlib import Path

class ListxService:
    """ List all files and directories in the current directory

    :return: list of files and directories
    """

    def __init__(self, path: str) -> None:
        self.path = Path(path)

        if not self.path.is_dir() and not self.path.is_file():
            raise ValueError("Invalid path, make sure this is not a symlink")

        self.path_stat = self.path.stat()

    def _is_valid_directory_item(self, item: Path) -> bool:
        if not (item.is_dir() or item.is_file()):
            return False

        if not os.access(item, os.R_OK):
            return False

        return True

    def _get_directory_size(self, directory: Path) -> int:
        """ GEt the size of a directory and all its subdirectories iteratively

        This is an iterative function that will return the total size of a directory
        O(n) time, where n is the number of items in the directory
        """
        size = 0

        q = [directory]
        while q:
            current_item = q.pop()
            if current_item.is_dir():
                q += [
                    child
                    for child in current_item.iterdir()
                    if self._is_valid_directory_item(child)
                ]
            else:
                size += current_item.stat().st_size

        return size

    def _get_directory_size_recursively(
        self, directory: Path, total_size: int = 0
    ) -> int:
        """ Get the size of a directory and all its subdirectories recursively

        This is a recursive function that will return the total size of a directory
        Runs into stack overflow if the directory is too deep
        O(n) time, where n is the number of items in the directory
        """
        if not directory.is_dir():
            return directory.stat().st_size

        for item in directory.iterdir():
            if not self._is_valid_directory_item(item):
                continue
            total_size += self._get_directory_size_recursively(item, 0)

        return total_size

    def _get_items(self) -> Dict[int, Path]:
        """ Get items

        Kicks of the function to get directory size and returns a dictionary of size to items
        """
        if not self.path.is_dir():
            return {self.path_stat.st_size: self.path}

        return {
            int(self._get_directory_size(directory) / 1000): directory
            for directory in self.path.iterdir()
            if self._is_valid_directory_item(directory)
        }

    def _order_items(self) -> List[Tuple[int, Path]]:
        """ Order items

        O(log n) time, where n is the number of items in the directory
        """
        return [
            (size, item) for size, item in sorted(self._get_items().items())
        ]

    def _get_formated_items(self) -> Iterator[Dict[str, Union[str, int]]]:
        """ Get formated items

        Formats the items in a dictionary to be returned
        """
        for size, directory in self._order_items():
            modified_time = directory.stat().st_mtime
            yield {
                "name": directory.name,
                "path": str(directory),
                "is_file": directory.is_file(),
                "size": size,
                "modified": strftime(
                    "%Y-%m-%d %H:%M:%S", localtime(modified_time)
                ),
            }

    def get_path_items(self) -> Iterator[Dict[str, Union[str, int]]]:
        """ Entry point for the class
        """
        return self._get_formated_items()
