                          图片处理脚本说明


1、功能：实现某一文件夹下所有JPG文件的显示-截取-保存
2、使用方法：
    (1)此脚本基于python2.7-win32版本，如果已经安装python2.7-win64，请卸载重新安装win32版本。
        (关于查看自己版本：cmd下进入python交互环境。
        >>>import platform
        >>>platform.architecture()
        根据显示信息确定版本。)
    (2)安装依赖：pip install -r requirements.txt
    (3)配置图片所在文件夹：修改open_image.py中第94行，udir_of_images替换成你图片所在文件夹目录，
    同时，请在当前目录下新建big和small文件夹，用于存储截图。
    (4)运行：python open_image.py
       进入操作页面：
       1、选择截取位置
       2、鼠标左键点击✔
       3、在choice选择small or big
       4、单张图片处理完毕，点击鼠标右键，然后鼠标左键点击close，进入下一张图片处理流程，以此类推。

    (注意：此脚本不存在撤销or暂停，如非脚本原因出现任何问题，请自行处理。)
    同时欢迎提Issues或直接联系我。