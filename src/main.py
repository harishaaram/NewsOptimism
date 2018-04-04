import DataPreperation as dp
from storeData import *
import shutil as SH

import os
yourpath = '/home/harish/PycharmProjects/NewsOptimism/dataset/Nov2017'




def main():
    count = 0
    ls = [] #list of links
    for root, dirs, files in os.walk(yourpath, topdown=False):

        for name in files:
            count += 1
            ls.append(str(os.path.join(root, name)))
    print(ls)
        # for name in dirs:
        #
        #     print(os.path.join(root, name))

    for l in ls:
        print(dp.collectWords_perNewsMedia(l))
        break

if __name__ == '__main__':
    main()
