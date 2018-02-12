import chainer
from src.dataset.svhn import svhn
from src.preprocess.preprocess_svhn import PreprocessSVHN
from src.extension.learning_rate_scheduler import LearningRateScheduler
from src.extension.learning_rate_scheduler import ExponentialSchedule

batchsize = 128
dataset = svhn()
epoch = 160
preprocess = PreprocessSVHN()
lr = 1e-2
optimizer = chainer.optimizers.NesterovAG(lr)
extension = [(LearningRateScheduler(ExponentialSchedule(.1, (80, 120))), (1, 'iteration'))]
