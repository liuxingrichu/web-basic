# CSS #
颜色、位置

## 编写CSS样式 ##
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
3. css样式也可以写在css文件中

    	<link rel="stylesheet" href="commons.css"/>
4. 注释

	    /*
	    xxx
	    */
5. 边框

	    宽度、样式、颜色（border：4px solid red）
	    左右上下
6. 常用格式


	    height               高度 
	    width                宽度（像素、百分比）
	    font-size            字体大小 
	    text-align:center    水平方向居中
	    line-height          垂直方法根据标签高度居中
	    font-weight          字体加粗
	    color                字体颜色
7. float

	    可实现标签浮动，块级标签也可以堆叠
		<div>
	        <div style="float:left;">子标签</div>
	        <!--解决子标签，浮动超出父标签的场景-->
	        <div style="clear:both;"><div>
	    </div>
8. display

	    display: none;      让标签不显示
	    display: inline;    转行内标签
	    display: block;     转块级标签
	    display: inline-block;
	        标签具备行内标签的属性，同时可以设置高度、宽度、padding、margin
	    *行内标签
	        无法设置高度、宽度、padding、margin
	    *块级标签
	        可设置高度、宽度、padding、margin
9. 边距padding margin

	    内边距：padding		内边距（自身发放变化）
	    外边距：margin
	    margin: 8px auto    居中，auto是左右，8px为上下
	    margin: auto        上下左右居中

10. position

	    fixed
	        作用：固定在页面的某个位置
	    relative + absolute
	        <!--absolute很少单独使用-->
	        <!--单独使用relative，与没使用一样-->
	        <!--relative + absolute 子标签是相对于父标签定位的-->
	        <div style="position:relative;">
	            <div style="position:absolute; left:0; top:0;"></div>
	        </div>
11. z-index 

层次显示顺序控制 越大越在前面

12. opacity 

透明度 0-1，越小越透明
 
13. overflow

	    auto   图片显示相应尺寸，同时带滚动条
	    hidden 图片隐藏，仅显示裁剪的尺寸
14. hover

当鼠标移动到当前标签上时，属性才生效

15. background-image    

图片作为背景，默认重复放满标签空间

background-image:url('rich.jpg') 图片地址

16. background-repeat 

重复机制

    repeat-x    x轴方向重复
    repeat-y    y轴方向重复
    no-repeat   不重复

17. background-position   

通过移动坐标，显示不同图标

    background-position-x: 0;       表示x轴
    background-position-y: -59px;   表示y轴
    background-position: 0 -59px;   分别表示x轴、y轴

18. background    

简写方式，有利于避免代码重复编写

	background: red url(chouti.png) 0 -60px no-repeat; 背景色 图标来源 x轴 y轴 不重复

## 多标签 ##
无空格

	<style>
        .pagination .page{
            display: inline-block;
            background-color: gold;
            padding: 5px;
            margin: 5px;
        }
        .pagination .page.active{
            background-color: red;
            color: white;
        }
    </style>

	<div class="pagination">
    	<a class="page active" href="/page/?p=8">8</a>
    </div>
	

	