from cai.core.base import CTask
import dns.resolver

class SubdomainEnumTask(CTask):
    def run(self, domain):
        subdomains = ['www', 'mail', 'ftp']
        found = []
        for sub in subdomains:
            try:
                dns.resolver.resolve(f"{sub}.{domain}", 'A')
                found.append(f"{sub}.{domain}")
            except:
                continue
        self.log(found)
        return found

