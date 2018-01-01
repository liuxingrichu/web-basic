# JS #
动态属性

独立的编程语言，而浏览器具有解析js的功能

## 基本知识

1. JavaScript代码的存在形式

		a)html中
		b)js文件中
2. JavaScript代码在html文件中的位置

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
3. 注释

		  单行注释  //xxx
		  多行注释  /* xxx */
  
4. 定时器

    setInterval('执行的JS代码', 间隔时间);  //间隔时间以毫秒为单位
    
5. 书写JS代码的方式
	   
		a) 书写在html文件中，再执行
		b）临时书写，可在浏览器的console终端上
		浏览器-》右键-》审查元素-》Console

6. 变量

		python:
			name = 'test'
		JavaScript:
			name = 'test'       // 默认，全局变量
			var name = 'test'   // 局部变量

7. 基本数据类型

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
	        str2.substring(2,4);    // 取字符串数组中[2,4）坐标的字符子串
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
        
[参阅](http://www.cnblogs.com/wupeiqi/articles/5602773.html)

8. 条件语句

	    if(条件)
	    {}
	    else if(条件)
	    {}
	    else
	    {}
	    
9. for循环

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

10. 函数


	   function 函数名(形参1，形参2)
	   {}
	   
	   函数名(1,2);
       
11. 分号

	    JS代码，可以不写分号，但建议写；
	    原因：转换工具会压缩代码，节约空间，实现流量的节省、效率的提升，同时可以提升理解、避免代码问题。
## Dom ##
	1 查找标签
	    a)直接查找
	        <!--标签id唯一-->
	        document.getElementById('i1');          根据id属性获取唯一标签
	        document.getElementsByTagName('a');     根据标签名获取标签集合
	        document.getElementsByName('nice');     根据name属性获取标签集合
	        document.getElementsByClassName('c1');  根据class属性获取标签集合
	    b)间接查找
	        tag = document.getElementById('i1');
	        parentNode          // 父节点
	        childNodes          // 所有子节点
	        firstChild          // 第一个子节点
	        lastChild           // 最后一个子节点
	        nextSibling         // 下一个兄弟节点
	        previousSibling     // 上一个兄弟节点 
	        parentElement           // 父节点标签元素
	        children                // 所有子标签
	        firstElementChild       // 第一个子标签元素
	        lastElementChild        // 最后一个子标签元素
	        nextElementSibling     // 下一个兄弟标签元素
	        previousElementSibling  // 上一个兄弟标签元素
	              
	2 操作标签
	    a）innerText
	        作用：获取标签里的文本内容
	        方法：标签.innerText
	        实现：对标签文件内容重新赋值
	        方法：标签.innerText = "xxxxx";
	    b) className
	        tag.className = '样式名';          //对整体样式操作
	        tag.classList.add('样式名');       //添加指定样式
	        tag.classList.remove('样式名');    //删除指定样式
	        PS:
	            <div onclick='func();'>点我</div>
	            <script>
	                function func(){
	                }
	            </script>
	    c) checked
	        检测标签属性
	        check_box.checked
	        设置标签值
	        check_box.checked = false;                    
	
[参阅](http://www.cnblogs.com/wupeiqi/articles/5643298.html)

### Django

- 字符串转对象

	var obj = JSON.parse(data);

- 对象转字符串

	JSON.stringify([1,2, 3])

- json对象，通过点操作

- 页面刷新

	location.reload();
- 页面跳转

	location.href = '/get_host'

- 获取对象值

	$('#edit_form').find('select').val();	
	$(this).parent().prev().prev().text();
	$(this).parent().parent().children().first().text();

- 设置对象值
	
	$('#edit_form').find('select').val("4");

	$('#edit_form').find('select').val(1);

- 绑定事件
	- class

		适合绑定一个或多个

			<tr hid="{{ row.nid }}" bid="{{ row.b_id }}">
				<td>
					<a class="edit">编辑</a>|<a class="delete">删除</a>
				</td>
			</tr>
			
			<script>
			 	$('.edit').click(function(){
			        $('.shade,.edit-modal').removeClass('hide');
			
			        var bid = $(this).parent().parent().attr('bid');
			        var nid = $(this).parent().parent().attr('hid');
			
			        $('#edit_form').find('select').val(bid);
			        $('#edit_form').find('input[name="nid"]').val(nid);
				})
		    </script>

	- id
	
		在一个html中，id要求唯一，仅适合绑定一个
			
			<a id="ajax_submit" >悄悄提交</a>
	
			<script>
			 $('#ajax_submit').click(function(){
				....
			 });
			</script>
	
	- 举例

			CSS
				<style>
			        .hide{
			            display: none;
			        }
			        .shade{
			            ....
			        }
			        .add-modal,.edit-modal{
			            ....
			        }
			    </style>

			html
				<input id="add_host" type="button" value="添加" />
				<div class="shade hide"></div>
			    <div class="add-modal hide">
			        <h3>添加主机信息</h3>
				</div>

			JS
				<script>
					 $(function() {
			             $('#add_host').click(function () {
			                 $('.shade,.add-modal').removeClass('hide');
			             });
					 });
				</script>