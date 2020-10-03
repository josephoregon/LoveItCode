import pandas as pd
import numpy as np

df = pd.read_csv('./train_Numerical_data.csv')

df.head()

df.info()

df.isna().sum()

df.isnull().sum()

def memory_usage_per_type(data_frame):
    types = ['float','int','object']
    for type in types:
        selected_col=data_frame.select_dtypes(include=[type])
        memory_usage_of_selected_type_b = selected_col.memory_usage(deep=True).sum()
        memory_usage_of_selected_type_mb=memory_usage_of_selected_type_b/1024**2
        print("memory usage for {} columns: {:03.2f} MB".format(type,memory_usage_of_selected_type_mb))


memory_usage_per_type(df)

def memory_usage(data_frame):
    return data_frame.memory_usage(deep=True).sum()/1024**2

print('Memory use before optimization {:.2f} MB'.format(memory_usage(df)))

### limit of subtypes

def subtypes_limit(subtype):
    if "int" in subtype:
        return np.iinfo(subtype).min,np.iinfo(subtype).max
    if "float" in subtype:
        return np.finfo(subtype).min,np.finfo(subtype).max

for type in ['int8','float16','int32','int64','uint8','uint16','uint32','uint64']:
    print(subtypes_limit(type))

### Downcast float and int column 

#Solution 1
def downcast_and_compare_memory_consuming_by_type_first(type_):
    selected_type = df.select_dtypes(include=[type_])
    converted_type = selected_type.apply(pd.to_numeric,downcast=type_)
    memory_before = memory_usage(selected_type)
    memory_after = memory_usage(converted_type)
    print('before the downcast:{:.2f} MB'.format(memory_before))
    print('after the downcast:{:.2f} MB'.format(memory_after))
    print('')
    compare_type_changes = pd.concat([selected_type.dtypes,converted_type.dtypes],axis=1)
    compare_type_changes.columns = ['before','after']
    return compare_type_changes.apply(pd.Series.value_counts)
    

downcast_and_compare_memory_consuming_by_type_first('float')

#Solution 2
def downcast_and_compare_memory_consuming_by_type_second(type_):
    selected_col = df.select_dtypes(include=[type_])
    memory_before = memory_usage(selected_col)
    optimize_col = selected_col.copy()
    for col in optimize_col.columns:
        mx_col = optimize_col[col].max()
        mn_col = optimize_col[col].min()
        if type_=='int':
            if mn_col>0:
                    if mx_col < 255:
                        optimize_col[col] = optimize_col[col].astype(np.uint8)
                    elif mx_col < 65535:
                        optimize_col[col] = optimize_col[col].astype(np.uint16)
                    elif mx_col < 4294967295:
                        optimize_col[col] = optimize_col[col].astype(np.uint32)
                    else:
                        optimize_col[col] = optimize_col[col].astype(np.uint64)
            else:
                    if mn_col > np.iinfo(np.int8).min and mx < np.iinfo(np.int8).max:
                        optimize_col[col] = optimize_col[col].astype(np.int8)
                    elif mn > np.iinfo(np.int16).min and mx < np.iinfo(np.int16).max:
                        optimize_col[col] = optimize_col[col].astype(np.int16)
                    elif mn > np.iinfo(np.int32).min and mx < np.iinfo(np.int32).max:
                        optimize_col[col] = optimize_col[col].astype(np.int32)
                    elif mn > np.iinfo(np.int64).min and mx < np.iinfo(np.int64).max:
                        optimize_col[col] = optimize_col[col].astype(np.int64)
        else:
            if mn_col > np.finfo(np.float16).min and mx_col < np.finfo(np.float16).max:
                    optimize_col[col] = optimize_col[col].astype(np.float16)
            elif mn_col > np.finfo(np.float32).min and mx_col < np.finfo(np.float32).max:
                    optimize_col[col] = optimize_col[col].astype(np.float32)
            else:
                    optimize_col[col] = optimize_col[col].astype(np.float64)
            
    memory_after = memory_usage(optimize_col)
    print('before the downcast:{:.2f} MB'.format(memory_before))
    print('after the downcast:{:.2f} MB'.format(memory_after))
    compare_type_changes = pd.concat([selected_col.dtypes,optimize_col.dtypes],axis=1)
    compare_type_changes.columns = ['before','after']
    return compare_type_changes.apply(pd.Series.value_counts)

downcast_and_compare_memory_consuming_by_type_second('float')

### Downcast the date object 

'object' in str(df['date'].dtypes)

df_op = df.copy()
df_op['date'] = pd.to_datetime(df_op['date'],format='%Y-%m-%d')
memory_before = memory_usage(df)
memory_after = memory_usage(df_op)
print('before : {:.2f} MB'.format(memory_before))
print('after : {:.2f} MB'.format(memory_after))

### Downcast the object data

def downcast_object():
    selected_col = df[['Store_id','Item_id']]
    print('before the downcast:{:.2f} MB'.format(memory_usage(selected_col)))
    optimize_col = selected_col.copy()
    for col in optimize_col.columns:
        numbr_of_unique = len(optimize_col[col].unique())
        numbr_total = len(optimize_col[col])
        if numbr_of_unique/numbr_total<0.5:
            
            optimize_col[col] = optimize_col[col].astype('category')
    print('before the downcast:{:.2f} MB'.format(memory_usage(optimize_col)))
    

downcast_object()

### Downcast all the date now 

def reduce_memory(data_frame):
    memory_before = memory_usage(data_frame)
    print('before: {:.2f} MB'.format(memory_before))
    subtype_int = ['uint8','uint16','uint32','uint64','int8','int16','int32','int64']
    subtype_float = ['float16','float32','float64']
    for col in data_frame.columns:
        col_type = str(data_frame[col].dtypes)
        mx_col = data_frame[col].max()
        mn_col = data_frame[col].min()
        if 'int'in col_type:
            for ele in subtype_int:
                if mn_col>np.iinfo(ele).min and mx_col<np.iinfo(ele).max:
                    data_frame[col] = data_frame[col].astype(ele)
                    break
        
        elif 'float' in col_type:
            for ele in subtype_float:
                if mn_col>np.finfo(ele).min and mx_col<np.finfo(ele).max:
                    data_frame[col] = data_frame[col].astype(ele)
                    break  
        elif 'object' in col_type:
                if col=='date':
                    data_frame['date'] = pd.to_datetime(data_frame['date'],format='%Y-%m-%d')
                else:
                    numbr_of_unique = len(df[col].unique())
                    numbr_total = len(df[col])
                    if numbr_of_unique/numbr_total<0.5:
                        
                        df[col] = df[col].astype('category')
    memory_after = memory_usage(data_frame)
    print('after:{:.2f} MB'.format(memory_after))
    print('Decreased by: {:.2f} % '.format(100*(memory_before-memory_after)/memory_before))

reduce_memory(df)
