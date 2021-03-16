import os

nums = 0

dirs = os.listdir()    # 获取当前目录下所有的文件夹
cwd = os.path.abspath('.')      # 获取当前目录的绝对路径


for i in dirs:
    dirs2 = os.walk(i)    # 获取文件夹下所有的子目录
    for j in dirs2:
        dir3 = os.path.join(cwd, j[0])    # 获取子目录的绝对路径
        try:
            os.removedirs(dir3)    # 删除空白子目录
            print('删除空文件夹{}'.format(dir3))
            nums += 1
        except OSError:
            pass

print('执行完毕,删除了{}个空文件夹'.format(nums))
