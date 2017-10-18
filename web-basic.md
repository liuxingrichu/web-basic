web开发三个组成部分：
（1）html 裸人
    1、一套浏览器识别规则
    2、开发人员
        需要掌握html规则
        开发后台运行程序
            --书写html文件（起到模板作用）
            --数据库获取数据，替换到html文件指定位置（Web框架）
    3、本地测试
        方式一：直接用浏览器打开
        方式二：Pycharm打开测试
    4、编写html文件
        --doctype对应关系
        --html标签，标签内部可以写属性，该标签仅能写一个
        --注释方法： <!-- 注释的内容 -->
    5、标签分类
        自动闭合标签(比较少)
            <meta charset="UTF-8"/>
            <br />
        主动闭合标签
            <title>人生摆渡</title>
    6 head标签
        <meta /> 编码、调转、刷新、关键字、描述、IE兼容
            <meta http-equiv="X-UA-COMPATIBLE" content="IE=IE9;IE=IE8;"/>
        title标签
        <link />搞图标，欠
        <style /> 见CSS
        <script>欠
    7 body标签
        &nbsp;空格&gt;大于&lt;小于
        h标签：标题
        p标签：段落
        br标签：换行 
        标签分类：
            行内标签
                span（白板：无特殊特性）
            块级标签
                h标签（加大加粗）、p标签（段落之间有间距）、br标签、
                div标签（白板）
            区分方法：
                chrome浏览器 右键-》元素审查-》点击放大镜图标-》移动鼠标来查看
                    该方式可以用于定位元素、查看样式。
        标签之间可以嵌套
        标签存在的意思：
            方便定位、操作；CSS操作；JS操作
        chrome审查元素
            方便定位和查看样式
        input系列 + form标签
            type="text"     有name、value属性
            type="password" 有name、value属性 
            type="button"   有value属性
            type="submit"   有value属性
            type="radio"    有value、checked（仅一个）、name属性（name相同则互斥）
            type="checkbox" 有value、checked（可多个）、name属性（name可用于批量获取数据）
            type="file"     依赖form表单中的enctype="multipart/form-data"属性
            type="reset"    重置
            <textarea>默认值</textarea>    有name属性
            select标签       有name属性，内部有option value，size多行显示，multiple可选中多行
        a标签（不提交到后台）
            使用场景：
            （1）超链接，实现调转
            （2）锚，锚点 href="#某标签的ID" 注：标签ID不可重复
        img标签属性：
            src     图片来源
            title   提示
            alt     图片找不到时的提示字符
        列表标签
            ul  标点模式
                li 
            ol  数字模式
                li 
            dl
                dt  标题
                dd  内容
        table表格标签
           thead    表头
                tr  行
                    th  列
           tbody    表内容
                tr  行
                    td  列
           colspan='n'  行内合并n个单元格
           rowspan='n'  跨行合并n个单元格
        label标签
            点击文字时，使关联的id的标签，获取光标
            一般配合input标签使用 
        fieldset标签
            legend 生成边框
    8 get方法与post方法的区别
    （1）get方法将输入的内容，填充到url中，url上内看到填写内容，再发放到服务端；
        post方法将输入内容，填充到body中，再发放到服务端。
    （2）get方法和post方法传输的内容，都可以通过抓包方式，获取内容，
        不存在那种方式更安全之说。
    需要记忆20个标签左右
    
（2）CSS  衣着
    颜色、位置
    编写CSS样式：
    1. 在标签上，设置style属性
    2. head标签中，书写style标签
        -id选择区（不推荐使用）
            #i1{
                background-color:red;
                height: 49px;
            }
        - class选择区
            .名称{
               ...
               }
            <标签 class="名称">xx</标签>
        - 标签选择器
            div{
                ...
            }
            所有div标签设置上此样式
        - 层级选择器(空格)
           span div .c2{
                ...
           }
        - 组合选择器（逗号）
            .c1 .c2 .c3{
                ...
            }
        - 属性选择器
            对选择到的标签，再通过属性进行一次筛选
        PS：
            优先级：标签上的style优先，编写顺序，就近原则（下面的先）
    2.5 css样式也可以写在css文件中
        <link rel="stylesheet" href="commons.css"/>
    3.注释
        /*
        xxx
        */
    4.边框
        宽度、样式、颜色（border：4px solid red）
        左右上下
    5 常用格式
        height               高度 
        width                宽度（像素、百分比）
        font-size            字体大小 
        text-align:center    水平方向居中
        line-height          垂直方法根据标签高度居中
        font-weight          字体加粗
        color                字体颜色
    6 float
        可实现标签浮动，块级标签也可以堆叠
        父标签控制浮动子标签：
            <div style="clear:both;"></div>
    7 display
        display: none;      让标签不显示
        display: inline;    转行内标签
        display: block;     转块级标签
        display: inline-block;
            标签具备行内标签的属性，同时可以设置高度、宽度、padding、margin
        *行内标签
            无法设置高度、宽度、padding、margin
        *块级标签
            可设置高度、宽度、padding、margin
    8 边距padding margin
        内边距：padding
        外边距：margin
        margin: 8px auto    居中，auto是左右，8px为上下
        margin: auto        上下左右居中
        
以上内容重点回顾：
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

