import os
import shutil
import time
from datetime import datetime
import platform

# Descobre a pasta HOME do usuário (Linux/Windows)
HOME = os.path.expanduser("~")
FROM_DIR = os.path.join(HOME, "backupsFrom")
TO_DIR   = os.path.join(HOME, "backupsTo")
LOG_FROM = os.path.join(HOME, "backupsFrom.log")
LOG_TO   = os.path.join(HOME, "backupsTo.log")

# Cria pastas caso não existam
os.makedirs(FROM_DIR, exist_ok=True)
os.makedirs(TO_DIR, exist_ok=True)

# Data limite: arquivos com mais de 3 dias
three_days_ago = time.time() - 3 * 24 * 60 * 60  # timestamp

def get_creation_time(file_path):
    """Retorna timestamp de criação do arquivo, se possível."""
    stat = os.stat(file_path)
    if platform.system() == "Windows":
        return stat.st_ctime
    else:  # Linux/macOS
        # Alguns sistemas suportam birthtime
        try:
            return stat.st_birthtime
        except AttributeError:
            # fallback: usar mtime como referência
            return stat.st_mtime

def format_file_info(file_path):
    """Retorna string com informações do arquivo."""
    stat = os.stat(file_path)
    size = stat.st_size
    creation_time = get_creation_time(file_path)
    modification_time = stat.st_mtime
    return (
        f"Nome: {os.path.basename(file_path)} | "
        f"Tamanho: {size} bytes | "
        f"Criação: {datetime.fromtimestamp(creation_time)} | "
        f"Modificação: {datetime.fromtimestamp(modification_time)}"
    )

separator = "-" * 40  # Linha de separação

print(f"\n=== Listando arquivos em {FROM_DIR} ===")
with open(LOG_FROM, 'a') as log_from:  # 'a' para append
    log_from.write(f"\n{separator}\nExecução em: {datetime.now()}\n{separator}\n")
    for root, _, files in os.walk(FROM_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            info = format_file_info(file_path)
            print(info)
            log_from.write(info + "\n")

print(f"\n=== Removendo arquivos com mais de 3 dias ===")
for root, _, files in os.walk(FROM_DIR):
    for file in files:
        file_path = os.path.join(root, file)
        creation_time = get_creation_time(file_path)
        if creation_time < three_days_ago:
            print(f"Removendo: {file}")
            os.remove(file_path)

print(f"\n=== Copiando arquivos recentes para {TO_DIR} ===")
with open(LOG_TO, 'a') as log_to:  # 'a' para append
    log_to.write(f"\n{separator}\nExecução em: {datetime.now()}\n{separator}\n")
    for root, _, files in os.walk(FROM_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            creation_time = get_creation_time(file_path)
            if creation_time >= three_days_ago:
                shutil.copy2(file_path, TO_DIR)
                info = format_file_info(file_path)
                print(f"Copiando: {file}")
                log_to.write(info + "\n")

print("\n=== Operação concluída! ===")
print(f"Logs gerados:\n - {LOG_FROM}\n - {LOG_TO}\n")