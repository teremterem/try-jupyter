import pandas as pd

some_frame = pd.DataFrame(data={
    'col1': ['c11', 'c12', 'c13', 'c14'],
    'col2': ['c21', 'c22', 'c23', 'c24'],
    'col3': ['c31', 'c32', 'c33', 'c34'],
})

some_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
}
some_other_frame = pd.DataFrame(some_dict.items(), columns=['key col', 'value col'])
