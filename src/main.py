#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 11:18
# @Author  : Guangchen Jiang
# @Email   : guangchen98.jiang@gmail.com
# @File    : src/main.py
# @Software: PyCharm

import logging
import torch

import _logger

if __name__ == '__main__':
    trainer_logger = _logger.get_logger(name="torch", filename="../new.log", level=logging.DEBUG)
    trainer_logger.debug("debug")
    trainer_logger.info("info")
    trainer_logger.warning("warning")
    trainer_logger.error("error")
    trainer_logger.critical("critical")
    trainer_logger.info(f"Pytorch Version: {torch.__version__}")
