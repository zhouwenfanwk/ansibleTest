# origin-localfile  destination-hbase

#-*- coding: utf-8 -*-
from thrift.transport import TSocket ,TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
import csv

host = 'GWSSI-CDH0105'
path = '/Users/wenfanzhou/Desktop/javaProject/sample/hbase.csv'
table_name = 'T1:TESTSTREAMSETS'
row_key = 'id'
fields = {'id':'data:id','name':'data:name', 'email':'data:email'}

def get_hbase(host):

    try:

        socket = TSocket.TSocket(host, 9090)
        socket.setTimeout(5000)
        transport = TTransport.TBufferedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        client = Hbase.Client(protocol)
        transport.open()
    except:
        raise Exception('connection error')
    # print(client.getTableNames())
    # print(client.getColumnDescriptors('T1:TESTSTREAMSETS'))
    # print(client.getTableRegions('T1:TESTSTREAMSETS'))
    # print(client.getRow('T1:TESTSTREAMSETS','4')[0].columns)

    return client

def get_localFile(path):
    if path == '':
        raise Exception('None File Path')
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)

            return list(reader)
    except:
        raise Exception('file not exist')

def data_check(hbase_client, csv_file, table_name, fields, row_key):
    if not csv_file:
        raise Exception('empty file')

    headers = csv_file[0]
    rk_id = headers.index(row_key)
    csv_file = csv_file[1:]
    for i, v in enumerate(csv_file):
        for l, k in enumerate(v):
            hb = hbase_client.getRow(table_name, v[rk_id])[0].columns[fields[headers[l]]].value
            assert hb == k

    print('Check Done')


print(get_localFile('/Users/wenfanzhou/Desktop/javaProject/sample/hbase.csv'))
# get_hbase(host)

data_check(hbase_client=get_hbase(host), csv_file=get_localFile(path), table_name=table_name, fields=fields, row_key=row_key)