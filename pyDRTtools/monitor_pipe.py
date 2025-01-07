import asyncio
import win32pipe
import win32file
import pywintypes

async def handle_client(pipe_handle):
    try:
        while True:
            overlapped = pywintypes.OVERLAPPED()
            hr, data = win32file.ReadFile(pipe_handle, 4096, overlapped)
            await asyncio.get_event_loop().run_in_executor(None, overlapped.GetOverlappedResult, True)
            if hr == 0:
                print(f"Received: {data.decode()}")
                response = f"Echo: {data.decode()}"
                win32file.WriteFile(pipe_handle, response.encode())
            else:
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        win32file.CloseHandle(pipe_handle)

async def server():
    pipe_name = r'\\.\pipe\AsyncPipe'
    while True:
        pipe_handle = win32pipe.CreateNamedPipe(
            pipe_name,
            win32pipe.PIPE_ACCESS_DUPLEX | win32file.FILE_FLAG_OVERLAPPED,
            win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
            1, 65536, 65536, 0, None
        )
        #win32pipe.ConnectNamedPipe(pipe_handle, None)
        #asyncio.create_task(handle_client(pipe_handle))
        break


def start_monitor_pipe():
   # asyncio.run(server())
    print (2+2)

