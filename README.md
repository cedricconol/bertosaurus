# bertosaurus
#### The better thesaurus.

Bertosaurus uses the latest language models to revolutionize the good old thesaurus.

## Installation
Bertosaurus is in beta. You may install the beta via `pip`.

```
pip install bertosaurus --extra-index-url=https://test.pypi.org/simple/
```

Or install the latest build.
```
git clone https://github.com/cedricconol/bertosaurus.git
cd bertosaurus
python setup.py install
```

## Usage

```python
from bertosaurus import Bertosaurus

thesaurus = Bertosaurus()

word = 'change'
sentence = 'I want to change the world.' # sentence which uses the word

thesaurus.ranked_synonyms(sentence, word)
```
Outputs the synonyms and their corresponding `similarity_score`:
```
[('alter', 0.95599),
 ('shift', 0.94458),
 ('modify', 0.92202),
 ('convert', 0.91599),
 ('switch', 0.90705),
 ('transfer', 0.90695),
 ('vary', 0.90642),
 ('deepen', 0.8948),
 ('exchange', 0.88716),
 ('interchange', 0.87401),
 ('commute', 0.85808)]
 ```

## TODO
- build streamlit web app
- make `sentence` optional
- find other sources of synonyms
- build documentation
- update CONTRIBUTING
- create unit tests

## License
Free software: MIT license

## Credits
This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the `[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.
