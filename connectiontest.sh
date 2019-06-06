#!/usr/bin/bash

if DBNAME=postgres PGPORT=5432 PGUSER=myprojectuser PGPASS=password
then
        echo "[OK]"
        exit 0;
else
        echo "[FAIL]"
        exit1;
        
fi
