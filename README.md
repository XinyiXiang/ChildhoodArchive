# ChildhoodArchive

## GitHub Desktop
- Click on the green ```Code``` button
- Select open with GitHub desktop
- See below


## ZIP file
- Click on the green ```Code``` button
- Select download zip files from the dropdown menu
- Unzip in Downloads
- Open the project with VS Code Studio
- Press control with ~ key to summon up a new terminal
- Run

```
python3 run_classifier.py --task_name=cola --do_train=true --do_eval=true --do_predict=true --data_dir=/Users/vic/Documents/GitHub/bert/datasets --vocab_file=/Users/vic/Downloads/uncased_L-12_H-768_A-12/vocab.txt --bert_config_file=/Users/vic/Downloads/uncased_L-12_H-768_A-12/bert_config.json --init_checkpoint=/Users/vic/Downloads/uncased_L-12_H-768_A-12/bert_model.ckpt.index --max_seq_length=400 --train_batch_size=8 --learning_rate=2e-5 --num_train_epochs=3.0 --output_dir=/Users/vic/Documents/GitHub/bert/bert_output --do_lower_case=True
```


Please use absolute path as above indicated

- Install any missing module

## Convert docx file to txt
-Download and move the docx2txt.sh shell script to the same directory as all ```.docx``` files
-Then type in command line/terminal```make docx2txt```


You should see the following lines : 

cat docx2txt.sh >docx2txt 

chmod a+x docx2txt


-Convert .docx files into .txt
```
docx2txt TAT11P46.docx
```
Replace the file names as needed, a .txt file with the same file name should apppear in the directory

-Extract interview question texts
```
grep "Q" < TAT11P46.txt > Q_TAT11P46.txt
```

Replace the file names as needed
-Extract interview answer texts
```
grep "A" < TAT11P46.txt > A_TAT11P46.txt
```

Replace the file names as needed
