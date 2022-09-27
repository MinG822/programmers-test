def solution(commands):
    N = 51
    tables = [[0 for _ in range(N)] for _ in range(N)]
    parent_to_child = {}
    child_to_parent = {}

    results = []


    def get_value(r1, c1):
        try:
            return child_to_parent[(r1, c1)]
        except:
            return r1, c1

    for command in commands:
        command_li = command.split(" ")

        if command_li[0] == "UPDATE":
            if len(command_li) == 4:
                r, c = int(command_li[1]), int(command_li[2])
                r, c = get_value(r, c)
                tables[r][c] = command_li[3]
            else:
                old, new = command_li[1], command_li[2]
                if old == new:
                    continue
                for i in range(1, N):
                    for j in range(1, N):
                        if tables[i][j] == old:
                            tables[i][j] = new

        elif command_li[0] == "MERGE":
            r1, c1, r2, c2 = (
                int(command_li[1]),
                int(command_li[2]),
                int(command_li[3]),
                int(command_li[4]),
            )
            if get_value(r1, c1) == (r1, c1):
                if get_value(r2, c2) == (r2, c2):
                    parent_to_child[(r1, c1)] = [(r2, c2)]
                    child_to_parent[(r2, c2)] = (r1, c1)
                else:
                    pr, pc = get_value(r2, c2)
                    child_to_parent[(r1, c1)] = (pr, pc)
                    child_to_parent[(r2, c2)] = (pr, pc)
                    parent_to_child[(pr, pc)].extend([(r1, c1), (r2, c2)])
            else:
                
    
            merged_position[(r2, c2)] = (r, c)

            if tables[r][c]:
                tables[r2][c2] = 0
            else:
                tables[r][c] = tables[r2][c2]
                tables[r2][c2] = 0

            if (r, c) != (r1, c1):
                tables[r1][c1] = 0

        elif command_li[0] == "UNMERGE":
            r, c = int(command_li[1]), int(command_li[2])
            rr, cc = get_value(r, c)  # NOTE
            value = tables[rr][cc]
            tables[rr][cc] = 0
            tables[r][c] = value

            new_merged_position = {}
            for k, v in merged_position.items():
                if k == (rr, cc):
                    continue
                elif v == (rr, cc):
                    continue
                new_merged_position[k] = v
            merged_position = new_merged_position

        elif command_li[0] == "PRINT":
            r, c = int(command_li[1]), int(command_li[2])
            r, c = get_value(r, c)  # NOTE
            results.append(tables[r][c] or "EMPTY")

        else:
            print(command_li)
            raise Exception()

    # print(results)
    return results


if __name__ == "__main__":
    assert str(
        solution(
            [
                "UPDATE 1 1 menu",
                "UPDATE 1 2 category",
                "UPDATE 2 1 bibimbap",
                "UPDATE 2 2 korean",
                "UPDATE 2 3 rice",
                "UPDATE 3 1 ramyeon",
                "UPDATE 3 2 korean",
                "UPDATE 3 3 noodle",
                "UPDATE 3 4 instant",
                "UPDATE 4 1 pasta",
                "UPDATE 4 2 italian",
                "UPDATE 4 3 noodle",
                "MERGE 1 2 1 3",
                "MERGE 1 3 1 4",
                "UPDATE korean hansik",
                "UPDATE 1 3 group",
                "UNMERGE 1 4",
                "PRINT 1 3",
                "PRINT 1 4",
            ]
        )
    ) == str(["EMPTY", "group"])
    assert str(
        solution(
            [
                "UPDATE 1 1 a",
                "UPDATE 1 2 b",
                "UPDATE 2 1 c",
                "UPDATE 2 2 d",
                "MERGE 1 1 1 2",
                "MERGE 2 2 2 1",
                "MERGE 2 1 1 1",
                "PRINT 1 1",
                "UNMERGE 2 2",
                "PRINT 1 1",
            ]
        )
    ) == str(["d", "EMPTY"])
