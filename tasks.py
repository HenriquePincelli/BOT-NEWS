from RPA_APP.bots import bot_aljazeera
from robocorp.tasks import task
import sys
import json


@task
def init_rpa():
    try:
        bot_aljazeera()
    except Exception as e:
            # >>>>>>>>>Tracing the Error>>>>>>>>>
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'line_number': exc_traceback.tb_lineno,
                'function_name': exc_traceback.tb_frame.f_code.co_name,
                'exception_type': exc_type.__name__,
                'exception_message': str(exc_value)
            }
            print("=-==-==-=ERROR=-==-==-=")
            print(traceback_details)
            print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            print({"status": False, "msg": json.dumps(traceback_details)})
    finally:
        # A place for teardown and cleanups. (Playwright handles browser closing)
        print("Automation finished!")
