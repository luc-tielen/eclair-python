import ctypes
import pathlib


def main():
    # TODO make path to shared lib configurable
    lib_path = pathlib.Path().absolute() / "eclair_python" / "libcadd.so"
    c_lib = ctypes.CDLL(lib_path)
    print(c_lib.add(123, 456))


if __name__ == "__main__":
    main()
