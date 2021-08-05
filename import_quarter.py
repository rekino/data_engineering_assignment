import psycopg2
import sys, getopt

def import_impressions(file, quarter):
    pass

def import_clicks(file, quarter):
    pass

def import_conversions(file, quarter):
    pass

def main(argv):
   folder = ''
   quarter = ''
   try:
      opts, args = getopt.getopt(argv,"hd:q:",["folder=","quarter="])
   except getopt.GetoptError:
      print ('import_quarter.py -f <folder> -q <quarter>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('import_quarter.py -f <folder> -q <quarter>')
         sys.exit()
      elif opt in ("-f", "--folder"):
         folder = arg
      elif opt in ("-q", "--quarter"):
         quarter = arg


if __name__ == "__main__":
   main(sys.argv[1:])