############################# LOGGING IN PYTHON ################################
###############################################################################
# Example_1: without formatting
# WAP to create a log file and write 'warning' & higher logging level messages

import logging  # import again (safe, no issue)

# Configure logging
# By default:
# - Level = WARNING
# - Output = console
# - File mode = append ('a')
#logging.basicConfig() #logging.basicConfig(level=logging.WARNING)
logging.basicConfig(
    filename="app.log",   # file name
    level=logging.DEBUG,  # capture all logs
    filemode='a'          # append (no overwrite)
)

print("logging in python demo_1")  # normal print (not logging)

# Logging messages:

# DEBUG → will NOT show (below WARNING level)
logging.debug("Harmless debug Message")

# INFO → will NOT show (below WARNING level)
logging.info("Just an information")

# WARNING → will show
logging.warning("Its a Warning")

# ERROR → will show
logging.error("Did you try to divide by zero")

# CRITICAL → will show
logging.critical("Internet is down")