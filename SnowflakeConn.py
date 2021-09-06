import snowflake.connector as sf
import config



print("connecting...")
cnn = sf.connect(user=config.username, password=config.password, account=config.account, region='us-east-2.aws')

cs = cnn.cursor()

try:
    cs.execute(' select C_NAME , C_ADDRESS, C_NATIONKEY, C_COMMENT FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF001.CUSTOMER LIMIT 10')
    row = cs.fetchall()
    print(row)
finally:
    cs.close
    cnn.close()
