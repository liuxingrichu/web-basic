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

（3）JS   动态属性

