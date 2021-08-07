DROP TABLE IF EXISTS conversions CASCADE;
DROP TABLE IF EXISTS clicks CASCADE;
DROP TABLE IF EXISTS impressions CASCADE;

CREATE TABLE impressions(
    banner_id    INT,
    campaign_id  INT,
    PRIMARY KEY (banner_id,campaign_id)
);

CREATE TABLE clicks(
    click_id         INT PRIMARY KEY,
    banner_id        INT,
    campaign_id      INT,
    quarter          INT NOT NULL,
    FOREIGN KEY (banner_id,campaign_id) REFERENCES impressions (banner_id,campaign_id)
);

CREATE TABLE conversions(
    conversion_id    INT PRIMARY KEY,
    click_id         INT,
    revenue          FLOAT NOT NULL,
    FOREIGN KEY (click_id) REFERENCES clicks (click_id)
);

CREATE VIEW banners_with_conversions_q1 AS
SELECT 
  impressions.campaign_id AS campaign_id, 
  impressions.banner_id AS banner_id, 
  COUNT(clicks.click_id) AS clicks, 
  COUNT(conversions.conversion_id) AS conversions 
FROM impressions 
LEFT JOIN clicks ON impressions.campaign_id = clicks.campaign_id AND impressions.banner_id = clicks.banner_id
LEFT JOIN conversions ON clicks.click_id = conversions.click_id
WHERE clicks.quarter = 1
GROUP BY impressions.campaign_id,impressions.banner_id;


CREATE VIEW banners_with_conversions_q2 AS
SELECT 
  impressions.campaign_id AS campaign_id, 
  impressions.banner_id AS banner_id, 
  COUNT(clicks.click_id) AS clicks, 
  COUNT(conversions.conversion_id) AS conversions 
FROM impressions 
LEFT JOIN clicks ON impressions.campaign_id = clicks.campaign_id AND impressions.banner_id = clicks.banner_id
LEFT JOIN conversions ON clicks.click_id = conversions.click_id
WHERE clicks.quarter = 2
GROUP BY impressions.campaign_id,impressions.banner_id;

CREATE VIEW banners_with_conversions_q3 AS
SELECT 
  impressions.campaign_id AS campaign_id, 
  impressions.banner_id AS banner_id, 
  COUNT(clicks.click_id) AS clicks, 
  COUNT(conversions.conversion_id) AS conversions 
FROM impressions 
LEFT JOIN clicks ON impressions.campaign_id = clicks.campaign_id AND impressions.banner_id = clicks.banner_id
LEFT JOIN conversions ON clicks.click_id = conversions.click_id
WHERE clicks.quarter = 3
GROUP BY impressions.campaign_id,impressions.banner_id;

CREATE VIEW banners_with_conversions_q4 AS
SELECT 
  impressions.campaign_id AS campaign_id, 
  impressions.banner_id AS banner_id, 
  COUNT(clicks.click_id) AS clicks, 
  COUNT(conversions.conversion_id) AS conversions 
FROM impressions 
LEFT JOIN clicks ON impressions.campaign_id = clicks.campaign_id AND impressions.banner_id = clicks.banner_id
LEFT JOIN conversions ON clicks.click_id = conversions.click_id
WHERE clicks.quarter = 4
GROUP BY impressions.campaign_id,impressions.banner_id;
