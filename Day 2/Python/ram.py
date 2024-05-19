import ctypes
import ctypes.wintypes
import sys

# Define constants
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
PAGE_READWRITE = 0x04
PROCESS_QUERY_INFORMATION = 0x0400

# Define structures
class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [("BaseAddress", ctypes.c_void_p),
                ("AllocationBase", ctypes.c_void_p),
                ("AllocationProtect", ctypes.c_ulong),
                ("RegionSize", ctypes.c_size_t),
                ("State", ctypes.c_ulong),
                ("Protect", ctypes.c_ulong),
                ("Type", ctypes.c_ulong)]

# Get process handle by PID
def get_process_handle(pid):
    return ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)

# Read memory
def read_memory(process_handle, address, size):
    buffer = ctypes.create_string_buffer(size)
    bytesRead = ctypes.c_size_t(0)
    ctypes.windll.kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(address), buffer, size, ctypes.byref(bytesRead))
    return buffer.raw

# Convert bytes to ASCII
def bytes_to_ascii(data):
    return ''.join([chr(b) if 32 <= b <= 126 else '.' for b in data])

# Main function to read notepad memory and print content
def main(pid):
    process_handle = get_process_handle(pid)
    if not process_handle:
        print(f"Failed to open process with PID {pid}")
        return
    
    address = 0
    mem_info = MEMORY_BASIC_INFORMATION()
    while ctypes.windll.kernel32.VirtualQueryEx(process_handle, ctypes.c_void_p(address), ctypes.byref(mem_info), ctypes.sizeof(mem_info)):
        if mem_info.Protect == PAGE_READWRITE and mem_info.State == 0x1000:
            try:
                memory_content = read_memory(process_handle, mem_info.BaseAddress, mem_info.RegionSize)
                ascii_content = bytes_to_ascii(memory_content)
                print(ascii_content)
            except:
                pass
        address += mem_info.RegionSize

    ctypes.windll.kernel32.CloseHandle(process_handle)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <PID>")
        sys.exit(1)
    
    pid = int(sys.argv[1])
    main(pid)
