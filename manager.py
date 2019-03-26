from subprocess import run, PIPE
import json

# TODO: convert to python3 docker library

def system(command_string):
    completed_process = run(
        ["/usr/bin/env", "bash", "-c", command_string],
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True
    )

    return (
        completed_process.stdout,
        completed_process.stderr,
        completed_process.returncode
    )

def run_in_container(command_string, print_output=False, dont_die=False):
    # create docker cmd
    if dont_die:
        docker_cmd = "docker run ubuntu "
    else:
        docker_cmd = "docker run --rm ubuntu "

    # run use command_string in docker
    stdout, stderr, exit_status = system(docker_cmd + command_string)

    # print_output?
    if print_output:
        if exit_status == 0:
            if stdout != "": print(stdout)
        else:
            print("exit_status: " + str(exit_status))
            if stderr != "": print(stderr)

def kill_exited_containers():
    system("yes | docker container prune")

def all_containers():
    stdout, _, _ = system("docker container list -a")
    lines = [[s for s in line.split(' ')] for line in stdout.splitlines()]

    colnames, lines = lines[0], lines[1:]
    return [{k:v for k,v in zip(colnames, line)} for line in lines]

if __name__ == "__main__":
    run_in_container("echo hello, world", print_output=True, dont_die=True)
    print(all_containers())

    kill_exited_containers()
