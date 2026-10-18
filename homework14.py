import time
import random
import threading

files = ["photo.jpg", "document.pdf", "video.mp4", "archive.zip", "music.mp3"]

def download_file(file_name):
    print(f"Start of downloading{file_name}")
    time.sleep(random.randint(1,3))
    print(f"Download comlpeted{file_name}")

start_time = time.perf_counter()

for file_name in files:
    download_file(file_name)

execution_time = time.perf_counter() - start_time
print(f"Execution time:{execution_time} seconds")

start_time = time.perf_counter()

threads = []

for file_name in files:
    thread = threading.Thread(
        target=download_file,
        args=(file_name,)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

parallel_time = time.perf_counter() - start_time
print(f"Parallel loading time:{parallel_time} seconds")

difference = execution_time - parallel_time
print(f"Time difference:{difference} seconds")