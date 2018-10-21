步骤一：新建一个Web框架工程[website]
    >django-admin startproject [website]
    ============================================================
    website         外层目录，名字可以更改
        website         工程目录，保存代码和文件
            init.py         一个将mysite定义为包的空文件
            [settings.py     部署和配置整个工程的配置文件（配置文件）]
            [urls.py         URL路由的声明文件（路由文件）]
            wsgi.py         基于WSGl的Web服务器的配置文件
        manage.py       一个与Django工程进行交互的命令工具

步骤二：修改工程，增加功能
    1、创建一个具体的应用
        \>python manage.py startapp helloapp
    2、修改应用的views.py
        views.py中包含对某个HTTP请求（url）的响应
    3、修改url路由[website——urls.py]
        在urls.py中指定URL与处理函数之间的路径关系
        路由：URL与处理函数的关联
    2、解惑
        2.1 工程（project）和应用（app）什么关系呢？
            工程对应于一个网站，是配置和应用的集合
            应用对应于特定功能，是具体功能的载体
            配置和功能分离是高度模块化的体现

步骤三：调试运行Web框架（在[website]工程目录下）
    在mysite工程目录下，\>python manage.py runserver

=======================================================================
两个工具
    1、django-admin  Django框架全局的管理工具
        \>django-admin <command>[options]
            建立并管理Django工程
            建立并管理Django工程使用的数据库
            控制调试或日志信息
            运行并维护Django工程
    2、manage.py
        \>python manage.py <command>[options]