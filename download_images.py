from datasets import load_dataset
import ipdb
import os

def download_images():
    with open('categories.txt') as fw:
        lines = fw.readlines()
        for line in lines:
            print(line)
            l = line.strip()
            meta_dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", f"raw_meta_{l}", split="full")
            for i in range(100):
                ipdb.set_trace()
                if len(meta_dataset[i]['images']['large']) > 0: 
                    img_name = meta_dataset[i]['images']['large'][0]
                    os.system(f"wget {img_name} -P images --no-check-certificate")

if __name__ == "__main__":
    download_images()
