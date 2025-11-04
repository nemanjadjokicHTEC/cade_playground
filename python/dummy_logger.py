import subprocess
from python.random_print_library.random_print_library import get_random_word


output = subprocess.check_output(["/Working_Directory/timestamp_provider"]).decode('ascii').rstrip()
print(f"{output}: {get_random_word()}")
