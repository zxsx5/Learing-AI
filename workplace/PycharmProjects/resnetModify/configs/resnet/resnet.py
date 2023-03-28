# @Time : 2023/3/9 11:10
# @Author : zhaogang
# @Email : zhaogang_1996@163.com
# @File : resnet.py
# @Software: PyCharm

_base_ = [
    'resnet50.py',
    'stanford_cars_bs8_448.py',
    'stanford_cars_bs8.py', 'default_runtime.py'
]

# use pre-train weight converted from https://github.com/Alibaba-MIIL/ImageNet21K # noqa
#checkpoint = 'https://download.openmmlab.com/mmclassification/v0/resnet/resnet50_3rdparty-mill_in21k_20220331-faac000b.pth'  # noqa
checkpoint = 'pretrain/resnet50_3rdparty-mill_in21k_20220331-faac000b.pth'
model = dict(
    type='ImageClassifier',
    backbone=dict(
        init_cfg=dict(
            type='Pretrained', checkpoint=checkpoint, prefix='backbone')),
    head=dict(num_classes=256, ))

log_config = dict(interval=50)
checkpoint_config = dict(
    interval=1, max_keep_ckpts=3)  # save last three checkpoints