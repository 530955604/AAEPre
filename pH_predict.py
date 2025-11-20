import os
import pandas as pd

model="AAEPre"
for fold in range(6):
    save_path = "/example/results/"+str(fold)

    cmd="python run_classification_correlation_2.py" \
    " --config_path config_2048.yaml " \
    "--do_predict True --description classification " \
    "--num_class 2 " \
    "--vocab_file  /data4/fanlingxi/generate_code/ph_model/2-0818/vocab_v2.txt " \
    "--device_id id "
    "--return_csv True " \
    "--data_url /example/predict_data.csv " \  
    "--load_checkpoint_url /model/"+str(model)+"/fold_"+str(fold)+"/saved_models/Best_Model.ckpt " \
    "--output_url "+save_path
    print(cmd)
    os.system(cmd)
dfs = []
prefix = None

for i in range(6):
    folder = f"/example/results/fold_{i}"
    for fname in os.listdir(folder):
        if fname.endswith("_predict_result.csv"):
            if prefix is None:
                prefix = fname.replace("_predict_result.csv", "")

            path = os.path.join(folder, fname)
            df = pd.read_csv(path)
            dfs.append(df)
            print(f"Loaded: {path}")

concat_df = pd.concat(dfs)

agg_df = concat_df.groupby(['id', 'seq'], as_index=False).agg({
    'dense_0': 'mean',
    'dense_1': 'mean'
})
agg_df['label'] = (agg_df['dense_1'] > agg_df['dense_0']).astype(int)

output_name = f"/example/results/{prefix}_results.csv"
agg_df.to_csv(output_name, index=False)
print(f"{output_name} is Done! ")


