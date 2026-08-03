# 16 Bokeh图表

</div>

<div class="part">

</div>

<div class="header3">


</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Anaconda开发环境中还集成了一个叫作Bokeh的模块，该模块同样可以根据数据集绘制对应的图表，以满足数据可视化的多种需求。本章将介绍如何使用Bokeh模块绘制数据图表。</span>

<span style="font-size:16px;font-family:'PingFang SC';">本章知识架构如下。</span>

<div style="display: block;text-align:center;">

<img src="images/image_553.jpg" width="900" />

</div>

</div>

<span id="Section107.xhtml"></span>

<div id="Section107.xhtml_Section107.xhtml">

</div>

<div class="header2">

## 16.1 了解Bokeh图表

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Bokeh是一个Python交互式可视化模块，支持Web浏览器，可提供完美的展示功能。Bokeh的目标是使用D3.js样式提供优雅、简洁、新颖的图形化风格，同时提供大型数据集的高性能交互功能。Bokeh可以快速创建交互式的绘图、仪表盘和数据应用。</span>

</div>

<div class="header3">

### 16.1.1 安装Bokeh模块

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在“命令提示符”窗口中安装Bokeh模块。在系统搜索框中输入cmd，打开“命令提示符”窗口，使用pip工具安装，命令如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">pip install bokeh</span>

<span style="font-size:16px;font-family:'PingFang SC';">当然，也可以在PyCharm开发环境中安装。</span>

</div>

<div class="header3">

### 16.1.2 词汇与接口说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在学习如何使用Bokeh绘图模块时，我们需要先了解一下相关词汇说明，具体内容如表16.1所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">表16.1 Bokeh模块的词汇说明</span>

<div style="display: block;text-align:center;">

<img src="images/image_554.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">Bokeh的主要功能所对应的接口及其用途如表16.2所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">表16.2 Bokeh模块的主要接口及其用途</span>

<div style="display: block;text-align:center;">

<img src="images/image_555.jpg" width="900" />

</div>

</div>

<div class="header3">

### 16.1.3 绘制第一张Bokeh图表

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在使用Bokeh模块绘制一张简单的图表时，分为以下几个步骤：</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入模块与函数。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）创建图形画布。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）准备数据。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（4）绘制图标。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（5）显示或保存图表文件。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.1】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制简单的折线图</span>**（实例位置：资源包\\MR\\Code\\16\\01）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">以绘制折线图为例，调用line()函数来进行图表绘制，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure, show  # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  p = figure()                           # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x = \[1, 2, 3, 4, 5\]                      #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标，图表底部</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y = \[1, 5, 2, 6, 3\]                      #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标，折线对应的数据位置</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  p.line(x,y,line_width = 2)               # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">绘制折线图，线宽度为</span>2</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  show(p)                                  # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用Bokeh模块绘制图表时，在运行程序后，首先将自动生成与当前.py文件相同名称的.html文件，然后通过浏览器自动打开这个.html图表文件，效果如图16.1所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">line()函数中提供了多种参数，用于修改折线图的各种属性，常用参数及其说明如表16.3所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">表16.3 line()函数的参数说明</span>

<div style="display: block;text-align:center;">

<img src="images/image_556.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">当需要在图表中绘制多条折线时，可通过多次调用line()函数实现。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.2】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制多折线图</span>**（实例位置：资源包\\MR\\Code\\16\\02）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用line()函数绘制多折线图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   from bokeh.plotting import figure, show</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   # </span>创建<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   x = \[1, 2, 3, 4, 5\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   y1 = \[6, 7, 2, 4, 5\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   y2 = \[2, 3, 4, 5, 6\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   y3 = \[4, 5, 5, 7, 2\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   p = figure(title="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">多折线图</span>", x_axis_label="x", y_axis_label="y")</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>绘制多折线图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  p.line(x, y1, legend_label="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">京东</span>", color="blue", line_width=2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  p.line(x, y2, legend_label="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">天猫</span>", color="red", line_width=2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  p.line(x, y3, legend_label="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">自营</span>", color="green", line_width=2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  # </span>显示图表</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  show(p)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.2所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">Bokeh模块还提供了一个可以直接绘制多个折线图的multi_line()函数，该函数只需要设置xs（轴）与ys（数据轴）的坐标参数即可，但两个参数的值必须是列表数据，其他参数与line()函数相同。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.3】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用multi_line()函数绘制多折线图</span>**（实例位置：资源包\\MR\\Code\\16\\03）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">本实例将使用multi_line()函数绘制多折线图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure, show                 # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  p = figure()                                          # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x = \[\[1, 2, 3\], \[4, 5, 6\],\[7,8,9\]\]                      #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标，图表底部</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  # </span>三个子列表，代表三个折线点的数据值</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  y = \[\[1, 2, 1\], \[2, 3, 2\],\[3,4,3\]\]                      #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标，折线对应的数据位置</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  p.multi_line(xs=x, ys=y,color=\['red','green','blue'\]) # </span>绘制折线图，并设置三个折线图的颜色</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  show(p)                                                 # </span>显示图表</span>

<div style="display: block;text-align:center;">

<img src="images/image_557.jpg" width="735" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.1 绘制第一个折线图</span>

<div style="display: block;text-align:center;">

<img src="images/image_558.jpg" width="765" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图16.2 使用line()函数绘制多折线图</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.3所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_559.jpg" width="720" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">图16.3 使用multi_line()函数绘制多折线图</span>

</div>

<div class="header3">

