DROP TABLE IF EXISTS conversions;
DROP TABLE IF EXISTS clicks;
DROP TABLE IF EXISTS impressions;

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