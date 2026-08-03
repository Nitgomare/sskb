# 19 综合案例：淘宝网订单分析

</div>

<div class="part">

</div>

<div class="header1">


</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">淘宝电商每时每刻都会产生大量的订单数据，虽然淘宝后台也提供了数据分析功能，但是很多时候无法满足用户的需求，用户不能按照自己的想法挖掘更有价值的信息进行分析。本章将专门针对淘宝电商订单数据进行挖掘和分析，包括从数据预处理到数据分析的完整过程，掌握了这些分析方法，不但可以大大提高运营效率，还可以定制营销策略，使利润最大化。</span>

<span style="font-size:16px;font-family:'PingFang SC';">本章知识架构及重难点如下。</span>

<div style="display: block;text-align:center;">

<img src="images/image_664.jpg" width="900" />

</div>

</div>

<span id="Section126.xhtml"></span>

<div id="Section126.xhtml_Section126.xhtml">

</div>

<div class="header2">

## 19.1 概述

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">淘宝电商订单分析系统主要包括数据读取与查看、数据缺失性分析、描述性统计分析、数据处理，这些预处理工作完成后，再对数据进行统计分析，包括数据整体情况分析、按订单类型分析订单量、按区域分析订单量、每日订单量分析和小时订单量分析，主要使用Pandas结合第三方图表模块Pyecharts实现。</span>

</div>

<span id="Section127.xhtml"></span>

<div id="Section127.xhtml_Section127.xhtml">

</div>

<div class="header2">

## 19.2 案例效果预览

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">淘宝网订单分析主要包括整体情况分析，如图19.1所示；按订单类型分析订单量，如图19.2所示；按区域分析订单量，如图19.3所示；每日订单量分析，如图19.4所示；小时订单量分析，如图19.5所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_665.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图19.1 整体情况分析</span>

<div style="display: block;text-align:center;">

<img src="images/image_666.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图19.2 按订单类型分析订单量</span>

<div style="display: block;text-align:center;">

<img src="images/image_667.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图19.3 按区域分析订单量</span>

<div style="display: block;text-align:center;">

<img src="images/image_668.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图19.4 每日订单量分析</span>

<div style="display: block;text-align:center;">

<img src="images/image_669.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图19.5 小时订单量分析</span>

</div>

<span id="Section128.xhtml"></span>

<div id="Section128.xhtml_Section128.xhtml">

</div>

<div class="header2">

## 19.3 案例环境

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">本章案例运行环境及所需模块具体如下。 <img src="images/image_670.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 操作系统：Windows 10。 <img src="images/image_670.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> Python版本：Python 3.9及以上。 <img src="images/image_670.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 开发工具：Anaconda3、Jupyter Notebook。 <img src="images/image_670.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 第三方模块：Pandas、Openpyxl、xlrd、xlwt、NumPy、Pyecharts。</span>

</div>

<span id="Section129.xhtml"></span>

<div id="Section129.xhtml_Section129.xhtml">

</div>

<div class="header2">

## 19.4 数据集介绍

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">淘宝电商订单分析系统要用到的数据集为TB_data.xlsx，如图19.6所示，该数据集为淘宝店铺导出的订单数据，其中的一些敏感数据已经进行处理，同时也删除了一些无用的数据。</span>

<span style="font-size:16px;font-family:'PingFang SC';">接下来我们就从这些数据中挖掘出有效的信息来分析淘宝电商订单数据。</span>

<div style="display: block;text-align:center;">

<img src="images/image_671.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">图19.6 数据集TB_data.xlsx</span>

<span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**注意**</span>

<span style="font-size:16px;font-family:'PingFang SC';">获取该数据集可以在本书提供的“资源包”中复制。</span>

</div>

<span id="Section130.xhtml"></span>

<div id="Section130.xhtml_Section130.xhtml">

</div>

<div class="header2">

## 19.5 前期准备

</div>

<div class="part">

</div>

<div class="header3">

### 19.5.1 安装第三方模块

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">本案例中涉及了比较重要的模块，即Pyecharts模块，该模块是一个用于生成Echarts图表的模块。Echarts是百度开源的一个数据可视化JS模块，用Echarts生成的图表可视化效果非常好，而Pyecharts则是专门为了与Python衔接的，方便在Python中直接使用可视化数据分析图表。使用Pyecharts可以生成独立的网页格式的图表，还可以在Flask、Django中直接使用，非常方便。</span>

<span style="font-size:16px;font-family:'PingFang SC';">在Anaconda中安装Pyecharts模块，单击系统“开始”菜单，选择Anaconda3（64-bit）→Anaconda Prompt（anaconda3），打开Anaconda Prompt（anaconda3）命令提示符窗口，使用pip命令安装，命令如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">pip install pyecharts</span>

