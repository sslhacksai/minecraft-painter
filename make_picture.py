import os
from init import *
from make_help_board import *
import make_frame

'''生成绘制图片的指令函数文件'''
def make_picture(imagename,origin):
    make_frame.make_frame(imagename,origin)
    file=open(fr"picture.mcfunction","a",encoding='UTF8')
    image=Image.open(imagename).convert('RGB')
    width=image.width
    height=image.height
    if width*height>65500:
        width=int(image.width/math.sqrt(image.width*image.height/65500))
        height=int(image.height/math.sqrt(image.width*image.height/65500))
        image=image.resize((width,height),Image.NEAREST).convert('RGB')
    for i in range(0,height):
        for j in range(0,width):
            '''command来自辅助颜料的额制作过程'''
            file.write(fr"setblock {origin[0]+j} {origin[1]} {origin[2]+i} minecraft:{command[fr'({i},{j})']}"+'\n')
    file.close()
    os.makedirs('build', exist_ok=True)
    shutil.copyfile('picture.mcfunction','build/picture.mcfunction')
    os.remove('picture.mcfunction')

if __name__=='__main__':
    make_picture(input(),eval(input()))