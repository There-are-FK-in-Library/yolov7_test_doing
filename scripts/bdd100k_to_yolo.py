#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os
import json


def search_file(data_dir, pattern=r'\.jpg$'):
    root_dir = os.path.abspath(data_dir)
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if re.search(pattern, f, re.I):
                abs_path = os.path.join(root, f)
                # print('new file %s' % absfn)
                yield abs_path


class Bdd2yolov5:
    def __init__(self):
        self.bdd100k_width = 1280
        self.bdd100k_height = 720
        # self.select_categorys = ["person", "car", "bus", "truck"]
        # self.cat2id = {
        #     "person": 0,
        #     "car": 1,
        #     "bus": 1,
        #     "truck": 1
        # }
        self.select_categorys = ["car","pedestrian", "truck","bus"]  # 要用到的类别名称
        self.cat2id = {

            "car": 0,
            'pedestrian':1,
            "truck": 2,
            "bus": 3,
        }


    def bdd2yolov5(self, path, save_txt_path):  # 输入一张图片的标签

        with open(path) as fp:
            j = json.load(fp)
            # if self._filter_by_attr(j['attributes']):  # 过滤掉晚上的图片
            #     return
            lines_dirs =""
            if SPLIT=="train":
                numbers_start=0
                numbers_end = 5000
            elif SPLIT=="val":
                numbers_start = 5001
                numbers_end = 6000
            else:
                numbers_start = 7001
                numbers_end = 8000

            for fr in j[numbers_start:numbers_end]:
                lines_dir="F:/yolov7_test_doing/BDD100k/images/{}/{}\n".format(SPLIT,fr["name"])
                lines_dirs +=lines_dir
                lines = ""
                dw = 1.0 / self.bdd100k_width
                dh = 1.0 / self.bdd100k_height
                for obj in fr["labels"]:
                    category = obj["category"]
                    # if (category == "traffic light"):
                    #     color = obj['attributes']['trafficLightColor']
                    #     category = "tf_" + color

                    if category in self.select_categorys:
                        idx = self.cat2id[category]
                        cx = (obj["box2d"]["x1"] + obj["box2d"]["x2"]) / 2.0
                        cy = (obj["box2d"]["y1"] + obj["box2d"]["y2"]) / 2.0
                        w = obj["box2d"]["x2"] - obj["box2d"]["x1"]
                        h = obj["box2d"]["y2"] - obj["box2d"]["y1"]
                        if w <= 0 or h <= 0:
                            continue
                        # if self._filter_by_box(w, h): # 过滤掉过于小的小目标
                        #     continue
                        # 根据图片尺寸进行归一化
                        cx, cy, w, h = cx * dw, cy * dh, w * dw, h * dh
                        line = f"{idx} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}\n"
                        lines += line
                if len(lines) != 0:
                    # 转换后的以*.txt结尾的标注文件放到指定目录save_txt_path位置
                    yolo_txt = fr["name"].replace(".jpg", ".txt")
                    # txt= yolo_txt.rsplit("\\", 1)[-1]
                    yolo_txt = os.path.join(save_txt_path,yolo_txt)
                    with open(yolo_txt, 'w') as fp2:
                        fp2.writelines(lines)
                    # print("%s has been dealt!" % path)

            if len(lines_dir) != 0:

                yolo_txt_train = "../BDD100k/{}.txt".format(SPLIT)
                with open(yolo_txt_train, 'w') as fp2:
                    fp2.writelines(lines_dirs)

SPLITs=["train","val"]
if __name__ == "__main__":
    for SPLIT in SPLITs:
        bdd_label_dir = "../BDD100k/train_label/det_train.json"
        save_txt_path = "../BDD100k/labels/{}".format(SPLIT)  # 指定转换后生成的文件存储的目录
        cvt = Bdd2yolov5()
        # for path in search_file(bdd_label_dir, r"\.json$"):
        cvt.bdd2yolov5(bdd_label_dir, save_txt_path)

