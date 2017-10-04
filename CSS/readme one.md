作业1：
1. CSS重用
    <style>
        若整个网页的宽度 > 900px:
        {
            .c{
                共有
            }
            .c1{
                特有
            }
        }
        
        .c2{
            特有
        }
    </style>
    <div style="c c1"></div>
    <div style="c c2"></div>
    
2 自适应和网页缩扩变型
    左右滚动条的出现
    宽度：百分比
    页面最外层：像素的宽度-》在最外层设置绝对宽度
    
    自适应：media
3 默认img标签，有1px宽度
    img{
            border: 0;
        }
    或者
    .img{
        border: 0;
    }
    
4 作业中的数量输入框    
    