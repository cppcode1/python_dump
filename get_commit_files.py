# this is the script that prints a commit file names out
import subprocess

commit = subprocess.check_output(["git", "show", "--pretty=", "--name-only", "HEAD~0...HEAD~10"])
print(commit)
commit_array = commit.decode("utf-8")
print(commit_array)
print(type(commit_array))