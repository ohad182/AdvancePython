import subprocess as sp



python_path = ""  # set the path to python interpreter to run

python_script_path = ""  # set the path to the python script to run

#

# exit_code = sp.call(["notepad"])

# print(f"Process finished with exit code {exit_code}")

#

# with open("out.txt", "w") as fo:

#     pass



# output = sp.check_output(["python.exe", "script..."])

# print(output)





# popen_obj = sp.Popen(["dir"], stdout=sp.PIPE, stderr=sp.PIPE)

# print(popen_obj.returncode)

# # do parent stuff - popen is non blocking

# # popen_obj.po

# output, errors = popen_obj.communicate()

# print("after subprocess is done, child exit code={}".format(popen_obj.returncode))

# print("output: {}".format(output))

# print("errors: {}".format(errors))





popen_obj = sp.Popen([python_path, python_script_path],

                     stdout=sp.PIPE, stderr=sp.STDOUT)

print(popen_obj.returncode)

# popen_obj.po

while True:

    try:

        # do parent stuff - popen is non blocking

        output, errors = popen_obj.communicate(timeout=.3)

    except sp.TimeoutExpired:

        print("Child still running")

    else:

        break



print("after subprocess is done, child exit code={}".format(popen_obj.returncode))

print("output: {}".format(output.decode('utf-8')))

print("errors: {}".format(errors))

