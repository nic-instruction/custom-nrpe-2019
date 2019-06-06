#!/usr/bin/bash
# test from django to postgres

connection=$(DBNAME=postgres PGPORT=5432 PGUSER=myprojectuser PGPASS=password)

if [ $connection == $connection ] ; then
        echo "[OK]"
        exit 0;
        
elif [ $connection != $connection ]; then
        echo "[FAIL]"
        exit 2;

else
        echo "STATUS:UNKNOWN"
        exit 3;
        
fi
