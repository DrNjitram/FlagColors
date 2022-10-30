from typing import Dict


def get_sections(file) -> Dict:


    TAGS = {}

    with open(file, "r", encoding="utf-8-sig") as content:
        lines = content.readlines()
        level = 0
        buffer = []
        for line in lines:
            if line.startswith(("#", "@")): continue
            line = line.rstrip()
            if "#" in line:
                line = line.split("#")[0]
            if line == "":
                continue

            if level == 0:
                if len(buffer) > 0:
                    TAG = buffer[0].split("=")[0].strip()
                    TAGS[TAG] = buffer
                    buffer = []

            buffer.append(line)

            level += line.count("{")
            level -= line.count("}")

    return TAGS


