# pip install --upgrade aligo

from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()  # 第一次使用，会弹出二维码，供扫描登录
    user = ali.get_user()  # 获取用户信息
    ll = ali.get_file_list()  # 获取网盘根目录文件列表
    # 遍历文件列表
    for file in ll:
        print(file.file_id, file.name, file.type)

    # 上传文件
    ali.upload_file('***.txt')
    # 下载文件
    ali.download_files([ali.get_file_by_path('***.tar.gz')])
