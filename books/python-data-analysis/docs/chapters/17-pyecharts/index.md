# 17 Pyecharts图表

</div>

<div class="part">

</div>

<div class="header1">


</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Echarts是一个由百度开发并开源的数据可视化工具，而Python是一门适用于数据处理和数据分析的语言，为了适应Python的需求，Pyecharts模块诞生了。本章以Pyecharts 2.0.3版本为载体，介绍Pyecharts的安装、链式调用、Pyecharts图表的组成以及如何绘制柱状图、折线图、饼形图等。</span>

<span style="font-size:16px;font-family:'PingFang SC';">本章知识架构如下。</span>

<div style="display: block;text-align:center;">

<img src="images/image_600.jpg" width="900" />

</div>

</div>

<span id="Section113.xhtml"></span>

<div id="Section113.xhtml_Section113.xhtml">

</div>

<div class="header2">

## 17.1 了解Pyecharts图表

</div>

<div class="part">

</div>

<div class="header3">

### 17.1.1 Pyecharts概述

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Pyecharts是一个生成Echarts图表的模块。Echarts是百度开源的一个数据可视化JS模块，其图表可视化效果非常好。Pyecharts是专门与Python衔接的可视化数据分析图表。使用Pyecharts可以生成独立的网页格式的图表，还可以在Flask、Django中使用，非常方便。</span>

<span style="font-size:16px;font-family:'PingFang SC';">Pyecharts的图表类型非常多，而且效果非常好。如图17.1～图17.3所示为线性闪烁图、仪表盘图和水球图。</span>

<div style="display: block;text-align:center;">

<img src="images/image_601.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图17.1 线性闪烁图</span>

<div style="display: block;text-align:center;">

<img src="images/image_602.jpg" width="606" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图17.2 仪表盘图</span>

<div style="display: block;text-align:center;">

<img src="images/image_603.jpg" width="769" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图17.3 水球图</span>

<span style="font-size:16px;font-family:'PingFang SC';">Pyecharts的图表类型主要包括Bar（柱形图／条形图）、Boxplot（箱形图）、Funnel（漏斗图）、Gauge（仪表盘）、HeatMap（热力图）、Line（折线／面积图）、Line3D（3D折线图）、Liquid（水球图）、Map（地图）、Parallel（平行坐标系）、Pie（饼形图）、Polar（极坐标系）、Radar（雷达图）、Scatter（散点图）和WordCloud（词云图）等。</span>

</div>

<div class="header3">

### 17.1.2 安装Pyecharts模块

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在“命令提示符”窗口中安装Pyecharts模块。在系统搜索框中输入cmd，打开“命令提示符”窗口，使用pip工具安装。安装命令如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">pip install pyecharts==2.0.3</span>

<span style="font-size:16px;font-family:'PingFang SC';">安装成功后，将提示安装成功的信息，如“Successfully installed pyecharts-2.0.3”。</span>

<span style="font-size:16px;font-family:'PingFang SC';">由于Pyecharts各版本的代码有一些区别，这里建议读者安装书中介绍的版本，以免造成不必要的麻烦。已安装过Pyecharts的读者，可使用如下方法查看Pyecharts的版本：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">import pyecharts</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">print(pyecharts.\_\_version\_\_)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，控制台输出结果为2.0.3。</span>

<span style="font-size:16px;font-family:'PingFang SC';">如果读者安装版本与笔者不同，建议卸载重新安装pyecharts-2.0.3。</span>

</div>

<div class="header3">

### 17.1.3 绘制第一张Pyecharts图表

</div>

