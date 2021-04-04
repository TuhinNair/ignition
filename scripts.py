import subprocess


def run_cmd(cmd):
    subprocess.run(cmd.split(" "))


def unittest():
    """
    run all unittests
    """
    run_cmd("python -u -m unittest discover")
