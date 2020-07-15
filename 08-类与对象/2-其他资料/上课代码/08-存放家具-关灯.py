class Home:
    def __init__(self, area):
        self.area = area
        self.light = "on"
        self.containsItem = []

    def __str__(self):
        msg = "家当前可用面积为:"+str(self.area)
        if len(self.containsItem)>0:
            msg += "\t"
            msg += "家里的物品有:"
            
            #msg += ",".join(self.containsItem)

            for temp in self.containsItem:
                #msg += temp.name + ","
                msg += temp.getName() + ","
            '''
            else:
                msg += "没有任何东西"
            '''
            msg = msg[:-1]

            if self.light == "on":
                msg += "\t" + "当前灯是开着灯，所有的物品都是可见的"
            else:
                msg += "\t" + "当前灯是关着的"


        return msg

    #添加一个新的物品到家里面
    def addItem(self, item):
        #if self.area > item.area:
        needArea = item.getArea()
        if self.area > needArea:
            self.containsItem.append(item)
            self.area -= needArea

    #关灯
    def turnoff(self):
        self.light = "off"
        #修改所有的物品的可见度
        for temp in self.containsItem:
            temp.turnoff()



class Bed:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.light = "on"

    def __str__(self):
        msg = self.name + "床的面积为:" + str(self.area) + " 当前的可见度为:" + self.light
        return msg

    def getName(self):
        return self.name

    def getArea(self):
        return self.area


    def turnoff(self):
        self.light = "off"



#创建一个家对象
home = Home(128)
print(home)


bed = Bed("席梦思", 4)
print(bed)

home.addItem(bed)
print(home)

bed2 = Bed("硬板床", 3)
print(bed2)

home.addItem(bed2)


print(home)




print("===========================分割================")

home.turnoff()
print(bed)
print(bed2)


# 打印
# 家当前可用面积为:128
# 席梦思床的面积为:4 当前的可见度为:on
# 家当前可用面积为:124    家里的物品有:席梦思     当前灯是开着灯，所有的物品都是可见的
# 硬板床床的面积为:3 当前的可见度为:on
# 家当前可用面积为:121    家里的物品有:席梦思,硬板床      当前灯是开着灯，所有的物品都是可见的
# ===========================分割================
# 席梦思床的面积为:4 当前的可见度为:off
# 硬板床床的面积为:3 当前的可见度为:off