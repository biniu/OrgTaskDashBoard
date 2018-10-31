
import re


class PyOrgParser():

    TASK_STATE_R = '(TODO|DONE)'

    org_file_raw_list = []

    def __init__(self, org_file_path):
        self.__parse_org_file(org_file_path)

    def __del__(self):
        del self.org_file_raw_list[:]

    def get_task_number(self):
        return len(self.org_file_raw_list)

    def get_task_name(self, elem):
        out = ''
        reg= r"%s(.*?)(\:PROPERTIES\:|DEADLINE\:|SCHEDULED\:)"\
            % (self.TASK_STATE_R)
        match = re.search(reg, elem)
        if match:
            out = match.group(2)
            # Remove task priority
            out = re.sub(r'\[#[A-Z]\]', '', out)
            out = out.lstrip(' ').rstrip(' ')
        return out

    def __parse_org_file(self, org_file_path):
        del self.org_file_raw_list[:]
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
