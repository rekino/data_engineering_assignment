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

CREATE INDEX impressions_campaign_id
  ON public.impressions
  (campaign_id);

CREATE INDEX clicks_campaign_id
  ON public.clicks
  (campaign_id);

CREATE INDEX conversions_click_id_conversion_id
  ON public.conversions
  (click_id, conversion_id);