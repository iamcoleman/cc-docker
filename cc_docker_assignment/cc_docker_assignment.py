import socket
from collections import Counter
from fnmatch import fnmatch
from os import listdir
from os.path import isfile, join
from pathlib import Path

DATA_DIR = "/home/data"


def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def get_all_files():
    files = [
        f
        for f in listdir(DATA_DIR)
        if isfile(join(DATA_DIR, f)) and fnmatch(f, "*.txt")
    ]

    return files


def get_words_per_file():
    files = get_all_files()

    files_word_count = dict()

    for filename in files:
        with open(DATA_DIR + "/" + filename, "r", encoding="utf-8-sig") as file:
            wordcount = Counter(file.read().split())
            total_words = 0
            for k, v in wordcount.items():
                total_words += v
            files_word_count[filename] = total_words

    return files_word_count


def get_ip_address():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return ip


def create_output_text(files_word_count, ip):
    output_text = "Result.txt File\n\n"

    if len(files_word_count) == 0:
        output_text += "No .txt files were found in '" + DATA_DIR + "'\n"
    else:
        output_text += "All .txt files found in '" + DATA_DIR + "':\n"
        max_filename = ""
        max_word_count = 0
        total_number_of_words = 0
        for k, v in files_word_count.items():
            output_text += "    " + k + " - " + str(v) + " words\n"
            total_number_of_words += v
            if v >= max_word_count:
                max_filename = k
                max_word_count = v
        output_text += (
            "\nThe largest .txt file is '"
            + max_filename
            + "' with "
            + str(max_word_count)
            + " words\n"
        )
        output_text += (
            "Total number of words in all "
            + str(len(files_word_count))
            + " .txt files: "
            + str(total_number_of_words)
            + "\n"
        )

    output_text += "\n"
    output_text += "The IP address for this machine is: " + ip + "\n"

    return output_text


def create_result_file():
    files_word_count = get_words_per_file()
    ip = get_ip_address()
    output_text = create_output_text(files_word_count, ip)

    # create directory if it does not exist
    Path("/home/output").mkdir(parents=True, exist_ok=True)

    # create 'result.txt' file
    with open("/home/output/result.txt", "w") as file:
        file.write(output_text)


def read_result():
    with open("/home/output/result.txt", "r", encoding="utf-8-sig") as file:
        file_contents = file.read()
        print(file_contents)
