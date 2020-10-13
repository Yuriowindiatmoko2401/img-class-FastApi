# img-class-FastApi

img-class-FastApi most reference from [FastImageClassification](https://github.com/CVxTz/FastImageClassification)

- after download all images using chrome extension download all image

- save each zip file into raw_data/all_labels

- extract files there and naming each folder based on labels that you decide (it will be your labels class name)

- create unique name in those folders
 
      python helper_utils/randomfilerenamer.py raw_data/all_labels/1_tugu_jogja 

- captioning image
- read file  
- python read_file.py <folder_image> <output_readfile>

      python script_utils/read_file.py ../1_tugu_jogja name_file.txt

- mapping anotasi
- python mapping_anotasi.py <list_anotasi manual> <output_readfile> <output caption json>

```bash
python script_utils/mapping_anotasi.py list_anotasi.txt name_file.txt caption_tugu.json
```
  
- manually crosscheck
http://jsonviewer.stack.hu/

- Finally merge all captions and image into each of it's folder

