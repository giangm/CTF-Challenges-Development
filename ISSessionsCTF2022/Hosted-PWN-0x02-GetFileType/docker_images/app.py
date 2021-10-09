import os
import sys
import subprocess as sp

def main():
    while True:
        file_name = str(input("monkey@monkey:/home/monkey$ file "))
        if file_name == "app.py":
            continue
        else:
            try:
                #output = sp.check_output(f"file {file_name}", shell=True).decode("utf-8")
                os.system("file " + file_name)
                ##print(output.strip())
            except Exception as e:
                print(e)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        try:
            print()
            sys.exit(0)
        except SystemExit:
            print()
            os._exit(0)
