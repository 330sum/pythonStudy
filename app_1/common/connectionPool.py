import logging
import os
import yaml
# pip install mysql-connector-python
from mysql.connector import Error
from mysql.connector import pooling

logger = logging.getLogger('service')

# YAML 파일에서 설정 읽기
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, '../config/common.yml'), 'r', encoding='utf-8') as yaml_conf:
    conf = yaml.safe_load(yaml_conf)[os.getenv('APP_ENV', 'local')]


def setup_connection_pool():
    try:
        db = conf['DATABASE_1']
        user_name: str = db['user_name']
        password: str = db['password']
        db_host: str = db['db_host']
        db_port: int = db['port']
        db_name: str = db['db_name']
        pool_size: int = db['pool_size']

        # 연결 풀 생성
        global connection_pool_1
        connection_pool_1 = pooling.MySQLConnectionPool(pool_name='mypool',
                                                        user=user_name,
                                                        password=password,
                                                        host=db_host,
                                                        port=db_port,
                                                        database=db_name,
                                                        pool_size=pool_size
                                                        )

    except Error as e:
        logger.error(f'커넥션 풀 에러 {e}')
#          로깅시 색깔 변경으로 좀 더 잘 보이게 해보자


def get_db():
    return connection_pool_1.get_connection()
