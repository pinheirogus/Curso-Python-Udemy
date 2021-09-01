import subprocess

# Windows apenas - ping 127.0.0.1

proc = subprocess.run(
    [   'ping', '127.0.0.1' ],
    capture_output = True,
    text = True
)

# print(proc.stderr)
# print(proc.stdout)
# print(proc.returncode)
# print(proc.args)

saida = proc.stdout
saida = saida.replace('TTL', 'Gustavo Pinheiro')

print(saida)