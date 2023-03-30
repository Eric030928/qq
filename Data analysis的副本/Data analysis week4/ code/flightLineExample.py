"""
this code is used to show the map visualization
"""
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType,SymbolType

c = (
    Geo().add_schema(maptype= "china")
    .add(".",[("哈尔滨",66),("重庆",88),("上海",100),("乌鲁木齐",30),("北京",30),("兰州",170)])
    .add("geo",[("北京","兰州"),("兰州","北京")],type_= ChartType.LINES,effect_opts = opts.EffectOpts(symbol = SymbolType.ARROW,symbol_size=6,color="blue"))
)

c.render("../result/flightExample.html")
