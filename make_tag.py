from init import *

def make_tag(imagename):
    file=open(fr'{imagename.split(".")[0]}.json','w',encoding='UTF8')
    file.write('{\n	"values": [\n		"draw:board",\n		"draw:help_board",\n		"draw:picture",\n		"draw:frame"\n	]\n}')
    file.close()
    os.makedirs('build', exist_ok=True)
    shutil.copyfile(fr'{imagename.split(".")[0]}.json',fr'build/{imagename.split(".")[0]}.json')
    os.remove(fr'{imagename.split(".")[0]}.json')

if __name__=='__main__':
    make_tag(input())