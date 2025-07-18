from airflow.models import BaseOperator
import pandas as pd

class BigDataOperator(BaseOperator):
    def __init__(self, path_to_csv_file, path_to_save_file, separator=';', file_type='parquet', **kwarg):
        super().__init__(**kwarg)
        self.path_to_csv_file = path_to_csv_file
        self.path_to_save_file = path_to_save_file
        self.separator = separator
        self.file_type = file_type

    def execute(self, context):
        df = pd.read_csv(self.path_to_csv_file, sep=self.separator)
        if self.file_type == 'parquet':
            df.to_parquet(self.path_to_save_file)
        elif self.file_type == 'json':
            df.to_json(self.path_to_save_file)
        else:
            raise ValueError('Tipo de arquivo inválido')
