#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    # 所有训练标签的文件夹路径
    path_label_files_train = "/home/wsy/data/BDD100K/dataSets/labels/train"
    path_label_files_val = "/home/wsy/data/BDD100K/dataSets/labels/val"
    # single_label_path = "/home/wsy/code/yolov5-6.1/BDD100_data/labels_traffic_sign_train/468724af-6af83d8d.txt"
    # 训练图像数据集和验证图像数据集的文件夹路径
    train_imageSet_file_path = "/home/wsy/data/BDD100K/dataSets/images/train"
    val_imageSet_file_path = "/home/wsy/data/BDD100K/dataSets/images/val"
    # print(labels_lists)
    # 存储训练图像、验证图像数据集路径的文件
    train_image_lists = "/home/wsy/code/yolov5-6.1/BDD100_data/ImageSets_path/train.txt"
    val_image_lists = "/home/wsy/code/yolov5-6.1/BDD100_data/ImageSets_path/val.txt"
    if not os.path.exists(train_image_lists):
        os.system(r"touch {}".format(train_image_lists))
    if not os.path.exists(val_image_lists):
        os.system(r"touch {}".format(val_image_lists))

    labels_train_lists = os.listdir(path_label_files_train)  # 读取所有标签文件名并存在一个列表当中
    labels_val_lists = os.listdir(path_label_files_val)  # 读取所有标签文件名并存在一个列表当中

    # 训练集标签集合文件生成
    with open(train_image_lists, 'w') as file_train:
        for label in labels_train_lists:
            label_name = label.rsplit("/", 1)[-1].split(".")[0] + ".jpg"
            line_name = os.path.join(train_imageSet_file_path, label_name)
            file_train.write(line_name) # 在txt文件中写入一行内容
            file_train.write("\n") # 换行

    # 验证集标签集合文件生成
    with open(val_image_lists, 'w') as file_val:
        for label2 in labels_val_lists:
            label_name2 = label2.rsplit("/", 1)[-1].split(".")[0] + ".jpg"
            line_name2 = os.path.join(val_imageSet_file_path, label_name2)
            file_val.write(line_name2) # 在txt文件中写入一行内容
            file_val.write("\n") # 换行

