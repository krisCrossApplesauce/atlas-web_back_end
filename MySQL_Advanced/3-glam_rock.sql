-- write an SQL script that lists all bands
-- with Glam rock as their main style,
-- ranked by their longevity
SELECT band_name, SUBTRACT(IFNULL(split, 2024), formed) as lifespan
FROM metal_bands
WHERE metal_bands.style LIKE 'Glam rock%'
ORDER BY lifespan DESC;
