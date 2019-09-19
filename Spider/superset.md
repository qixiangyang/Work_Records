$ cd /usr/local/virtual_env/superset # 创建目录
$ virtualenv --no-site-packages superset --python=python  # 创建虚拟环境
$ source /usr/local/virtual_env/superset/bin/activate # 激活虚拟环境

pip install superset -i https://pypi.tuna.tsinghua.edu.cn/simple

# 创建管理员账号
fabmanager create-admin --app superset 
若报错和pandas相关，执行 pip install pandas==0.23.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
安装完成后，重新执行 fabmanager create-admin --app superset 

# 初始化数据库
superset db upgrade
若报错和sqlalchemy相关，执行 pip install SQLAlchemy==1.2.18
安装完成后，重新执行 superset db upgrade

# 载入案例数据
superset load_examples

# 初始化角色和权限
superset init

# 启动服务，端口号 8088，使用 -p 更改端口号
superset runserver -p 8089