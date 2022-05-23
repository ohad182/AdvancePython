import os

import multiprocessing

import re





def count_words(tpl: tuple):

    path, word = tpl

    word = word.lower()

    counter = 0

    current_process = multiprocessing.current_process().name

    if not os.path.isdir(path):

        try:

            with open(path, "r") as fo:

                for line in fo:

                    words_in_line = re.split(r'\W+', line.lower())

                    counter += words_in_line.count(word)

            print("{} -- {} contains word {} {} times".format(current_process, path, word, counter))

            return path, counter

        except Exception as e:

            print("Error in file {} -- {} - {}".format(path, type(e), str(e)))

            return path, None





def get_files(directory, ignore_dirs=None):

    for name in os.listdir(directory):

        full_path = os.path.join(directory, name)

        if os.path.isdir(full_path):

            if ignore_dirs is None or name not in ignore_dirs:

                yield from get_files(full_path, ignore_dirs)

            # for entry in get_files(full_path):

            #     yield entry

        elif os.path.isfile(full_path):

            yield full_path

        else:

            print('Unidentified name %s. It could be a symbolic link' % full_path)





def main():

    search_dir = r"C:\Git\CpssApiDatabase"

    files = get_files(search_dir, [".git", ".idea", "env"])

    print(len(list(files)))

    # [os.path.join(search_dir, x) for x in os.listdir(search_dir)]  # move to generator function

    word = "import"



    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())



    results = pool.map(count_words, ((f, word) for f in files))



    for path, cnt in results:

        print(path, cnt)





if __name__ == '__main__':

    main()



# import os

# import multiprocessing

# import re

#

#

# def count_words(path, word, queue: multiprocessing.Queue):

#     counter = 0

#     current_process = multiprocessing.current_process().name

#     with open(path, "r") as f:

#         content = f.read()

#         words = content.split()

#         for i_word in words:

#             fixed_word = re.sub(r'\W+', '', i_word)

#             if word == fixed_word:

#                 counter += 1

#     queue.put({"file": path, "count": counter})

#     print("{} -- {} contains word {} {} times".format(current_process, path, word, counter))

#

#

# def main():

#     search_dir = r"C:\Git\CpssApiDatabase"

#     files = os.listdir(search_dir)

#     word = "import"

#     workers = multiprocessing.cpu_count()

#     q = multiprocessing.Queue()

#     process_array = []

#     for f in files:

#         file_path = os.path.join(search_dir, f)

#         if f.startswith(".") or os.path.isdir(file_path):

#             continue

#

#         p = multiprocessing.Process(target=count_words, args=(file_path, word, q))

#         process_array.append(p)

#         p.start()

#         # count_words(file_path, word)

#

#     for process in process_array:

#         process.join()

#

#     for i in range(len(process_array)):

#         d = q.get()

#         print("{} {}".format(d["file"], d["count"]))

#

#

# if __name__ == '__main__':

#     main()

