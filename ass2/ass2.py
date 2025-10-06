import pandas as pd
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import evaluate
df=pd.read_excel("cleandat.xlsx").head(100)
model_name="Helsinki-NLP/opus-mt-en-hi"
translator=pipeline("translation",model=model_name)
translations=[translator(text)[0]['translation_text'] for text in df["English"]]
df["Translated_Hindi"]=translations
df[["English","Translated_Hindi"]].to_excel("Translated_Output.xlsx",index=False)
bleu=evaluate.load("sacrebleu")
chrf=evaluate.load("chrf")
ter=evaluate.load("ter")
refs=[[r] for r in df["Hindi"][:100]]
preds=df["Translated_Hindi"].tolist()
bleu_score=bleu.compute(predictions=preds,references=refs)
chrf_score=chrf.compute(predictions=preds,references=refs)
ter_score=ter.compute(predictions=preds,references=refs)
with open("scores.txt","w",encoding="utf-8") as f:
    f.write(f"BLEU: {bleu_score['score']}\nCHRF: {chrf_score['score']}\nTER: {ter_score['score']}\n")
