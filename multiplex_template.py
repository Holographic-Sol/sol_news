import subprocess

crawler = ''

# Subprocess Info
info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0

cmd = 'python '+crawler
print('running command:', cmd)
xcmd = subprocess.Popen(cmd, shell=False, startupinfo=info, stdout=subprocess.PIPE)
while True:
    output = xcmd.stdout.readline()
    if output == '' or xcmd.poll() is not None:
        break
    if output:
        output = output.strip()
        output = str(output).replace("b'", '')
        output = str(output).replace("'", '')
        print(output)
        rc = xcmd.poll()
