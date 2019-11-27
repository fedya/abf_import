import subprocess
import os

log = 'import.log'


def print_log(message):
    print(message)
    try:
        logFile = open(log, 'a')
        logFile.write(message + '\n')
        logFile.close()
    except:
        print("Can't write to log file: " + log)


files = []


def get_all_srcrpms():
    path = '/home/omv/srpms'
    for r, d, f in os.walk(path):
        for file in f:
            if '.src.rpm' in file:
                files.append(os.path.join(r, file))


def importer():
    get_all_srcrpms()
    for srcrpm in files:
        try:
            # abf create -b openstack-queens ttembed-1.1-3.el7.src.rpm -v
            subprocess.check_call(
                ['abf', 'create', '-b', 'openstack-queens', srcrpm])
        except subprocess.CalledProcessError as e:
            print(e)
            print_log('import failed for package {}'.format(srcrpm))


importer()