### 16.1.4 通过数据类型绘制图表

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在使用Bokeh模块绘制图表时，可以使用多种数据类型的数据，如16.1.3小节中绘制的折线图就是使用了Python中的list（列表）数据，除了list（列表）数据，还可以使用dict（字典）类型的数据、NumPy中的Array（数组）数据、Pandas中的DataFrame以及Bokeh模块独特的ColumnDataSource数据类型，通过独特的数据类型可以很方便地在绘图函数中直接调用列名进行绘图。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. Python字典类型**</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用字典数据时，只需要直接获取键（key）所对应的值（value为列表数据），即可获取一个列表数据，此时便可以直接使用Bokeh模块实现图表的绘制了。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.4】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用字典类型数据绘制图表</span>**（实例位置：资源包\\MR\\Code\\16\\04）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先通过字典创建<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴和<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴数据，然后使用line()函数绘制折线图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure,show             # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  p = figure()                                     # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  # </span>字典类型的数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  dict_data = {'x':\[1, 2, 3, 4, 5\],'y':\[1,2,3,5,4\]}</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  x = dict_data\['x'\]                                 #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标，图表底部</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  y = dict_data\['y'\]                                 #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标，折线对应的数据位置</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  p.line(x,y,line_width = 2)                         # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">绘制折线图，线宽度为</span>2</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  show(p)                                            # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.4所示。</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在使用字典数据绘制图表时，还可以先在绘制图表函数中填写source参数，然后将字典数据直接传递给source参数，即可实现图表的绘制。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. NumPy数组类型**</span>

<span style="font-size:16px;font-family:'PingFang SC';">在使用NumPy中的数组数据绘制图表时，与使用Python中的list（列表）数据类似，直接指定数据值即可。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.5】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用NumPy数组类型数据绘制图表</span>**（实例位置：资源包\\MR\\Code\\16\\05）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先创建<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴和<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴数据，其中<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴数据通过列表创建，<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴数据则使用numpy数组随机创建，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure,show  # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  import numpy as np                      # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">numpy</span>模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  p = figure()                          # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  x = \[1,2,3,4,5\]                         #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标，图表底部</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  y = np.random.randint(1,5,size=5)       #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标，<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">numpy</span>数组随机数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  p.line(x,y,line_width = 2)              # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">绘制折线图，线宽度为</span>2</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  show(p)                                 # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.5所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_560.jpg" width="673" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.4 绘制字典数据的折线图</span>

<div style="display: block;text-align:center;">

<img src="images/image_561.jpg" width="665" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图16.5 绘制NumPy数组数据的折线图</span>

<span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**注意**</span>

<span style="font-size:16px;font-family:'PingFang SC';">由于使用了NumPy中的随机生成数组，所以每次运行程序，图表中的<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴数据都是不同的。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**3. DataFrame类型**</span>

<span style="font-size:16px;font-family:'PingFang SC';">Pandas是数据分析中最好用的一个模块，该模块有一个专属的数据类型DataFrame，而使用Bokeh模块绘图时，只需要将DataFrame数据传递给source参数即可。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.6】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用DataFrame类型数据绘制图表</span>**（实例位置：资源包\\MR\\Code\\16\\06）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先使用Pandas模块的DataFrame对象创建数据，然后使用multi_line()函数绘制图表，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure,show                    # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  import pandas as pd                                       # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">pandas</span>模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  # </span>创建数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  data = {'x':\[\[1,2,3,4,5\],\[6,7,8,9,10\]\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5         'y':\[\[5,2,1,4,3\],\[9,6,8,7,10\]\]}</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  d_dataframe = pd.DataFrame(data=data)                     # </span>创建<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">dataframe</span>数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  p = figure()                                            # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  p.multi_line('x','y',source=d_dataframe,line_width = 2) # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">绘制折线图，线宽度为</span>2</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  show(p)                                                   # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.6所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**4. ColumnDataSource类型**</span>

<span style="font-size:16px;font-family:'PingFang SC';">ColumnDataSource是Bokeh模块独有的数据类型，其对象的data参数用于传递数据，该参数可以传递三种数据类型：dict（字典）、DataFrame和DataFrame中的groupdy（分组统计数据）。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.7】**</span><span style="font-size:16px;font-family:'PingFang SC';">通过ColumnDataSource传递字典数据绘制图表</span>**（实例位置：资源包\\MR\\Code\\16\\07）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先使用字典创建数据，然后通过ColumnDataSource()对象的data参数传递数据并绘制图表，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure,show               # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from bokeh.models import ColumnDataSource            # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">ColumnDataSource</span>类</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  p = figure()                                       # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  # </span>字典类型的数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  dict_data = {'x_values':\[1, 2, 3, 4, 5\],'y_values':\[1,2,3,1,3\]}</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  # </span>传递字典数据创建<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">ColumnDataSource</span>数据对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  source = ColumnDataSource(data=dict_data)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  p.line(x='x_values',y='y_values',source=source)      # </span>绘制折线图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  show(p)                                              # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.7所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.8】**</span><span style="font-size:16px;font-family:'PingFang SC';">通过ColumnDataSource传递DataFrame数据绘制图表</span>**（实例位置：资源包\\MR\\Code\\ 16\\08）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先使用DataFrame()对象创建数据，然后通过ColumnDataSource()对象的data参数传递数据并绘制图表，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   from bokeh.plotting import figure, show              # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   import pandas as pd                             # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">pandas</span>模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   from bokeh.models import ColumnDataSource       # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">ColumnDataSource</span>类</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   p = figure()                                  # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   data = {'x_values': \[1, 2, 3, 4, 5\],            # </span>字典数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6          'y_values': \[6, 7, 2, 3, 6\]}</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   df = pd.DataFrame(data)                         # </span>转换<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">DataFrame</span>数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   # </span>传递<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">DataFrame</span>数据创建<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">ColumnDataSource</span>数据对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   source = ColumnDataSource(data=df)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  p.line('x_values','y_values',source=source)   # </span>绘制折线图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  show(p)                                         # </span>显示图表</span>

