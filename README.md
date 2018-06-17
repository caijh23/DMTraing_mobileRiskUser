# 数据挖掘实训JData比赛
数据挖掘实训Jdata算法比赛代码

[比赛链接（基于移动网络通讯行为的风险用户识别）](https://jdata.jd.com/html/detail.html?id=3)

#### 特征工程
- 关于sms,voice,wa都做了不同用户通话或者短信或者上网的总次数统计，与不同对端号码通信或者短信的个数统计以及访问不同网站个数统计（unique）,对与sms和voice不同的opp_head同样统计了unique,对opp_len统计了count，然后对in,out分别统计了次数，对于不同call_type，voice这里也分类别统计了，对于wa这边，对visit_dura，up_flow,down_flow的不同统计量做了统计
- 关于时间的处理，换算出通话时长后统计了通话时长各个统计量
- 关于多变量统计
  - voice的不同opp_head的in与out的统计
  - sms的不同opp_head的in与out的统计

#### 模型
模型没怎么变动，最后没做模型融合或更换什么的，还是用的baseline的lgb。