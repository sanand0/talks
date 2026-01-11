---
title: What is vibe coding?
date: 2026-01-11T21:34:22+08:00
---

## User

I'm in the middle of an NPTEL workshop. I want to show how ChatGPT, etc., can analyze data. Now, for this, I need a data set. I can maybe create a fake data set, but what is the fun in that? I would also like the participants to pick some data sets that they have and will be able to analyze it. But here's the thing. Now, right at the last minute, finding that data set is going to be time-consuming for me as well as for them. What are the top five data sets that almost anyone will be able to access instantly? They will readily have, and the data is large enough that some amount of data analysis is useful and worth doing on this. Please tell me both the data sets as well as how one can go about getting these data sets.

## Gemini

This is a common workshop challenge. You need data that is **personal** (to make it engaging), **instant** (no 2-hour "export processing" wait times), and **diverse** (text, numbers, time-series).

Here are the top 5 data sets that your participants already have and can access in under 2 minutes, along with instructions on how to get them.

### 1. WhatsApp Chat History (Text & Time Data)

**Why it’s great:** It contains rich natural language data, timestamps, and interaction patterns. Perfect for sentiment analysis, "who texts the most," or peak activity times.

- **Format:** `.txt`
- **How to get it (Instant):**

1. Open WhatsApp on your phone.
2. Swipe left (iOS) or long-press (Android) on a specific chat (e.g., a family group or best friend).
3. Tap **More** > **Export Chat**.
4. Select **"Without Media"** (this makes it instant and small).
5. Email it to yourself or save it to your computer.
6. _Upload the `.txt` file directly to ChatGPT._

### 2. Netflix Viewing Activity (Categorical & Time Data)

**Why it’s great:** It shows exactly what they watched and when. Good for analyzing binge-watching habits, favorite genres, or weekday vs. weekend patterns.

- **Format:** `.csv`
- **How to get it (Instant):**

1. Go to `Netflix.com/Account` on a laptop browser.
2. Scroll down to the **"Profile & Parental Controls"** section.
3. Click the arrow next to your profile.
4. Click **"Viewing Activity"** (View).
5. Scroll to the bottom and click **"Download all"**.
6. _You get an instant `NetflixViewingHistory.csv` file._

### 3. Local Computer File Inventory (Hierarchical & Big Data)

**Why it’s great:** Everyone has thousands of files on their laptop. This creates a massive dataset of file names, extensions, sizes, and dates instantly. Good for cleaning data, finding "storage hogs," or analyzing file creation habits.

- **Format:** `.csv` (generated via command line)
- **How to get it (Instant):**

- **For Windows:**

1. Open Command Prompt (`cmd`).
2. Type: `cd C:\Users\YourName\Documents` (or any folder you want to analyze).
3. Type: `dir /s /b > file_list.txt` (This lists every single file path in that folder and subfolders into a text file).

- **For Mac:**

1. Open Terminal.
2. Type: `cd ~/Documents`
3. Type: `ls -R -l > file_list.txt`

- _Upload `file_list.txt` to ChatGPT and ask it to convert it to a structured table or analyze the file types._

### 4. Bank or Credit Card Statement (Financial & Numerical Data)

**Why it’s great:** It’s real-world "messy" data. It has dates, descriptions (which need cleaning), and amounts. Perfect for categorization (Food vs. Travel) and spending trends.

- **Format:** `.csv` or `.pdf`
- **How to get it (Instant):**

1. Log into any net banking portal.
2. Select "Account Statement" or "Transaction History."
3. Choose "Last 6 months" and click **Download as CSV** (preferred) or PDF.
4. _Note for workshop:_ If participants are privacy-conscious, tell them to delete the "Account Number" column before uploading, or reassure them that ChatGPT (Enterprise/Team) has privacy controls—or simply use a mock statement if they are too uncomfortable.

### 5. Screen Time or Battery Usage (Image / Multimodal Data)

**Why it’s great:** This leverages the **Vision** capabilities of ChatGPT. Most mobile OSs don't export this data easily, but they visualize it beautifully. You can ask ChatGPT to "digitize" the chart.

- **Format:** `.jpg` / `.png` (Screenshot)
- **How to get it (Instant):**

1. **iPhone:** Settings > Battery (shows a nice bar chart of usage patterns and app lists).
2. **Android:** Settings > Digital Wellbeing & Parental Controls.
3. **Action:** Take a screenshot of the detailed view.
4. _Upload the screenshot to ChatGPT and ask: "Convert this image into a table of app usage data and tell me which app is draining my battery the most relative to screen time."_

---

### **Backup Plan (If they have absolutely nothing)**

If someone is on a borrowed machine or uncomfortable using personal data, give them this "Instant Public Data" link:

- **Rdatasets (GitHu):** A massive collection of standard CSV datasets (Titanic, Iris, Housing prices) that can be accessed via raw URL.

- _Quick Link:_ `https://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv` (Cars dataset—classic, small, easy to analyze).

**Next Step for You:**
Would you like me to write a specific **prompt** for any of these datasets (e.g., _"Here is a prompt to paste into ChatGPT to analyze the WhatsApp chat..._) so you can display it on the screen during the workshop?
