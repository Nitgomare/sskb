# 7 Pandas模块之数据的清洗

</div>

<div class="part">

</div>

<div class="header1">


</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">数据清洗是数据分析的一个重要工作，因为数据的质量直接影响数据分析以及算法模型的结果。本章主要介绍在进行数据清洗时如何处理缺失值、重复值和异常值，以及字符串操作和数据转换。</span>

<span style="font-size:16px;font-family:'PingFang SC';">本章知识架构如下。</span>

<div style="display: block;text-align:center;">

<img src="images/image_228.jpg" width="900" />

</div>

</div>

<span id="Section046.xhtml"></span>

<div id="Section046.xhtml_Section046.xhtml">

</div>

<div class="header2">

## 7.1 缺失值的处理

</div>

<div class="part">

</div>

<div class="header3">

### 7.1.1 了解数据中的缺失值

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">缺失值就是空值，即因某种原因导致的数据为空。缺失值会使数据分析陷入混乱，从而导致不可靠的分析结果。以下3种情况可能会造成数据为空： <img src="images/image_229.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 人为因素导致数据丢失。 <img src="images/image_229.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 数据采集过程中无法全面获取数据。如调查问卷，被调查者不愿意分享数据；医疗数据涉及患者隐私，患者不愿意提供等。 <img src="images/image_229.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 系统或设备出现故障。</span>

<span style="font-size:16px;font-family:'PingFang SC';">在Python中，缺失值一般表现为NaN，英文全称是not a number（不是一个数），如图7.1所示。除此以外，还可能是None、NaT（日期型，Not a Time）等数据。</span>

<div style="display: block;text-align:center;">

<img src="images/image_230.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图7.1 Python中的缺失值</span>

</div>

<div class="header3">

### 7.1.2 查看缺失值

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在Python中查找数据中的缺失值，有以下3种方法： <img src="images/image_229.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> info()函数：查看索引、数据有多少列、每一列的数据类型、非空值的数量和内存使用量。 <img src="images/image_229.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> isnull()函数：空值返回True，非空值返回False。 <img src="images/image_229.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> notnull()函数：与isnull()函数相反，空值返回False，非空值返回True。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.1】**</span><span style="font-size:16px;font-family:'PingFang SC';">查看数据概况</span>**（实例位置：资源包\\TM\\sl\\07\\01）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">以淘宝销售数据为例，首先输出数据，然后使用info()函数查看数据，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  pd.set_option('expand_frame_repr', False)               # </span>关闭多个列的折叠状态，防止列太多时显示不清楚</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  pd.set_option('display.unicode.east_asian_width', True) # </span>设置输出右对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  df=pd.read_excel('TB2023.xls')                          # </span>读取数据文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  print(df)                                                 # </span>打印数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  print(df.info())                                      # </span>打印数据详情信息</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.2所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_231.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图7.2 缺失值查看</span>

<span style="font-size:16px;font-family:'PingFang SC';">在Python中，缺失值一般以NaN表示，如图7.2所示，通过info()函数我们看到“买家会员名”“买家实际支付金额”“宝贝标题”和“订单付款时间”的非空数量是10，而“宝贝总数量”和“类别”的非空数量是8，那么说明这两项存在空值。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.2】**</span><span style="font-size:16px;font-family:'PingFang SC';">判断数据是否存在缺失值</span>**（实例位置：资源包\\TM\\sl\\07\\02）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">判断数据是否存在缺失值还可以使用isnull()函数和notnull()函数实现，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  print(df.isnull())</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  print(df.notnull())</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.3所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_232.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图7.3 判断缺失值</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用isnull()函数缺失值返回True，非缺失值返回False；notnull()函数正好相反，缺失值返回False，非缺失值返回True。</span>

<span style="font-size:16px;font-family:'PingFang SC';">如果使用df\[df.isnull() == False\]，则会将所有不是缺失值的数据找出来，只针对Series()对象。</span>

</div>

<div class="header3">

