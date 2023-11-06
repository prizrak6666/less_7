def helper(work):
    insert_in_memory = work

    def helper(work):
        return f"я можу допомогти із {insert_in_memory},"f"а післа цього хочу допомогти із {work}"
    return helper

helper = helper("homework")
print(helper("cleaning"))
print(helper("driving"))


