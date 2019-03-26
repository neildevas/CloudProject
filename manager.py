import subprocess

def system(command_string):
    subprocess.call(["/usr/bin/env", "bash", "-c", command_string])

def run_in_container(command_string):
    system("docker run ubuntu " + command_string)

if __name__ == "__main__":
    run_in_container("echo hello, world")

    print("\n"+"-"*5+"cleaning up exited containers"+"-"*5)
    system("yes | docker container prune")
