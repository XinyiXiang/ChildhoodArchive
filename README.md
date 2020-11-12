# ChildhoodArchive

## Reproduce using GitHub Desktop
- Click on the green ```Code``` button
- Select open with GitHub desktop
- See below
## OR reproduce with zip file
- Click on the green ```Code``` button
- Select download zip files from the dropdown menu
- Unzip in Downloads
- Open the project with VS Code Studio
- Press control with ~ key to summon up a new terminal
- Run ```python3 run_classifier.py --task_name=cola --do_train=true --do_eval=true --do_predict=true --data_dir=/Users/vic/Documents/GitHub/bert/datasets --vocab_file=./uncased_L-12_H-768_A-12/vocab.txt --bert_config_file=./uncased_L-12_H-768_A-12/bert_config.json --init_checkpoint=./uncased_L-12_H-768_A-12/bert_model.ckpt.index --max_seq_length=400 --train_batch_size=8 --learning_rate=2e-5 --num_train_epochs=3.0 --output_dir=./bert_output/ --do_lower_case=True```
- Install any missing module as reminded
