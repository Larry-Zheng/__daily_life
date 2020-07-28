# __daily_life
日常hape代码上传列一些to do和done list







![格式工厂startup](./README.assets/格式工厂startup.jpg)



- [x] GMM

- [x] 层次聚类linkage计算

- [x] Alexnet  

- [x] VGG   

- [x] Resnet

- [ ] shake-shake regu

- [x] NIN

- [ ] Xception

- [ ] DenseNet

- [ ] ？空间注意力与通道注意力不一定放在一起，浅层给空间注意力，深层给通道注意力等

- [ ] 细粒度模型

- [ ] ASPP(FF??)

- [x] Siamese Unet

- [x] 高斯滤波

- [x] 均值滤波

- [x] 形态学操作

- [x] 最近邻插值

- [x] 双线性插值

- [x] 直方图均衡化

  - [x] 如果对累加概率进行指数加权平均可以调整对比度效果，甚至可以减小对比度将图像变暗
  - [x] 累加概率的计算

- [x] 轮廓面积计算

  - [x] 向量积求和

- [x] moments

  - [x] 所谓灰度强度 m00 本质上就是上一条 求面积（即array(x,y)是求向量积）
  - [x] 中心坐标计算 x,y = m10/m00,m01/m00
  - [ ] moments做匹配

- [x] 三帧差法

  - [x] 一次取三帧 s1,s2,s3
  - [x] 分别作差值计算 diff1 = abs(s2-s1);diff2 = abs(s3-s2)
  - [x] diff1与diff2 bit_wise_and
  - [x] s1,s2 = s2,s3

- [ ] 模型剪枝蒸馏

- [ ] 贝叶斯网络

  








