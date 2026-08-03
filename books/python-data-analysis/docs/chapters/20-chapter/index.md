# 20 综合案例：网站用户数据分析

</div>

<div class="part">

</div>

<div class="header1">


</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">网站App平台注册用户分析，是指获得网站或App等平台用户的注册数据，并对用户注册数据进行统计、分析，从中发现产品推广对新注册用户的影响，以及目前的营销策略中可能存在的问题，为进一步修正或重新制定营销策略提供有效的依据。</span>

<span style="font-size:16px;font-family:'PingFang SC';">通过对注册用户的分析可以让企业更加详细、清楚地了解用户的行为习惯，从而找出产品推广中存在的问题，让企业的营销更加精准、有效，从而提高业务转化率，提升企业收益。</span>

<span style="font-size:16px;font-family:'PingFang SC';">本章知识架构及重难点如下。</span>

<div style="display: block;text-align:center;">

<img src="images/image_683.jpg" width="900" />

</div>

</div>

<span id="Section134.xhtml"></span>

<div id="Section134.xhtml_Section134.xhtml">

</div>

<div class="header2">

## 20.1 概述

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">网站App平台注册用户分析主要包括年度注册用户分析和新注册用户分析。其中，新注册用户分析对于新品推广尤为重要。网站App平台注册用户分析是对平台的注册用户数据进行统计和分析，可从中发现目前营销策略中存在的问题。由于平台使用了MySQL数据库，因此在进行数据统计与分析前，首要任务是通过Python连接MySQL数据库，并获取MySQL数据库中的数据。</span>

</div>

<span id="Section135.xhtml"></span>

<div id="Section135.xhtml_Section135.xhtml">

</div>

<div class="header2">

## 20.2 案例效果预览

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">网站用户数据分析包括年度注册用户分析，如图20.1所示；新用户注册时间分布，如图20.2所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_684.jpg" width="833" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图20.1 年度注册用户分析图</span>

<div style="display: block;text-align:center;">

<img src="images/image_685.jpg" width="831" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图20.2 新用户注册时间分布图</span>

</div>

<span id="Section136.xhtml"></span>

<div id="Section136.xhtml_Section136.xhtml">

</div>

<div class="header2">

## 20.3 案例环境

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">本案例运行环境及所需模块具体如下： <img src="images/image_686.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 操作系统：Windows 10。 <img src="images/image_686.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 语言：Python 3.9。 <img src="images/image_686.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 开发环境：PyCharm。 <img src="images/image_686.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 第三方模块：PyMySQL、Pandas、xlrd、xlwt、Scipy、NumPy、Matplotlib。</span>

</div>

<span id="Section137.xhtml"></span>

<div id="Section137.xhtml_Section137.xhtml">

</div>

<div class="header2">

## 20.4 MySQL数据

</div>

<div class="part">

</div>

<div class="header3">

### 20.4.1 导入MySQL数据

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">导入MySQL数据具体步骤如下。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）安装MySQL软件，设置密码（本项目密码为root，也可以是其他密码），该密码一定要记住，连接MySQL数据库时会用到，其他设置采用默认设置即可。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）创建数据库。运行MySQL，首先输入密码，进入mysql命令提示符，如图20.3所示，然后使用CREATE DATABASE命令创建数据库。例如，创建数据库test，命令如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">CREATE DATABASE test;</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）导入SQL文件（user.sql）。在mysql命令提示符下通过use命令进入对应的数据库。例如，进入数据库test，命令如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">use test;</span>

<span style="font-size:16px;font-family:'PingFang SC';">出现“Database changed”说明已经进入数据库。接下来使用source命令指定SQL文件，并导入该文件。例如，导入user.sql，命令如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">source D:/user.sql</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面预览导入的数据，使用SQL查询语句（select语句）查询表中前5条数据，命令如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">select \* from user limit 5;</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行结果如图20.4所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_687.jpg" width="864" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图20.3 mysql命令提示符</span>

<div style="display: block;text-align:center;">

<img src="images/image_688.jpg" width="872" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图20.4 导入成功后的MySQL数据</span>

<span style="font-size:16px;font-family:'PingFang SC';">至此，导入MySQL数据的任务就完成了，接下来在Python中安装PyMySQL模块，连接MySQL数据库。</span>

</div>

<div class="header3">

### 20.4.2 Python连接MySQL数据库

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">首先在PyCharm开发环境中安装PyMySQL模块，然后导入需要的模块，并使用连接语句连接MySQL数据库，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">import pymysql</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">\# </span>连接<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">MySQL</span>数据库</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">conn=pymysql.connect(host="localhost",user='root',passwd = password,db = database_name,</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">charset="utf8")</span>

<span style="font-size:16px;font-family:'PingFang SC';">上述语句中，需要修改的参数是passwd和db，即指定MySQL密码和项目使用的数据库。本项目连接代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">conn = pymysql.connect(host = "localhost",user = 'root',passwd ='root',db = 'test',charset="utf8")</span>

