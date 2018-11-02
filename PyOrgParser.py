
import re
from datetime import datetime


class PyOrgParser():

    task_entry = {
        'level',       # DONE
        'status',      # DONE
        'priority',    # DONE
        'task',        # DONE
        'tags',        # DONE
        'deadline',    # DONE
        'created',     # DONE
        'id',          # DONE
        'parent',      # TODO
        'childes',     # TODO
    }

    TASK_STATE_R = '(TODO|DONE)'

    org_file_raw_list = []

    def __init__(self, org_file_path):
        self.__parse_org_file(org_file_path)

    def __del__(self):
        del self.org_file_raw_list[:]

    def get_task_number(self):
        return len(self.org_file_raw_list)

    def get_task_name(self, elem):
        out = None
#        reg = r"%s(.*?)(\:PROPERTIES\:|DEADLINE\:|SCHEDULED\:)"\
        reg = r"%s(.*?)\:"\
            % (self.TASK_STATE_R)
        match = re.search(reg, elem)
        if match:
            out = match.group(2)
            # Remove task priority
            out = re.sub(r'\[#[A-Z]\]', '', out)
            out = out.lstrip(' ').rstrip(' ')
        return out

    def get_task_state(self, elem):
        out = None
        reg = r"%s" % self.TASK_STATE_R
        match = re.search(reg, elem)
        if match:
            out = match.group()

        return out

    def get_task_tags(self, elem):
        out = None
        reg = r"((\:(.*?)\:)+(.*?)\:|(\:(.*?)\:))"

        elem = elem[:elem.find('PROPERTIES') + 1]
        elem = elem[:elem.find('DEADLINE')]
        elem = elem[:elem.find('SCHEDULED')]

        match = re.search(reg, elem)
        if match:
            tmp_out = match.group()
            if tmp_out.startswith(':'):
                tmp_out = tmp_out[1:]
            if tmp_out.endswith(':'):
                tmp_out = tmp_out[:-1]
            out = tmp_out.split(':')

        return out

    def get_task_priority(self, elem):
        out = None
        reg = r"\[#[A-Z]\]"

        match = re.search(reg, elem)
        if match:
            out = match.group().replace(
                '[', '').replace(']', '').replace('#', '')

        return out

    def get_task_level(self, elem):
        out = None
        reg = r"^\*+"

        match = re.search(reg, elem)
        if match:
            out = len(match.group())

        return out


    def get_task_deadline(self, elem):
        out = None
        reg = r"DEADLINE:\s+\<\d+-\d+-\d+"
        match = re.search(reg, elem)
        if match:
            out = datetime.strptime(match.group(),
                                    'DEADLINE: <%Y-%m-%d')

        return out

    def get_task_creation_date(self, elem):
        out = None
        reg = r":CREATED:\s+\<\d+-\d+-\d+\s+\w+\s+\d+:\d+\>"
        match = re.search(reg, elem)
        if match:
            tmp_out = re.sub(r'\s+\w+\s+', ' ', match.group())
            out = datetime.strptime(tmp_out,
                                    ':CREATED: <%Y-%m-%d %I:%M>')

        return out

    def get_task_id(self, elem):
        out = None
        reg = r"\:ID\:\s+([0-9a-zA-Z]+\-)+([0-9a-zA-Z]+)"
        match = re.search(reg, elem)
        if match:
            out = match.group().replace(':ID:', '').lstrip(
                ' ').rstrip(' ')

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
