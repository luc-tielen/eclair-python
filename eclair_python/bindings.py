import ctypes
import pathlib
from dataclasses import dataclass


# Low level types used in the Eclair API
program_t = ctypes.c_void_p
uint32_t = ctypes.c_uint32
string_t = ctypes.c_char_p


class Symbol(ctypes.Structure):
    _fields_ = [("length", uint32_t), ("data", ctypes.POINTER(ctypes.c_char))]

    def __str__(self):
        string = ctypes.string_at(self.data, self.length)
        return string.decode()


@dataclass(frozen=True)
class Bindings:
    c_lib: ctypes.CDLL

    @staticmethod
    def initialize(lib_path: pathlib.Path):
        c_lib = ctypes.CDLL(str(lib_path))

        c_lib.eclair_program_init.argtypes = []
        c_lib.eclair_program_init.restype = program_t

        c_lib.eclair_program_destroy.argtypes = [program_t]
        c_lib.eclair_program_destroy.restype = None

        c_lib.eclair_program_run.argtypes = [program_t]
        c_lib.eclair_program_run.restype = None

        c_lib.eclair_add_fact.argtypes = [program_t, uint32_t, ctypes.POINTER(uint32_t)]
        c_lib.eclair_add_fact.restype = None

        c_lib.eclair_add_facts.argtypes = [
            program_t,
            uint32_t,
            ctypes.POINTER(uint32_t),
            uint32_t,
        ]
        c_lib.eclair_add_facts.restype = None

        c_lib.eclair_fact_count.argtypes = [program_t, uint32_t]
        c_lib.eclair_fact_count.restype = uint32_t

        c_lib.eclair_get_facts.argtypes = [program_t, uint32_t]
        c_lib.eclair_get_facts.restype = ctypes.POINTER(uint32_t)

        c_lib.eclair_free_buffer.argtypes = [ctypes.POINTER(uint32_t)]
        c_lib.eclair_free_buffer.restype = None

        c_lib.eclair_encode_string.argtypes = [program_t, uint32_t, string_t]
        c_lib.eclair_encode_string.restype = uint32_t

        c_lib.eclair_decode_string.argtypes = [program_t, uint32_t]
        c_lib.eclair_decode_string.restype = Symbol

        return Bindings(c_lib=c_lib)

    # TODO add wrapper methods with normal types for each foreign function


def main():
    lib_path = pathlib.Path().absolute() / "tests" / "fixtures" / "libpath.so"
    bindings = Bindings.initialize(lib_path)
    print(bindings)


if __name__ == "__main__":
    main()
