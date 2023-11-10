import os

prtsc_folder = 'screenshot'

def save(save_func, name, now):
    save_folder = prtsc_folder + '/' + name
    if not os.path.isdir(save_folder):
        os.makedirs(save_folder)
    save_func(save_folder + '/' + now.strftime('%Y_%m_%d_%H_%M_%S')+'.png')