<span style="font-size:16px;font-family:'PingFang SC';">安装成功后，将提示安装成功的字样，如“Successfully installed pyecharts-2.0.3”。</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">由于Pyecharts各个版本的相关代码有一些区别，因此这里建议读者安装与笔者相同的版本，以免造成不必要的麻烦。</span>

</div>

<div class="header3">

### 19.5.2 新建Jupyter Notebook文件

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">下面新建Jupyter Notebook文件夹和Jupyter Notebook文件，具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）在系统“搜索”文本框中输入Jupyter Notebook，运行Jupyter Notebook。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）新建一个Jupyter Notebook文件夹，命名为“淘宝电商订单分析系统”。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）新建Jupyter Notebook文件。单击“淘宝电商订单分析系统”文件夹，进入该文件夹，单击右上角的New按钮，由于我们创建的是Python文件，因此选择Python 3（ipykernel）。文件创建完成后就可以编写代码了。</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">具体步骤可以参考18.4.2节。</span>

</div>

<div class="header3">

### 19.5.3 导入必要的模块

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">本项目主要使用了Pandas、NumPy、Pyecharts模块，下面在Jupyter Notebook中导入项目所需要的模块，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">import numpy as np</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">from pyecharts.components import Table</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">from pyecharts.options import ComponentTitleOpts</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">from pyecharts.charts import Pie</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">from pyecharts.charts import Line</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">from pyecharts.charts import Bar</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">from pyecharts import options as opts</span>

</div>

<div class="header3">

### 19.5.4 数据读取与查看

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">使用Pandas的read_excel()函数读取数据，显示前5条数据，并使用Pandas的样式函数高亮显示指定值，此处显示缺失值，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df=pd.read_excel('TB_data.xlsx')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.head(5).style.highlight_null()</span>

<img src="images/image_672.jpg" width="39" />

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，单击工具栏中的运行按钮 ，或者按快捷键Ctrl+Enter运行本单元，效果如图19.7所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_673.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图19.7 数据读取（前5条）</span>

<span style="font-size:16px;font-family:'PingFang SC';">图19.7中的数据通过高亮显示，缺失值数据一目了然。数据的高亮显示主要使用了Pandas的style属性，它主要用来美化DataFrame和Series数据的输出格式，能够更加直观地显示数据结果。</span>

<span style="font-size:16px;font-family:'PingFang SC';">style属性可以对输出数据格式化，突出显示特殊值，像Excel一样的条件格式中的数据条样式，或者类似Excel的条件格式中的显示色阶样式，用颜色深浅来直观表示数据大小等。感兴趣的读者可以通过官网查阅。</span>

</div>

<span id="Section131.xhtml"></span>

<div id="Section131.xhtml_Section131.xhtml">

</div>

<div class="header2">

## 19.6 数据预处理

</div>

<div class="part">

</div>

<div class="header3">

### 19.6.1 缺失性分析

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">查看摘要信息和数据是否缺失。在进行数据统计分析前，首先要清晰地了解数据，查看数据中是否有缺失值、列数据类型是否正常。下面使用info()函数查看数据的类型、非空值情况以及内存使用量等，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">\# </span>查看摘要信息</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.info()</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，结果如图19.8所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">从运行结果得知：数据有2660行19列，并列出了每一列的名称和数据类型，部分数据包含缺失值，如宝贝标题、收货地址、是否手机订单、确认收货时间、订单付款时间。</span>

<span style="font-size:16px;font-family:'PingFang SC';">另外，还有一个函数可以查看缺失值，即查看列数据是否包含缺失值，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">\# </span>检查数据中的空值</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.isnull().any()</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，结果如图19.9所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_674.jpg" width="697" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图19.8 查看摘要信息</span>

<div style="display: block;text-align:center;">

<img src="images/image_675.jpg" width="587" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图19.9 查看列数据是否包含空值</span>

<span style="font-size:16px;font-family:'PingFang SC';">因此，通过该函数也可以清晰地看出包含缺失值的列。</span>

</div>

<div class="header3">

### 19.6.2 描述性统计分析

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">描述性统计分析主要查看数据的统计信息，如最大值、最小值、平均值等。同时，也可以从中洞察异常数据，如空数据和值为0的数据。下面使用DataFrame()对象的describe()函数快速查看统计信息，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">\# </span>描述性统计分析</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.describe()</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，结果如图19.10所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_676.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图19.10 描述性统计分析</span>

<span style="font-size:16px;font-family:'PingFang SC';">从运行结果得知：数据整体统计分布情况，包括总计数值、均值、标准差、最小值、1/4分位数（25%）、1/2分位数（50%）、3/4分位数（75%）和最大值。其中“买家实际支付金额”为43.89的占25%，62.86的占50%，199的占75%，说明大概率有75%的用户购买了编程词典个人版产品。</span>

