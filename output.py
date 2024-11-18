# Output 1
[
    {'id': id,
    'review': review,
    'topic': topic,
    'sentiment': sentiment},
    ...
]

# Output 2
[
    {'id': id,
     'aspect': aspect,
     'part_review': part_sentence,
     'sentiment': sentiment},
    ...
]

# Output 3
[
    {'aspect': aspect,
     'strength': positive_summary,
     'weakness': negative_summary,
     'fine': neutral_summary,},
    ...
]


# Main json file
{
    id: {
        'review': '',
        'date': '',
        'aspect': {
            aspect-1: {'ADJ': [(('helpful',), 'staff was helpful in setting phone.', 'Positive')],
                      'VERB': [],
                      'OTHER': []},
            ...
        },
        'topic': {
            'id_topic': int,
            'term': str,
            'contribution': float
        },
        ...
    }
}


# Storage data topic
{
    ''
}