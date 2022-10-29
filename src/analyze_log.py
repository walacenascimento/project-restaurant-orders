def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file) as file:
            file_content = file.read()
            txt_list = file_content.split("\n")

        resume_orders_by_costumers = dict()
        resume_dates_by_costumers = dict()

        for sentence in txt_list:
            customer, order, date = sentence.split(",")
            analyze_data_custumers(resume_orders_by_costumers, customer, order)
            analyze_data_custumers(resume_dates_by_costumers, customer, date)

        first_answer = max(resume_orders_by_costumers["maria"],
                           key=resume_orders_by_costumers["maria"].get)

        second_answer = resume_orders_by_costumers["arnaldo"]["hamburguer"]

        third_answer = analyze_unions(resume_orders_by_costumers)

        fourth_answer = analyze_unions(resume_dates_by_costumers)

        with open("data/mkt_campaign.txt", "w") as file_out:
            file_out.write(first_answer)
            file_out.write("\n")
            file_out.write(str(second_answer))
            file_out.write("\n")
            file_out.write(str(third_answer))
            file_out.write("\n")
            file_out.write(str(fourth_answer))

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def analyze_data_custumers(dict, customer, data):
    if customer in dict and data in dict[customer]:
        dict[customer][data] += 1
    if customer not in dict:
        dict[customer] = {data: 1}
    if data not in dict[customer]:
        dict[customer][data] = 1


def analyze_unions(dict):
    maria = set(dict["maria"].keys())
    arnaldo = set(dict["arnaldo"].keys())
    joao = set(dict["joao"].keys())
    jose = set(dict["jose"].keys())

    return (jose.union(arnaldo.union(maria))) - joao
