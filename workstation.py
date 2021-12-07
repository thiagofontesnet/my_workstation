import os

print('Script de instalação iniciado')

#   work with privileges root
os.system('sudo usermod -aG root thiagofontes')

#   utilities
os.system('apt install -y qbittorrent')
os.system('wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | apt-key add -')
os.system('echo "deb http://deb.anydesk.com/ all main" >> /etc/apt/sources.list.d/anydesk-stable.list')
os.system('apt update')
os.system('apt install -y anydesk')
os.system('')

#   Develops
os.system('apt install -y git')
os.system('git config --global user.name thiagofontesnet')
os.system('git config --global user.email particular@thiagofontes.net')


#   machines and docker
os.system('apt install -y virtualbox-qt')
os.system('apt install -y vagrant')
os.system('apt install -y ansible')
os.system('apt install -y docker.io')
os.system('apt install -y docker-compose')
os.system('chmod 777 /var/run/docker.sock')
os.system('apt install -y curl')
os.system('curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"')
os.system('chmod +x ./kubectl')
os.system('sudo mv ./kubectl /usr/local/bin/kubectl')
os.system('curl -Lo minikube https://storage.googleapis.com/minikube/releases/v1.12.1/minikube-linux-amd64 \ && chmod +x minikube')
os.system('sudo install minikube /usr/local/bin/')
os.system('')
os.system('')
os.system('')
os.system('')
os.system('')




#   
