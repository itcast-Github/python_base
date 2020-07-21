```
linux：多用户多任务的OS

ifconfig :查看ip地址

	WINDOWS中使用ipconfig

ping：

	ping 192.168.17.76 测试网络连接是否正常


ssh:远程登录

	ssh python@192.168.17.76
	ssh 用户名@ip

whoami：查看当前用户名

who:查看当前登录的用户信息

exit:退出登录

[ctrl+a 光标移到开始  ctrl+e 光标移到末尾]
useradd 新的用户名 -m -d /home/新用户名 -g 组名

passwd 用户名

su 需要切换的用户名【自己的qilei=》SAKESI4030   laowang=》laowang】
su - 需要切换的用户名, 切换用户后，还会主动跳转到该用户的家目录

python---->laowang----->python

sudo 当需要超级管理员的权限时需要添加，并且在命令行的最前面，后面需要空格
sudo passwd laowang

sudo -s 直接切换到root用户

groupadd YYY 添加一个YYY用户组
groupdel YYY 删除一个组，，，，注意需要sudo

cat /etc/group

groups laowang表示：查看laowang所属的所有用户组

usermod -g YYY laowang 把老王添加到YYY组里面

usermod -a -G XXX laowang 把老王添加到XXX组里面

	-g 和 -G，-g指定的是默认的组

useradd创建的新用户没有sudo，或者切换到root的权限，需要把这个用户添加到adm、sudo组里面才可以


chmod 修改文件的权限

	u：拥有者
	g:同组者
	o：其他人
	a:所有，即u、g、o

	+ 添加权限
	- 去除权限
	= 设定权限

	r:读------>对应的数字是4
	w：写------>对应的数字是2
	x：执行------>对应的数字是1

chmod 777 文件夹，只会修改文件夹的权限为777 ，不会修改里面文件的权限

	-R 会修改文件夹里面所有的文件、文件夹的权限（递归）



了解：mount 挂载命令







vi：
	从命令模式---》编辑模式：i、a、o、I、A、O
	从编辑模式----》命令模式：ESC
	从命令模式----》末行模式：输入一个冒号，即shit+;

	末行模式：
		w保存
		q退出
		！强制

		常用的：
		wq保存退出，等价于   x（小写的x），，，，还等价于在命令模式 shit+2个z(连续点击两次z)
		q!不保存退出

	命令模式：
		hjkl控制上下左右
		M中间位置
		L当前屏幕的最后一行
		yy 复制，8yy：表示从当前光标所在的行开始复制8行
		p 粘贴
		dd 剪切，8dd：表示从当前光标所在的行开始剪切8行

		u 撤销
		ctl+r 反撤销

		G 调到最后1行（===gg）
		15G 表示跳转到第15行
		1G表示跳转到第1行

		gg 跳转到第1行

		w 前跳
		b 后跳
		} 前跳一段
		{ 后跳一段
		其余见文档






```
