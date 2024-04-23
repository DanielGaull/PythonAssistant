import json

class Memory:

    def __init__(self):
        self.__mem = dict()
        self.__fp = None

    def memo(self):
        return self.__mem

    def load_from_file(self, fp: str):
        '''
        File format:
        <key>=<value>
        <key>=[<values...>]
        Value will always be valid python expression
        '''
        self.__fp = fp
        file = open(fp, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            if len(line) <= 0:
                continue
            equal_index = line.find('=')
            key = line[:equal_index]
            value_str = line[equal_index+1:]
            value = json.loads(value_str)
            self.__mem[key] = value

    def save(self):
        lines = list()
        for key in self.__mem:
            value = self.__mem[key]
            value_str = json.dumps(value)
            lines.append(key + '=' + value_str)

        file = open(self.__fp, "w")
        file.writelines(lines)
        file.close()


    def get(self, key: str) -> str | list[str]:
        if key not in self.__mem:
            return 'NOT SET'
        
        return self.__mem[key]

    def put(self, key: str, value: str) -> None:
        self.__mem[key] = value

    def delete(self, key: str) -> None:
        del self.__mem[key]

    def append(self, key: str, value: str) -> None:
        if key not in self.__mem:
            self.__mem[key] = list()
        self.__mem[key].append(value)

    def remove(self, key: str, value: str) -> None:
        self.__mem[key].remove(value)

    def keys(self):
        return self.__mem.keys()