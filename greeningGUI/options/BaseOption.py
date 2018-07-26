import os
from util import util
import torch

class BaseOption():
    def __init__(self):
        self.initialized=False
    
    def initialize(self, dataroot):
        self.dataroot=dataroot
        self.batchSize=1
        self.loadSize=512
        self.fineSize=512
        self.input_nc=3
        self.output_nc=3
        self.ngf=64
        self.ndf=64
        self.which_model_netD='basic'
        self.which_model_netG='resnet_9blocks'
        self.n_layers_D=3
        self.gpu_ids=['0']
        self.name='maps_cyclegan'
        self.dataset_mode=2
        self.model='cycle_gan'
        self.which_direction='BtoA'
        self.nThreads=1
#         self.checkpoints_dir='D:/checkpoints'
        self.checkpoints_dir=dataroot
        self.norm='instance'
        self.display_winsize=512
        self.display_id=1
        self.display_port=8097
        self.no_dropout=True
        self.max_dataset_size=1000000000
        self.resize_or_crop='resize_and_crop'
        self.init_type='normal'
        self.initialized=True
        
    def parse(self):
        if not self.initialized:
            self.initialize()
#         self.opt = self.parser.parse_args()
        self.isTrain = self.isTrain   # train or test

        str_ids = self.gpu_ids
        self.gpu_ids = []
        for str_id in str_ids:
            id = int(str_id)
            if id >= 0:
                self.gpu_ids.append(id)

        # set gpu ids
        if len(self.gpu_ids) > 0:
            torch.cuda.set_device(self.gpu_ids[0])

#         args = vars(self.opt)
# 
#         print('------------ Options -------------')
#         for k, v in sorted(args.items()):
#             print('%s: %s' % (str(k), str(v)))
#         print('-------------- End ----------------')

        # save to the disk
        expr_dir = os.path.join(self.checkpoints_dir, self.name)
        util.mkdirs(expr_dir)
        file_name = os.path.join(expr_dir, 'opt.txt')
        with open(file_name, 'w') as opt_file:
            opt_file.write('------------ Options -------------\n')
#             for k, v in sorted(args.items()):
#                 opt_file.write('%s: %s\n' % (str(k), str(v)))
#             opt_file.write('-------------- End ----------------\n')
#         return self.opt
        return 1










































