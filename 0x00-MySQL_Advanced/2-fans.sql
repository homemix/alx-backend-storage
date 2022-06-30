-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT DISTINCT origin, fans AS nb_fans
from metal_bands
ORDER BY nb_fans DESC;
