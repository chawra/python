import snowflake.connector as sf


username = 'arunchawra'
password = 'Chapotkat@01'
account = 'xw04627'
warehouse = 'computer_wh'
database = 'SNOWFLAKE_SAMPLE_DATA'

print("connecting...")
cnn = sf.connect(user=username, password=password, account=account, region='us-east-2.aws')

cs = cnn.cursor()

try:
    cs.execute('Select current_version()')
    row = cs.fetchone()
    print(row[0])
finally:
    cs.close
    cnn.close()
