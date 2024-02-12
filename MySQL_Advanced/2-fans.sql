-- write an SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
CREATE TABLE IF NOT EXISTS ranking (
    `origin` varchar(255) DEFAULT NULL,
    `nb_fans` int(11) DEFAULT NULL
)

SELECT metal_bands.origin as mb_origin, metal_bands.fans as mb_fans
FROM metal_bands
WHERE IF metal_bands.origin NOT EXISTS IN ranking.origin
THEN INSERT INTO ranking (origin, nb_fans) VALUES (metal_bands.origin, metal_bands.fans)
ELSE UPDATE ranking SET nb_fans=(nb_fans+metal_bands.fans) WHERE metal_bands.origin = ranking.origin
