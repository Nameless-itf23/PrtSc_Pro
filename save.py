import os
import clipboard

prtsc_folder = 'C:/Users/noname/Pictures/PrtSc_Pro'

def save(save_func, name, now):
    save_folder = prtsc_folder + '/' + name
    if not os.path.isdir(save_folder):
        os.makedirs(save_folder)
    save_path = save_folder + '/' + now.strftime('%Y_%m_%d_%H_%M_%S')+'.png'
    save_func(save_path)
    clipboard.save_img_to_clipboard(save_path)