<div style="display: block;text-align:center;">

<img src="images/image_562.jpg" width="733" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图16.6 绘制DataFrame数据折线图</span>

<div style="display: block;text-align:center;">

<img src="images/image_563.jpg" width="722" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图16.7 通过ColumnDataSource绘制字典数据折线图</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.8所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.9】**</span><span style="font-size:16px;font-family:'PingFang SC';">通过ColumnDataSource传递分组统计数据绘制图表</span>**（实例位置：资源包\\MR\\Code\\ 16\\09）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先使用DataFrame()对象创建数据，然后使用groupby()函数统计每月数据，最后通过ColumnDataSource()对象的data参数传递数据并绘制图表，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd                             # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">pandas</span>模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   from bokeh.plotting import figure,show          # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   from bokeh.models import ColumnDataSource       # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">ColumnDataSource</span>类</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   p = figure()                                  # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   # </span>创建字典数据，模拟<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1</span>～<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>月商品销量</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   dict_data = {'month':\[1,2,3,2,1,3,2,3,1\],'data':\[1,3,2,2,3,2,4,6,2\]}</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   df = pd.DataFrame(dict_data)                    # </span>创建<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">DataFrame</span>数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   group = df.groupby('month').sum()           # </span>根据月份分组并对每月的数据求和</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   source = ColumnDataSource(data=group)           # </span>传递分组数据创建<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">ColumnDataSource</span>数据对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  p.line(x='month',y = 'data',source=source)      # </span>绘制折线图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  show(p)                                         # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.9所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_564.jpg" width="738" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图16.8 通过ColumnDataSource绘制DataFrame数据折线图</span>

<div style="display: block;text-align:center;">

<img src="images/image_565.jpg" width="740" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图16.9 通过ColumnDataSource绘制groupby数据折线图</span>

</div>

<span id="Section108.xhtml"></span>

<div id="Section108.xhtml_Section108.xhtml">

</div>

<div class="header2">

## 16.2 绘制常见图表

</div>

<div class="part">

</div>

<div class="header3">

### 16.2.1 绘制散点图—circle()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">可以使用circle()函数绘制散点图。该函数的常用参数如表16.4所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">表16.4 circle()函数的常用参数及其说明</span>

<div style="display: block;text-align:center;">

<img src="images/image_566.jpg" width="900" />

</div>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.10】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用circle()函数绘制散点图</span>**（实例位置：资源包\\MR\\Code\\16\\10）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先创建<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴和<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴数据，然后使用circle()函数绘制散点图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure,show                       # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  p = figure()                                               # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x = \[1, 2, 3, 4, 5\]                                          #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y = \[2, 5, 3, 1, 4\]                                          #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  # </span>绘制散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  p.circle(x = x,y = y , size=30, color="green",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7         alpha=0.8,line_color='black',line_dash = 'dashed',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  show(p)                                                      # </span>显示散点图</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.10所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_567.jpg" width="619" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">图16.10 使用circle()函数绘制散点图</span>

</div>

<div class="header3">

### 16.2.2 绘制组合图表—line()、circle()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Bokeh也可以在一个画布上绘制多个不同类型的图表，如在折线图的数据点上绘制一个散点等。这样可以更加清晰地看出数据点所在的位置。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.11】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制折线图与散点图组合图表</span>**（实例位置：资源包\\MR\\Code\\16\\11）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先创建<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴、<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴数据，然后绘制折线图与散点图组合图表，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   from bokeh.plotting import figure, show                              # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   p = figure()                                                       # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   x = \[1, 2, 3, 4, 5\]                                                  #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标，图表底部</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   y = \[1.1,1.2,2,1.4,1.7\]                                              #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标，折线与散点对应的数据位置</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   y1 = \[1.4,1.6,2.6,3.8,2.7\]                                           # </span>第二条折线与散点数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   # </span>绘制折线图与散点图，并设置图例</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   p.line(x,y,legend_label='y',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   p.circle(x,y,legend_label='y',fill_color = 'white',line_color='red',size=10)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   p.line(x,y1,legend_label='y1',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  p.circle(x,y1,legend_label='y1',fill_color = 'blue',line_color='red',size=10)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  show(p)                                                              # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.11所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_568.jpg" width="737" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图16.11 组合绘图</span>

</div>

<div class="header3">

### 16.2.3 绘制条形图—vbar()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在Bokeh模块中，绘制垂直条形图可以使用vbar()函数。该函数中，参数x表示横轴坐标，width表示条形宽度，bottom表示条形底部高度，top表示条形顶部的<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴坐标，其他边线等参数与绘制散点图类似。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.12】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制垂直条形图</span>**（实例位置：资源包\\MR\\Code\\16\\12）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用vbar()函数绘制垂直条形图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure, show          # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  p = figure()                                   # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  p.vbar(x=\[1, 2, 3\], width=0.5, bottom=0,        # </span>绘制垂直条形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4        top=\[1.8, 2.3, 4.6\], color="firebrick",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5        line_width = 2,line_color = 'black',line_dash ='dashed')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  show(p)                                          # </span>显示垂直条形图</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.12所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制水平条形图可以使用hbar()函数，在该函数中，参数y为纵轴坐标，height为条形的高度（厚度），left为左边最小值，right为右边最大值。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.13】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制水平条形图</span>**（实例位置：资源包\\MR\\Code\\16\\13）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用hbar()函数绘制水平条形图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure, show         # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  p = figure()                                  # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  # </span>绘制水平条形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  p.hbar(y=\[1, 2, 3\], height=0.5, left=0,right=\[1.6, 3.5, 4.3\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5        color = \['blue','green','red'\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6        line_width = 2,line_color = 'black',line_dash ='dashed')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  show(p)                                         # </span>显示水平条形图</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.13所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_569.jpg" width="580" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.12 绘制垂直条形图</span>

