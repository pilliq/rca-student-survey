#!/bin/bash
SQL="select question from questions where id='$1';"
sqlite3 rca.db < <(echo $SQL)
