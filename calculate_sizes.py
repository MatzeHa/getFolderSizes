import os


def calculate_sizes(app):
    folders = []
    app_root = app.path.get()
    app.write_to_txt_results(app_root)
    for _dir in os.listdir(app_root):
        folders.append(os.path.join(app_root, _dir))
    print(folders)

    print("Start Counting")
    for folder in folders:
        print("FOLDER")
        print(folder)
        dir_size = 0
        for root, dirs, files in os.walk(folder, topdown=True):
            print(root)
            for file in files:
                f_path = os.path.join(root, file)
                file_size = os.stat(f_path).st_size
                dir_size += file_size
        print(dir_size)
        dir_size_mb = dir_size / (1024*1024)
        app.write_to_txt_results(folder + " ---> " + str(dir_size_mb))