<div style="display: block;text-align:center;">

<img src="images/image_570.jpg" width="617" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.13 绘制水平条形图</span>

</div>

<div class="header3">

### 16.2.4 绘制饼（环）形图—wedge()、annular\_wedge()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">饼形图一般用于表示不同分类的占比情况，主要使用wedge()函数绘制。该函数中，参数x表示圆心横轴的坐标，y表示圆心纵轴的坐标，radius表示圆的半径，start_angle表示从水平方向起始角度，end_angle表示水平方向结束角度，direction表示起始方向（默认逆时针），legend_field表示图例。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.14】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制饼形图</span>**（实例位置：资源包\\MR\\Code\\16\\14）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用wedge()函数绘制饼形图，程序代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_571.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.14所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">环形图与饼形图类似，只是将中间的区域挖空。绘制环形图主要使用annular_wedge()函数，其中参数x表示圆环中心的横轴坐标，y表示圆环中心的纵轴坐标，inner_radius表示内环半径，outer_radius表示外环半径。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.15】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制环形图</span>**（实例位置：资源包\\MR\\Code\\16\\15）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用annular_wedge()函数绘制环形图，程序关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  p = figure(title="</span>环图<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">",)      # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  # </span>绘制环形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  p.annular_wedge(x=0, y=1, outer_radius=0.5,inner_radius=0.4,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4          start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5          line_color="white",line_width = 2, fill_color='color', legend_field='city', source=data)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.15所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_572.jpg" width="870" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.14 绘制饼形图</span>

<div style="display: block;text-align:center;">

<img src="images/image_573.jpg" width="845" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.15 绘制环形图</span>

</div>

<span id="Section109.xhtml"></span>

<div id="Section109.xhtml_Section109.xhtml">

</div>

<div class="header2">

## 16.3 设置图表

</div>

<div class="part">

</div>

<div class="header3">

### 16.3.1 图表布局—column()、row()、gridplot()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">图表布局方式有3种，分别是列布局、行布局、网格布局。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. 列布局**</span>

<span style="font-size:16px;font-family:'PingFang SC';">列布局就是垂直方向显示多个图表，实现这种布局方式主要使用column()函数，将绘制的图表作为参数传入column()函数中。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.16】**</span><span style="font-size:16px;font-family:'PingFang SC';">垂直方向布局多个图表</span>**（实例位置：资源包\\MR\\Code\\16\\16）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先绘制图表，然后使用column()函数在垂直方向布局图表，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure, show            # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from bokeh.layouts import column                   # </span>导入列布局</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  p1 = figure()                                    # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  x = \[1, 2, 3, 4, 5\]                                #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标，图表底部</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  y = \[1, 5, 2, 6, 3\]                                #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标，折线对应的数据位置</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  p1.line(x,y,line_width = 2)                        # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">绘制折线图，线宽度为</span>2</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  p2 = figure()                                    # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  # </span>绘制散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  p2.circle(x = x,y = y , size=30, color="green",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10          alpha=0.8,line_color='black',line_dash = 'dashed',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  show(column(p1, p2))                          # </span>列布局显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.16所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. 行布局**</span>

<span style="font-size:16px;font-family:'PingFang SC';">行布局与列布局类似，只是在水平方向显示多个图表，实现这种布局方式主要使用row()函数，将绘制的图表作为参数传入row()函数中。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.17】**</span><span style="font-size:16px;font-family:'PingFang SC';">水平方向布局多个图表</span>**（实例位置：资源包\\MR\\Code\\16\\17）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先绘制图表，然后使用row()函数在水平方向布局多个图表，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   from bokeh.plotting import figure, show                              # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   from bokeh.layouts import row                                        # </span>导入行布局</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   p1 = figure()                                                      # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   x = \[1, 2, 3, 4, 5\]                                                  #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标，图表底部</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   y = \[1, 5, 2, 6, 3\]                                                  #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标，折线对应的数据位置</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   p1.line(x,y,line_width = 2)                                          # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">绘制折线图，线宽度为</span>2</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   p2 = figure()                                                      # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   # </span>绘制散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   p2.circle(x = x,y = y , size=30, color="green",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10          alpha=0.8,line_color='black',line_dash = 'dashed',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  show(row(p1, p2))                                                # </span>行布局显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.17所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_574.jpg" width="408" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.16 垂直方向布局图表</span>

<div style="display: block;text-align:center;">

<img src="images/image_575.jpg" width="821" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.17 水平方向布局多个图表</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**3. 网格布局**</span>

