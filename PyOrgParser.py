
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
        'parent',      # DONE
    }

    TASK_STATE_R = '(TODO|DONE)'

    org_file_raw_list = []
    task_list = []

    def __init__(self, org_file_path):
        self.org_file_path = org_file_path
        self.__parse_org_file(self.org_file_path)

    def __del__(self):
        del self.org_file_raw_list[:]

    def get_task_number(self):
        return len(self.org_file_raw_list)

    def get_task_name(self, elem):
        out = None
        reg = r"%s(.*?)\:"\
            % (self.TASK_STATE_R)
        match = re.search(reg, elem)
        if match:
            out = match.group(2)
            # Remove task priority
            out = re.sub(r'\[#[A-Z]\]', '', out)
            out = re.sub(r'DEADLINE', '', out)
            out = re.sub(r'SCHEDULED', '', out)
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

    def get_task(self, elem, parent):
        return {
            'level': self.get_task_level(elem),
            'status': self.get_task_state(elem),
            'priority': self.get_task_priority(elem),
            'task': self.get_task_name(elem),
            'tags': self.get_task_tags(elem),
            'deadline': self.get_task_deadline(elem),
            'created': self.get_task_creation_date(elem),
            'id': self.get_task_id(elem),
            'parent_id': parent,
        }

    def get_parent(self, elem):
        out = self.org_file_path
        if self.get_task_level(elem) == 1:
            return self.org_file_path
        else:
            _iter = len(self.task_list) - 1
            while _iter >= 0:
                if self.get_task_level(elem) > self.task_list[_iter]['level']:
                    return self.task_list[_iter]['id']
                _iter -= 1
        return out

    def get_struct(self):
        for elem in self.org_file_raw_list:
            self.task_list.append(self.get_task(
                elem, self.get_parent(elem)))

        return self.task_list

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


if __name__ == '__main__':
    tmp = PyOrgParser('TEST.org')

    tasks = tmp.get_struct()
    for task in tasks:
        print(task)
