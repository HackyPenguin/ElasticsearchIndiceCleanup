import datetime
from elasticsearch import Elasticsearch
import elasticsearch


# arrays to be edited are below:
# this is a 30 day deletion period
Monthly_deletion = [
]

# this array contains all indices which  are cleared up after 14 days
fourtnightly_deletion = [
]



# variable
es = Elasticsearch("localhost:9200")


def days_to_delete(date=60):
    time = str((datetime.datetime.utcnow() + datetime.timedelta(date)))
    time = time.split(" ", 1)[0]
    time = time.replace("-", ".")
    return time


# if you wish to change where you are preforming maintance please change this
# variable
# please set the month deletion array to contain all indices you wish to clear
# every month ( 30 days)


def indice_deleter(index=None, time=None):
    for indice in index:
        try:
            print("deleting indice:" + indice + "-" + time)
            es.indices.delete(index=indice + "-" + time, request_timeout=30)
        except elasticsearch.TransportError:
            print("indice" + "-" + time + " does not exist")


# lets clear up monthly logs

indice_deleter(Monthly_deletion, days_to_delete(30))
# lets clear up fournightly indices
indice_deleter(fourtnightly_deletion, days_to_delete(14))


print("cleanup complete!")
