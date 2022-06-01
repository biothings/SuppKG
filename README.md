# SuppKG

This is the plugin repo for SuppKG endpoints of Translator KP APIs.

SuppKG contains a variety of edges for Dietary Supplements.

- Publication: https://arxiv.org/abs/2106.12741
- Download link: https://github.com/zhang-informatics/SemRep_DS/tree/main/SuppKG

A sample document parsed by the plugin from the source data is as below:

```python
{
    '_id': 'C0001734_C0151763_CAUSES',
    'subject': {'umls': 'C0001734', 'name': 'aflatoxin', 'semtypes': ['bacs', 'hops']},
    'object': {'umls': 'C0151763', 'name': 'damage liver', 'semtypes': ['patf']},
    'relation': [
        {
            'pmid': 1394115,
            'sentence': 'Turmeric and curcumin were also found to reverse the aflatoxin 
induced liver damage produced by feeding aflatoxin B1 (AFB1) (5 micrograms/day per 14 days) 
to ducklings.',
            'conf': 0.9303833842,
            'tuid': 0
        },
        {
            'pmid': 1394115,
            'sentence': 'Reversal of aflatoxin induced liver damage by turmeric and 
curcumin.',
            'conf': 0.9396179318000001,
            'tuid': 0
        }
    ],
    'predicate': 'CAUSES'
}
```

For more details of the plugin, please refer to https://github.com/biothings/pending.api/issues/55.
