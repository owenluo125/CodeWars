# https://www.codewars.com/kata/54fdaa4a50f167b5c000005f/python

def get_status(is_busy):
    status = {}
    if is_busy:
        status["status"] = "busy"
    else:
        status["status"] = "available"
    return status
