with open("input.txt", "r") as file:
    inpt = file.read()

page_ordering, page_numbers = inpt.split("\n\n")

tmp_page_ordering = {}

for i in page_ordering.split("\n"):
    page, dep = i.split("|")
    page = int(page)

    if page in tmp_page_ordering:
        tmp_page_ordering[page].append(int(dep))
    else:
        tmp_page_ordering[page] = [int(dep)]

page_ordering = tmp_page_ordering
page_numbers = [
    list(map(int, i.split(","))) for i in page_numbers.split("\n") if i != ""
]


correct_updates = 0
middle_page_numbers = []


def is_order_correct(page_list):
    for i, page in enumerate(page_list):
        if i == len(page_list) - 1:
            return True
        for j in page_list[i + 1 :]:
            if page in page_ordering[j]:
                return False

    return True


for page_list in page_numbers:
    if is_order_correct(page_list):
        correct_updates += 1
        middle_page_numbers.append(page_list[int((len(page_list) - 1) / 2)])

print(
    f"The sum of middle page numbers in the correct updates are {sum(middle_page_numbers)}"
)

incorrect_orders = [i for i in page_numbers if not is_order_correct(i)]


def get_number_of_deps(order) -> dict[int, int]:
    deps = {i: 0 for i in order}
    for i in order:
        for j in order:
            if i == j:
                continue
            deps[i] += 1 if i in page_ordering[j] else 0
    return deps


def fix_wrong_updates(wrong_order):
    return sorted(
        n_deps := get_number_of_deps(wrong_order), key=lambda item: n_deps[item]
    )


fixed_orders = [fix_wrong_updates(i) for i in incorrect_orders]
middle_page_numbers = [
    page_list[int((len(page_list) - 1) / 2)] for page_list in fixed_orders
]
print(
    f"The sum of middle page numbers in the correct updates are {sum(middle_page_numbers)}"
)
