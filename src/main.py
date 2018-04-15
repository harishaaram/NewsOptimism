import DataPreperation as dp
import storeData as sd

import os
yourpath = '/home/harish/PycharmProjects/NewsOptimism/dataset/Nov2017'

json_data_dir = '/home/harish/PycharmProjects/NewsOptimism/json_data'


def main():
    count = 0
    ls = [] #list of links
    for root, dirs, files in os.walk(yourpath, topdown=False):

        for name in files:
            count += 1
            ls.append(str(os.path.join(root, name)))


    for l in ls:
        #getting json file name to store our dictionary
        fname = l.split('.')[0].split('/')
        date_val = fname[-2]
        file_name = date_val + ".json"
        file_dir = os.path.join(json_data_dir,fname[-1], file_name)


        if not os.path.isfile(file_dir):
            All_Words_article = dp.collectWords_perNewsMedia(l)
            sd.json_storage(All_Words_article, file_dir,date_val)


if __name__ == '__main__':
    main()
