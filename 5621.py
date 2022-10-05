def get_c_n_part(target):
    n_idx = len(target)

    for ci, c in enumerate(target[3:]):
        try:
            int(c)
            n_idx = ci + 3
            break
        except:
            pass
    c_part = target[:n_idx]
    n_part = target[n_idx:] if n_idx < len(target) else ""
    return c_part, n_part


def solution(registered_list, new_id):
    result = ""
    register_dict = {}
    for old_id in registered_list:
        c_part, n_part = get_c_n_part(old_id)
        if register_dict.get(c_part) is None:
            register_dict[c_part] = {n_part: True}
        else:
            register_dict[c_part][n_part] = True

    while True:
        c_part, n_part = get_c_n_part(new_id)
        if register_dict.get(c_part) is None:
            result = c_part + n_part
            break

        if register_dict[c_part].get(n_part) is None:
            result = c_part + n_part
            break

        if register_dict[c_part][n_part]:
            n_part = n_part or 0
            new_id = c_part + str(int(n_part) + 1)

    return result


if __name__ == "__main__":
    assert (
        solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15")
        == "ace15"
    )
    assert (
        solution(
            [
                "cow",
                "cow1",
                "cow2",
                "cow3",
                "cow4",
                "cow9",
                "cow8",
                "cow7",
                "cow6",
                "cow5",
            ],
            "cow",
        )
        == "cow10"
    )
    assert solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98") == "bird100"
    assert solution(["apple1", "orange", "banana3"], "apple") == "apple"
