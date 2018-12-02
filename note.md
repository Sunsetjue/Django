# Django系统
- 环境
    - python3.6
    - django1.18
- 参考资料
    - [django中文教程](http://python.usyiyi.cn/)
    - django架站的16堂课
# 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list: 显示当前环境安装的包
    - conda env list:显示安装的虚拟环境列表
    - conda create -n env_name python=3.6
    - 激活conda的虚拟环境
        - (Linux)source activate env_name
        - (win) activate env_name
    - pip install django=1.8


# 后台需要的流程

# 创建第一个django程序
- 命令行启动

        django-admin startproject tulingxueyuan
        cd tulingxueyuan
        python manage.py runserver

- pycharm 启动
    - 需要配置

# 路由系统-urls
- 创建app
    - app：负责一个具体业务或者一类具体业务的模块
    - python manage.py startapp teacher

- 路由
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能模块
    - django的信息控制中枢
    - 本质上是接受的URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用了RE
    - URL的具体格式入urls.py中所示
- 需要关注两点:
    1. 接受的URL是什么,即如何用RE对传入URL进行匹配
    2. 已知URL匹配到哪个处理模块

- url匹配规则
    - 从上往下一个一个比对
    - url格式是分级格式，则按照级别一级一级往下比对,主要对应url包含子url的情况
    - 子url一旦被调用，则不会返回到主url
        - `/one/two/three/`
    - 正则以r开头,表示不需要转义，注意尖号(^)和美元符号($)
        - `/one/two/three` 配对 r'^one/
        - `/oo/one/two/three` 不配对 r'^one/"
        - `/one/two/three/` 配对 r'three/$'
        - `/oo/one/two/three/oo/` 不配对 r'three/$"
        - 开头不需要有反斜杠
    - 如果从上向下都没有找到合适的匹配内容，则报错

# 2. 正常映射
- 把某一个符合RE的URL映射到事物处理函数中去
    - 举例如下:
        ```
        from showeast import views as sv

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^normalmap/', sv.normalmap),
        ]

# 3. URL中带参数映射
- 在事件处理代码中需要由URL传入参数,形如 /myurl/param中的param
- 参数都是字符串形式,如果需要整数等形式需要自行转换
- 通常的形式如下:
    ```
      /search/page/432 中的 432需要经常性变换，所以设置成参数比较合适
    ```        ```
# 4. URL在app中处理
- 如果所有应用URL都集中tulingxueyuan/urls.py中,可能导致文件的臃肿
- 可以把urls具体功能逐渐分散到每个app中
    - 从django.conf.urls 导入 include
    - 注意此时RE部分的写法
    - 添加include导入
- 使用方法
    - 确保include被导入
    - 写主路由的开头url
    - 写子路由
    - 编写views函数
- 同样可以使用参数
# 5. URL中的嵌套参数
- 捕获某个参数的一部分
- 例如URL /index/page-3, 需要捕获数字3作为参数
    ```
    url(r'index_1/(page-(\d+)/)?$', sv.myindex_1), #不太好
    url(r'index_2/(?:page-(?P<page_number>\d+)/)?$', sv.myindex_2), #好
    ```
- 上述例子会得到两个参数,但 ?: 表明忽略此参数

# 6. 传递额外参数
- 参数不仅仅来自以URL,还可能是我们自己定义的内容
    ```
    url(r'extrem/$', sv.extremParam, {'name':"sunbin"}),
    ```
- 附加参数同样适用于include语句,此时对include内所有都添加


# 7. URL的反向解析
- 防止硬编码
- 本质上是对每一个URL进行命名
- 以后再编码代码中使用URL的值，原则上都应该使用反向解析

# views 视图
# 1. 视图概述
- 视图即视图函数,接收web请求并返回web响应的事物处理函数.
- 响应指符合http协议要求的任何内容,包括json,string, html等
- 本章忽略事务处理,重点在如何返回处理结果上
# 2 其他简单视图
- django.http给我们提供类很多和HttpResponse类似的简单视图,
通过查看django.http代码我们知道,
- 此类视图使用方法基本类似,可以通过return语句昨晚直接反馈返回给浏览器
- Http404为Exception子类,所以需要raise使用

# 3. HttpResponse详解
- 方法
    - init ：使用页内容实例化HttpResponse对象
    - write(content)：以文件的方式写
    - flush()：以文件的方式输出缓存区
    - set_cookie(key, value='', max_age=None, expires=None)：设置Cookie
       -  key,value都是字符串类型
       -  max_age是一个整数，表示在指定秒数后过期
       -  expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期，注意datetime和timedelta值只有在使用PickleSerializer时才可序列化
       -  max_age与expires二选一
       -  如果不指定过期时间，则两个星期后过期
    - delete_cookie(key)：删除指定的key的Cookie，如果key不存在则什么也不发生

# 4. HttpResponseRedirect
   - 重定向，服务器端跳转
   - 构造函数的第一个参数用来指定重定向的地址
   - 案例 ShowViews/views.py
        ```python
           # 在 east/urls中添加一下内容
           url(r'^v10_1/', views.v10_1),
           url(r'^v10_2/', views.v10_2),
           url(r'^v11/', views.v11, name="v11"),
        ```
        ```python
        # /east/ShowViews/views中添加一下内容
        def v10_1(request):
            return HttpResponseRedirect("/v11")

        def v10_2(request):
            return HttpResponseRedirect(reverse("v11"))

        def v11(request):
            return HttpResponse("哈哈，这是v11的访问返回呀")

        ```

# 5.Request对象
- Request介绍
    - 服务器接收到http协议的请求后，会根据报文创建HttpRequest对象
    - 视图函数的第一个参数是HttpRequest对象
    - 在django.http模块中定义了HttpRequest对象的API
- 属性
    - 下面除非特别说明，属性都是只读的
    - path：一个字符串，表示请求的页面的完整路径，不包含域名
    - method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'
    - encoding：一个字符串，表示提交的数据的编码方式
        - 如果为None则表示使用浏览器的默认设置，一般为utf-8
        - 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
    - GET：一个类似于字典的对象，包含get请求方式的所有参数
    - POST：一个类似于字典的对象，包含post请求方式的所有参数
    - FILES：一个类似于字典的对象，包含所有的上传文件
    - COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串
    - session：一个既可读又可写的类似于字典的对象，表示当前的会话
        - 只有当Django 启用会话的支持时才可用，
        - 详细内容见“状态保持”
- 方法
    - is_ajax()：如果请求是通过XMLHttpRequest发起的，则返回True

- QueryDict对象
    - 定义在django.http.QueryDict
    - request对象的属性GET、POST都是QueryDict类型的对象
    - 与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况
    - 方法get()：根据键获取值
        - 只能获取键的一个值
        - 如果一个键同时拥有多个值，获取最后一个值
    - 方法getlist()：根据键获取值
        - 将键的值以列表返回，可以获取一个键的多个值
- GET属性
    - QueryDict类型的对象
    - 包含get请求方式的所有参数
    - 与url请求地址中的参数对应，位于?后面
    - 参数的格式是键值对，如key1=value1
    - 多个参数之间，使用&连接，如key1=value1&key2=value2
    - 键是开发人员定下来的，值是可变的
    - 案例/views/v8_get

- POST属性
    - QueryDict类型的对象
    - 包含post请求方式的所有参数
    - 与form表单中的控件对应
    - 表单中空间必须有name属性，name为键，value为值
        - checkbox存在一键多值的问题
    - 键是开发人员定下来的，值是可变的
    - 案例/views/v9_post
        - settings中设置模板位置(已经设置完毕)
        - 设置get页面的urls和函数
        ```python
            # east/urls.py
            # 需要在路由文件中添加两个路由
            url(r'^v9_get/', views.v9_get),
            url(r'^v9_post/', views.v9_post),
        ```
        ```python

             # ShowViews/views.py
             # 在文件中添加下面两个处理函数
            def v9_get(request):
                return  render_to_response("for_post.html")

            def v9_post(request):
                rst = ""
                for k,v in request.POST.items():
                    rst += k + "-->" + v
                    rst += ","

                return HttpResponse("Get value of POST is {0} ".format(rst))
        ```
        - 添加文件/east/templates/for_post.html
        - 由于安全原因，需要在设置中安全选项中删除csrf设置
        ```python
          # settings.py


            MIDDLEWARE = [
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                  #  下面这句话被注释掉
                #'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ]
        ```
- 手动编写视图
    - 实验目的：
        - 利用django快捷函数手动编写视图处理函数
        - 编写过程中理解视图运行原理
    - 分析：
        - django把所有信息封装入request
        - django通过urls模式把相应请求和事件处理函数链连起来，
            并大request参数传入
        - 在相应的处理函数中，我们需要完成两个部分
            - 处理业务
            - 把返回封装并返回，我们可以使用简单HttpRespones,同样也可以自己处理此功能
    - render
        - 使用模板和一个给定的上下文环境，返回一个渲染后的HttpRespones对象
        - request：django的传入请求
        - template_name：模板名称
        - content_instance：上下文环境
    - render_to_response
        - 根据给定的上下文字典渲染给定模板，返回渲染后的HttpRespones

- 系统内建视图
    - 系统内建视图，可以直接使用
    - 404
        - default.page_not_found(request, template_name='404.html')
        - 系统引发Http404时触发
        - 默认传递request_path变量给模板，即导致错误的URL
        - DEBUG=True则不会调用404， 取而代之的是调试信息
        - 404视图会被传递一个RequestContext对象并且可以访问模板上下文处理器提供的变量

    - 500(server error)
        - default.server_error(request, template_name='500.html')
        - 需要DEBUG=False，否则不能使用
    - 403(HTTP Forbidden)视图
        - defaults.permission_denied(request, template_name='403.html')
        - 通过PermissionDenied触发
    - 400(bad request)视图
        - defaults.bad_request(request,template_name='400.html')
        - DEBUG=False

Models 模型
- ORM
    - ObjectRelationMap:用于实现面向对象编程语言里不同类型系统的数据之间的转换
    - 类对应表格
    - 类中的属性对应表中的字段
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.Model的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用models.xxx不能使用python的
    - 在django中，Models负责跟数据库交互
- django链接数据库
    - 自带默认数据库Sqllite3
        - 关系型数据库
        - 轻量级
    - 建议开发用sqllite3，部署用mysql之类数据库
        - 切换数据库在settings中进行设置
            #django连接mysql
             DATABASES = [
                'default' ={
                    'ENGINE' : 'django.db.backends.mysql',
                    'NAME' : '数据库名',
                    'PASSWORD' : '数据库密码',
                    'HOST' : '127.0.0.1',
                    'PORT' : '3306',
                }
             ]
        - 需要在项目文件下的__init__文件中导入pymysql包

            '''
            # 在主项目的__init__文件中
            import pymysql
            pymysql.install_as_MySQLdb()

# models类的使用
- 定义和数据库表映射的类
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.Model 的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用models.xxx
- 字段常用参数
    1. max_length: 规定数值的最大长度
    2. blank: 是否允许字段为空，默认不允许
    3. null: 在DB中控制是否保存为null，默认为False
    4. default: 默认值
    5. unique: 唯一
    6. verbose_name: 假名
- 数据库的迁移
    1. 在命令行中，生成数据迁移的语句(生成sql语句)
        python3 manage.py makemigrations
    2. 在命令行中，输入数据迁移的指令
        pythons manage.py migrate
        ps: 如果迁移中出现没有变化或者报错，可以尝试强制迁移
    3. 强制迁移命令
        python3 manage.py makemigrations 应用名
        python3 manage.py migrate 应用名
    4. 对于默认数据库，为了避免出现混乱，将自带的sqlite3数据库删除

    - 查看数据库中的数据
    1. 启动命令行： python manage.py shell
    ps: 注意点： 对orm操作分为静态函数和非静态函数两种，静态是指在内存中只有一份
    2. 在命令行中导入对应的映射类
        from应用.models import 类名
    3. 使用object 属性操作数据库，object是模型中实际和数据库进行交互的
    4. 查询命令
        - 类名.objects.all()查询数据库表中的所有内容，返回的结果是一个QuerySet，类似一个列表
        - 类名.objects.filter(条件)

    - 添加数据
    1. 对象 = 类() #使用类实例化对象
    2. 对象.属性 = 值 #给对应的对象的属性赋值
    3. 对象.save() #必须执行保存操作,否则数据没有进入数据库

    python manage.py shell

    from 应用名.models import 类名
    from myapp.models import Teacher

    #实例化对象
    t = Teacher()
    t.name = 'xx'
    t.age = 'xxx'
    t.address = 'xxxx'
    t.save()

    - 常见的查找方法
    1. 通用查找格式: 属性名 __(用下面内容) = 值

    - gt: 大于
    - gte: 大于等于
    - lt: 小于
    - lte: 小于等于
    - range: 范围
    - year: 年份
    - isnull: 是否为空

    2. 查找等于指定值的格式: 属性名 = 值
    3. 模糊查找: 属性名 _ _(使用下面的内容) = 值

    - exact: 精确等于
    - iexact: 不区分大小写
    - contains: 包含
    - startwith: 以..为开头
    - endwith: 以..为结尾

- 数据库表关系
    - 多表联查，利用多个表联合查找某一项信息或者多项信息
    - 1:1 OneToOne
        - 建立关系：在模型任意一边即可，使用OneToOneField
        - add
            - 添加没有关系的一边，直接实例化保存就可以
            - 添加有关系的一边，使用create方法，或者使用实例化，使用实例化注意一一对应的关系
        - query:
            - 由子表查母表：>>> search = Manage.objects.get(manage_name='孙彬').my_school.school_name
                            >>> search
                            '江陵中学'

            - 由母表查子表：>>> search2 = School.objects.get(school_name='江陵中学').manage.manage_name
                            >>> search2
                            '孙彬'
        - change
            - 单个修改用save()
            - 多个修改用update(里面加要修改的内容)
        - delete: 直接用delete删除
    - 1:N OneToMany
        - 一个表格里的一个数据项/对象等。可以对应很多个另一个表格的数据项/对象
        - 建立关系：在多的那边使用ForeignKey
        - add
            - 和一对一的方法类似
        - query
            - 由多的一方向少的一方查找,即由子表查母表：>>> search3 = Teacher.objects.get(teacher_name='刘洋').teacher.school_name
                                                       >>> search3
                                                       '江陵中学'
            - 由母表查子表：系统会自动在母表名称的小写下面直接加上下划线set，用来表示：
                                                        search4 = School.objects.get(school_name='江陵中学').teacher_set.all()
                                                         >>> search4
                                                         [<Teacher: 江宝龙>, <Teacher: 刘洋>]
    - N:N ManyToMany
        - 表示一个表可以拥有对方表格很多数据，反之亦然
        - 建立关系：在任意一方，使用ManyToManyField定义，只需要定义一边
        - add
            - 和一对一的差不多，注意要对应多个
        - query
            - 和一对多差不多

# 模板系统
- 模板：一组相同或相似的页面，在需要个性化的地方进行留白，需要的时候只是用数据填充就可以使用
- 步骤：
    1. 在settings中进行设置：TEMPLATES
    2. 在templates文件夹下编写模板并调用

## 模板-变量
- 变量的表示方法： {{var_name}} var_name表示变量名
- 在系统调用模板的时候，会用相应的数据查找相应的变量名称，如果能找到则填充，或者叫渲染，否则就跳过

## 模板-标签
- for标签：{% for .. in.. %}
    - 用法：

            {% for .. in .. %}
            循环语句
            {% endfor %}
            
- if标签
    - 用来判断条件
    - 用法：
    
            {% if 条件 %}
                条件成立执行语句
            {% elif 条件 %}
                条件成立执行语句
            {% else %}
                以上条件都不成立执行语句
            {% endif %}
            
## csrf标签
- csrf:跨站请求伪造
- 在提交表单的时候，表单也要需要加上 {% csrf_token %}

## session
- 用来应对HTTP的无状态性
- 用来保存用户比较敏感的信息
- 属于request的一个属性
- 常用操作：

      request.session.get(key,defaultValue)
      request.session.clear() 清除session所有值
      request.session[key] = value 赋值
      request.session.flush() 删除当前会话且删除会话里的cookie
     
## 分页
- django提供现成的分页器来对结果进行分页
- from django.core.paginator import Paginator

## 基于类的视图
- 可以针对HTTP协议不同的方法创建不同的函数
- 可以使用Mixin等oop技术
- Mixin
    - 把来自父类的行为或者属性结合在一起
    - 解决多重继承的问题
    
## admin
### 1.创建超级用户进入后台  
    命令:python manage.py createsuperuser   
       
    可以把Django的后台改成中文
    在settings里面改 LANGUAUE_CODE改成'zh-Hans'
                    TIME_ZONE改成'Asia/Shanghai'
### 2.绑定管理模型
    在项目下的admin文件里 将models的模型导入admin文件里
        from xx.models import xx(类，模型)
    注册模型
        admin.site.register(xx)

### 3.设置admin管理类
- 实现方式
    - ModelAdmin
    - 装饰器
- 修改页面显示数量：list_per_page
- 操作选项：actions_on_top/button
- 控制列表中显示的内容：list_display=[] 
- 将方法作为类显示
    - 函数必须有返回值
    - 设置short_description作为显示内容
    - 排序使用admin_order_field
- 关联对象
    - 使用函数

- 右侧过滤器
    - 使用函数来定义

- 搜索框
    - search_field=[]
- 分组显示 
    - fieldsets=(
        ("str",{"fields":["属性",]})
        ("str",{"fields":["属性",]})
        ... ...
    )