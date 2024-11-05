import os
import time

def main():
    # tempdir = "output/reports/temp/%stemp" % time.strftime("%y%m%d-%H%M%S")
    os.system("pytest")

if __name__ == '__main__':
    main()