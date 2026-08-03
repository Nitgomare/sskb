# 13 Matplotlib模块进阶

</div>

<div class="part">

</div>

<div class="header1">


</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">相信通过上一章的学习，你已经掌握了Matplotlib的基础知识，学会了绘制各种类型的图表。本章是Matplotlib的进阶，包括图表的颜色设置、日期时间处理、次坐标轴图表、多个子图表绘制等内容。</span>

<span style="font-size:16px;font-family:'PingFang SC';">本章知识架构如下。</span>

<div style="display: block;text-align:center;">

<img src="images/image_449.jpg" width="900" />

</div>

</div>

<span id="Section084.xhtml"></span>

<div id="Section084.xhtml_Section084.xhtml">

</div>

<div class="header2">

## 13.1 图表的颜色设置

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">数据可视化过程中，可以通过颜色区分数据、展示数据的变化等，从而增加用户对可视化图形的理解。Matplotlib支持使用各种颜色和颜色图来可视化信息。</span>

</div>

<div class="header3">

### 13.1.1 常用颜色

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Matplotlib常用颜色为蓝色（blue）、绿色（green）、红色（red）、蓝绿色（cyan）、洋红色（magenta）、黄色（yellow）、黑色（black）、白色（white），如表13.1所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">表13.1 Matplotlib常用颜色</span>

<div style="display: block;text-align:center;">

<img src="images/image_450.jpg" width="900" />

</div>

</div>

<div class="header3">

### 13.1.2 可识别的颜色格式

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Matplotlib可以识别很多种颜色格式，具体如表13.2所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">表13.2 颜色格式及举例说明</span>

<div style="display: block;text-align:center;">

<img src="images/image_451.jpg" width="900" />

</div>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.1】**</span><span style="font-size:16px;font-family:'PingFang SC';">不同颜色格式的运用</span>**（实例位置：资源包\\Code\\13\\01）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面通过具体的例子演示Matplotlib可识别的颜色格式的运用，程序代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_452.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.1所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_453.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.1 不同颜色格式的运用</span>

</div>

<div class="header3">

### 13.1.3 颜色映射

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">数据可视化过程中，有时我们希望图表的颜色与数据集中某个变量的值相关，颜色可以随着该变量值的变化而变化，以反映数据变化趋势、数据的聚集、分析者对数据的理解等信息。这时，我们就可以使用Matplotlib的颜色映射功能，即将数据映射到颜色。需要注意的是，Matplotlib颜色映射仅支持cmap参数和colormap参数的图表类型。下面介绍与Matplotlib颜色映射有关的颜色图。 <img src="images/image_454.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 连续化按顺序的颜色图：在两种色调之间近似平滑变化。通常是从低饱和度到高饱和度（如从白色到明亮的蓝色）。适用于大多数科学数据，可直观地看出数据从低到高的变化。 <img src="images/image_455.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 以中间值颜色命名。例如，第一个viridis（松石绿），如图13.2所示。 <img src="images/image_455.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 以色系名称命名，由低饱和度到高饱和度过渡。 <img src="images/image_455.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 以风格命名。 <img src="images/image_454.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 两端发散的颜色图：具有中间值（通常是浅色），并在高值和低值处平滑变化为两种不同的色调。适用于数据的中间值很大的情况（如0，正值和负值分别表示颜色图的不同颜色）。 <img src="images/image_454.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 循环颜色图：两种不同颜色在不饱和颜色的中间和开始／结束处相交的亮度变化，应用于端点周围的值，如相位角、风向或一天中的时间。 <img src="images/image_454.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 定性的颜色图：常为杂色，用于表示没有顺序或关系的数据信息。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.2】**</span><span style="font-size:16px;font-family:'PingFang SC';">颜色映射的运用</span>**（实例位置：资源包\\Code\\13\\02）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">例如，一个简单的热力图，通过cmap参数设置颜色映射，使用连续化按顺序的颜色图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import matplotlib.pyplot as plt        # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  X = \[\[1,2\],\[3,4\],\[5,6\],\[7,8\],\[9,10\]\]   # </span>创建<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  plt.imshow(X,cmap='cool')            # </span>绘制热力图，设置<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">cmap</span>颜色映射为<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">cool</span>色图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  plt.show()                           # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.3所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_456.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图13.2 以中间值颜色命名的颜色图</span>

<div style="display: block;text-align:center;">

<img src="images/image_457.jpg" width="700" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图13.3 颜色映射的运用</span>

</div>

<span id="Section085.xhtml"></span>

<div id="Section085.xhtml_Section085.xhtml">

</div>

<div class="header2">

## 13.2 处理日期与时间

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">数据分析时经常会遇到日期类数据，图表中也经常需要在坐标轴上显示日期或将日期作为标签。本节就来介绍Matplotlib中是如何处理日期和时间的。</span>

