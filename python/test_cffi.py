import cffi

ffi = cffi.FFI()

ffi.cdef("""
int printf(const char *format, ...);   // copy-pasted from the man page
int system(const char *command);   // copy-pasted from the man page
""")

C = ffi.dlopen(None)
arg = ffi.new("char[]", "world")
arg2 = ffi.cast("int", 123)
C.printf("hi there, %s. %x\n", arg, arg2)
C.system("ls /dftjh\n")



