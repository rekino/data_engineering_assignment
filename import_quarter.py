import psycopg2
import sys, getopt
import logging
import csv

def import_impressions(conn, file, quarter):
    cur = conn.cursor()
    reader = csv.reader(file)
    reader.__next__() # ignoring the first line
    count = 0
    for i, row in enumerate(reader):
        if i % 100 == 0:
            conn.commit()
        try:
            cur.execute(f'''SELECT 1 FROM impressions WHERE banner_id={row[0]} AND campaign_id={row[1]}''')
            query = cur.fetchall()

            duplicate = False
            for _ in query:
                duplicate = True
                break

            if duplicate:
                logging.warning(f'duplicate impression in {file.name} line {i+2}: ({row[0]}, {row[1]})')
                continue

            cur.execute(f'''INSERT INTO impressions (banner_id,campaign_id) VALUES ({row[0]},{row[1]})''')

            count += 1
        except Exception as error:
            logging.error(f'error in importing impression in {file.name} line {i+2}: {error}')
            conn.commit()
    conn.commit()
    print(f'imported {count} of {i+1} impressions')

def import_clicks(conn, file, quarter):
    cur = conn.cursor()
    reader = csv.reader(file)
    reader.__next__() # ignoring the first line
    count = 0
    for i, row in enumerate(reader):
        if i % 100 == 0:
            conn.commit()
        try:
            cur.execute(f'''SELECT 1 FROM clicks WHERE click_id={row[0]}''')
            query = cur.fetchall()

            duplicate = False
            for _ in query:
                duplicate = True
                break

            if duplicate:
                logging.warning(f'duplicate click in {file.name} line {i+2}: ({row[0]}, {row[1]}, {row[2]})')
                continue

            cur.execute(f'''INSERT INTO clicks (click_id,banner_id,campaign_id,quarter) VALUES ({row[0]},{row[1]},{row[2]},{quarter})''')

            count += 1
        except Exception as error:
            logging.error(f'error in importing click in {file.name} line {i+2}: {error}')
            conn.commit()
    conn.commit()
    print(f'imported {count} of {i+1} clicks')

def import_conversions(conn, file, quarter):
    cur = conn.cursor()
    reader = csv.reader(file)
    reader.__next__() # ignoring the first line
    count = 0
    for i, row in enumerate(reader):
        if i % 100 == 0:
            conn.commit()
        try:
            cur.execute(f'''SELECT 1 FROM conversions WHERE conversion_id={row[0]}''')
            query = cur.fetchall()

            duplicate = False
            for _ in query:
                duplicate = True
                break

            if duplicate:
                logging.warning(f'duplicate conversion in {file.name} line {i+2}: ({row[0]}, {row[1]}, {row[2]})')
                continue

            cur.execute(f'''INSERT INTO conversions (conversion_id,click_id,revenue) VALUES ({row[0]},{row[1]},{row[2]})''')

            count += 1
        except Exception as error:
            logging.error(f'error in importing conversion in {file.name} line {i+2}: {error}')
            conn.commit()
    conn.commit()
    print(f'imported {count} of {i+1} conversions')

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

    with open(f'{folder}/impressions_{quarter}.csv') as impressions:
        import_impressions(conn, impressions, quarter)

    with open(f'{folder}/clicks_{quarter}.csv') as clicks:
        import_clicks(conn, clicks, quarter)

    with open(f'{folder}/conversions_{quarter}.csv') as conversions:
        import_conversions(conn, conversions, quarter)

    conn.close()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', filename='import_quarter.log', encoding='utf-8', level=logging.DEBUG)
    main(sys.argv[1:])