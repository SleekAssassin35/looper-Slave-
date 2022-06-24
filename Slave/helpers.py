from timeloop.exceptions import ServiceExit

[[--// OBL //-- ]]

def service_shutdown(signum, frame):
    raise ServiceExit
