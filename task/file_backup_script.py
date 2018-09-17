# 文件备份脚本
# 	要求：
# 		1、写明备份思路
# 		2、备份脚本
# 		3、脚本执行方法
# 		4、体现函数应用
#需要备份文件的目录
file_location='/root/scripts/master_file.py'
#备份的文件名
file_backup_location='/root/scripts/master_file1.py'
def backup_script(file_localtion,file_backup_location):
    with open(file_backup_location,"w") as d:
        #这里是为了确认源文件是否输入正确，如果正确的话直接执行try的语句,通过else返回最终结果。
        try:
            with open(file_localtion,"r") as s:
                for each_line in s:
                    line = each_line
                    #print(line)
                    d.write(line)
        except FileNotFoundError:
            print("请确认源文件是否输入正确！")
        else:
            print("%s 文件已备份已备份完成！" % file_backup_location)

if __name__ == "__main__":
    backup_script(file_location,file_backup_location)