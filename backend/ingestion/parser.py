import re

LOG_PATTERN = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \| (\w+) \| (\w+) \| (.*)"

def parse_line(line):

  match = re.search(LOG_PATTERN, line)
  if match:
    return {
      "timestamp": match.group(1),
      "level": match.group(2),
      "service": match.group(3),
      "message": match.group(4)
    }
  return None