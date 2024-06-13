-- Lists all bands with "Glam rock",
-- Ranked by their logevity.
SELECT band_name, (IFNULL(split, 2022) - formed) as lifespan
FROM metal_bands
WHERE style = "Glam rock"
LIMIT 10;
