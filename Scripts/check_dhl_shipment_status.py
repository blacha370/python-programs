from mysql.connector import connect, Error
import requests
import time
import datetime


HOST = 'HOST'
USER = 'USER'
PASSWORD = 'PASSWORD'
DATABASE = 'DATABASE'
API_KEY = 'API_KEY'

results = []

try:
    with connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE) as connection:
        with connection.cursor(dictionary=True, buffered=True) as cursor:
            cursor.execute("SELECT * FROM status WHERE status <> 'delivered'")
            results = cursor.fetchall()
except Error as e:
    print(e)

headers = {'Accept': 'application/json', 'DHL-API-Key': API_KEY}
done = [33, 66, 100]

i = 1

for result in results:
    r = requests.get('https://api-eu.dhl.com/track/shipments?trackingNumber={}&language=en&limit=1'.format(result['trackingid']),
                     headers=headers)
    status = r.json()['shipments'][0]['status']
    if status['statusCode'] != result['status']:
        try:
            with connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE) as connection:
                with connection.cursor(dictionary=True, buffered=True) as cursor:
                    date = status['timestamp'][:status['timestamp'].index('T')]
                    date_object = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                    perc = '0'
                    if status['statusCode'] == 'pre-transit':
                        perc = done[0]
                    elif status['statusCode'] == 'transit':
                        perc = done[1]
                    elif status['statusCode'] == 'delivered':
                        perc = done[2]
                    sql = "UPDATE status SET status = '{0}', zrobione = '{1}', datadelivery = '{2}' WHERE id = '{3}'".format(status['statusCode'], perc, date_object, result['id'])
                    cursor.execute(sql)
                    connection.commit()
        except Error as e:
            print(e)
    print('{0}/{1}'.format(i, len(results)))
    i += 1
    time.sleep(2)
