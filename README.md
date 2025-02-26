# 📝 Personalized Letter Generator

A Python script to generate **customized invitation letters** using a template. Simply provide a list of names, and the script will create a personalized letter for each person.

---

## 🔧 How It Works

1. The script reads the **starting letter template** from:
   - `./Input/Letters/starting_letter.txt`

2. It replaces `[name]` with actual names from:
   - `./Input/Names/invited_names.txt`

3. The **personalized letters** are saved in:
   - `./Output/ReadyToSend/letter_for_[name].txt`

---

## 🚀 Running the Script

Make sure Python is installed, then run:

```bash
python generate_letters.py
