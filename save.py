import os

save_folder = './screenshot/'

def save(save_func, name, now):
    if not os.path.isdir(save_folder+name):
        os.makedirs(save_folder+name)
    save_func(save_folder+name+'/'+now.strftime('%Y_%m_%d_%H_%M_%S')+'.png')
