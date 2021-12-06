import os
print('Script de instalação iniciado')

#   ultilitários
os.system('apt install -y qbittorrent')

#   Ferramentas de programação
os.system('apt install -y git')

#   machines and docker
os.system('apt install -y virtualbox-qt')
os.system('apt install -y vagrant')
os.system('apt install -y ansible')
os.system('apt install -y docker.io')
os.system('apt install -y docker-compose')

#   
os.system('apt install -y anydesk')