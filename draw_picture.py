import os
import shutil
import make_frame
import init
import zipfile
import make_tag
import make_pack
import make_board
import make_help_board
import make_picture

def draw(imagename,origin,edition):
    make_pack.make_pack(edition)
    make_board.make_board(imagename,origin)
    make_help_board.make_help_board(imagename,(origin[0],origin[1]+1,origin[2]))
    make_picture.make_picture(imagename,(origin[0],origin[1]+2,origin[2]))
    shutil.copyfile(fr"frame.mcfunction",'build/frame.mcfunction')
    os.remove(fr"frame.mcfunction")
    make_tag.make_tag(imagename)
    with zipfile.ZipFile(fr'draw_{imagename.split(".")[0]}.zip','w',zipfile.ZIP_DEFLATED) as zp:
        zp.write(fr'build\pack.mcmeta','pack.mcmeta')
        zp.write(fr'build\board.mcfunction',fr'data\draw\functions\board.mcfunction')
        zp.write(fr'build\help_board.mcfunction',fr'data\draw\functions\help_board.mcfunction')
        zp.write(fr'build\picture.mcfunction',fr'data\draw\functions\picture.mcfunction')
        zp.write(fr'build\frame.mcfunction',fr'data\draw\functions\frame.mcfunction')
        zp.write(fr'build\{imagename.split(".")[0]}.json',fr'data\draw\tags\functions\{imagename.split(".")[0]}.json')

if __name__=='__main__':
    draw(input(),eval(input()),input())