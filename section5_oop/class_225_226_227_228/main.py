from log import LogFileMixin
from eletronic import Smartphone

log_file = LogFileMixin()
log_file.log_success('Raising Success')

galaxy = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy.turn_on()
iphone.turn_off()