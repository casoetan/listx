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
    path_items = service.get_path_items()

    size = 0
    count = 0

    print(f"{'Item (KB)':<14} {'Name':<64} {'Is File':<10} {'Modified':<20}")
    print("---")

    for item in path_items:
        count += 1
        size += item["size"]
        cli_printer(item)

    print("---")
    print(f"total size {size} KB")
    print(f"total files {count}")

main()
