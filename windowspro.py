from ctypes import windll

windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B), 
    c_ulong(0), 
    nullptr, 
    nullptr, 
    c_uint(6), 
    byref(c_uint())
)