.system echo "Inside script <create_modules.sql>"
.system echo "----------------------------------"
DROP TABLE IF EXISTS modules;
CREATE TABLE modules(
module_id INTEGER PRIMARY KEY,
title TEXT,
threshold FLOAT);