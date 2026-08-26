import logging
from py_template.validacion import parsear_valor

logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(name)s: %(message)s")
log = logging.getLogger(__name__)

log.info("Arrancando")
parsear_valor("abc")