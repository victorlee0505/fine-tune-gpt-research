# prerequisite
a openai subscription and generated a OPENAI_API_KEY, set it in system envrionment variable
https://platform.openai.com/docs/guides/fine-tuning

# collect data
the raw data can be found in https://www.ontario.ca/page/public-sector-salary-disclosure
- sunshine_2022
- sunchine_2020

we like to compare salary for all OPS employee 2022 vs 2020 to see if there is a huge jump in salary and if there is a reason why.

# compare_4.py
    - merge and add 2 more columns for 'Salary Difference' and 'Job Change'
    - this will be our raw dataset for finetune

# generate_4.py
    - process raw dataset
    - to create {"prompt": "<prompt text>", "completion": "<ideal generated text>"} formatted csv

# fine tuning data prep
```
openai tools fine_tunes.prepare_data -f .\sunshine_prompt_completion.json
```

- This will create .jsonl file

- a text like this will inidicate your estmiation of time needed to fine tune your model
`
Once your model starts training, it'll approximately take 8.86 days to train a "curie" model, and less for "ada" and "babbage". Queue will approximately take half an hour per job ahead of you.
`

# fine tuning targeted model and dataset

```
openai api fine_tunes.create -t .\sunshine_prompt_completion_prepared.jsonl -m curie
```

please be aware of price model
Model	    Training	Usage
Ada	    $0.0004 / 1K tokens	$0.0016 / 1K tokens
Babbage	$0.0006 / 1K tokens	$0.0024 / 1K tokens
Curie	$0.0030 / 1K tokens	$0.0120 / 1K tokens
Davinci	$0.0300 / 1K tokens	$0.1200 / 1K tokens

| Model   | Training (1K tokens)  | Usage (1K tokens)   |
|---------|-----------|---------|
| Ada     | 0.0004   | 0.0016 |
| Babbage | 0.0006   | 0.0024 |
| Curie   | 0.0030   | 0.0120  |
| Davinci | 0.0300   | 0.1200  |

so if your dataset is 2000 char and you are training with davinci

2000 / 4 = 500 tokens

0.03 / 1000 * 500 = $0.015

at 3 epochs

$0.015 * 3 = $0.045

ex. 

davinci: if 1,100,000 char, 1100000 / 4 * (0.03/1000) *3 = $24.7

curie: if 1,100,000 char, 1100000 / 4 * (0.003/1000) *3 = $2.475


# check your fine tune model id

```
openai api fine_tunes.list
```

find the id, it is your own model tuned

# check status of your fine tune

```
openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>
```

# try to use

```
openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>
```

# Research Result: (updating....)
- fine tuning a pretrained is not the way to teach new knowledge to a model.
- if dataset prepared is not carefully crafted
    - exact prompt might generate exact completion from the dataset
    - other prompt not in dataset do not generate any meaningful completion
