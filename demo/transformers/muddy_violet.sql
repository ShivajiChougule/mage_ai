-- Docs: https://docs.mage.ai/guides/sql-blocks
INSERT INTO  wandering_feather
SELECT * FROM  {{ df_1 }}