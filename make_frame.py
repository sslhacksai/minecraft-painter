from init import *

'''生成一个画框的指令函数文件，保证辅助颜料不会从画板侧面漏出'''
def make_frame(imagename,origin):
    file=open(fr"frame.mcfunction",'a',encoding='UTF8')
    image=Image.open(imagename).convert('RGB')
    '''画框要比原画大一圈，因此起始点要移动'''
    first=(origin[0]-1,origin[1],origin[2]-1)
    width=image.width
    height=image.height
    if width*height>65500:
        width=int(image.width/math.sqrt(image.width*image.height/65500))
        height=int(image.height/math.sqrt(image.width*image.height/65500))
        image=image.resize((width,height),Image.NEAREST).convert('RGB')

    '''z轴方向的画框'''
    for i in range(0,height+2):
        file.write(fr"setblock {first[0]} {first[1]} {first[2]+i} minecraft:obsidian"+'\n')
        file.write(fr"setblock {first[0]+width+1} {first[1]} {first[2]+i} minecraft:obsidian"+'\n')
    '''x轴方向的画框'''
    for i in range(0,width+2):
        file.write(fr"setblock {first[0]+i} {first[1]} {first[2]} minecraft:obsidian" + '\n')
        file.write(fr"setblock {first[0]+i} {first[1]} {first[2]+height+1} minecraft:obsidian" + '\n')

    file.close()
    os.makedirs('build', exist_ok=True)

if __name__=='__main__':
    make_frame(input(),eval(input()))