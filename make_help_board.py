from init import *
import make_frame

command={}  # 该字典记录下了在画板上的对应位置应该生成什么方块

'''生成图片辅助颜料的指令函数文件，如珊瑚块下的水和树叶下的原木等，不需要辅助颜料的方块用黑曜石填充'''
def make_help_board(imagename,origin):
    make_frame.make_frame(imagename,origin)
    file = open(fr"help_board.mcfunction", "a", encoding='UTF8')
    image = Image.open(imagename).convert('RGB')
    width=image.width
    height=image.height
    if width*height>65500:
        width=int(image.width/math.sqrt(image.width*image.height/65500))
        height=int(image.height/math.sqrt(image.width*image.height/65500))
        image=image.resize((width,height),Image.NEAREST).convert('RGB')
    imagepixel = numpy.asarray(image)
    for i in range(0, height):
        for j in range(0, width):
            '''通过寻找相近颜色的方式，得到当前位置应该放置的方块'''
            name=find(tuple(imagepixel[i,j]))
            if name=='snow':    # 改变雪的厚度
                name=name+'[layers=8]'
            command[fr'({i},{j})']=name
            #  特殊颜料特殊处理
            file.write(fr"setblock {origin[0]+j} {origin[1]} {origin[2]+i} minecraft:obsidian"+'\n')
            if name.count("leaves")>0:  # 该方块是树叶，底下放原木
                file.write(fr"setblock {origin[0]+j} {origin[1]} {origin[2]+i} minecraft:{name.replace('leaves','wood')}"+'\n')
            if name.count("coral")>0:   #  该方块是珊瑚，底下放水
                file.write(fr"setblock {origin[0]+j} {origin[1]} {origin[2]+i} minecraft:water"+'\n')
            if name.count("snow")>0:
                file.write(fr"setblock {origin[0] + j} {origin[1]} {origin[2] + i} minecraft:grass_block"+'\n')

    file.close()
    os.makedirs('build', exist_ok=True)
    shutil.copyfile(fr"help_board.mcfunction",'build/help_board.mcfunction')
    os.remove(fr"help_board.mcfunction")


if __name__ == '__main__':
    make_help_board(input(), eval(input()))