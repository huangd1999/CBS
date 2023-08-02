output_path=dataset

mkdir -p ${output_path}
echo 'Output path: '$output_path

# 164 problems, 21 per GPU if GPU=8
gpu_num=9
idx=0
for ((i = 0; i < $gpu_num; i++)); do
  gpu=$((i))
  ((index++))
  (
    python bif.py --task ${i}
  ) 
done