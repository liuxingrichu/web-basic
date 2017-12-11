# CSS
	1 块级标签和行内标签
	2 form标签
	    <!--上传文件需要使用multipart/form-data-->
	    <form action="url（提交的地址）" method="get" enctype="multipart/form-data">
	        <div>块级标签</div>
	        <input  type="text" name="q"/>
	        <input type="text" name="b"/>
	        <!--上传文件-->
	        <input type="file" name="f"/>
	    </form>
	    GET：输入内容拼接到url上
	        http://xxx?q=用户输入的值
	        http://xxx?q=用户输入的值&b=用户输入的内容
	    POST：
	        请求头
	        请求内容
	3 display
	    block; inline; inline-block;
	4 float
	    <div>
	        <div style="float:left;">子标签</div>
	        <!--解决子标签，浮动超出父标签的场景-->
	        <div style="clear:both;"><div>
	    </div>
	5 margin: 0 auto;    外边距
	6 padding   内边距（自身发放变化）


----------
# CSS补充 #
- position
- background
- opacity
- z-index
- hover
- overflow

	实例：输入框右边放置图标

----------
# JavaScript #
    局部变量 var
    基本数据类型
        数字
        字符串
        数组
        字典
        布尔类型
    for循环
    条件语句
        ==
        !=
        ===
        !==
        &&
        ||
    函数的定义
        function func(){
            ......
        }

# Dom #
    查找标签
        直接查找
            $('#id')
            $('.c1').siblings()
        间接查找
    操作标签
        innerText
        checkbox:
            checked
        className
        classList
    事件
        <div onclick="函数(123);"></div>

        <script>
            ......
        </script>
    定时器
        setInterval("函数();", 4000);
    其它
        alert()
        console.log()

# 实例 #
    莅临指导
    多选
    模态对话框
    左侧菜单
    返回顶部



