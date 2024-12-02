import os
import sys

def runtime_init():
    if hasattr(sys, '_MEIPASS'):
        # 如果是打包后的环境
        os.environ['PYTHONPATH'] = sys._MEIPASS
        os.environ['TCL_LIBRARY'] = os.path.join(sys._MEIPASS, 'tcl')
        os.environ['TK_LIBRARY'] = os.path.join(sys._MEIPASS, 'tk')

runtime_init() 