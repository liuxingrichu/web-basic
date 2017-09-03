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
        <style />欠
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
        input系列
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
    8 get方法与post方法的区别
    （1）get方法将输入的内容，填充到url中，url上内看到填写内容，再发放到服务端；
        post方法将输入内容，填充到body中，再发放到服务端。
    （2）get方法和post方法传输的内容，都可以通过抓包方式，获取内容，
        不存在那种方式更安全之说。
        
        
        
    需要记忆20个标签左右  
（2）CSS  衣着
    颜色
    位置
（3）JS   动态属性

