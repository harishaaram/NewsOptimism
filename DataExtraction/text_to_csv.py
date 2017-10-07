import csv
import os


os.chdir('/home/harish/PycharmProjects/NewsOptimism/dataset/reuters/')
with open('xcel.csv', 'rb') as in_file:
    # stripped = (line.strip() for line in in_file)
    # lines = (line.split(",") for line in stripped if line)
    i = 0;
    for line in  in_file:
        if():
            break
        i = i+1
        print(line)
    # with open('log.csv', 'w') as out_file:
    #     for line in in_file:
    #         print(line)
    #             # writer.writerow(('title', 'intro'))
    #         out_file.write(line)
