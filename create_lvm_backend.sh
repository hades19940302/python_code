#!/bin/bash

dd if=/dev/zero of=/var/lib/cinder/vg_cinder.img bs=1M count=1024
losetup /dev/loop0 /var/lib/cinder/vg_cinder.img 
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

cinder type-key lvm set volume_backend_name=lvm

sleep 1

service openstack-cinder-volume restart
service openstack-nova-compute restart
enabled_backends = lvm
[lvm]
volume_driver = cinder.volume.drivers.lvm.LVMVolumeDriver
volume_group = vg_cinder
iscsi_protocol = iscsi
iscsi_helper = lioadm
volume_backend_name = lvm


service openstack-nova-compute restart


cinder-manage service remove cinder-volume con2@lvm
cinder-manage service remove BINARY_NAME HOST_NAME