<div class="part">

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.1】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制简单的柱形图</span>**（实例位置：资源包\\MR\\Code\\17\\01）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用Pyecharts绘制一张简单的柱形图，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）从Pyecharts.charts子模块中导入Bar类，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">from pyecharts.charts import Bar  # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Bar</span>类</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）创建一个空的Bar()对象（柱形图对象），代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">bar = Bar()</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）定义<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴和<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴数据，其中<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴为月份，<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴为销量。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">bar.add_xaxis(\["1<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "2<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "3<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "4<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "5<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "6<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>"\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">bar.add_yaxis("<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">零基础学</span>Python", \[2567, 1888, 1359, 3400, 4050, 5500\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">bar.add_yaxis("Python<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数据分析技术手册</span>", \[1567, 988, 2270,3900, 2750, 3600\])</span>

<span style="font-size:16px;font-family:'PingFang SC';">（4）渲染图表到HTML文件，并存放在程序所在目录下，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">bar.render("mycharts.html")</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，将在程序所在路径下生成一个名为mycharts.html的HTML文件，打开该文件，效果如图17.4所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_604.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">图17.4 绘制第一张Pyecharts图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">以上就是我们绘制的第一张Pyecharts图表。</span>

</div>

<div class="header3">

### 17.1.4 Pyecharts函数的链式调用

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">函数的调用分为单独调用和链式调用。单独调用就是常规的逐个函数调用。链式调用的关键在于函数化，现在很多开源模块或代码都使用链式调用。链式调用将所有需要调用的函数写在一个函数里，代码看上去更简洁、易懂。</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面以17.1.3节绘制的“第一张Pyecharts图表”为例，在调用Bar()对象的各个函数时，将单独调用与链式调用进行简单对比，效果如图17.5所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_605.jpg" width="797" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.5 单独调用与链式调用对比</span>

<span style="font-size:16px;font-family:'PingFang SC';">从图17.5中可以看出，链式调用将所有需调用的函数写在一个函数里，代码更简洁。当然，如果不习惯使用链式调用，也可以使用单独调用。</span>

</div>

<span id="Section114.xhtml"></span>

<div id="Section114.xhtml_Section114.xhtml">

</div>

<div class="header2">

## 17.2 Pyecharts图表的组成部分

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Pyecharts不仅具备Matplotlib图表的一些常用功能，还提供了独有的、别具特色的功能，主要包括主题风格的设置、图例、视觉映射、工具箱和区域缩放等，如图17.6所示。这些功能使得Pyecharts能够绘制出各种各样、超乎想象的图表。</span>

<div style="display: block;text-align:center;">

<img src="images/image_606.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.6 Pyecharts图表的组成</span>

</div>

<div class="header3">

### 17.2.1 主题风格—InitOpts()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Pyecharts内置了15种不同的主题风格，并提供了便捷的定制主题函数。通过options子模块的InitOpts()对象设置图表的主题风格。下面介绍InitOpts()对象的关键参数。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> width：字符型，图表画布宽度，以像素为单位。例如，width='500px'。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> height：字符型，图表画布高度，以像素为单位。例如，height='300px'。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> chart_id：图表的ID，图表的唯一标识，主要用于多图表时区分每个图表。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> page_title：字符型，网页标题。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> theme：图表主题，其参数值主要由ThemeType类提供。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> bg_color：字符型，图表背景颜色。例如，bg_color='black'或bg_color='#fff'。</span>

<span style="font-size:16px;font-family:'PingFang SC';">ThemeType类提供的15种图表主题风格如表17.1所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">表17.1 theme参数设置值</span>

<div style="display: block;text-align:center;">

<img src="images/image_608.jpg" width="900" />

</div>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.2】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表更换主题</span>**（实例位置：资源包\\MR\\Code\\17\\02）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面为“第一张Pyecharts图表”更换主题，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）从pyecharts.charts子模块中导入Bar类。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from pyecharts.charts import Bar</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）从pyecharts模块中导入options子模块。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts import options as opts</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）从pyecharts.globals子模块中导入主题类型的ThemeType类。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  from pyecharts.globals import ThemeType</span>

<span style="font-size:16px;font-family:'PingFang SC';">（4）设置画布大小、图表主题和图表背景颜色，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  bar =(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5      Bar(init_opts=opts.InitOpts(width='500px',height='300px',  # </span>设置画布大小</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6                              theme=ThemeType.LIGHT,               # </span>设置主题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7                              bg_color='#fff'))                  # </span>设置图表背景颜色</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8      #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴和<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9      .add_xaxis(\["1<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "2<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "3<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "4<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "5<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "6<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>"\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  .add_yaxis("<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">零基础学</span>Python", \[2567, 1888, 1359, 3400, 4050, 5500\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  .add_yaxis("Python<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数据分析技术手册</span>", \[1567, 988, 2270,3900, 2750, 3600\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  )</span>

<span style="font-size:16px;font-family:'PingFang SC';">（5）渲染图表到HTML文件，并将其存放在程序所在目录下，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  bar.render("mycharts1.html")  # </span>渲染图表到<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">HTML</span>文件</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，将在程序所在路径下生成一个名为mycharts1.html的HTML文件，打开该文件，效果如图17.7所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_609.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.7 设置主题风格</span>

</div>

<div class="header3">

### 17.2.2 图表标题—TitleOpts()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">图表标题主要通过set_global_options()函数的title_opts参数进行设置，该参数值参考options子模块的TitleOpts()对象，可实现主标题、副标题、距离以及文字样式等的设置。TitleOpts()对象的主要参数说明如下。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> title：字符型，默认值为None。主标题文本，支持换行符“\n”。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> title_link：字符型，默认值为None。主标题跳转URL链接。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> title_target：字符型，默认值为None。主标题跳转链接的方式，默认值为blank，表示在新窗口打开。可选参数self，表示在当前窗口打开。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> subtitle：字符型，默认值为None。副标题文本，支持换行符“\n”。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> subtitle_link：字符型，默认值为None。副标题跳转URL链接。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> subtitle_target：字符型，默认值为None。副标题跳转链接的方式，默认值为blank，表示在新窗口打开。可选参数self，表示在当前窗口打开。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_left：字符型，默认值为None。表示标题距左侧的距离。其值可以是具体像素值，可以是相对于容器的高和宽的百分比，也可以是left、center或right，标题将根据相应的位置自动对齐。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_right：字符型，默认值为None。表示标题距右侧的距离。其值可以是具体像素值，也可以是相对于容器的高和宽的百分比。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_top：字符型，默认值为None。表示标题距顶端的距离。其值可以是具体像素值，可以是相对于容器的高和宽的百分比，也可以是top、middle或bottom，标题将根据相应的位置自动对齐。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_bottom：字符型，默认值为None。表示标题距底端的距离。其值可以是具体像素值，也可以是相对于容器的高和宽的百分比。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> padding：标题内边距，单位为像素。默认值为各方向（上、右、下、左）内边距为5，接受数组分别设定上、右、下、左边距。例如，padding=\[10,4,5,90\]。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> item_gap：数值型，主标题与副标题之间的间距。例如，item_gap=3.5。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> title_textstyle_opts：主标题文字样式配置项，参考options子模块的TextStyleOpts()对象。主要包括颜色、字体样式、字体的粗细、字体的大小以及对齐方式等。例如，设置标题颜色为红色，字体大小为18，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">title_textstyle_opts=opts.TextStyleOpts(color='red',font_size=18) <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> subtitle_textstyle_opts：副标题文字样式配置项，参数配置同主标题。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.3】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表设置标题</span>**（实例位置：资源包\\MR\\Code\\17\\03）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面为“第一张Pyecharts图表”设置标题，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）从pyecharts.charts子模块中导入Bar类。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from pyecharts.charts import Bar</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）从pyechartsm模块中导入options子模块。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts import options as opts</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）从pyecharts.globals子模块中导入主题类型的ThemeType类。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  from pyecharts.globals import ThemeType</span>

<span style="font-size:16px;font-family:'PingFang SC';">（4）生成图表，设置图表标题，包括主标题、主标题字体颜色和大小、副标题、标题内边距以及主标题与副标题的间距。代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_610.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">（5）渲染图表到HTML文件，并将其存放在程序所在目录下。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19  bar.render("mycharts2.html")</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，将在程序所在路径下生成一个名为mycharts2.html的HTML文件，打开该文件，效果如图17.8所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_611.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.8 设置图表标题</span>

</div>

<div class="header3">

### 17.2.3 图例—LegendOpts()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">图例主要通过set_global_opts()函数的legend_opts参数进行设置，该参数值参考options子模块的LegendOpts()对象。LegendOpts()对象的主要参数说明如下。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> is_show：布尔值，表示是否显示图例，True为显示图例，False为不显示图例。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_left：字符串或数字，默认值为None。表示图例离容器左侧的距离，其值可以是具体像素值，可以是相对于容器高和宽的百分比，也可以是left、center或right，图例将根据相应的位置自动对齐。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_right：字符串或数字，默认值为None。表示图例离容器右侧的距离，其值可以是具体像素值，也可以是相对于容器高和宽的百分比。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_top：字符串或数字，默认值为None。表示图例离容器顶端的距离，其值可以是具体像素值，可以是相对于容器高和宽的百分比，也可以是top、middle或bottom，图例将根据相应的位置自动对齐。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_bottom：字符串或数字，默认值为None。表示图例离容器底端的距离，其值可以是具体像素值，也可以是相对于容器高和宽的百分比。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> orient：字符串，默认值为None。表示图例列表的布局朝向，其值为horizontal（横向）或vertical（纵向）。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> align：字符串。表示图例标记和文本的对齐，其值为auto、left或right，默认值为auto（自动）。根据图表的位置和orient参数（图例列表的朝向）决定。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> padding：整型，图例内边距，单位为像素（px），默认值为各方向内边距为5。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> item_gap：图例之间的间隔。横向布局时为水平间隔，纵向布局时为纵向间隔。默认间隔为10。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> item_width：图例标记的宽度。默认宽度为25。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> item_height：图例标记的高度。默认高度为14。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> textstyle_opts：图例的字体样式。参考options子模块的TextStyleOpts()对象，主要包括颜色、字体样式、字体的粗细、字体的大小以及对齐方式等。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> legend_icon：图例标记的样式。其值为circle（圆形）、rect（矩形）、roundRect（圆角矩形）、triangle（三角形）、diamond（菱形）、pin（大头针）、arrow（箭头）或none（无）。也可以设置为图片。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.4】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表设置图例</span>**（实例位置：资源包\\MR\\Code\\17\\04）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面为“第一张Pyecharts图表”设置图例，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）从pyecharts.charts子模块中导入Bar类。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from pyecharts.charts import Bar</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）从pyecharts模块中导入options子模块。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts import options as opts</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）生成图表，设置图表标题和图例。其中，图例主要包括图例离容器右侧的距离、图例标记的宽度和图例标记的样式，代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_612.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成一个名为mycharts3.html的HTML文件，打开该文件，效果如图17.9所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_613.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.9 设置图例</span>

</div>

<div class="header3">

### 17.2.4 提示框—TooltipOpts()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">提示框主要通过set_global_options()函数的tooltip_opts参数进行设置，该参数值参考options子模块的TooltipOpts()对象。TooltipOpts()对象的主要参数说明如下。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> is_show：布尔值，表示是否显示提示框。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> trigger：提示框触发的类型，可选参数。其中，item数据项图形触发，主要在散点图和饼形图等无类目轴的图表中使用。axis坐标轴触发，主要在柱形图和折线图等使用类目轴的图表中使用。None不触发，即无提示框。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> trigger_on：提示框触发的条件，可选参数。其中，mousemove为鼠标移动时触发，click为鼠标点击时触发，mousemove\|click为鼠标移动和点击同时触发，none为鼠标不移动或不点击时触发。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> axis_pointer_type：指示器类型，可选参数，其值如下。 <img src="images/image_614.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> line：直线指示器。 <img src="images/image_614.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> shadow：阴影指示器。 <img src="images/image_614.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> cross：十字线指示器。 <img src="images/image_614.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> none：无指示器。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> background_color：提示框的背景颜色。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> border_color：提示框边框的颜色。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> border_width：提示框边框的宽度。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> textstyle_opts：提示框中文字的样式。参考options子模块的TextStyleOpts()对象，主要包括颜色、字体样式、字体的粗细、字体的大小以及对齐方式等。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.5】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表设置提示框</span>**（实例位置：资源包\\MR\\Code\\17\\05）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面为图表设置提示框的样式，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入相关模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from pyecharts import options as opts</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import Bar</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  from pyecharts.globals import ThemeType</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）设置图表标题和图例。其中，图例主要包括图例离容器右侧的距离、图例标记的宽度和图例标记的样式，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   bar =(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5       Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))                    # </span>主题风格</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6       #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴和<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7       .add_xaxis(\["1<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "2<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "3<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "4<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "5<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>", "6<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>"\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8       .add_yaxis("<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">零基础学</span>Python", \[2567, 1888, 1359, 3400, 4050, 5500\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9       .add_yaxis("Python<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数据分析技术手册</span>", \[1567, 988, 2270,3900, 2750, 3600\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10      # </span>设置图表标题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11      .set_global_opts(title_opts=opts.TitleOpts(title="</span>热门图书销量分析<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">",      # </span>主标题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12                     padding=\[10,4,5,90\],                                         # </span>标题内边距</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13                     subtitle='www.mingrisoft.com',                               # </span>副标题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14                     item_gap=5,                                                  # </span>主标题与副标题的间距</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15                     # </span>主标题字体颜色和大小</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  title_textstyle_opts=opts.TextStyleOpts(color='red',font_size=18)),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  # </span>设置图例</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  legend_opts=opts.LegendOpts(pos_right=50,       # </span>图例离容器右侧的距离</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19             item_width=45,                        # </span>图例标记的宽度</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20             legend_icon='circle'),               # </span>图例标记的样式为圆形</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）生成图表，设置鼠标点击时触发提示框，设置提示框为十字线指示器，设置背景色、边框宽度和边框颜色，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21                     # </span>提示框</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22                     tooltip_opts=opts.TooltipOpts(trigger="axis",  # </span>坐标轴触发</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">23                                trigger_on='click',                  # </span>鼠标点击时触发</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">24                                axis_pointer_type='cross',           # </span>十字线指示器</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">25                                background_color='blue',             # </span>背景色为蓝色</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">26                                border_width=2,                      # </span>边框宽度</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">27                                border_color='red')                 # </span>边框颜色为红色</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">28                     )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">29      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">30  bar.render("mycharts5.html")                                     # </span>生成图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成一个名为mycharts5.html的HTML文件，打开该文件，效果如图17.10所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_615.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.10 设置提示框</span>

</div>

<div class="header3">

### 17.2.5 视觉映射—VisualMapOpts()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">视觉映射主要通过set_global_options()函数的title_opts参数进行设置，该参数值参考options子模块的VisualMapOpts()对象。VisualMapOpts()对象的主要参数说明如下。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> is_show：布尔型，表示是否显示视觉映射配置。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> type\_：映射过渡类型，可选参数。其值为color或size。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> min\_：整型或浮点型，颜色条的最小值。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> max\_：整型或浮点型，颜色条的最大值。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> range_text：颜色条两端的文本。例如，High或Low。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> range_color：序列。颜色范围（过渡颜色），例如，range_color=\["#FFF0F5"， "#8B008B"\] <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> orient：颜色条放置方式，水平（horizontal）或者竖直（vertical）。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_left：颜色条离左侧的距离。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> dimension：颜色条映射的维度。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> is_piecewise：布尔型，表示是否分段显示数据。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.6】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表添加视觉映射</span>**（实例位置：资源包\\MR\\Code\\17\\06）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面为图表添加视觉映射，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入相关模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from pyecharts import options as opts</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import Bar</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）为柱形图添加数据，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   bar=Bar()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   # </span>为柱形图添加数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   bar.add_dataset(source=\[</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6               \["val", "<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">销量</span>","<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月份</span>"\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7               \[24, 10009, "1<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>"\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8               \[57, 19988, "2<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>"\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9               \[74, 39870, "3<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>"\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10              \[50, 12345, "4<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>"\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11              \[99, 50145, "5<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>"\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12              \[68, 29146, "6<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月</span>"\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13              \]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14          )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  bar.add_yaxis(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16          series_name="</span>销量<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">",                       # </span>系列名称</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17          y_axis =\[\],                               # </span>系列数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18          encode={"x": "</span>销量<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">", "y": "</span>月份<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">"},        # </span>对<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据进行编码</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19          label_opts=opts.LabelOpts(is_show=False)  # </span>不显示标签文本</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20          )</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）设置图表标题和视觉映射，并生成图表，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21  bar.set_global_opts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22          title_opts=opts.TitleOpts(title="</span>线上图书月销量分析<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">",   # </span>主标题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">23                                 subtitle='www.mingrisoft.com'),  # </span>副标题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">24          xaxis_opts=opts.AxisOpts(name="</span>销量<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">"),                 #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴名称</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">25          yaxis_opts=opts.AxisOpts(type\_="category"),            #  <span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">轴类型为</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类目</span>”</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">26          # </span>视觉映射</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">27          visualmap_opts=opts.VisualMapOpts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">28              orient="horizontal",                                 # </span>水平放置颜色条</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">29              pos_left="center",                                   # </span>居中</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">30              min\_=10,                                             # </span>颜色条最小值</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">31              max\_=100,                                            # </span>颜色条最大值</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">32              range_text=\["High", "Low"\],                          # </span>颜色条两端的文本</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">33              dimension=0,                                         # </span>颜色条映射的维度</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">34              range_color=\["#FFF0F5", "#8B008B"\]                   # </span>颜色范围</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">35                           )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">36          )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">37  bar.render("mycharts6.html")                                   # </span>生成图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成一个名为mycharts6.html的HTML文件，打开该文件，效果如图17.11所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_616.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.11 视觉映射</span>

</div>

<div class="header3">

### 17.2.6 工具箱—ToolboxOpts()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">工具箱主要通过set_global_options()函数的title_opts参数进行设置，该参数值参考options子模块的ToolboxOpts()对象。ToolboxOpts()对象的主要参数说明如下。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> is_show：布尔值，表示是否显示工具箱。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> orient：工具箱的布局朝向。可选参数，水平（horizontal）或竖直（vertical）。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_left：工具箱离容器左侧的距离。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_right：工具箱离容器右侧的距离。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_top：工具箱离容器顶端的距离。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_bottom：工具箱离容器底端的距离。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> feature：工具箱中每个工具的配置项。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.7】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表添加工具箱</span>**（实例位置：资源包\\MR\\Code\\17\\07）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面为图表添加工具箱，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入相关模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from pyecharts import options as opts</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import Bar</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）绘制柱形图，代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_617.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">（3）添加工具箱，并生成图表，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">36          # </span>工具箱</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">37          toolbox_opts=opts.ToolboxOpts(is_show=True,    # </span>显示工具箱</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">38                                       pos_left=700)    # </span>工具箱离容器左侧的距离</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">39          )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">40  bar.render("mycharts7.html")                         # </span>生成图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成一个名为mycharts7.html的HTML文件，打开该文件，效果如图17.12所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_618.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.12 工具箱</span>

</div>

<div class="header3">

### 17.2.7 区域缩放—DataZoomOpts()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">区域缩放工具条主要通过set_global_options()函数的datazoom_opts参数进行设置，该参数值参考options子模块的DataZoomOpts()对象。DataZoomOpts()对象的主要参数说明如下： <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> is_show：布尔值，表示是否显示区域缩放工具条。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> type\_：区域缩放工具条的类型，可选参数，其值为slider或inside。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> is_realtime：布尔值，表示是否实时更新图表。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> range_start：数据窗口范围的起始百分比。其值为0~100，表示0%~100%。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> range_end：数据窗口范围的结束百分比。其值为0~100，表示0%~100%。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> start_value：数据窗口范围的起始数值。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> end_value：数据窗口范围的结束数值。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> orient：区域缩放工具条的布局方式。可选参数，其值为horizontal（水平）或vertical（竖直）。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_left：工具箱离容器左侧的距离。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_right：工具箱离容器右侧的距离。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_top：工具箱离容器顶端的距离。 <img src="images/image_607.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_bottom：工具箱离容器底端的距离。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.8】**</span><span style="font-size:16px;font-family:'PingFang SC';">为图表添加区域缩放</span>**（实例位置：资源包\\MR\\Code\\17\\08）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面为图表添加区域缩放工具条，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入相关模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from pyecharts import options as opts</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import Bar</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）绘制柱形图，代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_619.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">（3）添加区域缩放工具条，并生成图表，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">40          # </span>区域缩放工具条</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">41          datazoom_opts=opts.DataZoomOpts()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">42          )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">43  bar.render("mycharts8.html")               # </span>生成图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成一个名为mycharts8.html的HTML文件，打开该文件，效果如图17.13所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_620.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.13 区域缩放</span>

</div>

<span id="Section115.xhtml"></span>

<div id="Section115.xhtml_Section115.xhtml">

</div>

<div class="header2">

## 17.3 绘制Pyecharts图表

</div>

<div class="part">

</div>

<div class="header3">

### 17.3.1 绘制散点图—EffectScatter()对象

</div>

<div class="part">

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.9】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制简单的散点图</span>**（实例位置：资源包\\MR\\Code\\17\\09）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制涟漪特效散点图主要使用EffectScatter()对象的add_xaxis()、add_yaxis()函数实现。下面绘制一个简单的涟漪特效散点图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   from pyecharts.charts import EffectScatter</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   df = pd.read_excel('books.xlsx',sheet_name='Sheet2')       # </span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Excel</span>文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴和<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   x=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">年份</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   y1=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">京东</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   y2=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">天猫</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   y3=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">自营</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>绘制涟漪散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  scatter=EffectScatter()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  scatter.add_xaxis(x)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  scatter.add_yaxis("",y1)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  scatter.add_yaxis("",y2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  scatter.add_yaxis("",y3)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  scatter.render("myscatter.html")                     # </span>渲染图表到<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">HTML</span>文件，存放在程序所在目录下</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成名为myscatter.html的HTML文件，打开该文件，效果如图17.14所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_621.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.14 涟漪特效散点图</span>

</div>

<div class="header3">

### 17.3.2 绘制折线图和面积图—Line()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">绘制折线图和面积图主要使用Line对象的add_xaxis()和add_yaxis()函数。</span>

<span style="font-size:16px;font-family:'PingFang SC';">add_yaxis()函数的主要参数如下： <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> series_name：系列名称，用于提示文本和图例标签。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> y_axis：<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴数据。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> color：标签文本的颜色。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> symbol：标记，包括circle、rect、roundRect、triangle、diamond、pin、arrow或none，也可以设置为图片。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> symbol_size：标记大小。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> is_smooth：布尔值，表示是否为平滑曲线。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> is_step：布尔值，表示是否显示为阶梯图。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> linestyle_opts：线条样式。参考series_options.LineStyleOpts类。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> areastyle_opts：填充区域配置项，主要用于绘制面积图。该参数值需参考options子模块的AreaStyleOpts()对象。例如，areastyle_opts=opts.AreaStyleOpts（opacity=1）。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.10】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制折线图</span>**（实例位置：资源包\\MR\\Code\\17\\10）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制折线图，分析近7年各个电商平台的销量情况，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入相关模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import Line</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）绘制折线图，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   df = pd.read_excel('books.xlsx',sheet_name='Sheet2')  # </span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Excel</span>文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   x=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">年份</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   y1=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">京东</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   y2=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">天猫</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   y3=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">自营</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   line=Line()                                           # </span>创建折线图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>为折线图添加<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">x</span>轴和<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">y</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  line.add_xaxis(xaxis_data=x)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  line.add_yaxis(series_name="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">京东</span>",y_axis=y1)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  line.add_yaxis(series_name="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">天猫</span>",y_axis=y2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  line.add_yaxis(series_name="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">自营</span>",y_axis=y3)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  line.render("myline1.html")                           # </span>渲染图表到<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">HTML</span>文件，存放在程序所在目录下</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成myline1.html文件，打开该文件，效果如图17.15所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_623.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.15 折线图</span>

<span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**注意**</span>

<span style="font-size:16px;font-family:'PingFang SC';"><span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴数据必须为字符串，否则图表不显示。如果数据为其他类型，需要使用str()函数将数据转换为字符串，如x_data=\[str（i） for i in x\]。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.11】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制面积图</span>**（实例位置：资源包\\MR\\Code\\17\\11）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用Line()对象还可以绘制面积图，主要通过在add_yaxis()函数中指定areastyle_opts参数，该参数值由options子模块的AreaStyleOpts()对象提供。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入相关模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import Line</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  from pyecharts import options as opts</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）绘制面积图，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df = pd.read_excel('books.xlsx',sheet_name='Sheet2')  # </span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Excel</span>文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   x=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">年份</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   y1=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">京东</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   y2=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">天猫</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   y3=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">自营</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   line=Line()                                          # </span>创建面积图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  # </span>为面积图添加<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">x</span>轴和<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">y</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  line.add_xaxis(xaxis_data=x)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  line.add_yaxis(series_name="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">自营</span>",y_axis=y3,areastyle_opts=opts.AreaStyleOpts(opacity=1))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  line.add_yaxis(series_name="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">京东</span>",y_axis=y1,areastyle_opts=opts.AreaStyleOpts(opacity=1))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  line.add_yaxis(series_name="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">天猫</span>",y_axis=y2,areastyle_opts=opts.AreaStyleOpts(opacity=1))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  line.render("myline2.html")                          # </span>渲染图表到<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">HTML</span>文件，存放在程序所在目录下</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成myline2.html文件，打开该文件，效果如图17.16所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_624.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.16 面积图</span>

</div>

<div class="header3">

### 17.3.3 绘制柱形图—Bar()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">绘制柱形图／条形图主要使用Bar()对象实现，其主要函数如下： <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> add_xaxis()：<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴数据。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> add_yaxis()：<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴数据。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> reversal_axis()：翻转<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*xy*</span>轴数据。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> add_dataset()：原始数据。一般来说，原始数据表达的是二维表。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.12】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制多柱形图</span>**（实例位置：资源包\\MR\\Code\\17\\12）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">前述简单介绍了柱形图的绘制，下面先通过Pandas读取Excel文件中的数据，然后绘制多柱形图表，分析近7年各个电商平台的销量情况，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入相关模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import Bar</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  from pyecharts import options as opts</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  from pyecharts.globals import ThemeType</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）读取Excel文件，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   pd.set_option('display.unicode.east_asian_width', True)  # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   df = pd.read_excel('books.xlsx',sheet_name='Sheet2')     # </span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Excel</span>文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   print(df)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   #  </span><span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴和<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   x=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">年份</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  y1=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">京东</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  y2=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">天猫</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  y3=list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">自营</span>'\])</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）绘制多柱形图，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # </span>创建柱形图并设置主题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  # </span>为柱状图添加<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴和<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  bar.add_xaxis(x)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  bar.add_yaxis('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">京东</span>',y1)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  bar.add_yaxis('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">天猫</span>',y2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  bar.add_yaxis('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">自营</span>',y3)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19  bar.render("mybar1.html")       # </span>渲染图表到<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">HTML</span>文件，存放在程序所在目录下</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，两种数据展示方式对比效果如图17.17和图17.18所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_625.jpg" width="575" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图17.17 Excel数据展示</span>

<div style="display: block;text-align:center;">

<img src="images/image_626.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图17.18 图表数据展示</span>

</div>

<div class="header3">

### 17.3.4 绘制饼形图—Pie()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">绘制饼形图主要使用Pie()对象的add()函数实现。下面介绍add()函数的几个主要参数： <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> series_name：系列名称，用于提示文本和图例标签。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> data_pair：数据项，格式为\[（key1， value1）， （key2， value2）\]。可使用zip()函数先将可迭代对象打包成元组，再转换为列表。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> color：系列标签的颜色。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> radius：饼形图的半径，数组的第一项是内半径，第二项是外半径。默认设置为百分比，相对于容器高和宽中较小的一项的一半。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> rosetype：表示是否展开为南丁格尔图（也称玫瑰图），通过半径区分数据大小。其值为radius或area，radius表示用扇区圆心角展现数据的百分比，用半径展现数据的大小；area表示所有扇区圆心角相同，仅通过半径展现数据的大小。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> is_clockwise：饼形图的扇区是否以顺时针显示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.13】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制饼形图分析各地区销量占比情况</span>**（实例位置：资源包\\MR\\Code\\17\\13）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面绘制饼形图，分析各地区销量占比情况，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入相关模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import Pie</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  from pyecharts import options as opts</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）读取Excel文件，并将数据处理为列表加元组的格式，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df = pd.read_excel('data2.xls')      # </span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Excel</span>文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   x_data=df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">地区</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   y_data=df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">销量</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">将数据转换为列表加元组的格式</span>(\[(key1, value1), (key2, value2)\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   data=\[list(z) for z in zip(x_data, y_data)\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   data.sort(key=lambda x: x\[1\])          # </span>数据排序</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  print(x_data)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  print(data)</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）创建饼形图，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  pie=Pie()                            # </span>创建饼形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  # </span>为饼形图添加数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  pie.add(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15          series_name="</span>地区<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">",            # </span>序列名称</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16          data_pair=data,                # </span>数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  pie.set_global_opts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19          # </span>饼形图标题居中</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20          title_opts=opts.TitleOpts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21              title="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">各地区销量情况分析</span>",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22              pos_left="center"),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">23          # </span>不显示图例</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">24          legend_opts=opts.LegendOpts(is_show=False),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">25      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">26  pie.set_series_opts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">27          label_opts=opts.LabelOpts(), # </span>序列标签</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">28      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">29  pie.render("mypie1.html")            # </span>渲染图表到<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">HTML</span>文件，存放在程序所在目录下</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成名为mypie1.html的HTML文件，打开该文件，效果如图17.19所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_627.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.19 饼形图</span>

</div>

<div class="header3">

### 17.3.5 绘制箱形图—Boxplot()对象

</div>

<div class="part">

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.14】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制简单的箱形图</span>**（实例位置：资源包\\MR\\Code\\17\\14）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制箱形图主要使用Boxplot()对象的add_xaxis()和add_yaxis()函数实现。下面绘制一个简单的箱形图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import Boxplot</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  df = pd.read_excel('Tips.xlsx')  # </span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Excel</span>文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y_data=\[list(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">总消费</span>'\])\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  boxplot=Boxplot()                # </span>创建箱形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  # </span>为箱形图添加数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  boxplot.add_xaxis(\[""\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  boxplot.add_yaxis('',y_axis=boxplot.prepare_data(y_data))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  boxplot.render("myboxplot.html") # </span>渲染图表到<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">HTML</span>文件，存放在程序所在目录下</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成myboxplot.html文件，打开该文件，效果如图17.20所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_628.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.20 箱形图</span>

</div>

<div class="header3">

### 17.3.6 绘制词云图—WordCloud对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">绘制词云图主要使用WordCloud()对象的add()函数实现。下面介绍add()函数的几个主要参数。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> series_name：系列名称，用于提示文本和图例标签。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> data_pair：数据项，格式为\[（word1，count1）， （word2， count2）\]。可使用zip()函数先将可迭代对象打包成元组，再转换为列表。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> shape：字符型，词云图的轮廓。其值为circle、cardioid、diamond、triangle-forward、triangle、pentagon或star。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> mask_image：自定义图片，支持的图片格式为jpg、jpeg、png和ico。该参数支持base64（一种基于64个可打印字符来表示二进制数据的方法）和本地文件路径（相对或者绝对路径都可以）。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> word_gap：单词间隔。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> word_size_range：单词字体大小范围。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> rotate_step：旋转单词角度。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_left：距离左侧的距离。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_top：距离顶部的距离。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_right：距离右侧的距离。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pos_bottom：距离底部的距离。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> width：词云图的宽度。 <img src="images/image_622.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> height：词云图的高度。</span>

<span style="font-size:16px;font-family:'PingFang SC';">要实现词云图，首先需要通过jieba模块的textrank算法从文本中提取关键词。textrank是一种文本排序算法，基于著名的网页排序算法pagerank改动而来。textrank不仅能进行关键词提取，也能做自动文摘。</span>

<span style="font-size:16px;font-family:'PingFang SC';">根据某个词连接所有词汇的权重，重新计算该词汇的权重，并把重新计算的权重传递下去。直到这种变化达到均衡态，权重数值不再发生改变。根据最后权重值，取排列靠前的词汇作为关键词。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.15】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制词云图分析用户评论内容</span>**（实例位置：资源包\\MR\\Code\\17\\15）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面绘制词云图，分析用户的评论内容。具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）安装jieba模块。打开“命令提示符”窗口，通过pip命令安装jieba模块，安装命令如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  pip install jieba</span>

<span style="font-size:16px;font-family:'PingFang SC';">当然，也可以在PyCharm开发环境中安装。（2）导入相关模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import WordCloud</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  from jieba import analyse</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）使用textrank算法从文本中提取关键词，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  textrank = analyse.textrank</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  text = open('111.txt','r',encoding='gbk').read()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  keywords = textrank(text,topK=30)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  list1=\[\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  tup1=()</span>

<span style="font-size:16px;font-family:'PingFang SC';">（4）关键词列表，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   for keyword, weight in textrank(text,topK=30, withWeight=True):</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10      print('%s %s' % (keyword, weight))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11      tup1=(keyword,weight)       # </span>关键词权重</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12      list1.append(tup1)          # </span>添加到列表中</span>

<span style="font-size:16px;font-family:'PingFang SC';">（5）绘制词云图，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  mywordcloud=WordCloud()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  mywordcloud.add('',list1,word_size_range=\[20,100\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  mywordcloud.render('wordclound.html')</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成名为wordclound.html的HTML文件，打开该文件，效果如图17.21所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_629.jpg" width="720" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.21 词云图</span>

</div>

<div class="header3">

### 17.3.7 绘制热力图—HeatMap()对象

</div>

<div class="part">

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.16】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制热力图统计双色球中奖数字出现的次数</span>**（实例位置：资源包\\MR\\Code\\17\\16）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制热力图主要使用HeatMap()对象的add_xaxis()和add_yaxis()函数。下面通过绘制热力图统计2007—2023年双色球中奖数字出现的次数，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入相关模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pyecharts.options as opts</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  from pyecharts.charts import HeatMap</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  import pandas as pd</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）读取Excel文件，并进行数据处理，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df=pd.read_csv('data.csv')                       # </span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Excel</span>文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   series=df\['</span>中奖号码<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\].str.split('  ',expand=True)  # </span>提取中奖号码</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   # </span>统计每一位中奖号码出现的次数</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   df1=df.groupby(series\[0\]).size()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   df2=df.groupby(series\[1\]).size()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   df3=df.groupby(series\[2\]).size()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  df4=df.groupby(series\[3\]).size()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  df5=df.groupby(series\[4\]).size()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  df6=df.groupby(series\[5\]).size()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  df7=df.groupby(series\[6\]).size()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">横向表合并</span>(<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">行对齐</span>)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  data = pd.concat(\[df1,df2,df3,df4,df5,df6,df7\], axis=1,sort=True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  data=data.fillna(0)                               # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">将空值</span>NaN<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">替换为</span>0</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  data=data.round(0).astype(int)                  # </span>将浮点数转换为整数</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）将数据转换为HeatMap支持的列表格式，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  # </span>将数据转换为<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">HeatMap</span>支持的列表格式</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19  value1=\[\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20  for i in range(7):</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21      for j in range(33):</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22          value1.append(\[i,j,int(data.iloc\[j,i\])\])</span>

<span style="font-size:16px;font-family:'PingFang SC';">（4）绘制热力图，代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_630.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成heatmap.html文件，打开该文件，效果如图17.22所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_631.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.22 热力图</span>

</div>

<div class="header3">

### 17.3.8 绘制水球图—Liquid()对象

</div>

<div class="part">

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.17】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制水球图</span>**（实例位置：资源包\\MR\\Code\\17\\17）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制水球图主要使用Liquid()对象的add()函数实现。下面绘制一个简单的涟漪特效散点图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  from pyecharts.charts import Liquid</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  # </span>绘制水球图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  liquid=Liquid()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  liquid.add('',\[0.7\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  liquid.render("myliquid.html")</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成myliquid.html文件，打开该文件，效果如图17.23所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_632.jpg" width="397" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.23 水球图</span>

</div>

<div class="header3">

### 17.3.9 绘制日历图—Calendar()对象

</div>

<div class="part">

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例17.18】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制加班日历图</span>**（实例位置：资源包\\MR\\Code\\17\\18）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制日历图主要使用Calendar()对象的add()函数实现。下面绘制一个简单日历图，通过该日历图分析6月份的加班情况，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   from pyecharts import options as opts</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   from pyecharts.charts import Calendar</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df=pd.read_excel('202306.xls')                  # </span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Excel</span>文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   data=df.stack()                                 # </span>行列转换</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   # </span>求最大值和最小值</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   mymax=round(max(data),2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   mymin=round(min(data),2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   index=pd.date_range('20230601','20230630')      # </span>生成日期</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  data_list=list(zip(index,data))                 # </span>合并列表</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  calendar=Calendar()                             # </span>生成日历图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  calendar.add("",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13               data_list,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14               calendar_opts=opts.CalendarOpts(range\_=\['2023-06-01','2023-06-30'\]))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  calendar.set_global_opts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16          title_opts=opts.TitleOpts(title="2023<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">年</span>6<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">月加班情况</span>",pos_left='center'),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17          visualmap_opts=opts.VisualMapOpts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18              max\_=mymax,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19              min\_=mymin+0.1,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20              orient="horizontal",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21              is_piecewise=True,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22              pos_top="230px",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">23              pos_left="70px",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">24          ),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">25      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">26  calendar.render("mycalendar.html")</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，在程序所在路径下生成calendar.html文件，打开该文件，效果如图17.24所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_633.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图17.24 日历图</span>

</div>

<span id="Section116.xhtml"></span>

<div id="Section116.xhtml_Section116.xhtml">

</div>

<div class="header2">

## 17.4 小结

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">本章介绍了如何使用Pyecharts模块实现数据图表的绘制，相比Matplotlib和Seaborn，Pyecharts绘制的图表更加令人惊叹，其动感效果更是Matplotlib和Seaborn无法比拟的。但Pyecharts也存在不足之处，其生成的图表为网页格式，不能够随时查看，需要打开文件进行浏览。Pyecharts更适合Web程序。</span>

<span style="font-size:16px;font-family:'PingFang SC';">Pyecharts还有很多功能，由于篇幅有限不能一一进行介绍，希望读者在学习过程中能够举一反三，绘制出更多精彩的数据分析图表。</span>

</div>

<span id="Section117.xhtml"></span>

<div id="Section117.xhtml_Section117.xhtml">

</div>

<div class="header0">


</div>

<div class="part">

</div>

<div class="header0">


</div>

<div class="part">

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">本篇介绍了四个热门的数据分析项目，其中包含股票数据分析、淘宝网订单分析、网站用户数据分析以及NBA球员薪资的数据分析，通过四个不同类型的数据分析项目，让读者快速掌握Python数据分析的精髓，以将学习到的数据分析技术应用到实践开发中，并为以后的开发积累经验。</span>

<div style="display: block;text-align:center;">

<img src="images/image_634.jpg" width="900" />

</div>

</div>

<span id="Section118.xhtml"></span>

<div id="Section118.xhtml_Section118.xhtml">

</div>

<div class="header1">
