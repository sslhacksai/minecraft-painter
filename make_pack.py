from init import *
'''生成 mc 数据包所需的pack索引文件'''
def make_pack(edition):
    f = open(fr"pack.mcmeta", "w", encoding='UTF8')
    '''文件内容，数字部分为mc版本，可以根据不同情况修改，如 1.16.x 写为 6,1.18.x 写为 8'''
    f.write("{\n    \"pack\": {\n        \"pack_format\": "+edition.split('.')[1][-1]+",\n        \"description\": \"draw picture\"\n    }\n}")
    f.close()
    os.makedirs('build', exist_ok=True)
    shutil.copyfile(fr"pack.mcmeta",'build/pack.mcmeta')
    os.remove(fr"pack.mcmeta")

if __name__=='__main__':
    make_pack()