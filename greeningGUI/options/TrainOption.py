from options.BaseOption import BaseOption

class TrainOption(BaseOption):
    def __init__(self, dataroot=None, continue_train=False):
        BaseOption.initialize(self, dataroot)
        self.display_freq=100
        self.display_single_pane_ncols=0
        self.update_html_freq=1000
        self.print_freq=100
        self.save_latest_freq=1000
        self.save_epoch_freq=1
        self.continue_train=continue_train
        self.epoch_count=1
        self.phase='train'
        self.which_epoch='latest'
        self.niter=100
        self.niter_decay=100
        self.beta1=0.5
        self.lr=0.0002
        self.no_lsgan=True
        self.lambda_A=10.0
        self.lambda_B=10.0
        self.pool_size=50
        self.no_html=False
        self.lr_policy='lambda'
        self.lr_decay_iters=50
        self.identity=0.5
        self.no_flip=False
        self.serial_batches=False
        self.isTrain = True
        
