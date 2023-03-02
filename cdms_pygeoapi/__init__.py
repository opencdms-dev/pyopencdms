from pygeoapi.provider.postgresql import PostgreSQLProvider


class CDMSProvider(PostgreSQLProvider):
    def __init__(self, provider_def):
        super().__init__(provider_def=provider_def)
        self.conn_dic = provider_def["data"]
        self.get_fields()
