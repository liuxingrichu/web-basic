# html #
框架

1. 一套浏览器识别规则
2. 开发人员


	    需要掌握html规则
	    开发后台运行程序
	        --书写html文件（起到模板作用）
	        --数据库获取数据，替换到html文件指定位置（Web框架）
3. 本地测试

		方式一：直接用浏览器打开
		方式二：Pycharm打开测试
4. 编写html文件


	    --doctype对应关系
	    --html标签，标签内部可以写属性，该标签仅能写一个
	    --注释方法： <!-- 注释的内容 -->
5. 标签分类


	    自动闭合标签(比较少)
	        <meta charset="UTF-8"/>
	        <br />
	    主动闭合标签
	        <title>人生摆渡</title>
6. head标签


	    <meta /> 编码、调转、刷新、关键字、描述、IE兼容
	        <meta http-equiv="X-UA-COMPATIBLE" content="IE=IE9;IE=IE8;"/>
	    title标签
	    <link />搞图标，
	    <style /> 见CSS
	    <script> 见JavaScript
7. body标签


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
8.  input系列 


		一般结合form标签，一起使用
        type="text"     有name、value属性，placeholder属性（信息提示）
        type="password" 有name、value属性 
        type="button"   有value属性
        type="submit"   有value属性
        type="radio"    有value、checked（仅一个）、name属性（name相同则互斥）
        type="checkbox" 有value、checked（可多个）、name属性（name可用于批量获取数据）
        type="file"     依赖form表单中的enctype="multipart/form-data"属性
        type="reset"    重置
9. form标签

		生成表单
		使用场景：提交数据
		特性：提交后，页面会刷新
		参数：
			action 指定URL
			method 指定交互模式，一般是post和get

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
    
10. textarea

		<textarea>默认值</textarea>    有name属性
11.  select标签

作用：生成下拉框 
	  
		有name属性，内部有option value，size多行显示
		multiple可选中多行
		例如：
			<select name="group_id">
	            <option value="1">DB</option>
	            <option value="2">QA</option>
	            <option value="3">MQ</option>
	        </select>

12. a标签（不提交到后台）


        使用场景：
        （1）超链接，实现调转
        （2）锚，锚点 href="#某标签的ID" 注：标签ID不可重复
		target="_blank" 在新标签页中打开链接

13.   img标签


        src     图片来源
        title   提示
        alt     图片找不到时的提示字符
14.   列表标签

        ul  标点模式
            li 
        ol  数字模式
            li 
        dl
            dt  标题
            dd  内容
15.   table表格标签


	       thead    表头
	            tr  行
	                th  列
	       tbody    表内容
	            tr  行
	                td  列
	       colspan='n'  行内合并n个单元格
	       rowspan='n'  跨行合并n个单元格
16.   label标签

        点击文字时，使关联的id的标签，获取光标
        一般配合input标签使用 
17.    fieldset标签

legend 生成边框

需要记忆20个标签左右