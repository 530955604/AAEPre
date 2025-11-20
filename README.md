AAEPre

AAEPre is a transfer learning model for predicting acidophilic and alkalophilic proteins by fine-tuning the pre-trained model MP-BERT.

🔧 Installation

AAEPre is implemented using the MindSpore deep learning framework and is optimized for Huawei Ascend 910 NPUs.

MindSpore installation guide (Ascend / CPU / GPU):
https://www.mindspore.cn/install/

We recommend using Docker to ensure a clean, reproducible, and isolated environment for MindSpore deployment.

The model builds upon the MP-BERT pre-trained weights, which were trained in our previous work using unlabeled UniProt protein sequences.
By fine-tuning this backbone, users can directly build accurate pH-classification models without re-training a pre-trained model from scratch.

🔍 Prediction
Input Format

AAEPre accepts input sequences in CSV format with the following structure:

id	seq
id1	MKTLLA…
id2	GHATST…

An example file is included:
/example/T6PP.csv

Model Checkpoints
Fine-tuned AAEPre models are available at:
DOI: 10.5281/zenodo.17656434

Running Predictions

Use the prediction script:

python pH_predict_MF2.py

Before running, you must update three paths inside the script:
data_url
Path to the input CSV file containing protein sequences.
load_checkpoint_url
Path to the fine-tuned AAEPre model checkpoint (.ckpt).
save_path
Output path where prediction results will be written (CSV format).

These fields are clearly marked in the script and should be modified according to your working directory.

📤 Output Format

The prediction script generates a CSV file containing:

id	seq	    dense_0	 dense_1	label
id1	MKTLLA…	0.77	   0.22    	0
id2	GHATST…	0.40	   0.60    	1

This table shows the model predictions for protein sequences. dense_0 and dense_1 are the predicted probabilities for each class. The label column is the true class: 0 indicates a basic (alkaline) protein, and 1 indicates an acidic protein.

📄 Citation

If you use AAEPre in your research, please cite the corresponding publication and model DOI:

DOI: 10.5281/zenodo.17656434

