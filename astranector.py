from requests import post
from json import dumps as to_json
import secret_file


# uuid genrator https://www.uuidgenerator.net/

class Astranector:
    def __init__(self, databaseid=str, region=str, username=str, password=str, keyspace=str):
        self.username = username
        self.password = password
        self.databaseid = databaseid
        self.region = region
        self.keyspace = keyspace

        self.url = "https://{uuid}-{region}.apps.astra.datastax.com/api/rest/v1".format(uuid=databaseid,
                                                                                        region=region)

        payload = {'username': self.username,
                   'password': self.password}
        x = post(self.url + "/auth", data=to_json(payload))

        self.auth_token = x.json()["authToken"]

    def insert(self, tablename, column_to_add):
        url = self.url + "/keyspaces/{keyspaceName}/tables/{tableName}/rows".format(keyspaceName=self.keyspace,
                                                                                    tableName=tablename)
        payload = to_json(column_to_add)
        headers = {"X-Cassandra-Token": self.auth_token,
                   "X-Cassandra-Request-Id": "8f362b39-779e-4fc0-9586-cff47aa2ccc1"}

        x = post(url=url, data=payload, headers=headers)
        return x.json()

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
                        password=secret_file.database_password,
                        keyspace="python")

    astra.insert(tablename="tryitout", column_to_add={"columns": [
        {"name": "partition", "value": "1"},
        {"name": "whenupdated", "value": "4b7396ea-0582-11eb-adc1-0242ac120002"},
        {"name": "column", "value": "textitesttext"}
    ]
    })
