import subprocess

subprocess.call(["touch","sample.txt"])
subprocess.call(["ls"])
print("Sample file created")

subprocess.call(["rm","sample.txy"])

subprocess.call(["ls"])
print("Sample file Deleted")

