from os import path
from mysql import connector


def user(source):
    return source["user"]


def passwd(source):
    return source["password"]


def server(source):
    return source["server"]


def db(source):
    return source["database"]


def env_filename():
    my_path = path.abspath(path.dirname(__file__))
    filename = path.join(my_path, r"""../../.env/credentials.txt""")
    return filename


def vdw_connect():
    with open(env_filename()) as f:
        contents = f.read() # read credentials file
        vdw = eval(contents)["vdw"] # set source to vdw info

        # create connenction to vdw
        cn = \
            connector.connect(
                user=user(vdw), password=passwd(vdw), host=server(vdw), database=db(vdw))

        return cn

if __name__ == "__main__":
    vdw_connect()