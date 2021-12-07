---
title: 學習梯度下降簡單版本，Flowchart的作圖方式等
date: "2021-11-30T23:46:37.121Z"
template: "post"
draft: false
slug: "pleaseDecribe"
category: "每日學習記錄"
tags:
  - "工作記錄"
  - "生活管理"
description: "在事上磨練。記錄當天的課題與解決，新發現，與新改善點"
socialImage: "media/image-2.jpg"
---

# 今天嘗試使用了JAVA的代理機能
 
- Wrap了ResultSet，實現了Trim字符串的功能。
- 
[Javaにおける動的プロキシ - 開発者ドキュメント](https://ja.getdocs.org/java-dynamic-proxies/)

[java.lang.reflect.Proxy に触れてみる - vaguely](https://mslgt.hatenablog.com/entry/2018/05/25/192025)

[ResultSetInvocationHandler.java example](https://www.javatips.net/api/datasource-proxy-master/src/main/java/net/ttddyy/dsproxy/proxy/jdk/ResultSetInvocationHandler.java)

[【Java】SQLやSQL結果をログに出すためのプロキシ - Qiita](https://qiita.com/momosetkn/items/c0bc1d30b995bfd55fc3)

[L JDBC&nbsp;&laquo;&nbsp;Java](http://www.java2s.com/Code/Java/Database-SQL-JDBC/WrapsaResultSettotrimstringsreturnedbythegetStringandgetObjectmethods.htm)
 
# 今天突然發現陪伴孩子是上算得投資
 下定決心每天花時間陪他們成長。

# 不看字幕好像很有效
 在現了當天在Costo聽不懂店員跟我說話的場景。

# 每天進步一點pytourch 
買書？
[Coursera 上有哪些课程值得推荐？ - 知乎](https://www.zhihu.com/question/22436320)

[10月深入浅出pytorch-task02-ss](http://datawhale.club/t/topic/3209)

[PyTorch入门实战教程笔记（二）：简单回归问题。_Superstar02的博客-CSDN博客](https://blog.csdn.net/Superstar02/article/details/102881082?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-1.no_search_link&spm=1001.2101.3001.4242.2)


[PyTorch实战学习笔记_Superstar02的博客-CSDN博客](https://blog.csdn.net/superstar02/category_9480352.html)

# andrew ng 筆記
[GitHub - fengdu78/Coursera-ML-AndrewNg-Notes: 吴恩达老师的机器学习课程个人笔记](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes)

[GitHub - fengdu78/deeplearning_ai_books: deeplearning.ai（吴恩达老师的深度学习课程笔记及资源）](https://github.com/fengdu78/deeplearning_ai_books)

[https://www.bilibili.com/video/BV1YR4y147Np](https://www.bilibili.com/video/BV1YR4y147Np)

```python
#定义一个计算总的error（即总的loss），其中points为一系列的（x，y）的组合:
def compute_error_for_line_given_points(b, w, points):
    totalError = 0      				#定义总的loss
    for i in range(0, len(points)):
        x = points[i, 0]  				#取该点的x值
        y = points[i, 1]  				#取该点的y值
        totalError += (y - (w * x + b)) ** 2 		#将每一个点的loss累加
    return totalError / float(len(points))			#对总的error求一个平均，返回总的平均error

#定义一个计算梯度的函数：入口参数：b当前值，W当前值，点集合，学习率
def step_gradient(b_current, w_current, points, learningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))      #总的数据点的个数
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        #∂L/∂b = 2（Wx + b - y），所有梯度累加时除以N，以便结果不用再做平均
        b_gradient += -(2/N) * (y - ((w_current * x) + b_current))
        #∂L/∂W = 2（Wx + b - y）x，所有梯度累加时除以N，以便结果不用再做平均
        w_gradient += -(2/N) * x * (y - ((w_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_W = w_current - (learningRate * w_gradient)
    return [new_b, new_W]
#循环迭代W，b，入口参数：（x，y）点集合，初始b,初始W，学习率，迭代次数：
def gradient_descent_runner(points, starting_b, starting_w, learning_rate, num_iterations):
    b = starting_b
    w = starting_w
    for i in range(num_iterations):
        b, w = step_gradient(b, w, np.array(points), learning_rate) 	#np.array（point）为（x，y）的数组
    return [b, w]
def run():
    points = np.genfromtxt("data.csv", delimiter=",")       #取数据
    learning_rate = 0.0001
    initial_b = 0 # initial y-intercept guess
    initial_w = 0 # initial slope guess
    num_iterations = 1000
    print("Starting gradient descent at b = {0}, w = {1}, error = {2}"
          .format(initial_b, initial_w,
                  compute_error_for_line_given_points(initial_b, initial_w, points))
          )
    print("Running...")
    [b, w] = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, error = {3}".
          format(num_iterations, b, w,
                 compute_error_for_line_given_points(b, w, points))
          )

if __name__ == '__main__':
    run()

```

[https://www.bilibili.com/video/BV1Sr4y1N71H?p=3&t=543.3](https://www.bilibili.com/video/BV1Sr4y1N71H?p=3&t=543.3)

# svg
[Attention Required! | Cloudflare](https://codepen.io/BillKroger/pen/NdGybP)

[mermaid - Markdownish syntax for generating flowcharts, sequence diagrams, class diagrams, gantt charts and git graphs.](https://mermaid-js.github.io/mermaid/#/n00b-overview?id=creating-and-maintaining-diagrams)

[GitHub - Bogdan-Lyashenko/js-code-to-svg-flowchart: js2flowchart - a visualization library to convert any JavaScript code into beautiful SVG flowchart. Learn other’s code. Design your code. Refactor code. Document code. Explain code.](https://github.com/Bogdan-Lyashenko/js-code-to-svg-flowchart)

[SVG - Stroke](https://www.tutorialspoint.com/svg/svg_stroke.htm)

[Getting Title at 41:30](https://blog.htmlhifive.com/2016/06/24/svg-beautilful-graph-library/)

[GitHub - seflless/diagrams: Generate Flowcharts, Network Sequence Diagrams, GraphViz Dot Diagrams, and Railroad Diagrams](https://github.com/seflless/diagrams#flowchart)

[flowchart.js - Draws simple SVG flow chart diagrams from textual representation of the diagram](https://www.findbestopensource.com/product/adrai-flowchart-js)

[【VS Code + Marp】Markdownから爆速・自由自在なデザインで、プレゼンスライドを作る - Qiita](https://qiita.com/tomo_makes/items/aafae4021986553ae1d8)

[GitHub - hrhr49/tefcha: Text to Flowchart](https://github.com/hrhr49/tefcha)