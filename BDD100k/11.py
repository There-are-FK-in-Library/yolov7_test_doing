import os
import pickle

import numpy as np
import matplotlib.pyplot as plt

# from model.evaluations import Meter


class DrawConfusionMatrix:
    def __init__(self, labels_name, normalize=True):
        """
        normalize：是否设元素为百分比形式
        """
        self.normalize = normalize
        self.labels_name = labels_name
        self.num_classes = len(labels_name)
        self.matrix = np.zeros((self.num_classes, self.num_classes), dtype="float32")

    def clear(self):
        self.matrix = np.zeros((self.num_classes, self.num_classes), dtype="float32")

    def update(self, predicts, labels):
        """
        :param predicts: 一维预测向量，eg：array([0,5,1,6,3,...],dtype=int64)
        :param labels:   一维标签向量：eg：array([0,5,0,6,2,...],dtype=int64)
        :return:
        """
        for predict, label in zip(predicts, labels):
            self.matrix[predict, label] += 1

    def getMatrix(self, normalize=True):
        """
        根据传入的normalize判断要进行percent的转换，
        如果normalize为True，则矩阵元素转换为百分比形式，
        如果normalize为False，则矩阵元素就为数量
        Returns:返回一个以百分比或者数量为元素的矩阵

        """
        if normalize:
            per_sum = self.matrix.sum(axis=1)  # 计算每行的和，用于百分比计算
            for i in range(self.num_classes):
                self.matrix[i] = (self.matrix[i] / per_sum[i])  # 百分比转换
            self.matrix = np.around(self.matrix, 2)  # 保留2位小数点
            self.matrix[np.isnan(self.matrix)] = 0  # 可能存在NaN，将其设为0
        return self.matrix

    def drawMatrix(self, data_name):
        self.matrix = self.getMatrix(self.normalize)
        plt.imshow(self.matrix, cmap=plt.cm.Blues)  # 仅画出颜色格子，没有值
        # plt.title("Normalized confusion matrix")  # title
        plt.xlabel("Predict label", fontsize=16)
        plt.ylabel("Truth label", fontsize=16)
        plt.yticks(range(self.num_classes), self.labels_name, size=16)  # y轴标签
        plt.xticks(range(self.num_classes), self.labels_name, size=16)  # x轴标签

        for x in range(self.num_classes):
            for y in range(self.num_classes):
                value = float(format('%.2f' % self.matrix[y, x]))  # 数值处理
                if x == y:
                    plt.text(x, y, value, verticalalignment='center', horizontalalignment='center', color='white',
                             size=16)  # 写值
                else:
                    plt.text(x, y, value, verticalalignment='center', horizontalalignment='center', color='black',
                             size=16)  # 写值

        plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域

        plt.colorbar()  # 色条
        save_path = './outputs/ConfusionMatrix/'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        plt.savefig(os.path.join(save_path, data_name + '.tif'), bbox_inches='tight')
        plt.close()
        # plt.show()


with open('./smic_back_apex_without_mask_depth3_2_newAUs.pkl',  'rb') as f:  # only AUs
    data = pickle.load(f)

Y_pred = data['meter'].Y_pred.tolist()
Y_true = data['meter'].Y_true.tolist()
matrix = np.zeros((3, 3), dtype="float32")
for predict, label in zip(Y_pred,Y_true):
    matrix[predict, label] += 1
