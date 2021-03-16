bind = '0.0.0.0:8080'  # socket
backlog = 2048  # número de conexões pendentes

workers = 2  # numero de processos que deve manter-se ativo para lidar com solicitações.
worker_connections = 300 #número máximo de clientes simultâneos que um único processo pode controlar 1 - 1000
keepalive = 2  # O número de segundos de espera para a próxima solicitação em uma conexão HTTP 
threads = 5

spew = False

errorlog = 'log.txt'
# loglevel = 'info' #"debug", "info", "warning", "error", "critical"
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
