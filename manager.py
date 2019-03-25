import subprocess

def system(command_string):
    subprocess.call(["/usr/bin/env", "bash", "-c", command_string])

if __name__ == "__main__":
    system("echo hello, world")