### 7.1.3 处理缺失值

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">通过前面的判断得知数据缺失的情况，下面我们将缺失值删除，主要使用dropna()函数，该函数用于删除含有缺失值的行，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.dropna()</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.4所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_233.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图7.4 缺失值删除处理（1）</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">有些时候数据可能存在整行为空的情况，此时可以在dropna()函数中指定参数how='all'，删除所有空行。</span>

<span style="font-size:16px;font-family:'PingFang SC';">从运行结果得知：dropna()函数将所有包含缺失值的数据全部删除了，而如果此时我们认为有些数据虽然存在缺失值，但是不影响数据分析，那么可以使用以下方法处理。例如，上述数据中只保留“宝贝总数量”不存在缺失值的数据，而类别是否缺失无所谓，则可以使用notnull()函数判断，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df1=df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">宝贝总数量</span>'\].notnull()\]</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.5所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_234.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图7.5 缺失值删除处理（2）</span>

<span style="font-size:16px;font-family:'PingFang SC';">对于缺失数据，如果比例高于30%，就可以选择放弃这个指标，做删除处理；如果比例低于30%，则尽量不要删除，而是选择将这部分数据填充，一般以0、均值、众数（大多数）填充。DataFrame()对象中的fillna()函数可以实现填充缺失数据，pad/ffill表示用前一个非缺失值去填充该缺失值；backfill/bfill表示用下一个非缺失值填充该缺失值；None用于指定一个值去替换缺失值。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.3】**</span><span style="font-size:16px;font-family:'PingFang SC';">将NaN填充为0</span>**（实例位置：资源包\\TM\\sl\\07\\03）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">如果用于计算的数值型数据为空，可选择用0填充。例如，将“宝贝总数量”为空的数据填充0，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">宝贝总数量</span>'\] = df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">宝贝总数量</span>'\].fillna(0)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.6所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_235.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图7.6 缺失值填充处理</span>

</div>

<span id="Section047.xhtml"></span>

<div id="Section047.xhtml_Section047.xhtml">

</div>

<div class="header2">

## 7.2 处理数据中的重复值

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">对于数据中存在的重复数据，包括重复的行或者几行中某几列的值重复一般做删除处理，主要使用DataFrame()对象的drop_duplicates()函数。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.4】**</span><span style="font-size:16px;font-family:'PingFang SC';">处理淘宝电商销售数据中的重复数据</span>**（实例位置：资源包\\TM\\sl\\07\\04）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面以文件“1月.xlsx”中的淘宝销售数据为例，对其中的重复数据进行处理。关键代码如下：</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）判断每一行数据是否重复（完全相同）。返回值为False，表示不重复；返回值为True，表示重复。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df1.duplicated()</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）去除全部的重复数据。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df1.drop_duplicates()</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）去除指定列的重复数据。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df1.drop_duplicates(\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">买家会员名</span>'\])</span>

