"""
function:this source code demonstrates how to draw a bar figure
"""
from pyecharts.charts import Bar

bar = (Bar().add_xaxis(["car","ship","train","bus"])
       .add_yaxis("spring festival",[30,20,50,100])
       .add_yaxis("national day",[30,50,80,120])