</div>

<div class="header3">

### 13.2.1 dates子模块

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Matplotlib使用浮点数表示日期，浮点数指定从0001-01-01 UTC开始的天数，加上1。如0001-01-01，06:00是1.25，不是0.25。不支持小于1的值，即0001-01-01 UTC之前的日期。</span>

<span style="font-size:16px;font-family:'PingFang SC';">Matplotlib的dates子模块提供了一些函数，可以在datetime对象和Matplotlib日期之间进行转换，如表13.3所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">表13.3 dates子模块转换函数</span>

<div style="display: block;text-align:center;">

<img src="images/image_458.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">Matplotlib会自动管理刻度，尤其是刻度标签，导致可读性差、两个数据点之间的时间间隔不清晰、日期标签重叠等现象。dates子模块中提供了一些专门管理日期刻度的对象，如表13.4所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">表13.4 dates子模块日期刻度对象</span>

<div style="display: block;text-align:center;">

<img src="images/image_459.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">显示日期过程中，有时需要将日期格式化为需要的格式，dates子模块提供了一些关于格式化的对象，如表13.5所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">表13.5 dates模块日期格式化对象</span>

<div style="display: block;text-align:center;">

<img src="images/image_460.jpg" width="900" />

</div>

</div>

<div class="header3">

### 13.2.2 设置坐标轴日期的显示格式

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">绘制图表过程中，可能会出现由于日期显示过长而影响图表外观的情况。此时可以通过设置<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴日期的显示格式来解决这个问题，主要使用dates子模块的DateFormatter()对象，该对象可以将任意格式的日期按要求进行格式化。时间日期格式化符号如下： <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %y：两位数的年份表示（00～99）。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %Y：四位数的年份表示（0000～9999）。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %m：月份（01～12）。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %d：月内的一天（0～31）。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %H：24小时制小时数（0～23）。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %I：12小时制小时数（01～12）。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %M：分钟数（00～59）。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %S：秒（00～59）。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %a：本地简化星期名称。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %A：本地完整星期名称。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %b：本地简化的月份名称。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %B：本地完整的月份名称。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %c：本地相应的日期表示和时间表示。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %j：年内的一天（001～366）。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %p：本地A.M.或P.M.的等价符。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %U：一年中的星期数（00～53）星期天为星期的开始。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %w：星期（0～6），星期天为星期的开始。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %W：一年中的星期数（00～53）星期一为星期的开始。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %x：本地相应的日期表示。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %X：本地相应的时间表示。 <img src="images/image_461.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> %Z：当前时区的名称。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.3】**</span><span style="font-size:16px;font-family:'PingFang SC';">设置日期显示格式</span>**（实例位置：资源包\\Code\\13\\03）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">例如，日期为月、日、年的格式（如01/01/2023），下面使用DateFormatter()对象将其格式化为月日的格式（如01-01），程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import matplotlib.dates as mdates         # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.dates</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  import matplotlib.pyplot as plt           # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  # </span>生成<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*xy*</span>轴数据，<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴为日期字符串</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  x = \['01/02/2023', '01/03/2023', '01/04/2023'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  y=\[12,22,45\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  print(x)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))  # </span>配置横坐标格式化日期</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  plt.plot(x,y)                             # </span>绘制图表</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  plt.show()                              # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.4所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_462.jpg" width="724" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.4 设置日期显示格式</span>

</div>

<div class="header3">

### 13.2.3 设置坐标轴日期刻度标签

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">dates子模块的日期刻度对象可以快速完成坐标轴日期刻度的设置，如YearLocator()以年为刻度、MonthLocator()以月为刻度、WeekdayLocator()以星期为刻度等。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.4】**</span><span style="font-size:16px;font-family:'PingFang SC';">设置</span><span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span><span style="font-size:16px;font-family:'PingFang SC';">轴日期刻度为星期</span>**（实例位置：资源包\\Code\\13\\04）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">在<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴上显示日期问题很多，尤其是用日期做标签时难以管理。如图13.5所示，<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴日期刻度自动显示为半个月一个刻度，这样不符合需求。下面将其设置为一个星期一个刻度，程序代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_463.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.6所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_464.jpg" width="808" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图13.5 原日期</span>

<div style="display: block;text-align:center;">

<img src="images/image_465.jpg" width="812" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图13.6 设置<span style="font-size:16px;font-style: oblique;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">*x*</span>轴日期刻度为星期</span>

</div>

<span id="Section086.xhtml"></span>

<div id="Section086.xhtml_Section086.xhtml">

</div>

<div class="header2">

## 13.3 次坐标轴（双坐标轴）

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">次坐标轴也被称为第二坐标轴或副坐标轴，用于在一个图表中显示两个不同坐标的图表。在Matplotlib模块中可以通过twinx()函数和twiny()函数实现。</span>

</div>