<span style="font-size:16px;font-family:'PingFang SC';">网格布局相对比较好理解，就是通过网格的方式显示多个图表，实现这种布局方式可以使用gridplot()函数，需要将相关参数传入gridplot()函数中。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.18】**</span><span style="font-size:16px;font-family:'PingFang SC';">通过网格布局多个图表</span>**（实例位置：资源包\\MR\\Code\\16\\18）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先绘制图表，然后使用gridplot()函数实现将多个图表显示在网格中，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure, show  # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from bokeh.layouts import gridplot       # </span>导入网格布局</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   x=\[1,2,3,4,5\]                           #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标，图表底部</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   y = list(range(1,6))                #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   p1 = figure()                         # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   # </span>绘制圆点散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   p1.circle(x=x,y=y,size=10,color='red',line_color='black',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   p2 = figure()                         # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>绘制方形散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  p2.square(x=x,y=y,size=10,color='black',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  p3 = figure()                         # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  # </span>绘制三角散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  p3.triangle(x=x,y=y,size=10,color='yellow',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  p4 = figure()                         # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  # </span>绘制方形中<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">pin</span>散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  p4.square_pin(x=x,y=y,size=10,color='yellow',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  # </span>使用网格布局显示多个图表</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  grid = gridplot(\[p1, p2, p3,p4\], ncols=2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19  show(grid)                              # </span>显示网格布局的图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.18所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_576.jpg" width="815" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图16.18 网格布局图表</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">gridplot()函数中的ncols参数表示网格布局需要以几列进行展示。</span>

</div>

<div class="header3">

### 16.3.2 配置绘图工具

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">配置绘图工具包括两方面工作，分别是定位工具栏和指定工具，下面进行具体介绍。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. 定位工具栏**</span>

<span style="font-size:16px;font-family:'PingFang SC';">工具栏的默认位置一般会显示在图表的右侧，如果需要调整工具栏位置，可以通过figure()对象的toolbar_location参数来修改。该参数提供了4个值，分别为above、below、left、right，表示工具栏显示在图表的上、下、左、右4个位置。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.19】**</span><span style="font-size:16px;font-family:'PingFang SC';">在图表上显示工具栏</span>**（实例位置：资源包\\MR\\Code\\16\\19）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">将工具栏显示在图表上方，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure, show                                      # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  x=\[1,2,3,4,5\]                                                                #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标，图表底部</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  y = list(range(1,6))                                                     #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  p1 = figure(toolbar_location='above')                                      # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  p1.circle(x=x,y=y,size=10,color='red',line_color='black',line_width = 2)     # </span>绘制圆点散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  show(p1)                                                                     # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.19所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_577.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图16.19 将工具栏设置在图表上方</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">如果需要隐藏图表中的工具栏，可以将toolbar_location参数设置为None。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. 指定工具**</span>

<span style="font-size:16px;font-family:'PingFang SC';">指定工具就是指将需要的工具添加至工具栏当中，Bokeh模块提供了两种指定工具的方法，一种是先将需要添加的工具名称添加至字符串中，工具名称之间用逗号分隔，然后在创建figure()对象时将工具名称的字符串传递给tools参数。另一种添加工具的方式就是先创建figure()对象，然后通过该对象调用add_tools()函数，再将需要添加的工具对象作为参数传递至add_tools()函数中。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.20】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表指定平移、滑轮缩放和悬停工具</span>**（实例位置：资源包\\MR\\Code\\16\\20）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用add_tools()函数为图表指定平移、滑轮缩放和悬停工具，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure, show                                  # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from bokeh.models import WheelZoomTool                                   # </span>导入滑轮缩放工具类</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  tools = 'hover,pan'                                                      # </span>字符串方式添加悬停与平移工具名称</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  x=\[1,2,3,4,5\]                                                            #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标，图表底部</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  y = list(range(1,6))                                                 #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  p = figure()                                                           # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  p.circle(x=x,y=y,size=10,color='red',line_color='black',line_width = 2)  # </span>绘制圆点散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  p.add_tools(WheelZoomTool())                                         # </span>在<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">add_tools</span>中添加滑轮缩放工具</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  show(p)                                                                  # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.20所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_578.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">图16.20 为图表指定平移、滑轮缩放和悬停工具</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">除了以上介绍的三种工具，还可以在bokeh.models.tools子模块中查找其他工具。</span>

</div>

<div class="header3">

### 16.3.3 设置视觉属性

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">设置视觉属性包括三方面的内容，分别是切换主题、设置调色板、颜色映射器，下面进行具体介绍。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. 切换主题**</span>

<span style="font-size:16px;font-family:'PingFang SC';">Bokeh为了让图表变得更加美观，一共内置了5种主题样式，分别为caliber、dark_minimal、light_minimal、night_sky和contrast，如图16.21所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_579.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">图16.21 Bokeh图表的5种主题样式</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.21】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表设置主题样式</span>**（实例位置：资源包\\MR\\Code\\16\\21）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">在Bokeh图表中设置主题样式非常简单，只需要调用curdoc().theme属性并为其赋值要使用的主题样式即可。切换主题样式的程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.io import curdoc                                      # </span>导入可以切换主题的函数</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from bokeh.plotting import figure, show                          # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x=\[1,2,3,4,5\]                                                    #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y = list(range(1,6))                                         #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  curdoc().theme = 'caliber'                                     # </span>指定需要切换的主题样式</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  p = figure(title='caliber')                                    # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  p.circle(x=x,y=y,size=10,color='red',line_color='black',line_width = 2)   # </span>绘制散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  show(p)                                                          # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.22所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. 设置调色板**</span>

<span style="font-size:16px;font-family:'PingFang SC';">Bokeh内置了非常实用的调色板，可以在bokeh.palettes子模块中找到。例如，Category20中有多达20种常用的颜色，Category20调色板对应多种颜色，如图16.23所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_580.jpg" width="636" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.22 切换主题样式</span>

<div style="display: block;text-align:center;">

<img src="images/image_581.jpg" width="589" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图16.23 Category20调色板</span>

