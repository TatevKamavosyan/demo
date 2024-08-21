from transformers import AutoModelForCausalLM, AutoTokenizer

mgpt_mod = "ai-forever/mGPT-armenian"  # Укажите путь к вашей модели или её имя на Hugging Face
tokenizer = AutoTokenizer.from_pretrained(mgpt_mod)
model = AutoModelForCausalLM.from_pretrained(mgpt_mod)

def generate_text(input_text):
    inputs = tokenizer(input_text, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=50)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text