<div class="header3">

### 13.3.1 共享*x*坐标轴—twinx()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">twinx()函数用于创建并返回一个共享<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴、两个<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴且第二个<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴的刻度在子图的右侧显示，语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">plt.twinx(ax=None)</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_466.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> ax：ax的值的类型为Axes()对象，默认值为None，即当前子图。 <img src="images/image_466.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 返回值：Axes()对象，即新创建的子图。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.5】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制双</span><span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span><span style="font-size:16px;font-family:'PingFang SC';">轴图表</span>**（实例位置：资源包\\Code\\13\\05）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">如果想看到商品每日销售数量和销售金额随日期的变化，可以使用双<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴图表。程序代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_467.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.7所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_468.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.7 双<span style="font-size:16px;font-style: oblique;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">*y*</span>轴图表</span>

</div>

<div class="header3">

### 13.3.2 共享*y*坐标轴—twiny()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">twiny()函数用于创建并返回一个共享<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴、两个<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴且第二个<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴的刻度在子图的顶部显示，语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">plt.twiny(ax=None)</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_466.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> ax：ax的值的类型为Axes()对象，默认值为None，即当前子图。 <img src="images/image_466.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 返回值：Axes()对象，即新创建的子图。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.6】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制双</span><span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span><span style="font-size:16px;font-family:'PingFang SC';">轴图表</span>**（实例位置：资源包\\Code\\13\\06）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面绘制双<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴图表，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import matplotlib.pylab as plt  # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  # </span>创建<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴和<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x = \[1,2,3,4,5\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y = \[10,20,30,40,50\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  fig = plt.figure()            # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  ax1 = fig.add_subplot(111)      # </span>创建子图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  ax1.plot(x, y)                  # </span>绘制折线图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  ax2 = ax1.twiny()             # </span>共享<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴添加一条<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  plt.show()                    # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.8所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_469.jpg" width="811" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.8 双<span style="font-size:16px;font-style: oblique;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">*x*</span>轴图表</span>

</div>

<span id="Section087.xhtml"></span>

<div id="Section087.xhtml_Section087.xhtml">

</div>

<div class="header2">

## 13.4 绘制多个子图表

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Matplotlib可以实现在一张图上绘制多个子图表。Matplotlib提供了三种方法，一是subplot()函数，二是subplots()函数，三是add_subplot()函数，下面分别进行介绍。</span>

</div>

<div class="header3">

### 13.4.1 subplot()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">subplot()函数直接指定划分方式和位置，它可以将一个绘图区域划分为<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*n*</span>个子图，每个subplot()函数只能绘制一个子图。语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">plt.subplot(\*args,\*\*kwargs)</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_470.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> \*args：当传入的参数个数未知时使用\*args。 <img src="images/image_470.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> \*\*kwargs：关键字参数，其他可选参数。</span>

<span style="font-size:16px;font-family:'PingFang SC';">例如，绘制一个2×3的区域，subplot（2,3,3），将画布分成2行3列在第3个区域中绘制，用坐标表示如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">(1,1),(1,2),(1,3)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">(2,1),(2,2),(2,3)</span>

<span style="font-size:16px;font-family:'PingFang SC';">如果行列的值都小于10，那么可以把它们缩写为一个整数，例如，subplot（233）。</span>

<span style="font-size:16px;font-family:'PingFang SC';">另外，subplot在指定的区域中创建一个轴对象时，如果新创建的轴和之前创建的轴重叠，那么之前的轴将被删除。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.7】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用subplot()函数绘制多子图的空图表</span>**（实例位置：资源包\\Code\\13\\07）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制一个2×3包含6个子图的空图表，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import matplotlib.pyplot as plt  # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  # </span>绘制<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6</span>个子图的空图表</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  plt.subplot(2,3,1)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  plt.subplot(2,3,2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  plt.subplot(2,3,3)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  plt.subplot(2,3,4)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  plt.subplot(2,3,5)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  plt.subplot(2,3,6)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  plt.show()                       # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.9所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_471.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.9 6个子图的空图表</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.8】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制包含多个子图的图表</span>**（实例位置：资源包\\Code\\13\\08）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">将简单图表整合到一张图表中，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import matplotlib.pyplot as plt      # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1</span>个子图表<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">-</span>折线图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   plt.subplot(2,2,1)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   plt.plot(\[1, 2, 3, 4,5\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2</span>个子图表<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">-</span>散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   plt.subplot(2,2,2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   plt.plot(\[1, 2, 3, 4,5\], \[2, 5, 8, 12,18\], 'ro')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>个子图表<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">-</span>柱形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   plt.subplot(2,1,2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  x=\[1,2,3,4,5,6\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  height=\[10,20,30,40,50,60\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  plt.bar(x,height)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  plt.show()                           # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.10所示。上述举例，有两个关键点一定要掌握：</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）每绘制一个子图表都要调用一次subplot()函数。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）绘图区域位置编号。</span>

