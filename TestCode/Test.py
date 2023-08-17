import subprocess

file_path = r"D:\PROJECTS\PythonSockets\ETH\downloadutube\Download\3 PYTHON AUTOMATION PROJECTS FOR BEGINNERS.mp4"

# Enclose the file path in double quotes within the PowerShell command
command = ["powershell.exe", f'start "{file_path}"']

terminal = subprocess.Popen(
    command,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE,
)

output, errors = terminal.communicate()  # Capture output and errors

output = output.decode()  # Convert bytes to string
errors = errors.decode()

print("Output:", output)
print("Errors:", errors)
