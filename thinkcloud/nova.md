# NOVA

* 激活环境变量：
```shell
source /etc/kolla/admin-openrc.sh
```

* 查询虚拟机id 或者name：
```shell
nova list

```

* 修改虚拟机状态
```shell
nova reset-state <name> --active
```

* 关闭虚拟机
```shell
nova stop <name>
```

* 启动虚拟机
```shell
nova start <name>
```