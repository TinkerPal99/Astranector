from requests import post
from json import dumps as to_json
import secret_file


class Astranector:
    def __init__(self, databaseid=str, region=str, username=str, password=str):
        self.username = username
        self.password = password
        self.databaseid = databaseid
        self.region = region
        self.url = "https://{uuid}-{region}.apps.astra.datastax.com/api/rest/v1/auth".format(uuid=databaseid,
                                                                                             region=region)

        payload = {'username': self.username,
                   'password': self.password}
        x = post(self.url, data=to_json(payload))

        self.auth_token = x.json()["authToken"]
        print(self.auth_token)

    def insert(self, cql):
        pass

    def retrieve(self, cql):
        pass

    def update(self, cql):
        pass

    def delete(self, cql):
        pass


if __name__ == "__main__":
    astra = Astranector(databaseid=secret_file.database_uuid,
                        region=secret_file.database_region,
                        username=secret_file.database_username,
                        password=secret_file.database_password)
