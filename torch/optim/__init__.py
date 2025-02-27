"""
:mod:`torch.optim` is a package implementing various optimization algorithms.

Most commonly used methods are already supported, and the interface is general
enough, so that more sophisticated ones can also be easily integrated in the
future.
"""

from .adadelta import Adadelta
from .adagrad import Adagrad
from .adam import Adam
from .adamw import AdamW
from .sparse_adam import SparseAdam
from .adamax import Adamax
from .asgd import ASGD
from .sgd import SGD
from .radam import RAdam
from .rprop import Rprop
from .core import CoRe
from .rmsprop import RMSprop
from .optimizer import Optimizer
from .nadam import NAdam
from .lbfgs import LBFGS
from . import lr_scheduler
from . import swa_utils

del adadelta
del adagrad
del adam
del adamw
del sparse_adam
del adamax
del asgd
del sgd
del radam
del rprop
del core
del rmsprop
del optimizer
del nadam
del lbfgs
