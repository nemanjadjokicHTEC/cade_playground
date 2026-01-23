import subprocess
from python.random_print_library.random_print_library import get_random_word


def main():
    output = subprocess.check_output(["/app/timestamp_provider"]).decode('ascii').rstrip()
    return f"{output}: {get_random_word()}"


if __name__ == "__main__":
    print(main())