from init import *
import make_frame

'''生成一块大小与图片相等的黑曜石画板的指令函数文件，使颜料在空中不受重力影响'''
def make_board(imagename,origin):

    make_frame.make_frame(imagename, origin)
    file = open(fr"board.mcfunction", "a", encoding='UTF8')
    image = Image.open(imagename).convert('RGB')
    width=image.width
    height=image.height
    if width*height>=65500:
        '''数据包最大可一次性执行命令的个数为 65536 ，过大的图片要进行压缩'''
        width=int(image.width/math.sqrt(image.width*image.height/65500))
        height=int(image.height/math.sqrt(image.width*image.height/65500))
        image=image.resize((width,height),Image.NEAREST).convert('RGB')

    '''在绘画区域内生成指令填充黑曜石'''
    for i in range(0, height):
        for j in range(0, width):
            file.write(fr"setblock {origin[0] + j} {origin[1]} {origin[2] + i} minecraft:obsidian" + '\n')
    file.close()

    '''处理程序运行后的临时数据文件，统一放入 build 中'''
    os.makedirs('build', exist_ok=True)
    shutil.copyfile(fr"board.mcfunction",'build/board.mcfunction')
    os.remove(fr"board.mcfunction")

if __name__=='__main__':
    make_board(input(),eval(input()))