<span style="font-size:16px;font-family:'PingFang SC';">subplot()函数的前面两个参数指定的是一个画布被分割成的行数和列数，后面一个参数则指定的是当前绘制区域位置编号，编号规则是行优先。</span>

<span style="font-size:16px;font-family:'PingFang SC';">例如，图13.10中有3个子图表，第1个子图表subplot（2,2,1），即将画布分成2行2列，在第1个子图中绘制折线图；第2个子图表subplot（2,2,2），即将画布分成2行2列，在第2个子图中绘制散点图；第3个子图表subplot（2,1,2），即将画布分成2行1列，由于第1行已经占用了，所以我们在第2行也就是第3个子图中绘制柱形图。示意图如图13.11所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_472.jpg" width="781" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图13.10 多个子图</span>

<div style="display: block;text-align:center;">

<img src="images/image_473.jpg" width="625" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图13.11 多个子图示意图</span>

</div>

<div class="header3">

### 13.4.2 subplots()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">使用subpot()函数绘图时，每次都需要指定绘图区域，非常麻烦。subplots()函数则非常直接，它会事先把画布区域分割好。</span>

<span style="font-size:16px;font-family:'PingFang SC';">subplots()函数用于创建画布和子图，语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot.subplots(nrows,ncols,sharex,sharey,squeeze,subplot_kw,gridspec_kw,\*\*fig_kw)</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_470.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> nrows和ncols：表示将画布分割成几行几列。例如，nrows=2、ncols=2表示将画布分割为2行2列，起始值都为0。当调用画布中的坐标轴时，ax\[0，0\]表示调用左上角的，ax\[1，1\]表示调用右下角的。 <img src="images/image_470.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> sharex和sharey：布尔值，或者值为none、all、row、col，默认值为False。用于控制<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴或<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴之间的属性共享。具体参数值说明如下： <img src="images/image_474.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> True或者all：表示<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴或<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴属性在所有子图中共享。 <img src="images/image_474.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> False或者none：每个子图的<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴或<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴都是独立的部分。 <img src="images/image_474.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> row：每个子图在一个<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴或<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴共享行（row）。 <img src="images/image_474.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> col：每个子图在一个<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴或<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴共享列（column）。 <img src="images/image_470.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> squeeze：布尔值，默认值为True。额外的维度从返回的Axes（轴）对象中挤出，对于n×1或1×n个子图，返回一个一维数组，对于n×m，n＞1和m＞1返回一个二维数组；如果值为False，则表示不进行挤压操作，返回一个元素为Axes实例的二维数组，即使它最终是1×1。 <img src="images/image_470.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> subplot_kw：字典类型，可选参数。把字典的关键字传递给add_subplot来创建每个子图。 <img src="images/image_470.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> gridspec_kw：字典类型，可选参数。把字典的关键字传递给GridSpec构造函数创建子图放在网格里（grid）。 <img src="images/image_470.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> \*\*fig_kw：把所有详细的关键字参数传给figure。</span>

<span style="font-size:16px;font-family:'PingFang SC';">subplots()函数的返回值是一个元组，包括一个画布对象figure()和坐标轴对象axes()，其中axes()对象的数量等于nrows×ncols，且每个axes()对象都可以通过索引值访问。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.9】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用subplots()函数绘制多子图的空图表</span>**（实例位置：资源包\\13\\09）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制一个2×3包含6个子图的空图表，使用subplots()函数只需3行代码。</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import matplotlib.pyplot as plt  # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  figure,axes=plt.subplots(2,3)    #  2</span>行<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>列的子图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  plt.show()                     # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">上述代码中，figure和axes是两个关键点。 <img src="images/image_470.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> figure：绘制图表的画布。 <img src="images/image_470.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> axes：坐标轴对象，可以理解为在figure（画布）上绘图坐标轴对象，它帮我们规划出了一个个科学作图的坐标轴系统。</span>

<span style="font-size:16px;font-family:'PingFang SC';">通过图13.12很容易明白，灰色的是画布（figure），白色带坐标轴的是坐标轴对象（axes）。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.10】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用subplots()函数绘制多子图图表</span>**（实例位置：资源包\\Code\\13\\10）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用subplots()函数将前面所学的简单图表整合到一张图表中，效果如图13.13所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_475.jpg" width="868" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图13.12 坐标系统示意图</span>

<div style="display: block;text-align:center;">

