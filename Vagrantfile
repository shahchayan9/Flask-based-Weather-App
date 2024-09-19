Vagrant.configure("2") do |config|
  # Specify the base box
  config.vm.box = "bento/ubuntu-20.04"
  config.vm.hostname = "weather-app"
  config.vm.network "forwarded_port", guest: 5000, host: 5002

  # Provisioning script
  config.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      source /home/vagrant/venv/bin/activate
      pip install --upgrade pip
      cd /vagrant
      if [ -f requirements.txt ]; then
        sudo pip3 install -r requirements.txt
      fi
      FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000
    SHELL

  # Sync the current directory to /vagrant in the VM
  config.vm.synced_folder ".", "/vagrant"

  # Use VMware Fusion as the provider
  config.vm.provider "vmware_fusion" do |v|
    v.memory = 1024
    v.cpus = 2
    v.gui = true
  end
end