# @Time : 2023/3/16 11:46
# @Author : zhaogang
# @Email : zhaogang_1996@163.com
# @File : split_caltech256.py.py
# @Software: PyCharm


import os
import shutil
from sklearn.model_selection import train_test_split

def split_dataset(dataset_path, train_path, test_path, test_size=0.2, random_seed=42):
    if not os.path.exists(train_path):
        os.makedirs(train_path)

    if not os.path.exists(test_path):
        os.makedirs(test_path)

    folders = [folder for folder in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, folder))]

    for folder in folders:
        class_path = os.path.join(dataset_path, folder)
        images = os.listdir(class_path)

        if len(images) == 0:
            print(f"类别 {folder} 中没有图像文件，已跳过。")
            continue

        train_images, test_images = train_test_split(images, test_size=test_size, random_state=random_seed)

        train_class_path = os.path.join(train_path, folder)
        test_class_path = os.path.join(test_path, folder)

        if not os.path.exists(train_class_path):
            os.makedirs(train_class_path)

        if not os.path.exists(test_class_path):
            os.makedirs(test_class_path)

        for image in train_images:
            try:
                shutil.copy(os.path.join(class_path, image), os.path.join(train_class_path, image))
            except PermissionError:
                print(f"无法复制图像 {image} 到训练集：权限错误。已跳过。")

        for image in test_images:
            try:
                shutil.copy(os.path.join(class_path, image), os.path.join(test_class_path, image))
            except PermissionError:
                print(f"无法复制图像 {image} 到测试集：权限错误。已跳过。")

if __name__ == "__main__":
    dataset_path = "E:\\workplace\\PycharmProjects\\resnetModify\\DataSet_process\\Caltech 256"
    train_path = "E:\\workplace\\PycharmProjects\\resnetModify\\DataSet_process\\train"
    test_path = "E:\\workplace\\PycharmProjects\\resnetModify\\DataSet_process\\test"

    split_dataset(dataset_path, train_path, test_path)

