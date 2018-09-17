#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 文件或目录创建脚本
# 	要求：
# 		1、写明备份思路
# 		2、解释所应用模块
# 		3、备份脚本
# 		4、脚本执行方法
import os,shutil
#文件二使用os，和shutil达成备份复制的方法，以确保源文件存在是否为文件还是目录，
#并确保目标文件存在与否，不存在的话创建文件夹，已有文件的话执行覆盖命令，可继续修改。
#定义输入文件的位置
input_path="/root/my_python36/learnpy"
input_pathname, input_filename=os.path.split(input_path)
#定义输出文件夹的位置
output_path="/root/my_python36/testcp2/"+input_filename
output_pathname, output_filename = os.path.split(output_path)

if not os.path.exists(input_path):
    print("%s：指定文件夹或文件不存在！" % input_path)
elif not os.listdir(input_path):
    print("%s: 指定文件夹为空！" % input_path)
else:
    if not os.path.exists(output_pathname):
        print("%s文件夹不存在，正在为您创建%s文件夹" % (output_pathname,output_pathname))
        os.makedirs(output_pathname)
    else:
        if os.path.isdir(input_path):
            try:
                shutil.copytree(input_path,output_path)
            except FileExistsError:
                print("目标文件夹已存在，是否要覆盖？y/n")
                shutil.rmtree(output_path)
                shutil.copytree(input_path, output_path)
                print("目标文件夹已覆盖")
        elif os.path.isfile(output_path):
            shutil.copyfile(input_path,output_path)
        print("复制文件: %s ----------> %s" % (input_path, output_path))
