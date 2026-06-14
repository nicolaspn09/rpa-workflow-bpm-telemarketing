import git
import os
import shutil

# URL do repositório que você quer clonar
repo_url = "https://gitlab.dev-COMPANY_NAME.com/COMPANY_NAME/rpa/bpm-tlv.git"

# Diretório onde você quer que o repositório seja clonado
clone_dir = r"\\10.1.1.202\c\rpa\Python\Televendas"

def handleRemoveReadonly(func, path, exc):
    pass # Logica de negocio removida por seguranca corporativa
