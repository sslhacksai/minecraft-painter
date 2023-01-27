# 按照对spec文件大包资源要求的格式将 resourses 文件夹中的所有文件输出

import os
rootpath=r'.\resourses'
filepath=[]
for (dirpath,dirnames,filenames) in os.walk(rootpath):
    for fn in filenames:
        fpath=os.path.join(dirpath,fn)
        filepath.append((str(fpath).replace('\\','/'),'resourses'))
print(filepath)