<span style="font-size:16px;font-family:'PingFang SC';">调色板是（十六进制）RGB颜色字符串，数据类型为字典类型，字典数据中的key为调色板前的数字（最小为3、最大为20），通过字典中的数字key即可获取对应数量的RGB颜色字符串。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.22】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用调色板为图表设置颜色</span>**（实例位置：资源包\\MR\\Code\\16\\22）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面先使用Category20设置调色板，然后为图表设置颜色，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.palettes import Category20                                     # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Category20</span>调色板</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from bokeh.plotting import figure, show                                   # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x=\[1,2,3,4,5\]                                                             #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>为横轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y = list(range(1,6))                                                  #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>为纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  colors=Category20\[5\]                                                      # </span>获取调色板<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5</span>个颜色值</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  p = figure()                                                            # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  p.circle(x=x,y=y,size=10,color=colors,line_color='black',line_width = 2)  # </span>绘制散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  show(p)                                                                   # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.24所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**3. 颜色映射器**</span>

<span style="font-size:16px;font-family:'PingFang SC';">颜色映射器就是将调色板中的颜色值映射为数据序列的编码。Bokeh拥有以下几种颜色映射器。 <img src="images/image_582.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> bokeh.transform.factor_cmap：将颜色映射到特定的分类元素。 <img src="images/image_582.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> bokeh.transform.linear_cmap：将颜色值从高到低映射可用颜色范围内的数值。 <img src="images/image_582.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> bokeh.transform.log_cmap：与linear_cmap类似，但使用自然对数比例来映射颜色。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.23】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用颜色映射器为图表设置颜色</span>**（实例位置：资源包\\MR\\Code\\16\\23）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用颜色映射器为图表设置颜色，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   from bokeh.models import  ColumnDataSource                     # </span>导入数据类</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   from bokeh.palettes import Category20                          # </span>导入调色板</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   from bokeh.plotting import figure,show                         # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   from bokeh.transform import linear_cmap                        # </span>导入线性颜色映射器</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   x = list(range(1,10))                                      # </span>创建横轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   y = list(range(1,10))                                      # </span>创建纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   # </span>创建颜色映射器</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   mapper = linear_cmap(field_name='y', palette=Category20\[10\] ,low=min(y) ,high=max(y))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   source = ColumnDataSource(dict(x=x,y=y))                   # </span>转换数据类型</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  p = figure()                                                 # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  p.circle(x='x', y='y',color=mapper,size=12, source=source)   # </span>绘制散点图，传入颜色映射器</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  show(p)                                                        # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.25所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_583.jpg" width="588" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.24 使用调色板为图表设置颜色</span>

<div style="display: block;text-align:center;">

<img src="images/image_584.jpg" width="805" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图16.25 使用颜色映射器为图表设置颜色</span>

</div>

<div class="header3">

### 16.3.4 图表注释

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">图表注释包括添加标题、添加图例、图例自动分组三部分内容，下面进行具体介绍。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. 添加标题**</span>

<span style="font-size:16px;font-family:'PingFang SC';">图表中最常见的注释就是图表的标题，从标题上可以很清楚地看出当前图表的名称以及图表的意义。在Bokeh中添加图表的标题只需要在创建画布对象（figure）时，添加title参数并指定对应的标题名称即可。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.24】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表设置标题</span>**（实例位置：资源包\\MR\\Code\\16\\24）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面通过title参数为图表设置标题，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.plotting import figure,show # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  p = figure(title="</span>我是图表标题<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">")     # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x = \[1,2,3\]                            # </span>横轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y = \[1,2,1\]                            # </span>纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  p.circle(x,y,size=10)                # </span>绘制散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  show(p)                                # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.26所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">在添加图表标题时，标题会默认显示在图表的左上方，如果在画布对象（figure）中设置title_location参数，便可以修改图表标题所显示的位置，如above（上）、below（下）、left（左）、right（右）。例如，设置图表标题位于图表下方，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">p = figure(title="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">我是图表标题</span>",title_location='below')</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.27所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_585.jpg" width="604" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.26 为图表设置标题</span>

<div style="display: block;text-align:center;">

<img src="images/image_586.jpg" width="621" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.27 修改图表标题的位置</span>

<span style="font-size:16px;font-family:'PingFang SC';">除了设置标题位置，还可以通过画布对象（figure）调用title()对象，然后通过各种属性来自定义标题。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.25】**</span><span style="font-size:16px;font-family:'PingFang SC';">设置图表标题颜色和大小等</span>**（实例位置：资源包\\MR\\Code\\16\\25）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用title()对象设置图表标题内容、文本方向、文字大小、文字颜色和标题背景颜色，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   from bokeh.plotting import figure, show  # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   p = figure()                           # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   x = \[1, 2, 3\]                            # </span>横轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   y = \[1, 2, 1\]                            # </span>纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   p.circle(x, y, size=10)                # </span>绘制散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   # </span>设置图表标题属性</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   p.title.text = "</span>我是图表标题<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">"            # </span>设置标题内容</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   p.title.align = "center"                 # </span>设置标题相对于文本的方向</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   p.title.text_color = "white"             # </span>设置标题文字颜色</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  p.title.text_font_size = "25px"          # </span>设置标题文字大小</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  p.title.background_fill_color = "red"    # </span>设置标题背景颜色</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  show(p)                                  # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.28所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">在设置图表标题时，可能会出现需要多个标题的需求，这时就需要先单独创建一个标题（Title）对象，然后通过添加布局的方式，将新创建的标题对象添加到图表的指定位置。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.26】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表设置双标题</span>**（实例位置：资源包\\MR\\Code\\16\\26）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">为图表设置双标题，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.models import Title             # </span>导入标题类</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from bokeh.plotting import figure, show    # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  p = figure(title="</span>我是上标题<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">")           # </span>创建图形画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  x = \[1, 2, 3\]                              # </span>横轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  y = \[1, 2, 1\]                              # </span>纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  p.circle(x, y, size=10)                  # </span>绘制散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  new_title = Title(text="</span>我是下标题<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">")     # </span>添加标题对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  p.add_layout(new_title, "below")         # </span>添加布局的方式，添加标题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  show(p)                                    # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.29所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_587.jpg" width="617" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.28 自定义图表标题</span>

