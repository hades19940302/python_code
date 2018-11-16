#CEPH

##  Ceph 存储集群至少需要一个 Ceph Monitor 和两个 OSD 守护进程。而运行 Ceph 文件系统客户端时，则必须要有元数据服务器（ Metadata Server ）。

## Ceph OSDs

* Ceph OSD 守护进程（ Ceph OSD ）的功能是存储数据，处理数据的复制、恢复、回填、再均衡，并通过检查其他OSD 守护进程的心跳来向 Ceph Monitors 提供一些监控信息。当 Ceph 存储集群设定为有2个副本时，至少需要2个 OSD 守护进程，集群才能达到 active+clean 状态（ Ceph 默认有3个副本，但你可以调整副本数）。
* Ceph Monitor维护着展示集群状态的各种图表，包括监视器图、 OSD 图、归置组（ PG ）图、和 CRUSH 图。 Ceph 保存着发生在Monitors 、 OSD 和 PG上的每一次状态变更的历史信息（称为 epoch ）。
*  Ceph 元数据服务器（ MDS ）为 Ceph 文件系统存储元数据（也就是说，Ceph 块设备和 Ceph 对象存储不使用MDS ）。元数据服务器使得 POSIX 文件系统的用户们，可以在不对 Ceph 存储集群造成负担的前提下，执行诸如 ls、find 等基本命令。

## CEPH 于OpenStack
* 所有的计算节点共享存储，迁移时不需要拷贝根磁盘，即使计算节点挂了，也能立即在另一个计算节点启动虚拟机（evacuate）。

* 利用COW（Copy On Write)特性，创建虚拟机时，只需要基于镜像clone即可，不需要下载整个镜像，而clone操作基本是0开销，从而实现了秒级创建虚拟机。

* Ceph RBD支持thin provisioning，即按需分配空间，有点类似Linux文件系统的sparse稀疏文件。创建一个20GB的虚拟硬盘时，最开始并不占用物理存储空间，只有当写入数据时，才按需分配存储空间。

## CEPH RBD功能
* ceph的rbd功能核心对象微块设备，对应openstack当中的volume，即cinder管理部分，不过ceph当中成为image，ceph当中还有一个pool概念，类似openstack当中namespace，不同的poll可以定制不同的副本数量，pg数量，放置策略等。每个image必须指定pool，image的命名规范为pool_name/image_name@snapshot,比如openstack/test_volume@test_snap,表示在openstack pool当中的test volume的快照test_snap,因此以下两个命令的效果相同。<br>
```shell
rbd snap create --pool openstack --image test-image --snap test-snap
rbd snap create openstack/test-image@test-snap
```

* 在openstack pool当中创建一个1G的image，
```shell
rbd -p openstack create --size 1024 int32bit-test-1
```
* image支持快照功能，即snapshot，创建一个快照即保存当前image的状态，相当于git commit，用户可以随时将image回滚到快照任意点上，相当于git reset。创建快照命令：
```shell
rbd -p openstack snap create int32bit-test-1@snap-1
```
* 查看rbd列表：

```shell
rbd -p openstack ls -l | grep int32bit-test
int32bit-test-1        1024M 2
int32bit-test-1@snap-1 1024M 2
```

* 基于快照创建一个image，成为clone，clone不会立即复制原来的image，而是COW策略，即写时候copy，只有当需要写入一个对象时候，才从parent中copy那个对象到本地，因此copy也是秒级完成，并且需要注意的是，同一个快照创建的所有image，共享快照之前的image，因此clone之前我们必须保护快照，被保护快照不允许删除，clone类似git branch，clone一个image命令如下：

```shell
rbd -p openstack snap protect int32bit-test-1@snap-1
rbd -p openstack clone int32bit-test-1@snap-1 int32bit-test-2
```

* 我们可以查看一个image的子image(children)有哪些，也能查看一个image是基于哪个image clone的(parent)

```shell
$ rbd -p openstack children int32bit-test-1@snap-1
openstack/int32bit-test-2
$ rbd -p openstack info int32bit-test-2 | grep parent
parent: openstack/int32bit-test-1@snap-1
```

* 不断地创建快照并clone image，就会形成一条很长的image链，链很长时，不仅会影响读写性能，还会导致管理非常麻烦。可幸的是Ceph支持合并链上的所有image为一个独立的image，这个操作称为flatten，类似于git merge操作，flatten需要一层一层拷贝所有顶层不存在的数据，因此通常会非常耗时。

```shell
$ rbd -p openstack flatten int32bit-test-2
Image flatten: 31% complete...
```
## Rbd image是动态分配存储空间，通过du命令可以查看image实际占用的物理存储空间:
```shell
$ rbd du int32bit-test-1
NAME            PROVISIONED   USED
int32bit-test-1       1024M 12288k
```
## 删除image必须删除快照，保证没有依赖的children
```shell
rbd -p openstack snap unprotect int32bit-test-1@snap-1
rbd -p openstack snap rm int32bit-test-1@snap-1
rbd -p openstack rm int32bit-test-1
```

## Cinder简介
* Cinder是OpenStack的块存储服务，类似AWS的EBS，管理的实体为volume。Cinder并没有实现volume provide功能，而是负责管理各种存储系统的volume，比如Ceph、fujitsu、netapp等，支持volume的创建、快照、备份等功能，对接的存储系统我们称为backend。只要实现了cinder/volume/driver.py中VolumeDriver类定义的接口，Cinder就可以对接该存储系统。
* Cinder不仅支持本地volume的管理，还能把本地volume备份到远端存储系统中，比如备份到另一个Ceph集群或者Swift对象存储系统中，本文将只考虑从源Ceph集群备份到远端Ceph集群中的情况。

