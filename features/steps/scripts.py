import subprocess


def run_cmd(cmd, capture_output=False, quiet=False):
    if quiet:
        return subprocess.run(
            cmd.split(" "),
            capture_output=capture_output,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
    return subprocess.run(cmd.split(" "), capture_output=capture_output)