<div style="display: block;text-align:center;">

<img src="images/image_588.jpg" width="621" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.29 设置双标题</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. 添加图例**</span>

<span style="font-size:16px;font-family:'PingFang SC';">如果图表中出现多个数据，就可以在绘图函数中添加图例参数（legend_label），这样可以更加清晰地区分每个数据。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.27】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表添加图例</span>**（实例位置：资源包\\MR\\Code\\16\\27）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制折线图并添加图例，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   from bokeh.plotting import figure, show     # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   x=\[1,2,3,4,5\]                               # </span>横轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   # </span>纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   y = \[1,2,1,2,1\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   y2 = \[2,3,2,3,2\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   y3 = \[3,4,3,4,3\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   p = figure()                              # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   # </span>绘制圆散点与对应折线</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   p.circle(x,y,size=10,color='yellow',legend_label='<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">圆</span>',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  p.line(x,y,color='yellow',legend_label='<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">圆</span>',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  # </span>绘制三角散点与对应折线</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  p.triangle(x=x,y=y2,size=10,color='yellow',legend_label='<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">三角</span>',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  p.line(x=x,y=y2,color='yellow',legend_label='<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">三角</span>',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  # </span>绘制方形散点与对应折线</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  p.square(x=x,y=y3,size=10,color='yellow',legend_label='<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">方形</span>',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  p.line(x=x,y=y3,color='yellow',legend_label='<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">方形</span>',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  show(p)                                     # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.30所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">在绘图函数中直接添加legend_label参数很方便，但经常出现图例遮挡部分图表的现象。此时可单独创建legend()对象，通过添加布局的方式指定图例显示的位置。这样既方便观看图表数据，又不会遮挡图表。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.28】**</span><span style="font-size:16px;font-family:'PingFang SC';">指定图例所显示的位置</span>**（实例位置：资源包\\MR\\Code\\16\\28）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">通过添加布局的方式单独指定图例所显示的位置，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   from bokeh.models import Legend             # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Legend</span>类</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   from bokeh.plotting import figure, show     # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   x=\[1,2,3,4,5\]                               # </span>横轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   # </span>纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   y = \[1,2,1,2,1\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   y2 = \[2,3,2,3,2\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   y3 = \[3,4,3,4,3\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   p = figure()                              # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>绘制圆散点与对应折线</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  c0=p.circle(x,y,size=10,color='yellow',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  c1=p.line(x,y,color='yellow',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  # </span>绘制三角散点与对应折线</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  t0=p.triangle(x=x,y=y2,size=10,color='yellow',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  t1=p.line(x=x,y=y2,color='yellow',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  # </span>绘制方形散点与对应折线</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  s0=p.square(x=x,y=y3,size=10,color='yellow',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  s1=p.line(x=x,y=y3,color='yellow',line_color='red',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  # </span>创建<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Legend</span>对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19  legend = Legend(location='center',items=\[('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">圆</span>',\[c0,c1\]),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20              ('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">三角</span>',\[t0,t1\]),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21              ('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">方形</span>',\[s0,s1\])\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22  p.add_layout(legend, 'right')             # </span>图例添加在图表右侧</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">23  show(p)                                     # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图16.31所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_589.jpg" width="713" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.30 添加图例</span>

<div style="display: block;text-align:center;">

<img src="images/image_590.jpg" width="726" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.31 修改图例显示位置</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**3. 图例自动分组**</span>

<span style="font-size:16px;font-family:'PingFang SC';">如果使用的数据是ColumnDataSource类，Bokeh可从ColumnDataSource数据中的label列生成对应的图例名称，从而实现图例的自动分组。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.29】**</span><span style="font-size:16px;font-family:'PingFang SC';">图例自动分组</span>**（实例位置：资源包\\MR\\Code\\16\\29）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面实现图例自动分组，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from bokeh.models import ColumnDataSource      # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">ColumnDataSource</span>类</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   from bokeh.plotting import figure, show       # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   # </span>创建数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   source = ColumnDataSource(dict(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5       x=\[1, 2, 3, 4, 5, 6\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6       y=\[2, 1, 2, 1, 2, 1\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7       color=\['red', 'blue', 'red', 'blue', 'red', 'blue'\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8       label=\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">红</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">蓝</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">红</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">蓝</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">红</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">蓝</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   ))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  p = figure(x_range=(0, 7), y_range=(0, 3))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  # </span>绘制散点图，图例通过数据中的<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">label</span>进行分组</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  p.circle(x='x', y='y', size = 15,color='color', legend_group='label', source=source)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  show(p)                                        # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">程序运行，效果如图16.32所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_591.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图16.32 图例自动分组</span>

</div>

<span id="Section110.xhtml"></span>

<div id="Section110.xhtml_Section110.xhtml">

</div>

<div class="header2">

## 16.4 图表可视化交互

</div>

<div class="part">

</div>

<div class="header3">

