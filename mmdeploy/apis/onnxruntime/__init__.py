import importlib
import os.path as osp

from .init_plugins import get_ops_path
from .onnxruntime_utils import ORTWrapper

__all__ = ['get_ops_path', 'ORTWrapper']


def is_available():
    onnxruntime_op_path = get_ops_path()
    if not osp.exists(onnxruntime_op_path):
        return False
    return importlib.util.find_spec('onnxruntime') is not None