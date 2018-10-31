
class PyOrgParser():

    org_file_raw_list = []

    def __init__(self, org_file_path):
        self.__parse_org_file(org_file_path)

    def get_task_number(self):
        return len(self.org_file_raw_list)

    def __parse_org_file(self, org_file_path):
        with open(org_file_path) as of:
            self.org_file_raw = of.read()

            tmp_entry = ""
            for line in self.org_file_raw.split('\n'):
                if line.startswith('*'):
                    self.org_file_raw_list.append(tmp_entry)
                    tmp_entry = line
                else:
                    tmp_entry += line
            self.org_file_raw_list.append(tmp_entry)
            self.org_file_raw_list = \
                list(filter(None, self.org_file_raw_list))