### 16.4.1 微调器

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">微调器是Bokeh中的一个小部件，通过它可以实现图表属性的调节。在图表中添加微调器需要先创建微调器对象Spinner()，再调用js_link()函数，当微调器数值修改时同时修改图表所对应的属性。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.30】**</span><span style="font-size:16px;font-family:'PingFang SC';">通过微调器调节散点图中散点的大小</span>**（实例位置：资源包\\MR\\Code\\16\\30）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面实现使用微调器调节散点图中散点的大小，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   from bokeh.layouts import column, row           # </span>导入行列布局</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   from bokeh.models import Spinner                # </span>导入微调器</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   from bokeh.plotting import figure,show          # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   from bokeh.palettes import Category20           # </span>导入调色板</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   x = \[1,2,3,4,5\]                                 # </span>横轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   y = \[1,2,1,2,1\]                                 # </span>纵轴坐标</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   colors = Category20\[5\]                          # </span>调色板中五个颜色</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   p = figure()                                  # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   points=p.circle(x,y,color=colors,size = 10)   # </span>绘制散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  # </span>创建微调器对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  spinner = Spinner(title="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">微调器</span>", low=1, high=40, step=2, value=10, width=80)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  # </span>调用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">js</span>事件处理，用于通过微调器值修改图表中散点大小</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  spinner.js_link('value', points.glyph, 'size')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  # </span>使用行与列布局将微调器显示出来</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  show(row(column(spinner, width=100), p))</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，将显示如图16.33所示的图表，然后将微调器数据调大，此时图表中的散点将同时变大，如图16.34所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_592.jpg" width="825" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.33 微调器默认值</span>

<div style="display: block;text-align:center;">

<img src="images/image_593.jpg" width="803" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.34 微调器值变大</span>

</div>

<div class="header3">

### 16.4.2 选项卡

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">当页面中需要显示多个图表时，可以使用选项卡小部件实现，这样既节省空间，还方便切换查看。例如，要实现两个图表之间的切换，需要创建两个选项卡对象TabPanel()，分别指定对应的图表，并将两个选项卡对象添加至Tabs()对象中。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.31】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表添加选项卡</span>**（实例位置：资源包\\MR\\Code\\16\\31）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">在图表中添加选项卡，通过选项卡查看不同的图表，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   from bokeh.plotting import figure, show                                # </span>导入图形画布与显示</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   from bokeh.models import Tabs, TabPanel                                # </span>导入选项卡</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   p_v = figure()                                                       # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   p_v.vbar(x=\[1, 2, 3\], width=0.5, bottom=0,                            # </span>绘制垂直条形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5          top=\[1.8, 2.3, 4.6\], color="firebrick",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6          line_width = 2,line_color = 'black',line_dash ='dashed')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   tab_v = TabPanel(child=p_v,title='</span>垂直条形图<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">')                       # </span>第一个选项卡</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   p_c = figure()                                                       # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   x = \[1, 2, 3, 4, 5\]                                                    #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  y_c = \[2, 5, 3, 1, 4\]                                                  #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴散点数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  y_l = \[1, 5, 2, 6, 3\]                                                  #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴折线数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  # </span>绘制散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  p_c.circle(x = x,y = y_c , size=30, color="green",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14           alpha=0.8,line_color='black',line_dash = 'dashed',line_width = 2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  tab_c = TabPanel(child=p_c,title='</span>散点图<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">')                           # </span>第二个选项卡</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  p_l = figure()                                                       # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  p_l.line(x,y_l,line_width = 2)                                         # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">绘制折线图，线宽度为</span>2</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  tab_l = TabPanel(child=p_l,title='</span>折线图<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">')                           # </span>第三个选项卡</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19  tabs = Tabs(tabs = \[tab_v,tab_c,tab_l\])                                # </span>集中选项卡</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20  show(tabs)                                                             # </span>显示选项卡及图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，默认显示如图16.35所示的带选项卡的图表，通过选项卡依次切换到“散点图”“折线图”，效果如图16.36和图16.37所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_594.jpg" width="614" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.35 选项卡图表（1）</span>

<div style="display: block;text-align:center;">

<img src="images/image_595.jpg" width="619" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.36 选项卡图表（2）</span>

<div style="display: block;text-align:center;">

<img src="images/image_596.jpg" width="624" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.37 选项卡图表（3）</span>

</div>

<div class="header3">

### 16.4.3 滑块功能

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">除了可以使用微调器调节图表属性，还可以使用滑块来调节图表中的数据值，让图表根据滑块值改变自身形态。首先需要自定义一个JS回调函数，动态修改图表中的数据值，然后创建滑块对象Slider()并通过调用js_on_change()函数实现回调函数的执行。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例16.32】**</span><span style="font-size:16px;font-family:'PingFang SC';">通过滑块调整图表</span>**（实例位置：资源包\\MR\\Code\\16\\32）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用滑块修改折线图的数值，程序代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_597.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，默认显示如图16.38所示的图表，将图表上方的滑块滑动至右侧，图表数据将被动态修改，效果如图16.39所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_598.jpg" width="664" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.38 默认显示数据的图表</span>

<div style="display: block;text-align:center;">

<img src="images/image_599.jpg" width="647" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图16.39 滑动滑块修改数据后的图表</span>

</div>

<span id="Section111.xhtml"></span>

<div id="Section111.xhtml_Section111.xhtml">

</div>

<div class="header2">

## 16.5 小结

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">本章介绍了如何使用Bokeh模块实现数据图表的绘制，Bokeh并未提供复杂的绘图功能，如各种三维曲线图和曲面图等。另外，Bokeh不是基于Python语言开发的交互工具，它实质上是用JavaScript实现在浏览器中绘图的工具，和Python常用的绘图工具并没有什么关系，Python中绝大多数的绘图工具都是基于Matplotlib实现的，是纯Python语言的绘图。所以，在实现Matplotlib和Bokeh交互时是比较困难的，而用JavaScript会容易一些，但同时也要求读者对JavaScript有一定的了解。</span>

</div>

<span id="Section112.xhtml"></span>

<div id="Section112.xhtml_Section112.xhtml">

</div>

<div class="header1">
