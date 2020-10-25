import pandas as pd
import numpy as np
from pandas import DataFrame


def make_df():
    df = pd.read_csv("./Invokabilities-w7ry3boc7fcczbydbhi56dhbqm-dev.csv")

    scores = df["scores (S)"]
    dss = df["ds_split (S)"]

    # find unique indices
    indices = []
    for score in scores:
        score = eval(score)
        for item in score:
            indices.append(item["name"].replace("Article", "").strip())

    indices = sorted(list(set(indices)))

    # find unique dss
    columns = []
    for ds in dss:
        ds_num = ds.split("_")[0]
        columns.append(int(ds_num))

    dss = sorted(list(set(columns)), reverse=True)
    dss = ['DS ' + str(ds) for ds in dss]

    cites = DataFrame(
        np.zeros((len(dss), len(indices))),
        index=dss,
        columns=indices
    )

    labels = DataFrame(
        abs(np.random.randn(len(dss), len(indices))),
        index=dss,
        columns=indices,
    )

    for index, row in df.iterrows():
        ds = int(row["ds_split (S)"].split("_")[0])
        score = row["scores (S)"]
        score = eval(score)

        for item in score:
            art = item["name"].replace("Article", "").strip()
            if art in indices:
                pred = item["pred"]
                label = item["label"]

                cites.at['DS ' + str(ds), art] = pred
                labels.at['DS ' + str(ds), art] = label
            else:
                pass
    return cites  #labels


if __name__ == "__main__":
    pass
