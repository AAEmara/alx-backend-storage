-- Lists all bands with "Glam rock",
-- Ranked by their logevity.
SELECT band_name, (IFNULL(split, 2022) - formed) as lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
LIMIT 10;
