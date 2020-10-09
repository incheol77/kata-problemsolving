from typing import List
import time


class LogSystem:
    def __init__(self):
        self.log_dict = {}

    def put(self, id: int, timestamp: str) -> None:
        self.log_dict[id] = timestamp

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        def parse_year(timestamp: str) -> str:
            return timestamp.split(":")[0]

        def parse_month(timestamp: str) -> str:
            return timestamp.split(":")[1]

        def parse_day(timestamp: str) -> str:
            return timestamp.split(":")[2]

        def parse_hour(timestamp: str) -> str:
            return timestamp.split(":")[3]

        def parse_minute(timestamp: str) -> str:
            return timestamp.split(":")[4]

        def parse_second(timestamp: str) -> str:
            return timestamp.split(":")[5]

        def is_valid_year(s: str, e: str, log: str) -> bool:
            return parse_year(s) <= parse_year(log) <= parse_year(e)

        def is_valid_month(s: str, e: str, log: str) -> bool:
            return parse_month(s) <= parse_month(log) <= parse_month(e)

        def is_valid_day(s: str, e: str, log: str) -> bool:
            return parse_day(s) <= parse_day(log) <= parse_day(e)

        def is_valid_hour(s: str, e: str, log: str) -> bool:
            return parse_hour(s) <= parse_hour(log) <= parse_hour(e)

        def is_valid_minute(s: str, e: str, log: str) -> bool:
            return parse_minute(s) <= parse_minute(log) <= parse_minute(e)

        def is_valid_second(s: str, e: str, log: str) -> bool:
            return parse_second(s) <= parse_second(log) <= parse_second(e)

        def is_valid_log(s: str, e: str, log: str, gra: str) -> bool:
            if gra == "Year":
                return is_valid_year(s, e, log)
            if gra == "Month":
                return is_valid_year(s, e, log) and is_valid_month(s, e, log)
            elif gra == "Day":
                return is_valid_year(s, e, log) and is_valid_month(s, e, log) \
                       and is_valid_day(s, e, log)
            elif gra == "Hour":
                return is_valid_year(s, e, log) and is_valid_month(s, e, log) \
                       and is_valid_day(s, e, log) and is_valid_hour(s, e, log)
            elif gra == "Minute":
                return is_valid_year(s, e, log) and is_valid_month(s, e, log) \
                       and is_valid_day(s, e, log) and is_valid_hour(s, e, log) \
                       and is_valid_minute(s, e, log)
            elif gra == "Second":
                print("hear : ", s, e, log, gra)
                return is_valid_year(s, e, log) and is_valid_month(s, e, log) \
                       and is_valid_day(s, e, log) and is_valid_hour(s, e, log) \
                       and is_valid_minute(s, e, log) and is_valid_second(s, e, log)

        def filter_log(s: str, e: str, log: str, gra: str) -> bool:
            if s and e and gra and log:
                if is_valid_log(s, e, log, gra):
                    return True
            return False

        result = []
        for key in self.log_dict:
            if filter_log(s, e, self.log_dict[key], gra):
                result.append(key)
        return result


def main():
    logSystem = LogSystem()

    inputs = [[1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"]]
    outputs = [[1,2,3], [1,2]]
    reqs = [
            ["2016:01:01:01:01:01","2017:01:01:23:00:00","Year"],
            ["2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"],
            ["2017:01:01:23:59:59","2017:01:02:23:59:59","Month"]
    ]
    '''
    inputs = [[1, "2017:01:01:23:59:59"], [2, "2017:01:02:23:59:59"]]
    outputs = [[1, 2]]
    reqs = [
        ["2017:01:01:23:59:58", "2017:01:02:23:59:58", "Year"]
    ]
    '''

    for log in inputs:
        logSystem.put(log[0], log[1])

    for i in range(len(outputs)):
        start = time.time()
        res = logSystem.retrieve(reqs[i][0], reqs[i][1], reqs[i][2])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end - start, " sec")
        else:
            print("false : ", end - start, " sec")


if __name__ == "__main__":
    main()