<img src="images/image_476.jpg" width="864" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图13.13 多子图图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import matplotlib.pyplot as plt                 # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   figure,axes=plt.subplots(2,2)                   #  2</span>行<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2</span>列的子图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   axes\[0,0\].plot(\[1, 2, 3, 4,5\])                # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1</span>个子图表<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">-</span>折线图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   axes\[0,1\].plot(\[1, 2, 3, 4,5\], \[2, 5, 8, 12,18\], 'ro')  # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2</span>个子图表<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">-</span>散点图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>个子图表<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">-</span>柱形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   x=\[1,2,3,4,5,6\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   height=\[10,20,30,40,50,60\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   axes\[1,0\].bar(x,height)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4</span>个子图表<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">-</span>饼形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  x = \[2,5,12,70,2,9\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  axes\[1,1\].pie(x,autopct='%1.1f%%')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  plt.show()                                    # </span>显示图表</span>

</div>

<div class="header3">

### 13.4.3 add\_subplot()函数

</div>

<div class="part">

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.11】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用add_subplot()函数绘制多子图图表</span>**（实例位置：资源包\\Code\\13\\11）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">add_subplot()函数也可以实现在一张图上绘制多个子图表，用法与subplot()函数基本相同。我们先来看一段代码：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import matplotlib.pyplot as plt    # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   fig = plt.figure()               # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   # </span>绘制多子图图表</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   ax1 = fig.add_subplot(2,3,1)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   ax2 = fig.add_subplot(2,3,2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   ax3 = fig.add_subplot(2,3,3)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   ax4 = fig.add_subplot(2,3,4)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   ax5 = fig.add_subplot(2,3,5)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   ax6 = fig.add_subplot(2,3,6)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  plt.show()                       # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">上述代码同样是绘制一个2×3包含6个子图的空图表。首先创建figure实例（画布），然后通过ax1 = fig.add_subplot（2,3,1）创建第1个子图表，返回Axes实例（坐标轴对象），第1个参数为行数，第2个参数为列数，第3个参数为子图表的位置。</span>

<span style="font-size:16px;font-family:'PingFang SC';">以上我们用3种方法实现了在一张图上绘制多个子图表，3种方法各有所长。subplot()和add_subplot()函数比较灵活，定制化效果比较好，可以实现子图表在图中的各种布局（如一张图上3个图表或5个图表可以随意摆放），而subplots()函数则不那么灵活，但它可以用较少的代码实现绘制多个子图表。</span>

</div>

<div class="header3">

