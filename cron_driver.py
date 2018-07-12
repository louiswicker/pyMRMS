#!/usr/bin/env python

from apscheduler.schedulers.blocking import BlockingScheduler
import time
import os
import sys
import datetime

def run_mrms():

    cmd = "/work/wicker/REALTIME/pyMRMS/cron_prep_mrms.py >& /work/wicker/REALTIME/pyMRMS/log_prep_mrms.txt &"

    print(" Cmd: %s" % (cmd))

    ret = os.system("%s" % cmd)
    if ret != 0:
        print("\n ============================================================================")
        print("\n CRON_DRIVE did not run correctly")
        print("\n ============================================================================")

schedular = BlockingScheduler()

# schedule the prep_mrms...

job = schedular.add_job(run_mrms, trigger='cron', hour='10', minute='30')

time.sleep(300)
job.unschedule()

