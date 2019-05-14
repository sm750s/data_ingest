import sys
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: CountJPGs.py <logfile>"
        exit(-1)

    sc = SparkContext()
    sc.setLogLevel("WARN")

    print '##################################'
    print '#### Starting',sys.argv[0]
    print '##################################'

    logfile = sys.argv[1]
    wc = sc.textFile(logfile)\
        .filter(lambda line: ".jpg" in line)\
        .count()

    print '> Total count of JPG requests:',wc

    sc.stop()
