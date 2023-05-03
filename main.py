import atexit
from terms import bot, database
import pandas as pd
import func_question_handler_edition


def inserting_in_data_base(new_rows):
    temp_df = pd.DataFrame(new_rows).transpose().rename_axis('user_id').reset_index()
    temp_df = temp_df.melt(id_vars=['user_id'], var_name='variable', value_name='value')
    temp_df = temp_df.pivot(index='user_id', columns='variable', values='value').reset_index()
    global df
    df = pd.concat([df, temp_df])
    return df


def saving_data_base():
    print("Saving data base...")
    print(df)
    df.to_csv("data.csv")
    print("Database is saved")


if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    del df["Unnamed: 0"]
    bot.polling()
    print(database)
    df = inserting_in_data_base(database)
    atexit.register(saving_data_base)
