# change only the name without suffix
import os
import os.path


def load_data(dataPath, suffix, datas):
    for root, dirs, files in os.walk(dataPath):
        for filename in files:
            if filename.find(suffix) != -1:
                datas.append(os.path.join(root, filename))


if __name__ == "__main__":
    # 1. get all the data names
    dataPath = "kk"
    suffix = ".x2m"
    datas = []
    load_data(dataPath, suffix, datas)
    print('load datas:')
    print(datas)
    # 2. sort
    sorted_datas = sorted(datas, key=lambda x: os.path.getmtime(x))
    print('sorted datas with modified time')
    print(sorted_datas)
    # 3. rename
    for n in range(len(sorted_datas)):
        print('mtime = ' + str(os.path.getmtime(sorted_datas[n])))
        last_seg = sorted_datas[n].rfind('/')
        new_path = sorted_datas[n][:last_seg]
        os.rename(sorted_datas[n], os.path.join(new_path, str(n) + suffix))
        print(new_path)
    print("all done")