</div>

<div class="header3">

### 19.6.3 数据处理

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">通过缺失性分析和描述性统计分析，发现数据中存在异常，如宝贝标题为空、订单付款时间为空、买家实际支付金额为0等。下面对异常数据进行删除处理，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">\# </span>去除空值，订单付款时间和宝贝标题非空值才保留</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">\# </span>去除买家实际支付金额为<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">0</span>的记录</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df1=df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单付款时间</span>'\].notnull() & df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">宝贝标题</span>'\].notnull() & df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">买家实际支付金额</span>'\] !=0\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">print(df1.head(10))</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，结果如图19.11所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_677.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图19.11 数据处理（部分数据）</span>

</div>

<span id="Section132.xhtml"></span>

<div id="Section132.xhtml_Section132.xhtml">

</div>

<div class="header2">

## 19.7 数据统计分析

</div>

<div class="part">

</div>

<div class="header3">

### 19.7.1 整体情况分析

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">数据处理完成后，接下来对淘宝电商订单数据进行整体分析，主要包括总订单数、总订单金额、已完成订单数、总实际收入金额、退款订单数、总退款金额、未付款订单数、成交率和退货率。程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   # </span>创建表格对象</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   table=Table()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   # </span>设置表头</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   headers=\['</span>总订单数<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>总订单金额<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>已完成订单数<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>总实际收入金额<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>退款订单数<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>总退款金额<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>未付款订单数<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>成交率<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>退</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">    <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">货率</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   # </span>行数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   rows=\[\[df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count(),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7          df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">总金额</span>'\].sum(),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8          df1\[df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单状态</span>'\] == '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">交易成功</span>'\]\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count(),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9          df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">买家实际支付金额</span>'\].sum(),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10         df1\[df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单关闭原因</span>'\] == '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">退款</span>'\]\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count(),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11         f"{df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">退款金额</span>'\].sum():.2f}",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12         df1\[df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单关闭原因</span>'\] == '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">买家未付款</span>'\]\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count(),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13         f"{df1\[df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单状态</span>'\] == '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">交易成功</span>'\]\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count()/df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count():.2%}",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14         f"{df1\[df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单关闭原因</span>'\] == '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">退款</span>'\]\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count()/df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count():.2%}"\]\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  # </span>增加表格</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  table.add(headers,rows)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  # </span>设置表格标题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  table.set_global_opts(title_opts=ComponentTitleOpts(title='<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">整体情况分析表</span>'))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19  # </span>显示表格</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20  table.render_notebook()</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，结果如图19.12所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_678.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图19.12 整体情况分析表</span>

</div>

<div class="header3">

### 19.7.2 按订单类型分析订单量

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">淘宝电商订单大多数为手机订单，下面通过饼形图分析手机订单占比情况，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  # </span>计算手机和非手机订单量</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  a=df1\[df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">是否手机订单</span>'\] == '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">手机订单</span>'\]\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  b=df1\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count()-a</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  x_data=\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">手机订单</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">非手机订单</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  y_data=\[int(a),int(b)\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">将数据转换为列表加元组的格式</span>(\[(key1, value1), (key2, value2)\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   data=\[list(z) for z in zip(x_data, y_data)\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   pie=Pie()                                 # </span>创建饼形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>为饼形图添加数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  pie.add(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11          series_name="</span>订单类型<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">",             # </span>序列名称</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12          data_pair=data,                     # </span>数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  pie.set_global_opts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15          # </span>饼形图标题居中</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16          title_opts=opts.TitleOpts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17              title="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">按订单类型分析订单量</span>",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18              pos_left="center"),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19          # </span>不显示图例</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20          legend_opts=opts.LegendOpts(is_show=False),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22  pie.set_series_opts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">23          # </span>序列标签和百分比</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">24          label_opts=opts.LabelOpts(formatter='{b}:{d}%'),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">25      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">26  # </span>显示图表</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">27  pie.render_notebook()</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，结果如图19.13所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_679.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图19.13 按订单类型分析订单量</span>

<span style="font-size:16px;font-family:'PingFang SC';">从图19.13中可以看出，手机订单占据所有订单类型的69%，可见大多数用户都使用手机购买支付。</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">由于模块版本不同，运行的图表可能会出现颜色、样式等不同的显示效果。</span>

</div>

<div class="header3">

### 19.7.3 按区域分析订单量

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">通过饼形图统计分析不同区域的订单量，可实现按区域分析订单量，不同区域主要来源于“收货地址”。而在导出的订单数据中，我们发现“收货地址”是复合组成的（即由多项内容组成）。例如，“收货地址”由省、市、区、街道门牌号等信息组成。那么，如果要按区域分析订单量，则首先需要使用split()函数将“收货地址”信息中的“省”“市”和“区”进行拆分，然后实现按区域统计分析订单量，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   df2=df1.copy()                                            # </span>复制数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   series=df2\['</span>收货地址<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\].str.split(' ',expand=True)           # </span>拆分收货地址</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   df2\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">省</span>'\]=series\[0\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df2\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">市</span>'\]=series\[1\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   df2\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">区</span>'\]=series\[2\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   # </span>按区域统计订单量并降序排序</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   df_groupby=df2.groupby('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">省</span>')\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count().sort_values(ascending=False)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   print(df_groupby)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>获取区域和订单量</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  x_data=df_groupby.index</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  y_data=df_groupby.values.astype(str)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">将数据转换为列表加元组的格式</span>(\[(key1, value1), (key2, value2)\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  data=\[list(z) for z in zip(x_data, y_data)\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  pie=Pie()                                                 # </span>创建饼形图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  # </span>为饼形图添加数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  pie.add(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17          series_name="</span>区域<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">",                                 # </span>序列名称</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18          data_pair=data,                                     # </span>数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20  pie.set_global_opts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21          # </span>饼形图标题居中</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22          title_opts=opts.TitleOpts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">23              title="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">按区域分析订单量</span>",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">24              pos_left="center"),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">25          legend_opts=opts.LegendOpts(is_show=False),       # </span>不显示图例</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">26      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">27  pie.set_series_opts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">28          label_opts=opts.LabelOpts(formatter='{b}:{d}%'),  # </span>序列标签和百分比</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">29      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">30  pie.render_notebook()                                     # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，结果如图19.14所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_680.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图19.14 按区域分析订单量</span>

<span style="font-size:16px;font-family:'PingFang SC';">从图19.14中可以看出，广东省订单量最多，是购买力较强的区域。</span>

</div>

<div class="header3">

### 19.7.4 每日订单量分析

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">通过折线图分析每日订单量，由于“订单付款时间”为日期时间格式，因此首先需要对“订单付款时间”进行处理，从中提取日期，然后按日期统计订单量，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   # </span>复制数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   df3=df1.copy()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   # </span>格式化<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>订单付款时间<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>为日期格式</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df3\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">日期</span>'\]=df3\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单付款时间</span>'\].dt.strftime('%Y-%m-%d')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   # </span>按日期统计订单量</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   df3=df3.groupby('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">日期</span>')\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单编号</span>'\].count()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   # </span>创建折线图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   line=Line()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>为折线图添加<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴和<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  line.add_xaxis(list(df3.index))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  line.add_yaxis("<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单量</span>",list(df3.values.astype(str)))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  line.set_global_opts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13          # </span>折线图标题居中</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14          title_opts=opts.TitleOpts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15              title="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">每日订单量分析</span>",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16              pos_left="center"),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17          # </span>不显示图例</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18          legend_opts=opts.LegendOpts(is_show=False),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20  # </span>显示图表</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21  line.render_notebook()</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，结果如图19.15所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_681.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图19.15 每日订单量分析</span>

</div>

<div class="header3">

### 19.7.5 小时订单量分析

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">通过柱形图分析小时订单量，由于“订单付款时间”为日期时间格式，因此首先需要对“订单付款时间”进行处理，从中提取小时，然后按小时统计订单量，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   df4=df1.copy()                                       # </span>复制数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   df4\['</span>小时<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\]=df4\['</span>订单付款时间<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\].dt.strftime('%H')    # </span>格式化<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>订单付款时间<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>为小时格式</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   df4=df4.groupby('</span>小时<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">')\['</span>订单编号<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\].count()        # </span>按小时统计订单量</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   bar = Bar()                                          # </span>创建柱形图并设置主题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   # </span>为柱形图添加<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*x*</span>轴和<span style="font-size:14px;font-style: oblique;color:rgb(0, 0, 0);font-family:'Source Code Pro';">*y*</span>轴数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   bar.add_xaxis(list(df4.index))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   bar.add_yaxis('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">订单量</span>',list(df4.values.astype(str)))</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   bar.set_global_opts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9           # </span>柱形图标题居中</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10          title_opts=opts.TitleOpts(</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11              title="<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">小时订单量分析</span>",</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12              pos_left="center"),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13          legend_opts=opts.LegendOpts(is_show=False),   # </span>不显示图例</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14      )</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  bar.render_notebook()                                 # </span>显示图表</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，结果如图19.16所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_682.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图19.16 小时订单量分析</span>

<span style="font-size:16px;font-family:'PingFang SC';">从图19.16中可以看出，上午9点—11点这个时间段订单付款较多。</span>

</div>

<span id="Section133.xhtml"></span>

<div id="Section133.xhtml_Section133.xhtml">

</div>

<div class="header1">
