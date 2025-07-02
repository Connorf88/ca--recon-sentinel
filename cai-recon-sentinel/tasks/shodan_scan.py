from cai.core.base import CTask
import shodan

class ShodanScanTask(CTask):
    def run(self, target_ip):
        api = shodan.Shodan("YOUR_SHODAN_API_KEY")
        result = api.host(target_ip)
        self.log(result)
        return result

