# -*- coding: UTF-8 -*-
#author：zhongqin
import logging
import os
import time

import read_config

cf = read_config.ReadConfig()

class Logging:

    def logger(self, test_case_Id, moudle, test_case_name, result):
        '''日志   将结果写入日志文件'''
        status = ""
        if result:
            status = "PASS"
        else:
            status = "FAIL"

        date = time.strftime('%Y%m%d', time.localtime())  # 获取作为log文件名的日期格式
        dir_path = os.path.join(read_config.abs_path, "results\logfile\\")

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        file_path = dir_path + date + ".txt"
        cur_time = time.strftime('%Y-%m-%d %X', time.localtime())
        content = test_case_Id + " , " + moudle + " , " + test_case_name + " , " + str(status) + " , " + cur_time + "\n"
        ff = open(file_path, "a+")
        ff.write(content)
        ff.close()
        print "%s %s %s用例记录log成功" % (test_case_Id, moudle, test_case_name)

    def logStep(self, log_info):
        log_filename = "outPut_" + time.strftime('%Y%m%d', time.localtime()) + ".log"
        result_path = os.path.join(read_config.abs_path, "results\logSteps\\")

        if os.path.exists(result_path) is False:
            os.makedirs(result_path)

        log_path = os.path.join(result_path, log_filename)
        logging.basicConfig(filename=log_path, level=logging.INFO)
        logging.info(time.strftime('%Y-%m-%d %X', time.localtime()) + " - "+log_info)

if __name__ == "__main__":
    log = Logging()
    log.logStep("haha")