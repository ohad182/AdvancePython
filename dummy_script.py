import sys



sys.stderr.write("This is error\n")

sys.stderr.flush()



sys.stdout.write("This is log\n")

sys.stdout.flush()



sys.stderr.write("This is another error\n")

sys.stderr.flush()



sys.stdout.write("This is another log\n")

sys.stdout.flush()

