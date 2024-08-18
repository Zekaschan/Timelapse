import os
import datetime


def makedirandfile(dir, prefix, timespec, use_subdir = False):
    if use_subdir:
        dir = dir + str(datetime.date.today()) + '/'
    PrepOutputDir(dir)
    return dir+get_newfname(prefix, timespec)


#Make sure output directory exists
def PrepOutputDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        print('Created new day: '+dir)
    else:
        #print('Path exists, continuing')
        pass

#Get new filename via datetime
def get_newfname(prefix, timespec):
    return prefix + datetime.datetime.now().isoformat(sep=' ', timespec=timespec) + '.jpg'

def missedFrame(dir):
    folder = dir + str(datetime.date.today())
    file = folder + '/MissedFrames.txt'
    i = 0
    if os.path.exists(file):
        f = open(file, 'r')
        i = int(f.read())
        f.close()
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    f = open(file, "w")
    f.write(str(i+1))
    f.close()


#PrepOutputDir('test/', True)
#print(makedirandfile('./test/', 'wowSoWow', 'minutes', True))
