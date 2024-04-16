import os
import zipfile
import urllib.request

# Download/unzip labels
output_dir = '../coco'  # unzip directory
url = 'https://github.com/ultralytics/yolov5/releases/download/v1.0/'
filename = 'coco2017labels-segments.zip'  # or 'coco2017labels.zip', 68 MB
print('Downloading', url + filename, '...')
urllib.request.urlretrieve(url + filename, filename)
with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall(output_dir)
os.remove(filename)

# Download/unzip images
output_dir = '../coco/images'  # unzip directory
url = 'http://images.cocodataset.org/zips/'
# filenames = ['train2017.zip', 'val2017.zip', 'test2017.zip']  # 19G, 1G, 7G respectively (optional)
filenames = ['val2017.zip']  # 19G, 1G, 7G respectively (optional)
for filename in filenames:
    print('Downloading', url + filename, '...')
    urllib.request.urlretrieve(url + filename, filename)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    os.remove(filename)

print('Download and extraction completed.')