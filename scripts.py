import subprocess


def unittest():
    """
    run all unittests
    """
    subprocess.run(["python", "-u", "-m", "unittest", "discover"])
