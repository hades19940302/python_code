#!/bin/bash

dd if=/dev/zero of=/home/vg_cinder.img bs=1M count=307200
												   122880
losetup /dev/loop0 /home/vg_cinder.img 
partprobe /dev/loop0
pvcreate /dev/loop0
vgcreate vg_cinder /dev/loop0

sleep 1

sed -i '/enabled_backends/a\enabled_backends = lvm' /etc/cinder/cinder.conf 
echo "[lvm]" >> /etc/cinder/cinder.conf
echo "lvm_type = default" >> /etc/cinder/cinder.conf
echo "iscsi_helper = tgtadm" >> /etc/cinder/cinder.conf
echo "volume_group = vg_cinder" >> /etc/cinder/cinder.conf
echo "volume_driver = cinder.volume.drivers.lvm.LVMVolumeDriver" >> /etc/cinder/cinder.conf
echo "volume_backend_name = lvm" >> /etc/cinder/cinder.conf

cinder type-create lvm
cinder type-key lvm set volume_backend_name=lvm

sleep 1

service openstack-cinder-volume restart
service openstack-nova-compute restart
enabled_backends = lvm
enabled_backends
[lvm]
volume_driver = cinder.volume.drivers.lvm.LVMVolumeDriver
volume_group = vg_cinder
iscsi_protocol = iscsi
iscsi_helper = lioadm
volume_backend_name = lvm


service openstack-nova-compute restart


cinder-manage service remove cinder-volume con2@lvm
cinder-manage service remove BINARY_NAME HOST_NAME

openstack compute service list
cinder reset-state 86645f-1b48-480d-9a32-ccf4c0dcd1 --state available
neutron net-delete 6a89b2b5-0c34-49f1-b3fe-e81c653a283f
service neutron-dhcp-agent restart
：.,$d
neutron agent-list  
rabbitmqctl cluster_status
/sbin/service rabbitmq-server start

glance image-create --name CentOS_64_template_newest --container-format bare --disk-format qcow2 --file /home/CentOS_64_template_newest-disk1.qcow2 --progress

select id, status, display_name from volumes where id='499c58d9-82ae-4ca4-91b5-7a6954896bdf';


update volumes set deleted=1 where id='499c58d9-82ae-4ca4-91b5-7a6954896bdf';
yum install python-pip
pip install shadowsocks
ssserver -p 8388 -k password -m aes-256-cfb  --log-file /tmp/ss.log -d start
iptables -A INPUT -p tcp --dport 8388 -j ACCEPT


ovs-vsctl del-port br-enp9s0f0 enp9s0f0
		  add-port
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'pwssw0rd' WITH GRANT OPTION;

		  