<span style="font-size:16px;font-family:'PingFang SC';">接下来，使用Pandas模块的read_sql()函数读取MySQL数据，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  sql_query = 'SELECT \* FROM test.user'        #  SQL</span>查询语句</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  data = pd.read_sql(sql_query, con=conn)      # </span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">MySQL</span>数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  conn.close()                               # </span>关闭数据库连接</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  print(data.head())                       # </span>输出部分数据</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图20.5所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_689.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">图20.5 读取MySQL数据（部分数据）</span>

</div>

<span id="Section138.xhtml"></span>

<div id="Section138.xhtml_Section138.xhtml">

</div>

<div class="header2">

## 20.5 实现过程

</div>

<div class="part">

</div>

<div class="header3">

### 20.5.1 数据准备

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">本案例分析了近3年的网站用户注册数据，即2020年1月1日至2022年12月31日，主要包括用户名、最后访问时间、访问次数和注册时间。</span>

</div>

<div class="header3">

### 20.5.2 数据检测

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">鉴于数据量非常大，下面使用DataFrame()对象提供的函数对数据进行检测。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）使用info()方法查看每个字段的情况，如类型、是否为空等，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">data.info()</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）使用describe()函数查看数据描述信息，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">data.describe()</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）统计每列的空值情况，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">data.isnull().sum()</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图20.6所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_690.jpg" width="855" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图20.6 数据检测结果</span>

<span style="font-size:16px;font-family:'PingFang SC';">从运行结果得知：用户注册数据表现非常好，不存在异常数据和空数据。</span>

</div>

<div class="header3">

### 20.5.3 年度注册用户分析

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">按月统计每一年注册用户的增长情况，程序代码如下：</span>

<div style="display: block;text-align:center;">

<img src="images/image_691.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图20.7所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">通过折线图（图20.7）分析可知：2020年注册用户增长比较平稳，2021年、2022年比2020年注册用户增长约6倍。2021年和2022年数据每次的最高点都在同一个月，存在一定的趋势变化。</span>

<div style="display: block;text-align:center;">

<img src="images/image_692.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图20.7 年度注册用户分析图</span>

</div>

<div class="header3">

### 20.5.4 新注册用户分析

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">通过年度注册用户分析情况，我们观察新注册用户的时间分布，近三年新用户的注册量最高峰值出现在2021年4月。下面以2021年4月1日至4月30日数据为例，对新注册用户进行分析，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pymysql</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   import seaborn as sns</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   import matplotlib.pyplot as plt</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   from pandas.plotting import register_matplotlib_converters</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   register_matplotlib_converters()                     #</span>解决图表显示日期出现警告信息</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   #<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">连接</span>MySQL<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数据库，指定密码</span>(passwd)<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">和数据库</span>(db)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   conn = pymysql.connect(host = "localhost",user = 'root',passwd ='root',db = 'test',charset="utf8")</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   sql_query = 'SELECT \* FROM test.user'                                               #SQL</span>查询语句</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  data = pd.read_sql(sql_query, con=conn)                                             #</span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">MySQL</span>数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  conn.close()                                                                      #</span>关闭数据库连接</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  data=data\[\['username','addtime'\]\]                                                   #</span>提取指定列数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  data.rename(columns = {'addtime':'</span>注册日期<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','username':'</span>用户数量<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'},inplace=True)  #</span>列重命名</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  data\['</span>注册日期<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\] = pd.to_datetime(data\['</span>注册日期<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\])                                 #</span>将数据类型转换为日期类型</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  data = data.set_index('</span>注册日期<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">')                                                 #</span>将日期设置为索引</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  data=data\['2021-04-01':'2021-04-30'\]                                                #</span>提取指定日期数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  #</span>按天统计新注册用户</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  df=data.resample('D').size().to_period('D')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19  df.to_excel('result1.xlsx',index=False)# </span>导出数据为<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Excel</span>文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20  x=pd.date_range(start='20210401', periods=30)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21  y=df</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22  #</span>绘制折线图</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">23  sns.set_style('darkgrid')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">24  plt.rcParams\['font.sans-serif'\]=\['SimHei'\]                                          #</span>解决中文乱码</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">25  plt.title('</span>新用户注册时间分布图<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">')                                                 #</span>图表标题</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">26  plt.xticks(fontproperties = 'Times New Roman', size = 8,rotation=20)              # x</span>轴字体大小</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">27  plt.plot(x,y)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">28  plt.xlabel('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">注册日期</span>')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">29  plt.ylabel('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">用户数量</span>')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">30  plt.show()</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图20.8所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_693.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图20.8 新用户注册时间分布图</span>

<span style="font-size:16px;font-family:'PingFang SC';">通过图20.8，首先观察新用户注册的时间分布，可以发现在此期间内新用户的注册量有3次小高峰，并且在4月13日迎来最高峰。此后新用户注册量逐渐下降。</span>

<span style="font-size:16px;font-family:'PingFang SC';">经过研究发现，这个期间推出了新品，同时开放了新品并纳入了开学季活动，致使新用户人数达到新高峰。</span>

</div>

<span id="Section139.xhtml"></span>

<div id="Section139.xhtml_Section139.xhtml">

</div>

<div class="header1">
