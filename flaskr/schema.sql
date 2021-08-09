DROP TABLE IF EXISTS conversions_q1 CASCADE;
DROP TABLE IF EXISTS conversions_q2 CASCADE;
DROP TABLE IF EXISTS conversions_q3 CASCADE;
DROP TABLE IF EXISTS conversions_q4 CASCADE;
DROP TABLE IF EXISTS clicks_q1 CASCADE;
DROP TABLE IF EXISTS clicks_q2 CASCADE;
DROP TABLE IF EXISTS clicks_q3 CASCADE;
DROP TABLE IF EXISTS clicks_q4 CASCADE;
DROP TABLE IF EXISTS impressions CASCADE;

CREATE TABLE impressions(
    banner_id    INT,
    campaign_id  INT,
    PRIMARY KEY (banner_id,campaign_id)
);

CREATE TABLE clicks_q1(
    click_id         INT PRIMARY KEY,
    banner_id        INT,
    campaign_id      INT,
    FOREIGN KEY (banner_id,campaign_id) REFERENCES impressions (banner_id,campaign_id)
);

CREATE TABLE clicks_q2(
    click_id         INT PRIMARY KEY,
    banner_id        INT,
    campaign_id      INT,
    FOREIGN KEY (banner_id,campaign_id) REFERENCES impressions (banner_id,campaign_id)
);

CREATE TABLE clicks_q3(
    click_id         INT PRIMARY KEY,
    banner_id        INT,
    campaign_id      INT,
    FOREIGN KEY (banner_id,campaign_id) REFERENCES impressions (banner_id,campaign_id)
);

CREATE TABLE clicks_q4(
    click_id         INT PRIMARY KEY,
    banner_id        INT,
    campaign_id      INT,
    FOREIGN KEY (banner_id,campaign_id) REFERENCES impressions (banner_id,campaign_id)
);

CREATE TABLE conversions_q1(
    conversion_id    INT PRIMARY KEY,
    click_id         INT,
    revenue          FLOAT NOT NULL,
    FOREIGN KEY (click_id) REFERENCES clicks_q1 (click_id)
);

CREATE TABLE conversions_q2(
    conversion_id    INT PRIMARY KEY,
    click_id         INT,
    revenue          FLOAT NOT NULL,
    FOREIGN KEY (click_id) REFERENCES clicks_q2 (click_id)
);

CREATE TABLE conversions_q3(
    conversion_id    INT PRIMARY KEY,
    click_id         INT,
    revenue          FLOAT NOT NULL,
    FOREIGN KEY (click_id) REFERENCES clicks_q3 (click_id)
);

CREATE TABLE conversions_q4(
    conversion_id    INT PRIMARY KEY,
    click_id         INT,
    revenue          FLOAT NOT NULL,
    FOREIGN KEY (click_id) REFERENCES clicks_q4 (click_id)
);

CREATE INDEX impressions_campaign_id
  ON public.impressions
  (campaign_id);

CREATE INDEX clicks_q1_campaign_id
  ON public.clicks_q1
  (campaign_id);

CREATE INDEX clicks_q2_campaign_id
ON public.clicks_q2
(campaign_id);

CREATE INDEX clicks_q3_campaign_id
  ON public.clicks_q3
  (campaign_id);

CREATE INDEX clicks_q4_campaign_id
  ON public.clicks_q4
  (campaign_id);

CREATE INDEX conversions_q1_click_id_conversion_id
  ON public.conversions_q1
  (click_id, conversion_id);

CREATE INDEX conversions_q2_click_id_conversion_id
  ON public.conversions_q2
  (click_id, conversion_id);

CREATE INDEX conversions_q3_click_id_conversion_id
  ON public.conversions_q3
  (click_id, conversion_id);

CREATE INDEX conversions_q4_click_id_conversion_id
  ON public.conversions_q4
  (click_id, conversion_id);