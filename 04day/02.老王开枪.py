class Person():
    def __init__(self,name):
        self.name = name
        self.hp = 100
    def NaQiang(self,gun):
        self.gun = gun#相当于老王的一个属性

    def KaiQiang(self,person):
        zd = self.gun.dj.popzd()#请求就发射一个子弹
        zd.kill(person)
        
    def DiaoXue(self,count):#掉血
        self.hp -= count
        if self.hp <= 0:
            self.hp = 0
            print("死了%d"%self.hp)
class Gun():
    def __init__(self,name):
        self.name = name

    def zhuangdanjia(self,dj):#装弹夹
        self.dj = dj

class DanJia():
    def __init__(self):
        self.list = []#装子弹
    
    def zhuangzidan(self,zd):
        self.list.append(zd)#装子弹

    def popzd(self):#开枪会减少一发子弹
        return self.list.pop()#把子弹给枪
    
class ZiDan():
    def __init__(self):
        self.k = 5

    def kill(self,person):#子弹杀人
        person.DiaoXue(self.k)

lw = Person("老王")#创建老王对象
ak47 = Gun("ak47")#创建枪对象
dj = DanJia()#创建一个弹夹
for i in range(30):#创建一些子弹
    zd = ZiDan()
    dj.zhuangzidan(zd)#把子弹装进弹夹
ak47.zhuangdanjia(dj)#把弹夹装到枪上
ls = Person("老宋")#创建一个敌人

lw.NaQiang(ak47)#老王拿起枪
for i in range(30):
    lw.KaiQiang(ls)#老王开枪














