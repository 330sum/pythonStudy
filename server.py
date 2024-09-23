import uvicorn
import yaml
import os

if __name__ == '__main__':
    print(os.getcwd())  # 현재 디렉토리
    print(os.path.realpath(__file__))  # 파일
    print(os.path.dirname(os.path.realpath(__file__)))  # 파일이 위치한 디렉토리

    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, './app/config/common.yml'), 'r', encoding='utf-8') as yaml_conf:
        conf = yaml.safe_load(yaml_conf)[os.getenv('APP_ENV', 'local')]
        print(conf)
        uvicorn_conf = conf["UVICORN_CONF"]

    uvicorn.run("app.main:app",
                host=uvicorn_conf["HOST"],
                port=uvicorn_conf["PORT"],
                reload=uvicorn_conf["RELOAD"],
                workers=uvicorn_conf["WORKERS"],
                log_level=uvicorn_conf["LOG_LEVEL"],
                proxy_headers=True,
                forwarded_allow_ips='*',
                )