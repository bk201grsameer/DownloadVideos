import subprocess

file_path = r"D:\PROJECTS\PythonSockets\ETH\downloadutube\Download\Making a Game in Python with No Experience.mp4"

# Enclose the file path in double quotes within the PowerShell command
print(f'start "{file_path}"')
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
