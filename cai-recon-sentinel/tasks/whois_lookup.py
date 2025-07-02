from cai.core.base import CTask
import whois

class WhoisLookupTask(CTask):
    def run(self, domain):
        result = whois.whois(domain)
        self.log(result)
        return result

