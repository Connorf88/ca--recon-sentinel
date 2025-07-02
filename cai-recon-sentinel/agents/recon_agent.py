from cai.core import CAgent

class ReconAgent(CAgent):
    def setup(self):
        self.register_task("shodan_scan")
        self.register_task("whois_lookup")
        self.register_task("subdomain_enum")

    def run(self, input_data):
        results = {}
        for task_name in self.tasks:
            result = self.tasks[task_name].run(input_data)
            results[task_name] = result
        self.log(results)
        return results

