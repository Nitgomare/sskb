# 6 Pandas模块之数据的处理

</div>

<div class="part">

</div>

<div class="header1">


</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">数据读取后并不是所有的数据都是我们所需要的，因此还要对数据进行简单的处理，本章将主要介绍如何进行数据的抽取，数据的增、删、改、查以及如何对数据进行排序与排名操作。</span>

<span style="font-size:16px;font-family:'PingFang SC';">本章知识架构如下。</span>

<div style="display: block;text-align:center;">

<img src="images/image_197.jpg" width="900" />

</div>

</div>

<span id="Section041.xhtml"></span>

<div id="Section041.xhtml_Section041.xhtml">

</div>

<div class="header2">

## 6.1 数据抽取

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">在数据分析的过程中，数据读取后，并不是所有的数据都是我们所需要的，此时可以抽取部分数据，主要使用DataFrame()对象的loc属性和iloc属性，示意图如图6.1所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_198.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图6.1 loc属性和iloc属性示意图</span>

<span style="font-size:16px;font-family:'PingFang SC';">DataFrame()对象的loc属性和iloc属性都可以抽取数据，区别如下： <img src="images/image_199.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> loc属性：以列名（columns）和行名（index）作为参数，当只有一个参数时，默认是行名，即抽取整行数据，包括所有列，如df.loc\['A'\]。 <img src="images/image_199.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> iloc属性：以行和列位置索引（即0，1，2，…）作为参数，0表示第一行，1表示第二行，以此类推。当只有一个参数时，默认是行索引，即抽取整行数据，包括所有列。如抽取第一行数据，df.iloc\[0\]。</span>

</div>

<div class="header3">

