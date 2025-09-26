#!/bin/bash

mysqldump \
  -u root \
  -p \
  --databases sales \
  --tables sales_data \
  > /root/data/sales_data.sql



