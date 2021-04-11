from ignition.toolchain.tool import Tool
from pathlib import Path
import subprocess
import os


class Git(Tool):
    @property
    def name(self):
        return "git"

    def register_arguments(self, parser_handler):
        parser_handler.add_argument(
            "--first-name",
            dest="first_name",
        )
        parser_handler.add_argument(
            "--last-name",
            dest="last_name",
        )
        parser_handler.add_argument(
            "--email",
            dest="email",
        )

    def process(self, args):
        if args.first_name is None:
            print("git needs a value for first_name")
            return
        if args.last_name is None:
            print("git needs a value for last_name")
            return
        if args.email is None:
            print("git needs a value for email")
            return

        default_template = self.load_default_template_path()
        commit_template_path = os.path.abspath(default_template)
        if args.dry_run:
            self.print_dry_run(
                args.first_name, args.last_name, args.email, commit_template_path
            )
        else:
            self.configure_git(
                args.first_name, args.last_name, args.email, commit_template_path
            )

    def configure_git(self, first_name, last_name, email, commit_template):
        full_name = self.full_name(first_name, last_name)

        self.set_git_config_name(full_name)
        self.set_git_config_email(email)
        self.set_git_commit_template(commit_template)

    def print_dry_run(self, first_name, last_name, email, commit_template):
        print("[git] The following changes will be made:")
        full_name = self.full_name(first_name, last_name)
        print(f"[git] git.user.name={full_name}")
        print(f"[git] git.user.email={email}")
        print(f"[git] git.commit.template={commit_template}")

    def full_name(self, first_name, last_name):
        return f"{first_name} {last_name}"

    def set_git_config_name(self, name):
        cmd = "git config --local --replace-all user.name".split(" ")
        cmd.append(f"{name}")
        process = subprocess.run(cmd)
        if process.returncode != 0:
            print("error setting git config name")

    def set_git_config_email(self, email):
        cmd = f"git config --local --replace-all user.email {email}".split(" ")
        process = subprocess.run(cmd)
        if process.returncode != 0:
            print("error setting git config email")

    def set_git_commit_template(self, template_file):
        cmd = f"git config --local --replace-all commit.template {template_file}".split(
            " "
        )
        process = subprocess.run(cmd)
        if process.returncode != 0:
            print("error setting git config commit template")

    def load_default_template_path(self):
        return Path("ignition/toolchain/git_template/ignition_default_git_commit.txt")