### 13.4.4 子图表共用一个坐标轴

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">绘图过程中，经常会遇到几个子图共用一个坐标轴的情况，如共用横坐标轴（<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>坐标轴）或共用纵坐标轴（<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>坐标轴），此时可以通过sharex和sharey参数进行设置。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.12】**</span><span style="font-size:16px;font-family:'PingFang SC';">多个子图共用一个</span><span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span><span style="font-size:16px;font-family:'PingFang SC';">轴</span>**（实例位置：资源包\\Code\\13\\12）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制两个子图，一个折线图，一个散点图，共用一个<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴。首先使用subplots()函数创建子图，然后设置sharey参数值为True，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import matplotlib.pyplot as plt                   # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   plt.rcParams\['font.sans-serif'\]=\['SimHei'\]        # </span>解决中文乱码</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   # </span>为<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴指定数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   x=\[1, 2, 3, 4,5\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   y= \[2, 5, 8, 12,18\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   fig,ax=plt.subplots(nrows=1,ncols=2,sharey=True)  # </span>绘制<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1</span>行两列的子图，<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">sharey=True</span>设置共用<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">绘制第一个图</span>(<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">折线图</span>)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   ax1=ax\[0\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   ax1.plot(x,y)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  ax1.set_title("<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">折线图</span>")</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">绘制第二个图</span>(<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">散点图</span>)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  ax2=ax\[1\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  ax2.scatter(x,y,color='red')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  ax2.set_title("<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">散点图</span>")</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  plt.show()                                      # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.14所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_477.jpg" width="815" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.14 多个子图共用一个<span style="font-size:16px;font-style: oblique;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">*y*</span>轴</span>

</div>

<span id="Section088.xhtml"></span>

<div id="Section088.xhtml_Section088.xhtml">

</div>

<div class="header2">

## 13.5 绘制函数图像

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在数学当中经常需要绘制函数图像，在Python中通过Matplotlib模块并结合NumPy数据计算模块也可以绘制出各种函数图像。</span>

</div>

<div class="header3">

### 13.5.1 一元一次函数图像

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">形如y=kx+b（k≠0）的函数称为一元一次函数，而在平面直角坐标系中一元一次函数图像是一条直线。当k\>0时，函数是严格增函数；当k\<0时，函数是严格减函数。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.13】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制一元一次函数图像</span>**（实例位置：资源包\\Code\\13\\13）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先使用NumPy创建<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴数据，然后根据一元一次函数计算<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴，最后绘制一元一次函数图像。程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import matplotlib.pyplot as plt  # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  import numpy as np               # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">numpy</span>模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x=np.arange(-5,5,0.1)            # </span>创建<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y=2\*x+1                          # </span>通过一元一次函数计算<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  plt.plot(x,y)                    # </span>绘制图像</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  plt.show()                     # </span>显示图像</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.15所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_478.jpg" width="730" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.15 一元一次函数图像</span>

</div>

<div class="header3">

### 13.5.2 一元二次函数图像

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">一元二次函数的基本表示形式为y=ax²+bx+c（a≠0），该函数最高次必须为二次，它的图像是一条对称轴与<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴平行或重合于<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴的抛物线。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.14】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制一元二次函数图像</span>**（实例位置：资源包\\Code\\13\\14）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先使用NumPy创建<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴数据，然后根据一元二次函数计算<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴，最后绘制一元二次函数图像。程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import matplotlib.pyplot as plt   # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  import numpy as np                # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">numpy</span>模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x=np.arange(-5,5,0.1)             # </span>创建<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y=x\*\*2+1                          # </span>通过一元二次函数计算<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  plt.plot(x,y)                     # </span>绘制图像</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  plt.show()                      # </span>显示图像</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.16所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_479.jpg" width="779" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.16 一元二次函数图像</span>

</div>

<div class="header3">

### 13.5.3 正弦函数图像—sin()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">正弦函数和余弦函数都是三角函数，我们在高中数学中都曾经学过。Python中主要使用Matplotlib模块和NumPy模块中的sin()函数绘制正弦函数图像。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.15】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制正弦函数图像</span>**（实例位置：资源包\\Code\\13\\15）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先使用sin()函数计算<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴，然后绘制图像。程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import numpy as np                          # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">numpy</span>模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  import matplotlib.pyplot as plt             # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x = np.arange(0, 360)                     #  <span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">轴数据</span>(0~360<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">的数组，不包含</span>360)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y = np.sin(x \* np.pi / 180)               # </span>通过<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">sin()</span>函数计算<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  plt.rcParams\['font.sans-serif'\]=\['SimHei'\]  # </span>解决中文乱码</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  plt.rcParams\['axes.unicode_minus'\]=False    # </span>解决正常显示负号</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  plt.plot(x, y)                              # </span>绘制图像</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  plt.title("</span>正弦函数图像<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">")                 # </span>设置标题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  plt.show()                                # </span>显示图像</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.17所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_480.jpg" width="641" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.17 正弦函数图像</span>

</div>

<div class="header3">

### 13.5.4 余弦函数图像—cos()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Python中主要使用Matplotlib模块和NumPy模块的cos()函数来绘制余弦函数图像。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.16】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制余弦函数图像</span>**（实例位置：资源包\\Code\\13\\16）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先使用NumPy的cos()函数计算<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴，然后绘制图像，程序代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_481.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.18所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_482.jpg" width="657" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.18 余弦函数图像</span>

</div>

<div class="header3">

### 13.5.5 S型生长曲线— Sigmoid()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在高中生物中，S型曲线和J型曲线是比较常见的。S型曲线指种群在一个有限环境中的增长过程，种群数量达到环境条件所允许的最大值（K值），有时会在最大容纳量上下保持相对稳定。下面我们来学习如何使用Matplotlib模块绘制S型生长曲线。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.17】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制高中生物S型曲线</span>**（实例位置：资源包\\Code\\13\\17）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制S型生长曲线，首先使用NumPy的linspace()函数生成等差数列表示<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>轴数据（即时间），使用指数函数exp()计算<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>轴数据（即种群数量），然后绘制图像。程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import numpy as np                     # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">numpy</span>模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  import matplotlib.pyplot as plt        # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  x=np.linspace(-5,5,1000)             # </span>在<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">-5</span>到<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5</span>之间生成<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1000</span>个等差数列</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  y=\[1/(1+np.exp(-i)) for i in x\]    # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">对生成的</span>1000<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">个数循环用</span>Sigmoid<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">函数求对应的</span>y</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  plt.plot(x,y)                          # </span>绘制图像</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  plt.show()                           # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.19所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_483.jpg" width="667" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.19 S型曲线</span>

</div>

<span id="Section089.xhtml"></span>

<div id="Section089.xhtml_Section089.xhtml">

</div>

<div class="header2">

## 13.6 形状与路径

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">除了绘制折线图、柱形图、饼形图、箱形图等，有时我们也需要绘制一些特殊的形状和路径，如绘制椭圆。当然，我们可以通过椭圆的函数表达式，选取一系列坐标值依次相连，但这样的绘制效率很低下，而且绘制出来的图表并不好看。本节介绍两个非常好用的子模块，通过它们可以快速绘制想要的图形。</span>

</div>

<div class="header3">

### 13.6.1 绘制形状—patches子模块

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">形状指的是matplotlib.patches子模块里的一些对象，如圆、椭圆、矩形、多边形、弧、箭头等，也称为“块”。patches子模块框架图如图13.20所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_484.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.20 patches子模块框架图</span>

<span style="font-size:16px;font-family:'PingFang SC';">patches子模块中的对象语法及其说明如表13.6所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">表13.6 patches子模块中对象语法及其说明</span>

<div style="display: block;text-align:center;">

<img src="images/image_485.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">这些几何形状存在于Matplotlib的patches子模块中，若想画出想要的几何图形首先需要导入patches子模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">import matplotlib.patches as patches</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制几何图形的具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）导入patches子模块。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）利用图形模块产生一个几何图形。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）使用add_patch()函数在图像上添加“块”（也就是图形）。</span>

</div>

<div class="header3">

### 13.6.2 绘制路径—path子模块

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">路径通常是一系列可能断开、可能关闭的线和曲线，这里指的是matplotlib.path子模块中Path对象的功能。例如，一条曲线、一个心形都是路径。绘制路径主要使用Path()对象，语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">class matplotlib.path.Path(vertices,codes=None,\_interpolation_steps=1,closed=False,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">readonly=False)</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_486.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> vertices：（N,2）维，float数组，指的是路径path所经过的关键点的一系列坐标（x,y）。 <img src="images/image_486.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> codes：N维数组，定点坐标类型，和vertices长度保持一致。指的是点与点之间到底是怎么连接的，是直线连接、曲线连接还是其他方式连接。codes的类型如下： <img src="images/image_487.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> MOVETO：一个顶点，移动到指定的顶点。一般指的是“起始点”。 <img src="images/image_487.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> LINETO：从当前位置绘制直线到指定的顶点。 <img src="images/image_487.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> CURVE3：从当前位置（用指定控制点）画二次贝塞尔曲线到指定的端点（结束位置）。 <img src="images/image_487.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> CURVE4：从当前位置（用指定控制点）画三次贝塞尔曲线到指定的端点。 <img src="images/image_487.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> CLOSEPOLY：将线段绘制到当前折线的起始点。 <img src="images/image_487.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> STOP：整个路径末尾的标记，一个顶点，path的终点。 <img src="images/image_486.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> \_interpolation_steps：int型，可选参数。 <img src="images/image_486.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> closed：布尔值，可选参数，如果值为True，path将被当作封闭多边形。 <img src="images/image_486.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> readonly：布尔值，可选参数，表示是否不可变。</span>

<span style="font-size:16px;font-family:'PingFang SC';">path路径模块所涉及的内容比较多，这里只介绍简单的应用。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.18】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用path子模块绘制矩形路径</span>**（实例位置：资源包\\Code\\13\\18）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制一个简单的矩形路径，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import matplotlib.pyplot as plt                           # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   from matplotlib.path import Path                          # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.path</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   import matplotlib.patches as patches                      # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.patches</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   verts = \[</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5          (0., 0.),                                        # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">矩形左下角的坐标</span>(left,bottom)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6          (0., 1.),                                        # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">矩形左上角的坐标</span>(left,top)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7          (1., 1.),                                        # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">矩形右上角的坐标</span>(right,top)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8          (1., 0.),                                        # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">矩形右下角的坐标</span>(right, bottom)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9          (0., 0.)\]                                        # </span>封闭到起点</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  codes = \[Path.MOVETO,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11          Path.LINETO,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12          Path.LINETO,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13          Path.LINETO,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14          Path.CLOSEPOLY\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  path = Path(verts, codes)                               # </span>创建一个路径<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Path()</span>对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  # </span>创建画图对象以及创建子图对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  fig = plt.figure()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  ax = fig.add_subplot(111)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19  patch = patches.PathPatch(path, facecolor='red', lw=2)  # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">创建一个</span>patch</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20  ax.add_patch(patch)                                     # </span>将创建的<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">patch</span>添加到<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Axes()</span>对象中</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21  ax.axis(\[-1,2,-1,2\])                                      # </span>设置<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴的坐标轴范围</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22  plt.show()                                              # </span>显示图形</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.21所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_488.jpg" width="611" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.21 绘制矩形路径</span>

</div>

<div class="header3">

### 13.6.3 绘制圆—Circle()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">绘制圆主要使用matplotlib.patches中的Circle()对象，语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">class matplotlib.patches.Circle(xy, radius=5, \*\*kwargs)</span>

<span style="font-size:16px;font-family:'PingFang SC';">在Matplotlib中绘制圆，xy=（x,y）为圆心，radius为半径，默认值为5。其他有效关键字参数如表13.7所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">表13.7 Circle()对象关键字参数</span>

<div style="display: block;text-align:center;">

<img src="images/image_489.jpg" width="900" />

</div>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.19】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制圆形</span>**（实例位置：资源包\\Code\\13\\19）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用内置的几何形状Circle()绘制圆形，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import matplotlib.pyplot as plt             # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  import matplotlib.patches as patches        # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.patches</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  # </span>使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">subplots()</span>函数创建子图，返回值是一个元组，包括一个图形对象和<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">axes</span>对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  fig, ax= plt.subplots()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  circle = patches.Circle((0.5, 0.5), 0.25, alpha=0.5, color='green')   # </span>使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">patches.Circle</span>模块绘制圆</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  ax.add_patch(circle)                      # </span>使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">add_patch()</span>函数在<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">axes</span>对象中添加圆</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  plt.show()                                # </span>显示图形</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.22所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_490.jpg" width="789" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.22 绘制圆形</span>

</div>

<div class="header3">

### 13.6.4 绘制矩形—Rectangle()对象

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">绘制矩形主要使用matplotlib.patches中的Rectangle()对象，该对象用于绘制一个由定位点xy及其宽度和高度定义的矩形。语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">class matplotlib.patches.Rectangle(xy, width, height, angle=0.0, \*\*kwargs)</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_486.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> xy：浮点型，xy=（x,y），矩形在<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*x*</span>方向从xy\[0\]扩展到xy\[0\] +宽度，在<span style="font-size:16px;font-style: oblique;font-family:'PingFang SC';">*y*</span>方向从xy\[1\]扩展到xy\[1\] +高度。 <img src="images/image_486.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> width：浮点型，矩形的宽度。 <img src="images/image_486.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> height：浮点型，矩形的高度。 <img src="images/image_486.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> angle：浮点型，默认值为0.0，绕xy逆时针旋转的角度。</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">其他关键字参数可以参考Circle()对象。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.20】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用Rectangle()对象绘制矩形</span>**（实例位置：资源包\\Code\\13\\20）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">本实例将使用内置的几何形状Rectangle()对象绘制矩形，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import matplotlib.pyplot as plt                               # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  import matplotlib.patches as patches                          # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.patches</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  # </span>使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">subplots()</span>函数创建子图，返回值是一个元组，包括一个图形对象和<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Axes()</span>对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  fig, ax= plt.subplots()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  ax.axis(\[0,5,0,5\])                                          # </span>使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">axis()</span>函数设置<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴和<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴的坐标轴范围</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  rectangle = patches.Rectangle((1, 1),2,3,color='green')   # </span>使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">patches.Rectangle()</span>对象绘制矩形</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  ax.add_patch(rectangle)                                     # </span>使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">add_patch()</span>函数在<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Axes()</span>对象中添加矩形</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  plt.show()                                                  # </span>显示图形</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，效果如图13.23所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_491.jpg" width="855" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图13.23 绘制矩形</span>

</div>

<span id="Section090.xhtml"></span>

<div id="Section090.xhtml_Section090.xhtml">

</div>

<div class="header2">

## 13.7 绘制3D图表

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">3D图表有立体感，也比较美观。下面介绍两种3D图表：三维柱形图和三维曲面图。</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制3D图表依旧使用Matplotlib模块，但需要设置projection参数为3d，具体代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">fig.add_subplot(projection='3d')</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.21】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制3D柱形图</span>**（实例位置：资源包\\Code\\13\\21）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制3D柱形图，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import matplotlib.pyplot as plt              # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">matplotlib.pyplot</span>子模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   import numpy as np                           # </span>导入<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">numpy</span>模块</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   fig = plt.figure()                         # </span>创建画布</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   zs = \[1, 5, 10, 15, 20\]                      # </span>创建<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*z*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   ax = fig.add_subplot(projection='3d')      # </span>添加<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3D</span>图表</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   # </span>绘制<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3D</span>柱形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   for z in zs:</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8       x = np.arange(0, 10)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9       y = np.random.randint(0, 30, size=10)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10      ax.bar(x, y, zs=z, zdir='x', color=\['r', 'green', 'yellow', 'c'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  plt.show()                                 # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图13.24所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例13.22】**</span><span style="font-size:16px;font-family:'PingFang SC';">绘制3D曲面图</span>**（实例位置：资源包\\Code\\13\\22）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">绘制3D曲面图，程序代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_492.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图13.25所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_493.jpg" width="847" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图13.24 3D柱形图</span>

<div style="display: block;text-align:center;">

<img src="images/image_494.jpg" width="846" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图13.25 3D曲面图</span>

</div>

<span id="Section091.xhtml"></span>

<div id="Section091.xhtml_Section091.xhtml">

</div>

<div class="header2">

## 13.8 小结

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">本章内容是Matplotlib模块的进阶，包括许多不经常使用的知识和实例。本章应重点学习如何绘制多子图和次坐标轴的应用，这两部分内容在实际工作中还是非常实用的。其他内容可以有选择性地学习，或者作为查阅资料。</span>

</div>

<span id="Section092.xhtml"></span>

<div id="Section092.xhtml_Section092.xhtml">

</div>

<div class="header1">
