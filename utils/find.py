from utils.common.file_operations import save_to_file, read_file


class NotFoundError(Exception):
    pass


def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
        raise NotFoundError(f'{expected} not found in the provided iterable')


print(__name__)
if __name__ == "__main__":
    print("i ran as script")

