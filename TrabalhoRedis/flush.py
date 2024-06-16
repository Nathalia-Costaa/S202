import redis

redis_conn = redis.Redis(
    host="redis-18924.c326.us-east-1-3.ec2.redns.redis-cloud.com",
    port=18924,
    username="default",# use your Redis user. More info https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/
    password="nIQXoeOwbc7KJMSl4Iot7VLVpSrbp4sK",  # use your Redis password
    decode_responses=True
)

redis_conn.flushall()