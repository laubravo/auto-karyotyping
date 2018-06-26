from PIL import Image
import os as os
import numpy as np

in_dir = '/home/laubravo/Documents/cariotipos/MFISH_split/annotations'
out_dir = '/home/laubravo/Documents/cariotipos/MFISH_split_binaries/train/annotations'

#filename = os.path.join(in_dir, 'A0101.png')

def getBinaryIms(im, out_path, org_name):
    """ im: image with one channel 
        out_path: path to save the image
        org_name: original name of the image 
        ann_num: is the annotation number """
    imp = np.array(im)

    for chromosome in range(1,25):
        binaryIm = [imp == chromosome]
        binaryIm = binaryIm[0].reshape(im.size[1], im.size[0])*255
        binaryIm = Image.fromarray(binaryIm.astype('uint8'),'L')
        ann_id = chromosome
        if chromosome < 10:
            new_name = os.path.join(out_path, org_name[:-4] + '_c0' + str(chromosome) + '_' + str(ann_id) + '.png')
        else:
            new_name = os.path.join(out_path, org_name[:-4] + '_c' + str(chromosome) + '_' + str(ann_id) + '.png')
        binaryIm.save(new_name, 'png')


def main():
    files = os.listdir(in_dir)
    files.sort()
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for f in files:
        im = Image.open(os.path.join(in_dir,f))
        getBinaryIms(im, out_dir, f)


#    print(np.unique(np.reshape(im,-1)))

if __name__ == "__main__":
    main()