CSS补充：
1 position
    fixed
        作用：固定在页面的某个位置
    relative + absolute
        <!--absolute很少单独使用-->
        <!--单独使用relative，与没使用一样-->
        <!--relative + absolute 子标签是相对于父标签定位的-->
        <div style="position:relative;">
            <div style="position:absolute; left:0; top:0;"></div>
        </div>
2 z-index 
    层次显示顺序控制 越大越在前面
3 opacity 
    透明度 0-1，越小越透明 
4 overflow
    auto   图片显示相应尺寸，同时带滚动条
    hidden 图片隐藏，仅显示裁剪的尺寸
5 hover
    当鼠标移动到当前标签上时，属性才生效
6 background-image    图片作为背景，默认重复放满标签空间
    background-image:url('rich.jpg') 图片地址
7 background-repeat 重复机制
    repeat-x    x轴方向重复
    repeat-y    y轴方向重复
    no-repeat   不重复
8 background-position   通过移动坐标，显示不同图标
    background-position-x: 0;       表示x轴
    background-position-y: -59px;   表示y轴
    background-position: 0 -59px;   分别表示x轴、y轴
9 background    简写方式，有利于避免代码重复编写
    background: red url(chouti.png) 0 -60px no-repeat; 背景色 图标来源 x轴 y轴 不重复 
    
（3）JS   动态属性
    独立的编程语言，而浏览器具有解析js的功能

1 JavaScript代码的存在形式
    a)html中
    b)js文件中
2 JavaScript代码在html文件中的位置
    a) JavaScript代码最好放在body标签中的最下方（推荐）
        例如：
            <body>
                // html或者CSS代码
                // JavaScript 代码
            </body>
        原因：JS是实现动态效果的，页面解析顺序是从上到下的。
    b）html的头部，例如
         <head>
                <script>
                    // JavaScript代码
                </script>
                // 或者
                <script type="text/javascript">
                    // JavaScript代码
                </script>
                // 或者
                <script src='js文件路径'></script>
         </head>
3 注释
  单行注释  //xxx
  多行注释  /* xxx */
  
4 定时器
    setInterval('执行的JS代码', 间隔时间);  //间隔时间以毫秒为单位
    
5 书写JS代码的方式
   a) 书写在html文件中，再执行
   b）临时书写，可在浏览器的console终端上
    浏览器-》右键-》审查元素-》Console

6 变量
      python:
        name = 'test'
      JavaScript:
        name = 'test'       // 默认，全局变量
        var name = 'test'   // 局部变量

7 基本数据类型
    数字
        a = 10;
        str1 = '123';
        i = parseInt(str1);     // 字符串转整型
        j = parseFloat(str1);   // 字符串转浮点型
    字符串
        字符串是不可修改的
        str2 = 'today';
        str2.charAt(0);         // 取字符串数组中的0号坐标字符
        str2.charAt(4);
        str2.substring(2,4);    // 取字符串数组中[2,4]坐标的字符子串
        str2.length;            // 获取字符串长度
        obj = '  1A   2a  ';
        obj.trim();             //移除两边的空白
        obj.trimLeft();         //移除左边的空白
        obj.trimRight();        //移除右边的空白
        obj.concat('1', ...)    //拼接
        obj.indexOf(子串, start)      //从start坐标开始向右查询，子串所在的坐标
        obj.lastIndexOf(子串, start)  //从start坐标开始向左查询，子串所在的坐标
        obj.slice(start, end)   //切片(start, end]
        obj.toLowerCase()       //字母转小写
        obj.toUpperCase()       //字母转大写
    布尔类型
        true    小写
        false   小写
        &&      与
        ||      或
        ==      相等
        !=      不相等
        ===     值与类型相等
        !==    不相等
    数组
        a = [11, 22, 22, 33]
        a.length;           //长度
        a.push(6);          //在尾部追加一个元素
        a.pop();            //从尾部取一个元素
        a.unshift(1);       //在头部添加一个元素
        a.shift();          //在头部取一个元素
        a.slice(开始坐标, 删除的个数, value)    //可实现插入。删除。替换
        obj = [1, 2, 3];
        obj.splice(1, 1 ,0); //[1, 2, 3]替换成[1, 0, 3]
        obj.splice(1,1);     //[1, 0, 3]删除成[1, 3]
        obj.splice(2,2, 6);  //[1, 3]插入成[1, 3, 6]，每次仅能插入一个，start位置可以有跨度
        a.slice(start, end); //切片（start,end]
        a.reverse();         //反转
        a.join('-');         //用‘-’，将数组连接成一个字符串
        a.concat('123');     //数组拼接
        a.sort();            //数组排序
    字典
        a = {'k1':'v1', 'k2':'v2'}
        
参阅：http://www.cnblogs.com/wupeiqi/articles/5602773.html

8 条件语句
    if(条件)
    {}
    else if(条件)
    {}
    else
    {}
    
9 for循环
    // 方式一： 循环元素是下标
    var a = [11, 22, 33, 44];
    for (var item in a)
    {
        console.log(item, a[item]);
    }
    var b = {'k1':'v1', 'k2':'v2'};
    for (var item in b)
    {
        console.log(item)
    }
    // 方式二: 类似其他语言, 该方式不支持字典操作
    for (var i=0; i< a.length; i++){
        console.log(a[i]);
    }

10 函数
   function 函数名(形参1，形参2)
   {}
   
   函数名(1,2);
       