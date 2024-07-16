def rank_array(input_array):
    new_array=input_array.copy()
    new_array.sort()
    for i in range(len(input_array)):
        for j in range(len(new_array)):
            if input_array[i]==new_array[j]:
                input_array[i]=j+1
                break;
input_array=[12,2,2,11]
rank_array(input_array)
print(input_array)
