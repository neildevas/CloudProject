from subprocess import run, PIPE

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

if __name__ == "__main__":
    run_in_container("echo hello, world", print_output=True)
    run_in_container("echo hello world; sleep 5; echo hello, world2", print_output=True)

    kill_exited_containers()
