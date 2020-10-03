from requests import post
from json import dumps as to_json
import secret_file


class Astranector:
    """
    class, made to make a communication to an stardb easy
    """

    def __init__(self, databaseid=str, region=str, username=str, password=str, keyspace=str):
        """
        constructor also generates the needed authtoken to communicate with astra

        :param databaseid: what is the database named ?
        :param region: where is the database located ?
        :param username: the username you want to log in with ?
        :param password: the passowrd coresponding to the user ?
        :param keyspace: what is the keyspace named you want to work with ?
        """
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
        """

        :param tablename: to which table do you want to add the data ?
        :param column_to_add: what data do you want to add ? Please watch conventions as in
        https://docs.astra.datastax.com/reference?utm_campaign=Onboarding&utm_content=3.+Connect+to+Your+Database&utm_medium=email_action&utm_source=customer.io#addrow-1
        mentioned
        TODO add method do generate payload
        """

        url = self.url + "/keyspaces/{keyspaceName}/tables/{tableName}/rows".format(keyspaceName=self.keyspace,
                                                                                    tableName=tablename)
        payload = to_json(column_to_add)
        headers = {"X-Cassandra-Token": self.auth_token,
                   "X-Cassandra-Request-Id": "8f362b39-779e-4fc0-9586-cff47aa2ccc1"}

        post(url=url, data=payload, headers=headers)

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

    astra.insert(tablename="tryitout", column_to_add=secret_file.testdata1)
