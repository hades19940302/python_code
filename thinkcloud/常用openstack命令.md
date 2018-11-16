# openstack
## 查看宿主机网桥

```shell
brctl show
```
## virsh 
```shell
virsh list
virsh edit id
```
## neutron  ovs 配置
```shell
ovs-vsctl show
```
## ovc 转发规则表
```shell
 ovs-ofctl dump-flows br-int
 ovs-ofctl dump-flows br-tun
```
获取br-int 上port
```shell
ovs-vsctl list-ports
```
selinux
```shell
getenforce 
setenforce 0
```


