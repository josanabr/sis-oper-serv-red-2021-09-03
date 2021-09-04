# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.define "master" do |m|
  	m.vm.box = "ubuntu/focal64"
        m.vm.hostname = "docker.localhost"
        m.vm.network "private_network", ip: "192.168.33.10"
        m.vm.provision "docker"
  	m.vm.provider :virtualbox do |vb|
		vb.customize [ 'modifyvm', :id, '--memory', '4000' ]
		vb.customize [ 'modifyvm', :id, '--cpus', '1' ]
		vb.customize [ 'modifyvm', :id, '--name', 'docker' ]
  	end
  end
  config.vm.define "worker" do |m|
  	m.vm.box = "ubuntu/focal64"
        m.vm.hostname = "docker-worker.localhost"
        m.vm.network "private_network", ip: "192.168.33.11"
#        m.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
  	m.vm.provider :virtualbox do |vb|
		vb.customize [ 'modifyvm', :id, '--memory', '1024' ]
		vb.customize [ 'modifyvm', :id, '--cpus', '1' ]
		vb.customize [ 'modifyvm', :id, '--name', 'docker-worker' ]
  	end
  end
end
