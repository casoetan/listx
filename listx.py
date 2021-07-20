import argparse

from listx.service import ListxService


def cli_printer(item):
    print(
        f"{item['size']:<14} {item['name']:<64} {item['is_file']:<10} {item['modified']:<20}"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Lister: List directory items"
    )
    parser.add_argument("path", help="Directory to list")

    args = parser.parse_args()

    service = ListxService(args.path)
    path_size = service.get_path_size()
    path_items = service.get_path_items()

    print(f"total files {len(path_items)}")
    print(f"total size {path_size}")
    print("---")

    print(f"{'Item':<14} {'Name':<64} {'Is File':<10} {'Modified':<20}")
    print("---")

    for item in path_items:
        cli_printer(item)


main()
