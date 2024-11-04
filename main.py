import os
import time

def main():
    tempdir = "output/reports/temp/%stemp" % time.strftime("%y%m%d-%H%M%S")
    os.system("pytest --alluredir %s" % tempdir)
    os.system("allure generate %s"
              " -o output/reports/allure_report --clean" % tempdir)

if __name__ == '__main__':
    main()