<span style="font-size:16px;font-family:'PingFang SC';">（4）保留重复行中的最后一行。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df1.drop_duplicates(\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">买家会员名</span>'\],keep='last')</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">以上代码中参数keep的值有3个。当keep='first'时，表示保留第一次出现的重复行，是默认值。当keep为另外两个取值last和False时，分别表示保留最后一次出现的重复行和去除所有重复行。</span>

<span style="font-size:16px;font-family:'PingFang SC';">（5）直接删除，保留一个副本。其中，inplace=True表示直接在原来的DataFrame上删除重复项，而默认值False表示删除重复项后生成一个副本。代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df1.drop_duplicates(\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">买家会员名</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">买家支付宝账号</span>'\],inplace=Fasle)</span>

</div>

<span id="Section048.xhtml"></span>

<div id="Section048.xhtml_Section048.xhtml">

</div>

<div class="header2">

## 7.3 数据中异常值的检测与处理

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">数据分析中，异常值是指超出或低于正常范围的值，如年龄大于200、身高大于3米、宝贝总数量为负数等数据。这些异常数据该如何检测呢？主要有以下3种方法： <img src="images/image_236.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 根据给定的数据范围进行判断，不在范围内的数据视为异常值。 <img src="images/image_236.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 根据均方差判断。统计学中，如果一组数据接近正态分布，那么将会有68%的数据处于均值的一个标准差范围内，95%的数据处于两个标准差范围内，99.7%的数据处于3个标准差范围内。 <img src="images/image_236.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 通过箱形图判断。箱形图是显示一组数据分散情况的统计图，将数据以四分位数的形式进行图形化描述。其中，上限和下限是数据分布的边界，高于上限或低于下限的数据都是异常值，如图7.7所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">异常值的处理方式比较简单，主要有以下3种： <img src="images/image_236.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 删除异常值。 <img src="images/image_236.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 将异常值当作缺失值处理，以某个值填充。 <img src="images/image_236.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 将异常值当作特殊情况，分析其出现的原因。</span>

<div style="display: block;text-align:center;">

<img src="images/image_237.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图7.7 箱形图</span>

</div>

<span id="Section049.xhtml"></span>

<div id="Section049.xhtml_Section049.xhtml">

</div>

<div class="header2">

## 7.4 数据中字符串的操作函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">字符串操作也是数据清洗的一部分。商业数据表中经常需要处理字符型数据，而Pandas的Series.str字符串对象下有几十种函数可以处理。这些函数可通过str字符串对象访问，它们和Python内置的字符串处理函数名字相同。</span>

</div>

<div class="header3">

### 7.4.1 字符串对象中的常见函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Series()对象中的字符串对象str的内建函数可以实现大部分文本操作，简单快捷。字符串对象函数如表7.1所示。</span>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">表7.1 字符串对象函数</span>

<div style="display: block;text-align:center;">

<img src="images/image_238.jpg" width="900" />

</div>

<span style="font-size:16px;font-family:'PingFang SC';">下面针对常用的字符串对象函数进行举例。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.5】**</span><span style="font-size:16px;font-family:'PingFang SC';">字符串大小写转换</span>**（实例位置：资源包\\TM\\sl\\07\\05）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面分别实现将字符串中的大写字母转换为小写字母，小写字母转换为大写字母，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  s=pd.Series(\["mr","MR-soft","www.MINGRISOFT.COM"\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  # </span>原始数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  print('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">原始数据：</span>')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  print(s)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  print('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">转换为小写：</span>')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  print(s.str.lower())</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  print('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">转换为大写：</span>')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  print(s.str.upper())</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.8所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.6】**</span><span style="font-size:16px;font-family:'PingFang SC';">去掉字符串中的空格</span>**（实例位置：资源包\\TM\\sl\\07\\06）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面实现去掉字符串中的空格，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   s=pd.Series(\["mr ","MR soft "," ww w.MINGRISOFT.COM "\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   # </span>通过长度检验是否去掉了空格</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   print('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">原始数据及数据长度：</span>')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   print(s)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   print(s.str.len())</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   print('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">去掉两边空格后的长度：</span>')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   a=s.str.strip()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   print(a.str.len())</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  print('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">去掉左边空格后的长度：</span>')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  a=s.str.lstrip()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  print(a.str.len())</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  print('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">去掉右边空格后的长度：</span>')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  a=s.str.rstrip()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  print(a.str.len())</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.9所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_239.jpg" width="386" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.8 字符串大小写转换</span>

<div style="display: block;text-align:center;">

<img src="images/image_240.jpg" width="414" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.9 去掉字符串中的空格</span>

</div>

<div class="header3">

### 7.4.2 替换字符串—replace()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">字符串替换函数replace()是最常用的函数之一，可以实现对字符串数据进行替换。在进行数据分析的过程中，数据可能有各种各样的问题，尤其是爬取到的数据，可能存在一些乱码，或者其他的操作符号，这个时候就可以使用replace()函数进行剔除。</span>

<span style="font-size:16px;font-family:'PingFang SC';">例如，将“a”替换为“明日科技”，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">s=pd.Series(\['a','b','c'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">s=s.str.replace('a','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">明日科技</span>')</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.7】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用replace()函数替换数据中指定的字符</span>**（实例位置：资源包\\TM\\sl\\07\\07）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">对爬取的二手房价信息进行清理，首先去除房价信息中的单位“万”和“平米”，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">查找替换</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">总价</span>”<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">中的</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">万</span>”'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   df=pd.read_csv("data.csv")</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   print(df.head())</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   # </span>删除无用的列</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   del df\['Unnamed: 0'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>去除单位</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">总价</span>'\]=df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">总价</span>'\].str.replace('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">万</span>','')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">建筑面积</span>'\]=df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">建筑面积</span>'\].str.replace('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">平米</span>','')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  print(df.head())</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.10和图7.11所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_241.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.10 原始数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_242.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.11 清洗后的数据</span>

<span style="font-size:16px;font-family:'PingFang SC';">replace()函数除了可以替换数据中的字符，还可以替换标题中的字符。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.8】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用replace()函数替换标题中指定的字符</span>**（实例位置：资源包\\TM\\sl\\07\\08）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先构建一组随机数据，然后使用replace()函数将标题中的空格替换掉，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   import numpy as np</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   # </span>随机生成<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4</span>行<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>列的数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   df=pd.DataFrame(np.random.randn(4,3),columns=\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">高一年级</span> 1<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">班</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">高一年级</span> 2<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">班</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">高一年级</span> 3<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">班</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   print(df)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   # </span>替换标题中的空格</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   df.columns=df.columns.str.replace(' ','')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  print(df)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.12和图7.13所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_243.jpg" width="654" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.12 随机生成的原始数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_244.jpg" width="603" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.13 去除空格后的标题</span>

<span style="font-size:16px;font-family:'PingFang SC';">也可以将空格替换成其他字符，如“-”，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.columns=df.columns.str.replace(' ','-')</span>

</div>

<div class="header3">

### 7.4.3 数据切分—split()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">数据分析过程中，数据通常形式多样。例如，规格中的长、宽、高，地址中的省、市、区都是连在一起的，这时可以使用split()函数将规格中的长、宽、高或地址中的省、市、区切分出来。</span>

<span style="font-size:16px;font-family:'PingFang SC';">Series()对象的str字符串对象中的split()函数可以实现字符串的切分，语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Series.str.split(pat=None, n=-1, expand=False)</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_245.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pat：字符串、符号或正则表达式。是字符串切分的依据，默认以空格切分字符串。 <img src="images/image_245.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> n：整型，切分次数，默认值是-1，0或-1都将返回所有切分。 <img src="images/image_245.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> expand：布尔型，表示切分后的结果是否转换为DataFrame()对象，默认值是False。split()函数的返回值为Series()对象、DataFrame()对象、索引或多重索引。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.9】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用split()函数切分地址</span>**（实例位置：资源包\\TM\\sl\\07\\09）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用split()函数将“收货地址”切分为省、市、区地址，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   # </span>设置数据显示的最大列数和宽度</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   pd.set_option('display.max_columns',20)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   pd.set_option('display.width',3000)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">读取</span>Excel<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">文件指定列数据</span>(“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">买家会员名</span>”<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">和</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">收货地址</span>”)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   df = pd.read_excel('mrbooks.xls',usecols=\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">买家会员名</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">收货地址</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   print(df.head())</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">使用</span>split()<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">函数切分</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">收货地址</span>”'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  s=df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">收货地址</span>'\].str.split(' ',expand=True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">省</span>'\]=s\[0\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">市</span>'\]=s\[1\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">区</span>'\]=s\[2\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">地址</span>'\]=s\[3\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  print(df.head())</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.14所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_246.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">图7.14 使用split()函数切分地址</span>

<span style="font-size:16px;font-family:'PingFang SC';">上述代码中，直接将特征数据切出来，即省、市、区和地址，并且“收货地址”被切分后直接转成了DataFrame()对象，设置expand参数为True。</span>

</div>

<div class="header3">

### 7.4.4 判断字符串—contains()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">当我们拿到一份数据时，经常会发现什么五花八门的数据都有。在处理这些数据的过程中，可以使用contains()函数判断其是否包含指定的字符，是否包含前缀、尾缀，或指定的值，这些都可以进行判断。contains()函数的返回值为布尔型。除此之外，使用contains()函数还可以对数据进行筛选归类。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.10】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用contains()函数筛选数据并归类</span>**（实例位置：资源包\\TM\\sl\\07\\10）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">在京东电商销售数据中，首先通过contains()函数筛选“商品名称”中包含“Python”的图书，其次实现按照“商品名称”中包含指定的字符串对商品进行归类，例如“商品名称”中包含“Python”，则类别为“Python”；包含“Java”，则类别为“Java”，以此类推，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  pd.set_option('display.unicode.east_asian_width', True)      # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  # </span>设置数据显示的宽度和最大列数</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  pd.set_option('display.width', 1000)                         # </span>显示宽度</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   pd.set_option('display.max_columns', 20)                    # </span>显示列数</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   # </span>读取<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">Excel</span>文件</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   df = pd.read_excel('data1.xlsx', usecols=\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">成交商品件数</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">成交码洋</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   print(df.head())</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   print(df\[df\['</span>商品名称<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\].str.contains('Python')\].head()) # </span>使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">contains()</span>函数筛选包含<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“Python”</span>的数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数据筛选并归类</span>'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  # </span>筛选符合条件的行的索引，使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.loc</span>属性进行赋值</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  df.loc\[df \[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>'\].str.contains('Python')\].index,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>'\]='Python'</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  df.loc\[df \[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>'\].str.contains('Java')\].index,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>'\]='Java'</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  df.loc\[df \[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>'\].str.contains('C#')\].index,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>'\]='C#'</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  df.loc\[df \[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>'\].str.contains('PHP')\].index,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>'\]='PHP'</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  df.loc\[df \[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>'\].str.contains('JavaWeb')\].index,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>'\]='JavaWeb'</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  df.loc\[df \[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>'\].str.contains('C<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语言</span>')\].index,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>'\]='C<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语言</span>'</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  df.loc\[df \[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>'\].str.contains('JSP')\].index,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>'\]='JSP'</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">19  df.loc\[df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>'\].str.contains('C\\+')\].index, '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>'\] = 'C++'</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">20  df.loc\[df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>'\].str.contains('Android')\].index, '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>'\] = 'Android'</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">21  df.loc\[df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">商品名称</span>'\].str.contains('WEB<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">前端</span>')\].index, '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>'\] = 'WEB<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">前端</span>'</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">22  print(df.head())</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.15所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_247.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">图7.15 使用contains()函数筛选数据并归类</span>

<span style="font-size:16px;font-family:'PingFang SC';">在“df.loc\[df\[df\['商品名称'\].str.contains（'C\\+'）\].index, '类别'\] = 'C++'”这段代码中使用了反斜杠“\\，它的用法是转义，由于代码中的字符“++”是正则表达式中的符号，表示重复前面一个匹配字符一次或者多次，因此使用了反斜杠“\\进行转义。</span>

</div>

<span id="Section050.xhtml"></span>

<div id="Section050.xhtml_Section050.xhtml">

</div>

<div class="header2">

## 7.5 数据转换

</div>

<div class="part">

</div>

<div class="header3">

### 7.5.1 通过字典映射的方式实现数据转换—map()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在日常的数据处理中，经常需要对数据进行转换，例如，将性别“男”转换为1，“女”转换为2。使用Series()对象的map()函数可以很容易实现数据转换，它可以帮助我们解决绝大部分类似的数据处理需求。</span>

<span style="font-size:16px;font-family:'PingFang SC';">map()函数可以接受一个函数或含有映射关系的字典型对象。使用map()函数实现元素级转换以及数据处理工作是一种非常便捷的方式。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.11】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用map()函数将数据中的性别转换为数字</span>**（实例位置：资源包\\TM\\sl\\07\\11）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">首先使用numpy创建一组数据，然后使用字典映射将性别“男”转换为1，“女”转换为2，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  import numpy as np</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  pd.set_option('display.unicode.east_asian_width', True)  # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   # </span>创建数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   boolean=\[True,False\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   sex=\["<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">男</span>","<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">女</span>"\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   df=pd.DataFrame({</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8       "<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">身高</span>":np.random.randint(150,190,100),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9       "<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">体重</span>":np.random.randint(35,90,100),</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10      "<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">是否接种疫苗</span>":\[boolean\[x\] for x in np.random.randint(0,2,100)\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11      "<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">性别</span>":\[sex\[x\] for x in np.random.randint(0,2,100)\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12      "<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">年龄</span>":np.random.randint(18,70,100)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  })</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  print(df.head())</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  sex_mapping={'</span>男<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">':1,'</span>女<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">':2}                          # </span>创建性别字典</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  df\['</span>性别<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\]=df\['</span>性别<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\].map(sex_mapping)               # </span>使用字典映射将性别转换为数字</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  print(df.head())</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.16和图7.17所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_248.jpg" width="591" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.16 原始数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_249.jpg" width="597" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.17 转换性别后的数据</span>

</div>

<div class="header3">

### 7.5.2 数据分割—cut()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">Pandas的cut()函数的作用是将一组数据分割成离散的区间。例如，有一组年龄数据，可以使用cut()函数将这组数据分割成不同的年龄段并打上标签。cut()函数语法格式如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">pandas.cut(x,bins,right=True, labels=None, retbins=False,precision=3, include_lowest=False, duplicates='raise')</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_250.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> x：被分割的类数组（array-like）数据，必须是一维的（不能是DataFrame()对象）。 <img src="images/image_250.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> bins：被分割后的区间（也被称作“桶”“箱”或“面元”）。有3种形式，一个int型的标量、标量序列（数组）或者pandas.IntervalIndex。 <img src="images/image_251.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 一个int型的标量：当bins为一个int型的标量时，代表将x分成bins份。x的范围在每侧扩展0.1%，以包括x的最大值和最小值。 <img src="images/image_251.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 标量序列：标量序列定义了被分割后每一个bin的区间边缘，此时x没有扩展。 <img src="images/image_251.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pandas.IntervalIndex：定义要使用的精确区间。 <img src="images/image_250.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> right：布尔型，默认值为True，表示是否包含区间右边的值。例如，如果bins=\[1,2,3\]，right=True，则区间为（1,2\]（包括2）、（2,3\]（包括3）；right=False，则区间为（1,2）（不包括2）、（2,3）（不包括3）。 <img src="images/image_250.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> labels：给分割后的bins打标签。例如，将年龄x分割成年龄段bins后，可以给年龄段打上“未成年人”“青年人”“中年人”等标签。labels的长度必须和划分后的区间长度相等，例如，bins=\[1,2,3\]划分后有2个区间，即（1,2\]和（2,3\]，则labels的长度必须为2。如果指定labels=False，则返回x中的数据在第几个bin中（从0开始）。 <img src="images/image_250.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> retbins：布尔型，表示是否将分割后的bins返回，当bins为一个int型的标量时比较有用，这样可以得到划分后的区间，默认值为False。 <img src="images/image_250.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> precision：保留区间小数点的位数，默认值为3。 <img src="images/image_250.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> include_lowest：布尔型，表示区间的左边是开还是闭的，默认值为False，也就是不包含区间左边的值。 <img src="images/image_250.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> duplicates：表示是否允许重复区间。值为raise表示不允许，值为drop表示允许。cut()函数的返回值分为以下两种： <img src="images/image_251.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> out：一个pandas.Categorical、Series()对象或者ndarray数组类型的值，代表分区后x中的每个值在哪个区间中，如果指定了labels参数，则返回对应的标签。 <img src="images/image_251.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> bins：分隔后的区间，当指定retbins参数为True时返回分隔后的区间。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.12】**</span><span style="font-size:16px;font-family:'PingFang SC';">分割成绩数据并标记为“优秀”“良好”“一般”</span>**（实例位置：资源包\\TM\\sl\\07\\12）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面通过Pandas的cut()函数将学生的英语得分数据进行分割并标记为“优秀”“良好”和“一般”，0～59分为一般，60～69分为良好，70～100分为优秀。程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  pd.set_option('display.unicode.east_asian_width', True)   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  df=pd.read_csv('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语成绩报告</span>.csv',encoding='gbk')         # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">读取</span>CSV<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">文件，指定编码格式为</span>gbk</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  print(df.head())                                        # </span>输出前<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5</span>条数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  # </span>使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">cut()</span>函数将数据分割成离散的区间并进行标记</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  scores = df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">得分</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">标记</span>'\]=pd.cut(scores, \[0,60,70,100\], labels=\[u"<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">一般</span>",u"<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">良好</span>",u"<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">优秀</span>"\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  print(df.head())                                        # </span>输出前<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5</span>条数据</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.18和图7.19所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_252.jpg" width="501" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.18 原始数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_253.jpg" width="575" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.19 分割后的数据</span>

</div>

<div class="header3">

### 7.5.3 数据分类—get\_dummies()函数

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">数据分析过程中，经常会遇到用于分类的数据，例如，性别“男”“女”，颜色“红”“绿”“蓝”等。这些数据不是连续的，是离散的、无序的。如果对这种特征的数据进行分析，则需要将它们数字化，有以下两种方式。 <img src="images/image_250.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 如果分类数据的取值不区分大小，那么可以使用one-hot编码方式，主要通过Pandas的get_dummies()函数实现。 <img src="images/image_250.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 如果分类数据的取值区分大小，如尺码XS、S、M、L、XL是从小到大，那么需要使用数值的映射（如{'XL': 5，'L': 4，'M': 3，'S':2，'XS':1}），主要使用Series()对象的map()函数。</span>

<span style="font-size:16px;font-family:'PingFang SC';">那么，什么时候可以用到分类数据转换呢？当我们在做关联分析的时候，例如，分析购物车，即不同人的购物车，先将当前购物表数字化，然后进行统计分析、关联分析。在购物车分析当中经常会用到get_dummies()函数。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例7.13】**</span><span style="font-size:16px;font-family:'PingFang SC';">将分类数据转换为数字</span>**（实例位置：资源包\\TM\\sl\\07\\13）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">假设对购物车中的“连衣裙”进行分析，首先将分类数据“颜色”和“尺码”转换为数字，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   pd.set_option('display.unicode.east_asian_width', True)  # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   df = pd.DataFrame(\[                                        # </span>创建数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4       \['polo<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">连衣裙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">黑色</span>', 'M', 778\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5       \['polo<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">连衣裙</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">浅灰</span>', 'S', 778\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6       \['polo<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">连衣裙</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">粉色</span>', 'L',778\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7       \['polo<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">连衣裙</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">浅灰</span>','S',778\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8       \['polo<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">连衣裙</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">浅灰</span>','XS',778\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9       \['polo<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">连衣裙</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">浅灰</span>', 'XL', 778\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  \])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  df.columns = \['</span>商品名称<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>颜色分类<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">', '</span>尺码<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">', '</span>单价<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\]       # </span>设置列名</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  size_mapping = {'XL': 5,'L': 4,'M': 3,'S':2,'XS':1}        # </span>创建<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>尺码<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>字典</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  df\['</span>尺码<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\] = df\['</span>尺码<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\].map(size_mapping)                  # </span>将<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>尺码<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>映射为数字</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  df1=pd.get_dummies(df)                                   # </span>使用<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">get_dummies()</span>函数进行编码</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  print(df1)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图7.20和图7.21所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_254.jpg" width="523" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.20 原始数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_255.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图7.21 数字化后的数据</span>

</div>

<div class="header3">

### 说明

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">one-hot编码又称独热编码，是分类变量作为二进制向量的表示。首先将分类值映射为整数值，然后每个整数值被表示为二进制向量。one-hot编码就是保证每个样本中的单个特征只有1位处于状态1，其他位都是0。</span>

</div>

<span id="Section051.xhtml"></span>

<div id="Section051.xhtml_Section051.xhtml">

</div>

<div class="header2">

## 7.6 小结

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">本章介绍了如何使用Pandas模块实现数据中缺失值的处理、重复值的处理、异常值的检测与处理，还介绍了数据中字符串的操作函数以及数据转换相关知识点。其中在实现数据分析时，处理数据中的缺失值、重复值以及数据中异常值的检测与处理是比较常见的一些操作，希望大家可以勤加练习。其中字符串的操作函数以及数据转换可以根据实际需求进行调用。</span>

</div>

<span id="Section052.xhtml"></span>

<div id="Section052.xhtml_Section052.xhtml">

</div>

<div class="header1">
