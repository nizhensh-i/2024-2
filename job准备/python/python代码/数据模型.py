class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name:{self.name}'
    
    @property
    def school(self):
        return self._school
    

    @school.setter
    def school(self,val):
        self._school = '设置'+val

    @school.deleter
    def school(self):
        raise '不能删'

# p = Person('张三',12)
# # print(p)
# p.school = '山大'
# print(p._school)
# print(p.school)
        


class Score:

    # 场景
    __scene = None
    # 区
    __district = None
    # 开始时间
    __begin_time = None
    # 结束时间
    __end_time = None


   

    # 设置区值
    def set_district(self,value:str):
        if value != '静安区' and value != '徐汇区' and value != '金山区':
            print('区不在范围内')
            return
        Score.__district = value

    # 获取区值
    def get_district(self):
        return Score.__district


    #设置区值
    @property
    def distinct(self):
        return self.__district
    
    @distinct.setter
    def distinct(self,value):
        self.__district = '设置' + value

    @distinct.deleter
    def distinct(self):
        raise '不能删除'

if __name__ == '__main__':
    a = Score()
    a.distinct  = '静安区'
    print(a.distinct)
    del a.distinct





