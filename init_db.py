import psycopg2

print('Begin migration...')

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="db", port="5432")
print('Opened database successfully')

cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS conversions,clicks,impressions;''')

cur.execute('''CREATE TABLE impressions
      (banner_id    INT,
       campaign_id  INT,
       PRIMARY KEY (banner_id,campaign_id));''')

cur.execute('''CREATE TABLE clicks
      (click_id         INT PRIMARY KEY,
       banner_id        INT,
       campaign_id      INT,
       quarter          INT NOT NULL,
       FOREIGN KEY (banner_id,campaign_id) REFERENCES impressions (banner_id,campaign_id));''')

cur.execute('''CREATE TABLE conversions
      (conversion_id    INT PRIMARY KEY,
       click_id         INT,
       revenue          FLOAT NOT NULL,
       FOREIGN KEY (click_id) REFERENCES clicks (click_id));''')

print('Tables created successfully')

conn.commit()
conn.close()