import psycopg2
import sys, getopt
import logging
import csv

def import_impressions(cur, file, quarter):
    pass

def import_clicks(cur, file, quarter):
    pass

def import_conversions(cur, file, quarter):
    pass

def main(argv):
    folder = ''
    quarter = ''

    try:
        opts, _ = getopt.getopt(argv,"hf:q:",["folder=","quarter="])
    except getopt.GetoptError:
        print ('usage: import_quarter.py -f <folder> -q <quarter>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('import_quarter.py -f <folder> -q <quarter>')
            sys.exit()
        elif opt in ("-f", "--folder"):
            folder = arg
        elif opt in ("-q", "--quarter"):
            quarter = arg

    if folder == '' or quarter == '':
        print ('usage: import_quarter.py -f <folder> -q <quarter>')
        sys.exit(2)

    print(f'importing folder {folder} with quarter {quarter}')

    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="db", port="5432")

    cur = conn.cursor()

    with open(f'{folder}/impressions_{quarter}.csv') as impressions:
        import_impressions(cur, impressions, quarter)

    with open(f'{folder}/clicks_{quarter}.csv') as clicks:
        import_clicks(cur, clicks, quarter)

    with open(f'{folder}/conversions_{quarter}.csv') as conversions:
        import_conversions(cur, conversions, quarter)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', filename='import_quarter.log', encoding='utf-8', level=logging.DEBUG)
    main(sys.argv[1:])