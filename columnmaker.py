# code is unclean, as is documentation, further improvement suggested


__template_versuch1 = [
    {"name": "",
     "value": ""},
    {"name": "",
     "value": ""},
    {"name": "",
     "value": ""}
]


def fill_data(data):
    """
    orders the data into a format that can be uploaded into the db

    :param data: collection of data to add, consists of lists within list.
    Each list shall consist of the columnname and data to add
    :return: column that can be added
    """
    filled_template = {"columns": []}

    for dpair in data:
        column_template = {'name': dpair[0], 'value': dpair[1]}
        filled_template['columns'].append(column_template)

    return filled_template


if __name__ == "__main__":
    print(fill_data(data=[
                            ["partition", "2"],
                            ["whenupdated", "fd25b708-0634-11eb-adc1-0242ac120002"],
                            ["column", "test"]
                        ]
                    )
        )
