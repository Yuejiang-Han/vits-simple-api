manual_seed = 42
model_source = "bert-base-chinese"
window_size = 32
num_workers = 1
use_mask = True
use_conditional = True
param_conditional = {
    "bias": True,
    "char-linear": True,
    "pos-linear": False,
    "char+pos-second": True,
}

batch_size = 256
use_pos = True
param_pos = {
    "weight": 0.1,
    "pos_joint_training": True,
}
