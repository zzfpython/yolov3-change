from flyai.train_helper import submit, upload_data, download, sava_train_model

# 遇到问题不要着急，添加小姐姐微信
# train_name: 提交训练的名字,推荐使用英文，不要带特殊字符
# code_path: 提交训练的代码位置，不写就是当前代码目录，也可以上传zip文件
# cmd: 在服务器上要执行的命令，多个命令可以用 && 拼接
# 如：pip install -i https://pypi.flyai.com/simple keras && python train.py -e=10 -b=30 -lr=0.0003
# 会把当前submit所在的代码目录提交，cmd可以自己编写，GPU上使用python开头即可
# submit("train_yolov3", cmd="python train.py --data data/coco.data --weights '' --cfg cfg/yolov3-cbam.cfg")

# 另一种提交方式，提交代码压缩包,目前支持zip格式的压缩包,代码会自动解压到运行目录下
# submit("train_yolov3",cmd="python train.py --data data/coco.data --weights '' --cfg cfg/yolov3-cbam.cfg")
submit("train_yolov3",cmd="python train.py --data data/data/coco.data --weights '' --cfg cfg/yolov3-cbam.cfg")
# sava_train_model(model_file="./train_yolov3/yolov3/weights/best.pt", dir_name="/model", overwrite=False)