### 6.1.1 抽取指定行数据

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">实现抽取一行数据时可以使用loc属性。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.1】**</span><span style="font-size:16px;font-family:'PingFang SC';">抽取一行学生成绩数据</span>**（实例位置：资源包\\TM\\sl\\06\\01）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">抽取一行名为“甲”的学生成绩数据（包括所有列），程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  data = \[\[110,105,99\],\[105,88,115\],\[109,120,130\],\[112,115\]\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  name = \['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丁</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  columns = \['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  df = pd.DataFrame(data=data, index=name, columns=columns)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  print(df.loc\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>'\])</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.2所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_200.jpg" width="549" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图6.2 抽取一行数据</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用iloc属性抽取第一行数据，指定行索引即可，如df.iloc\[0\]。</span>

</div>

<div class="header3">

### 6.1.2 抽取多行数据

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">通过loc属性和iloc属性指定行名和行索引即可实现抽取任意多行数据。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.2】**</span><span style="font-size:16px;font-family:'PingFang SC';">抽取多行学生成绩数据</span>**（实例位置：资源包\\TM\\sl\\06\\02）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">抽取行名为“甲”和“丙”（即第1行和第3行数据）的学生成绩数据，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  print(df.loc\[\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>'\]\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  print(df.iloc\[\[0,2\]\])</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.3所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">在loc属性和iloc属性中合理使用冒号（:），即可抽取连续任意多行数据。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.3】**</span><span style="font-size:16px;font-family:'PingFang SC';">抽取多个学生成绩数据</span>**（实例位置：资源包\\TM\\sl\\06\\03）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面抽取连续任意多个学生成绩数据，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  print(df.loc\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>':'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丁</span>'\])  # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">从</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>”<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">到</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丁</span>”</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  print(df.loc\[:'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>':\])       # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">第</span>1<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">行到</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>”</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  print(df.iloc\[0:4\])         # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1</span>行到第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4</span>行</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  print(df.iloc\[1::\])         # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2</span>行到最后<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1</span>行</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.4所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_201.jpg" width="543" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.3 抽取多行数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_202.jpg" width="666" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.4 抽取连续任意多行数据</span>

</div>

<div class="header3">

### 6.1.3 抽取指定列数据

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">抽取指定列数据，可以直接使用列名，也可以使用loc属性和iloc属性。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.4】**</span><span style="font-size:16px;font-family:'PingFang SC';">抽取学生“语文”和“数学”成绩</span>**（实例位置：资源包\\TM\\sl\\06\\04）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">抽取列名为“语文”和“数学”的学生成绩数据，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  data = \[\[110,105,99\],\[105,88,115\],\[109,120,130\],\[112,115\]\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  name = \['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丁</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  columns = \['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  df = pd.DataFrame(data=data, index=name, columns=columns)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  print(df\[\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>'\]\])</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.5所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_203.jpg" width="310" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图6.5 “语文”和“数学”成绩</span>

<span style="font-size:16px;font-family:'PingFang SC';">loc属性和iloc属性都有两个参数，第一个参数代表行，第二个参数代表列，抽取指定列数据时，行参数不能省略。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.5】**</span><span style="font-size:16px;font-family:'PingFang SC';">抽取指定学科的成绩</span>**（实例位置：资源包\\TM\\sl\\06\\05）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用loc属性和iloc属性抽取指定列数据，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  print(df.loc\[:,\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>'\]\])  # <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">抽取</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>”<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">和</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>”</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  print(df.iloc\[:,\[0,1\]\])             # </span>抽取第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1</span>列和第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2</span>列</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  print(df.loc\[:,'</span>语文<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">':\])            # </span>抽取从<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>语文<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>开始到最后一列</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  print(df.iloc\[:,:2\])                # </span>连续抽取从第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1</span>列开始到第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>列，但不包括第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>列</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.6所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_204.jpg" width="827" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图6.6 抽取指定学科的成绩</span>

</div>

<div class="header3">

### 6.1.4 抽取指定的行、列数据

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">抽取指定行、列数据主要使用loc属性和iloc属性，这两个属性的两个参数都指定就可以实现指定行列数据的抽取。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.6】**</span><span style="font-size:16px;font-family:'PingFang SC';">抽取指定学科和指定学生的成绩</span>**（实例位置：资源包\\TM\\sl\\06\\06）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用loc属性和iloc属性抽取指定行、列数据，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   data = \[\[110,105,99\],\[105,88,115\],\[109,120,130\],\[112,115\]\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   name = \['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丁</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   columns = \['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   df = pd.DataFrame(data=data, index=name, columns=columns)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   print(df.loc\['</span>乙<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>英语<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\])            # </span>输出<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>乙<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>的<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';"> “</span>英语<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>成绩</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   print(df.loc\[\['</span>乙<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\],\['</span>英语<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\]\])          #  “</span>乙<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>的<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>英语<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>成绩</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  print(df.loc\[\['</span>乙<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\],\['</span>数学<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>英语<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\]\]) #  “</span>乙<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>的<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>数学<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>和<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>英语<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>成绩</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  print(df.iloc\[\[1\],\[2\]\])                 # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2</span>行第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>列</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  print(df.iloc\[1:,\[2\]\])                  # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2</span>行到最后一行的第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>列</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  print(df.iloc\[1:,\[0,2\]\])                # </span>第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2</span>行到最后一行的第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1</span>列和第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>列</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  print(df.iloc\[:,2\])                     # </span>所有行，第<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3</span>列</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.7所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">在上述结果中，第一个输出结果是一个数，不是DataFrame类型的数据，这是由于“df.loc\['乙'，'英语'\]”没有使用方括号\[\]。</span>

<div style="display: block;text-align:center;">

<img src="images/image_205.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图6.7 抽取指定学科和指定学生的成绩</span>

</div>

<span id="Section042.xhtml"></span>

<div id="Section042.xhtml_Section042.xhtml">

</div>

<div class="header2">

## 6.2 数据的增、删、改、查

</div>

<div class="part">

</div>

<div class="header3">

### 6.2.1 增加数据

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">DataFrame()对象增加数据主要包括列数据增加和行数据增加。我们首先来看原始数据，如图6.8所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. 直接为DataFrame()对象赋值**</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.7】**</span><span style="font-size:16px;font-family:'PingFang SC';">增加一列“物理”成绩</span>**（实例位置：资源包\\TM\\sl\\06\\07）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">增加一列“物理”成绩，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  data = \[\[110,105,99\],\[105,88,115\],\[109,120,130\],\[112,115,140\]\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  name = \['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丁</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  columns = \['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>'\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  df = pd.DataFrame(data=data, index=name, columns=columns)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">物理</span>'\]=\[88,79,60,50\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9  print(df)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.9所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. 使用loc属性在DataFrame()对象的最后增加一列**</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.8】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用loc属性增加一列“物理”成绩</span>**（实例位置：资源包\\TM\\sl\\06\\08）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用loc属性在DataFrame()对象的最后增加一列。例如，增加“物理”列，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.loc\[:,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">物理</span>'\] = \[88,79,60,50\]</span>

<span style="font-size:16px;font-family:'PingFang SC';">在DataFrame()对象最后增加一列“物理”，其值为等号右边数据。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**3. 在指定位置插入一列**</span>

<span style="font-size:16px;font-family:'PingFang SC';">在指定位置插入一列，主要使用insert()函数实现。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.9】**</span><span style="font-size:16px;font-family:'PingFang SC';">在第一列后面插入“物理”成绩</span>**（实例位置：资源包\\TM\\sl\\06\\09）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">例如，在第一列后面插入“物理”，其值为wl的数值，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  wl =\[88,79,60,50\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  df.insert(1,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">物理</span>',wl)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  print(df)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.10所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_206.jpg" width="386" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.8 原始数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_207.jpg" width="496" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.9 增加一列“物理”成绩</span>

<div style="display: block;text-align:center;">

<img src="images/image_208.jpg" width="472" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.10 在第一列后插入“物理”成绩</span>

</div>

<div class="header3">

### 6.2.2 按行增加数据

</div>

<div class="part">

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. 增加一行数据**</span>

<span style="font-size:16px;font-family:'PingFang SC';">增加一行数据主要使用loc属性实现。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.10】**</span><span style="font-size:16px;font-family:'PingFang SC';">在成绩表中增加一行数据</span>**（实例位置：资源包\\TM\\sl\\06\\10）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">在成绩表中增加一行数据，即“戊”同学的成绩，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  df.loc\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">戊</span>'\] = \[100,120,99\]</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.11所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. 增加多行数据**</span>

<span style="font-size:16px;font-family:'PingFang SC';">增加多行数据主要使用字典结合append()函数实现。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.11】**</span><span style="font-size:16px;font-family:'PingFang SC';">在成绩表中增加多行数据</span>**（实例位置：资源包\\TM\\sl\\06\\11）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">在原有数据中增加“戊”“己”和“庚”3名同学的成绩，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  df_insert=pd.DataFrame({'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>':\[100,123,138\],'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>':\[99,142,60\],'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>':\[98,139,99\]},index = \['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">戊</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">己</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">庚</span>'\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  df1 = df.append(df_insert)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.12所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_209.jpg" width="390" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.11 增加一行数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_210.jpg" width="389" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.12 增加多行数据</span>

</div>

<div class="header3">

### 6.2.3 删除数据

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">删除数据主要使用DataFrame()对象的drop()函数。语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> labels：表示行标签或列标签。 <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> axis：axis = 0，表示按行删除；axis = 1，表示按列删除；默认值为0。 <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> index：删除行，默认值为None。 <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> columns：删除列，默认值为None。 <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> level：针对有两级索引的数据。level = 0，表示按第1级索引删除整行；level = 1表示按第2级索引删除整行；默认值为None。 <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> inplace：可选参数，对原数组做出修改并返回一个新数组。默认值为False，如果值为True，那么原数组直接就被替换。 <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> errors：参数值为ignore或raise，默认值为raise。如果值为ignore（忽略），则取消错误。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. 删除行列数据**</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.12】**</span><span style="font-size:16px;font-family:'PingFang SC';">删除学生成绩数据</span>**（实例位置：资源包\\TM\\sl\\06\\12）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">删除指定的学生成绩数据，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  df.drop(\['</span>数学<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\],axis=1,inplace=True)         # </span>删除某列</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  df.drop(columns='</span>数学<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">',inplace=True)          # </span>删除<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">columns</span>为<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>数学<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>的列</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  df.drop(labels='</span>数学<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">', axis=1,inplace=True) # </span>删除列标签为<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>数学<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>的列</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  df.drop(\['</span>甲<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">','</span>乙<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\],inplace=True)           # </span>删除某行</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  df.drop(index='</span>甲<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">',inplace=True)              # </span>删除<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">index</span>为<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>甲<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>的行</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  df.drop(labels='</span>甲<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">', axis=0,inplace=True)   # </span>删除行标签为<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>甲<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>的行</span>

<span style="font-size:16px;font-family:'PingFang SC';">以上代码中的函数都可以实现删除指定的行列数据，读者选择一种就可以。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. 删除特定条件的行**</span>

<span style="font-size:16px;font-family:'PingFang SC';">删除满足特定条件的行，首先找到满足该条件的行索引，然后使用drop()函数将其删除。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.13】**</span><span style="font-size:16px;font-family:'PingFang SC';">删除符合条件的学生成绩数据</span>**（实例位置：资源包\\TM\\sl\\06\\13）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">删除“数学”中包含88的行、“语文”小于110的行，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  df.drop(index=df\[df\['</span>数学<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\].isin(\[88\])\].index\[0\],inplace=True)  # </span>删除<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>数学<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>包含<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">88</span>的行</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  df.drop(index=df\[df\['</span>语文<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\]\<110\].index\[0\],inplace=True)         # </span>删除<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>语文<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>小于<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">110</span>的行</span>

</div>

<div class="header3">

### 6.2.4 修改数据

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">修改数据包括行、列、标题和数据的修改，我们首先来看原始数据，如图6.13所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. 修改列标题**</span>

<span style="font-size:16px;font-family:'PingFang SC';">修改列标题主要使用DataFrame()对象的cloumns属性，直接赋值即可。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.14】**</span><span style="font-size:16px;font-family:'PingFang SC';">修改“数学”的列名</span>**（实例位置：资源包\\TM\\sl\\06\\14）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">将“数学”修改为“数学（上）”，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.columns=\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>(<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">上</span>)','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>'\]</span>

<span style="font-size:16px;font-family:'PingFang SC';">上述代码中，即使我们只修改“数学”为“数学（上）”，但是也要将所有列的标题全部写上，否则将报错。</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.14所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面再介绍一种方法，使用DataFrame()对象的rename()函数修改列标题。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.15】**</span><span style="font-size:16px;font-family:'PingFang SC';">修改多个学科的列名</span>**（实例位置：资源包\\TM\\sl\\06\\15）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">将“语文”修改为“语文（上）”、“数学”修改为“数学（上）”、“英语”修改为“英语（上）”，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.rename(columns = {'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>':'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>(<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">上</span>)','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>':'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>(<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">上</span>)','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>':'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>(<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">上</span>)'},inplace = True)</span>

<span style="font-size:16px;font-family:'PingFang SC';">上述代码中，参数inplace为True，表示直接修改df；否则，不修改df，只返回修改后的数据。</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.15所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_212.jpg" width="380" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.13 原始数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_213.jpg" width="454" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.14 修改“数学”的列名</span>

<div style="display: block;text-align:center;">

<img src="images/image_214.jpg" width="670" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.15 修改多个学科的列名</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. 修改行标题**</span>

<span style="font-size:16px;font-family:'PingFang SC';">修改行标题主要使用DataFrame()对象的index属性，直接赋值即可。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.16】**</span><span style="font-size:16px;font-family:'PingFang SC';">将行标题统一修改为数字编号</span>**（实例位置：资源包\\TM\\sl\\06\\16）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">将行标题统一修改为数字编号，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.index=list('1234')</span>

<span style="font-size:16px;font-family:'PingFang SC';">使用DataFrame()对象的rename()函数也可以修改行标题。例如，将行标题统一修改为数字编号，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.rename({'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>':1,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>':2,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>':3,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丁</span>':4},axis=0,inplace = True)</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**3. 修改数据**</span>

<span style="font-size:16px;font-family:'PingFang SC';">修改数据主要使用DataFrame()对象的loc属性和iloc属性。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.17】**</span><span style="font-size:16px;font-family:'PingFang SC';">修改学生成绩数据</span>**（实例位置：资源包\\TM\\sl\\06\\17）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">（1）修改整行数据。例如，修改“甲”同学的各科成绩，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.loc\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>'\]=\[120,115,109\]</span>

<span style="font-size:16px;font-family:'PingFang SC';">如果各科成绩均加10分，可以直接在原有值加10，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.loc\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>'\]=df.loc\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>'\]+10</span>

<span style="font-size:16px;font-family:'PingFang SC';">（2）修改整列数据。例如，修改所有同学的“语文”成绩，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.loc\[:,'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>'\]=\[115,108,112,118\]</span>

<span style="font-size:16px;font-family:'PingFang SC';">（3）修改某一数据。例如，修改“甲”同学的“语文”成绩，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.loc\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>'\]=115</span>

<span style="font-size:16px;font-family:'PingFang SC';">（4）使用iloc属性修改数据。通过iloc属性指定行列位置实现修改数据，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  df.iloc\[0,0\]=115                # </span>修改某一数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  df.iloc\[:,0\]=\[115,108,112,118\]  # </span>修改整列数据</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  df.iloc\[0,:\]=\[120,115,109\]      # </span>修改整行数据</span>

</div>

<div class="header3">

### 6.2.5 查询数据

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">DataFrame()对象查询数据主要是通过运算符和函数对数据进行筛选。主要包括： <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 逻辑运算符：\>、\>=、\<、\<=、==（双等于）、!=（不等于）。 <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 复合逻辑运算符：&（并且）、\|（或者）。 <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 逻辑运算函数：query()、isin()和between()。其中query()函数主要用于简化查询代码，isin()函数表示包含，between()函数表示区间。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.18】**</span><span style="font-size:16px;font-family:'PingFang SC';">通过逻辑运算符查询数据</span>**（实例位置：资源包\\TM\\sl\\06\\18）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面通过逻辑运算符查询学生成绩数据，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df= pd.DataFrame({'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">姓名</span>':\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>'\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>':\[110,105,109\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>':\[105,88,120\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>':\[99,115,130\]})</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   print(df)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   ''' <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">逻辑运算符号：</span>\> <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">、</span>\>=<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">、</span> \<<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">、</span> \<=<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">、</span> == (<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">双等于</span>)<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">、</span>!=(<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">不等于</span>)'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  print(df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>'\]\>105\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  print(df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>'\]\>=115\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  print(df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>'\]==115\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  print(df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>'\]!=115\])</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.16所示。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.19】**</span><span style="font-size:16px;font-family:'PingFang SC';">通过复合运算符查询数据</span>**（实例位置：资源包\\TM\\sl\\06\\19）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面通过复合运算符分别查询“语文”大于105并且“数学”大于88的学生成绩和“语文”大于105或者数学大于88的学生成绩，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df= pd.DataFrame({'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">姓名</span>':\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丁</span>'\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>':\[110,105,109,99\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>':\[105,88,120,90\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>':\[99,115,130,120\]})</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">复合逻辑运算符：</span>&(<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">并且</span>) <span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">、</span>\|(<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">或者</span>)'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">查询</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>”<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">大于</span>105<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">并且</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>”<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">大于</span>88'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  print(df\[(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>'\]\>105) & (df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>'\]\>88)\])</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">查询</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>”<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">大于</span>105<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">或者数学大于</span>88'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  print(df\[(df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>'\]\>105) \| (df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>'\]\>88)\])</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.17所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面重点介绍逻辑运算函数。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. query()函数**</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.20】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用query()函数简化查询代码</span>**（实例位置：资源包\\TM\\sl\\06\\20）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">在前面的示例中，当查询“语文”大于105的学生成绩时，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>'\]\>105\]</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用query()函数进行简化，代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.query('<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>\>105')</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. isin()函数**</span>

<span style="font-size:16px;font-family:'PingFang SC';">isin()函数不仅可以针对整个DataFrame()对象进行操作，也可以针对DataFrame()对象中的某一列（Series()对象）进行操作，而针对Series()对象的操作才是最常用的。</span>

<span style="font-size:16px;font-family:'PingFang SC';">isin()函数的作用如下： <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 判断整个DataFrame()对象中是否包含某个值或某些值。 <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 判断DataFrame()对象中的某一列（Series()对象）是否包含某个值或某些值。 <img src="images/image_211.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> 利用一个DataFrame()对象中的某一列，对另一个DataFrame()对象中的数据进行过滤，这一点非常重要。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.21】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用isin()函数查询数据</span>**（实例位置：资源包\\TM\\sl\\06\\21）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用isin()函数查询两种数据：一是查询所有数据中包含45和60的数据；二是查询“化学”中包含45和60的数据，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df= pd.DataFrame({'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">姓名</span>':\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>'\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>':\[110,105,109\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>':\[105,60,120\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>':\[99,115,130\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">物理</span>':\[60,89,99\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">化学</span>':\[45,60,70\]})</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">逻辑运算函数：</span>isin()<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">函数</span>'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">判断所有数据中包含</span>45<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">和</span>60<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">的数据</span>'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12  df1=df\[df.isin(\[45,60\])\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13  print(df1)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">判断</span>“<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">化学</span>”<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">中包含</span>45<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">和</span>60<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">的数据</span>'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  df2=df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">化学</span>'\].isin(\[45,60\])\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  print(df2)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.18所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_215.jpg" width="446" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.16 通过逻辑运算符查询数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_216.jpg" width="438" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.17 通过复合运算符查询数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_217.jpg" width="605" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图6.18 使用isin()函数查询数据</span>

<span style="font-size:16px;font-family:'PingFang SC';">isin()函数的另外一种用法是可以实现一个DataFrame()对象中的某一列对另一个DataFrame()对象中的数据进行过滤。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.22】**</span><span style="font-size:16px;font-family:'PingFang SC';">查询女生的学习成绩</span>**（实例位置：资源包\\TM\\sl\\06\\22）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">通过学生基本信息数据（df2）中的“性别”，对学生成绩（df1）进行筛选，查询所有女生的学习成绩，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df1= pd.DataFrame({'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">姓名</span>':\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>'\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>':\[110,105,109\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>':\[105,60,120\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>':\[99,115,130\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">物理</span>':\[60,89,99\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">化学</span>':\[45,60,70\]})</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  print(df1)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  df2=pd.DataFrame({'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">姓名</span>':\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>'\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">12                    '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">性别</span>':\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">男</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">女</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">女</span>'\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">13                    '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">年龄</span>':\[16,15,16\]})</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">14  print(df2)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">15  '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">逻辑运算函数：</span>isin()<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">函数</span>'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">16  '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">利用</span>df2<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">中的性别一列，来对</span>df1<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">中的数据进行筛选</span>'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">17  df1=df1\[df2\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">性别</span>'\].isin(\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">女</span>'\])\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">18  print(df1)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.19所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_218.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">图6.19 查询所有女生的学习成绩</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**3. between()函数**</span>

<span style="font-size:16px;font-family:'PingFang SC';">between()函数用于查询指定范围内的数据，返回布尔值。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.23】**</span><span style="font-size:16px;font-family:'PingFang SC';">使用between()函数查询数据</span>**（实例位置：资源包\\TM\\sl\\06\\23）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">下面使用between()函数查询“语文”100～120分的数据，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1   import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   df= pd.DataFrame({'<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">姓名</span>':\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">甲</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">乙</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">丙</span>'\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>':\[110,105,109\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">数学</span>':\[105,88,120\],</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7                     '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">英语</span>':\[99,115,130\]})</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   '''<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">逻辑运算函数：</span>between()<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">函数</span>'''</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   df1=df\[df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">语文</span>'\].between(100,120)\]</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  print(df1)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，输出结果如图6.20所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_219.jpg" width="421" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">图6.20 使用between()函数查询数据</span>

</div>

<span id="Section043.xhtml"></span>

<div id="Section043.xhtml_Section043.xhtml">

</div>

<div class="header2">

## 6.3 数据的排序和排名

</div>

<div class="part">

</div>

<div class="header3">

### 6.3.1 数据的排序

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">DataFrame数据排序主要使用sort_values()函数，该函数类似于SQL中的order by语句。sort_values()函数可以根据指定的行或列进行排序，语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">DataFrame.sort_values(by,axis=0,ascending=True,inplace=False,kind='quicksort',na_position='last',ignore_index=False)</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> by：要排序的名称列表。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> axis：轴，0表示行，1表示列，默认按行排序。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> ascending：升序或降序排序，布尔值。指定多个排序时可以使用布尔值列表。默认值为True。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> inplace：布尔值，表示是否修改原数据。默认值为False，表示不修改；如果值为True，则在原数据中进行排序。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> kind：指定排序算法，值为quicksort（快速排序）、mergesort（混合排序）或heapsort（堆排），默认值为quicksort。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> na_position：空值（NaN）的位置。值为first，表示空值在数据开头；值为last，表示空值在数据最后。默认值为last。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> ignore_index：布尔值，表示是否忽略索引。值为True，标记索引（从0开始按顺序的整数值）；值为False，则忽略索引。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. 按一列数据排序**</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.24】**</span><span style="font-size:16px;font-family:'PingFang SC';">按“销量”降序排序</span>**（实例位置：资源包\\TM\\sl\\06\\24）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">按“销量”降序排序，排序对比效果如图6.21和图6.22所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_221.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.21 原始数据</span>

<div style="display: block;text-align:center;">

<img src="images/image_222.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';display: block;text-align:center;">▲图6.22 按“销量”降序排序</span>

<span style="font-size:16px;font-family:'PingFang SC';">程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  df =pd.read_excel('mrbook.xlsx')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3  # </span>设置数据显示的列数和宽度</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4  pd.set_option('display.max_columns',500)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5  pd.set_option('display.width',1000)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6  # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7  pd.set_option('display.unicode.ambiguous_as_wide', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8  pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   # </span>按<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>销量<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>列降序排序</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  df=df.sort_values(by='<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">销量</span>',ascending=False)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  print(df)</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. 按多列数据排序**</span>

<span style="font-size:16px;font-family:'PingFang SC';">多列排序是按照给定列的先后顺序进行排序的。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.25】**</span><span style="font-size:16px;font-family:'PingFang SC';">按照“图书名称”和“销量”降序排序</span>**（实例位置：资源包\\TM\\sl\\06\\25）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">按照“图书名称”和“销量”降序排序，首先按“图书名称”降序排序，然后按“销量”降序排序，排序后的效果如图6.23所示。</span>

<span style="font-size:16px;font-family:'PingFang SC';">关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df.sort_values(by=\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">图书名称</span>','<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">销量</span>'\],ascending=\[False,False\])</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**3. 对统计结果排序**</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.26】**</span><span style="font-size:16px;font-family:'PingFang SC';">对分组统计数据进行排序</span>**（实例位置：资源包\\TM\\sl\\06\\26）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">按“类别”分组统计销量并进行降序排序，统计排序后的效果如图6.24所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_223.jpg" width="900" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图6.23 按照“图书名称”和“销量”降序排序</span>

<div style="display: block;text-align:center;">

<img src="images/image_224.jpg" width="407" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图6.24 按“类别”分组统计销量并降序排序</span>

<span style="font-size:16px;font-family:'PingFang SC';">关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  df1=df.groupby(\["<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">类别</span>"\])\["<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">销量</span>"\].sum().reset_index()</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2  df2=df1.sort_values(by='<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">销量</span>',ascending=False)</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**4. 按行数据排序**</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.27】**</span><span style="font-size:16px;font-family:'PingFang SC';">按行数据排序</span>**（实例位置：资源包\\TM\\sl\\06\\27）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">按行排序，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">dfrow.sort_values(by=0,ascending=True,axis=1)</span>

<span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**注意**</span>

<span style="font-size:16px;font-family:'PingFang SC';">按行排序的数据类型要一致，否则会出现错误提示。</span>

</div>

<div class="header3">

### 6.3.2 数据排名

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">排名是根据Series()对象或DataFrame()对象的某几列的值进行排名，主要使用rank()函数，语法如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">DataFrame.rank(axis=0,method='average',numeric_only=None,na_option='keep',ascending=True,pct=False)</span>

<span style="font-size:16px;font-family:'PingFang SC';">参数说明： <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> axis：轴，0表示行，1表示列，默认按行排序。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> method：表示在具有相同值的情况下所使用的排序函数。设置值如下： <img src="images/image_225.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> average：默认值，平均排名。 <img src="images/image_225.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> min：最小值排名。 <img src="images/image_225.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> max：最大值排名。 <img src="images/image_225.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> first：按值在原始数据中出现的顺序分配排名。 <img src="images/image_225.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> dense：密集排名，类似最小值排名，但是排名每次只增加1，即排名相同的数据只占1个名次。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> numeric_only：对于DataFrame()对象，如果设置值为True，则只对数字列进行排序。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> na_option：空值的排序方式，设置值如下： <img src="images/image_225.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> keep：保留，将空值等级赋值给NaN值。 <img src="images/image_225.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> top：如果按升序排序，则将最小排名赋值给NaN值。 <img src="images/image_225.svg" width="12" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> bottom：如果按升序排序，则将最大排名赋值给NaN值。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> ascending：升序或降序排序，布尔值。指定多个排序时可以使用布尔值列表。默认值为True。 <img src="images/image_220.svg" width="14" /></span>

<span style="font-size:16px;font-family:'PingFang SC';"> pct：布尔值，表示是否以百分比形式返回排名。默认值为False。</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**1. 顺序排名**</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.28】**</span><span style="font-size:16px;font-family:'PingFang SC';">对产品销量按顺序进行排名</span>**（实例位置：资源包\\TM\\sl\\06\\28）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">排名相同的，按照相同的值出现的顺序排名，程序代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">1  import pandas as pd</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">2   df = pd.read_excel('mrbook.xlsx')</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">3   # </span>设置数据显示的最大列数和宽度</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">4   pd.set_option('display.max_columns',500)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">5   pd.set_option('display.width',1000)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">6   # </span>设置数据显示的编码格式为东亚宽度，以使列对齐</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">7   pd.set_option('display.unicode.ambiguous_as_wide', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">8   pd.set_option('display.unicode.east_asian_width', True)</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">9   df=df.sort_values(by='</span>销量<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">',ascending=False)                          # </span>按<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">“</span>销量<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">”</span>列降序排序</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';"><span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">10  df\['</span>顺序排名<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\] = df\['</span>销量<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">'\].rank(method="first", ascending=False)   # </span>顺序排名</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">11  print(df\[\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">图书名称</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">销量</span>', '<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">顺序排名</span>'\]\])</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**2. 平均排名**</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';"><span style="font-size:16px;font-weight: bold;font-family:'PingFang SC';">**【例6.29】**</span><span style="font-size:16px;font-family:'PingFang SC';">对产品销量进行平均排名</span>**（实例位置：资源包\\TM\\sl\\06\\29）**</span>

<span style="font-size:16px;font-family:'PingFang SC';">排名相同的，以顺序排名的平均值作为平均排名，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">平均排名</span>'\]=df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">销量</span>'\].rank(ascending=False)</span>

<span style="font-size:16px;font-family:'PingFang SC';">运行程序，下面对比一下顺序排名与平均排名的不同，效果如图6.25和图6.26所示。</span>

<div style="display: block;text-align:center;">

<img src="images/image_226.jpg" width="850" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图6.25 销量相同按出现的先后顺序排名</span>

<div style="display: block;text-align:center;">

<img src="images/image_227.jpg" width="836" />

</div>

<span style="font-size:16px;color:rgb(0, 0, 0);font-family:'FZFangSong-Z02';">▲图6.26 销量相同按顺序排名的平均值排名</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**3. 最小值排名**</span>

<span style="font-size:16px;font-family:'PingFang SC';">排名相同的，以顺序排名取最小值作为排名，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">销量</span>'\].rank(method="min",ascending=False)</span>

<span style="font-size:16px;font-weight: bold;color:rgb(0, 0, 0);font-family:'PingFang SC';">**4. 最大值排名**</span>

<span style="font-size:16px;font-family:'PingFang SC';">排名相同的，以顺序排名取最大值作为排名，关键代码如下：</span>

<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'Source Code Pro';">df\['<span style="font-size:14px;color:rgb(0, 0, 0);font-family:'PingFang SC';">销量</span>'\].rank(method="max",ascending=False)</span>

</div>

<span id="Section044.xhtml"></span>

<div id="Section044.xhtml_Section044.xhtml">

</div>

<div class="header2">

## 6.4 小结

</div>

<div class="part">

<span style="font-size:16px;font-family:'PingFang SC';">本章介绍了如何使用Pandas模块实现数据的处理工作，其中包含数据抽取，数据的增、删、改、查操作，最后介绍了如何实现数据的排序以及数据的排名操作。本章所学习的内容都是数据分析中最为常见的技术，希望大家能够熟练掌握这些技术。</span>

</div>

<span id="Section045.xhtml"></span>

<div id="Section045.xhtml_Section045.xhtml">

</div>

<div class="header1">
