import tableauserverclient as TSC
from .. import log
from ... import Session
from .. import ReencryptExtractsParser
from ..extracts.extracts_command import ExtractsCommand
from ..site.site_command import SiteCommand


class ReencryptExtracts(ExtractsCommand):
    def __init__(self, args, site_name):
        super().__init__(args)
        self.site_name = site_name
        self.args = args
        self.logging_level = args.logging_level
        self.logger = log('pythontabcmd2.reencryptextracts_command',
                          self.logging_level)

    @classmethod
    def parse(cls):
        args, site_name = ReencryptExtractsParser.reencrypt_extracts_parser()
        return cls(args, site_name)

    def run_command(self):
        session = Session()
        server_object = session.create_session(self.args)
        self.reencrypt_extract(server_object)

    def reencrypt_extract(self, server):
        site_id = SiteCommand.find_site_id(server, self.site_name)
        server.sites.encrypt_extracts(site_id)
