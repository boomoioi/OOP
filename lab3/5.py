def update_records(dictionary_record, id, property, value):
    if value == '':
        del dictionary_record[id][property]
    elif property == 'tracks':
        if property not in dictionary_record[id].keys():
            dictionary_record[id].update({property : [value]})
        else:
            dictionary_record[id][property].append(value)
    else:
        dictionary_record[id].update({property : value})

    return dictionary_record

record_collection = {
    2548: {
        'albumTitle' : 'Slippery When Wet',
        'artist' : 'Bon Jovi',
        'tracks': ['Let It Rock', 'You Give Love a Bad Name']
    },
    2468: {
        'albumTitle' : '1999',
        'artist' : 'Prince',
        'tracks' : ['1999', 'Little Red Corvette']
    },
    1245: {
        'artist' : 'Robert Palmer',
        'tracks' : []
    },
    5439: {
        'albumTitle' : 'ABBA Gold'
    }
}
update_records(record_collection, 2548, 'tracks', 'abc')
print(record_collection)