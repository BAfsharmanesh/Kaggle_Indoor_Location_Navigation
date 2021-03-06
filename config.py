class Config():
    DATA_DIR = '../input/indoorunifiedwifids'
    SAVE_DIR = './save'
    
    seed = 42
    epochs = 300
    num_wifi_feats = 20
    fold_num = 5
    train_batch_size = 256
    val_batch_size = 256
    num_workers = 16
    device = 'gpu'
    neptune = True
    lr = 5e-3


