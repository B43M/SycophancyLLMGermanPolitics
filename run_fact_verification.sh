#! /bin/bash
set -ex

pip install -r requirements.txt
python scripts/model.py \
  --model_name_or_path  tiiuae/falcon-180b-chat\
  --tasks_names text-generation \
  --max_seq_length 256 \
  --per_device_train_batch_size 8 \
  --per_device_eval_batch_size 128 \
  --learning_rate 2e-5 \
  --max_steps 20000 \
  --save_step 4000 \
  --overwrite_cache \
  --output_dir results/answers \
  "$@"
#--do_train
  #--fp16 \
  #--test_tasks vitc_real vitc_synthetic \
  #--do_predict \
  #--model_name_or_path albert-base-v2 \
  #--do_eval \
#export PYTHONPATH="${PYTHONPATH}:${PWD}/Explainable_NLP/"
