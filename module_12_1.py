import threading
import time


def wite_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
    print(f'Завершилась запись в файл {file_name}')


time_start = time.time()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
time_end = time.time()
print(time_end - time_start)
# работа с потоком
time_start1 = time.time()
thread1 = threading.Thread(target=wite_words, args=(10, "example5.txt"))
thread2 = threading.Thread(target=wite_words, args=(30, "example6.txt"))
thread3 = threading.Thread(target=wite_words, args=(200, "example7.txt"))
thread4 = threading.Thread(target=wite_words, args=(100, "example8.txt"))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
time_end1 = time.time()
print(time_end1 - time_start1)
