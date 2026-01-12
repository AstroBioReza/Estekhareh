import random
import tkinter as tk
import webbrowser
import requests
from bs4 import BeautifulSoup

All = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99,101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163,165,167,169,171,173,175,177,179,181,183,185,187,189,191,193,195,197,199,201,203,205,207,209,211,213,215,217,219,221,223,225,227,229,231,233,235,237,239,241,243,245,247,249,251,253,255,257,259,261,263,265,267,269,271,273,275,277,279,281,283,285,287,289,291,293,295,297,299,301,303,305,307,309,311,313,315,317,319,321,323,325,327,329,331,333,335,337,339,341,343,345,347,349,351,353,355,357,359,361,363,365,367,369,371,373,375,377,379,381,383,385,387,389,391,393,395,397,399,401,403,405,407,409,411,413,415,417,419,421,423,425,427,429,431,433,435,437,439,441,443,445,447,449,451,453,455,457,459,461,463,465,467,469,471,473,475,477,479,481,483,485,487,489,491,493,495,497,499,501,503,505,507,509,511,513,515,517,519,521,523,525,527,529,531,533,535,537,539,541,543,545,547,549,551,553,555,557,559,561,563,565,567,569,571,573,575,577,579,581,583,585,587,589,591,593,595,597,599,601,603]
Bad = [3,13,15,19,21,23,201,211,213,223,225,227,229,235,237,401,409,423,435,441,447,53,59,69,75,89,93,251,271,275,289,451,455,457,461,465,471,473,479,491,493,497,101,105,113,115,117,121,123,125,129,137,139,145,311,321,323,325,341,505,509,513,517,519,523,525,527,531,567,581,349,351,369,373,379,381,393,395,153,161,163,167,181,193,195,197,439]
Good = 	[1,25,29,31,207,219,239,243,245,405,407,443,57,61,73,79,259,265,269,281,285,295,453,467,481,487,107,133,135,141,299,301,303,315,317,319,327,329,333,337,507,549,551,561,571,585,587,589,591,595,359,363,365,371,385,387,389,391,397,157,159,179,199]
Middle = [125,129,137,139,145,311,321,323,325,341,505,509,513,517,519,523,525,527,531,567,581,349,351,369,373,379,381,393,395,153,161,163,167,181,193,195,197,1,25,29,31,207,219,239,243,245,405,407,443,57,61,73,79,259,265,269,281,285,295,453,467,481,487,107,133,135,141,299,301,303,315,317,319,327,329,333,337,507,549,551,561,571,585,587,589,591,595,359,363,365,371,385,387,389,391,397,157,159,179,199,7,27,37,419,49,91,463,469,119,147,573,173,175,183,185]
Middle_Bad = [9,41,43,217,413,427,433,437,445,63,81,83,95,97,255,283,297,475,143,345,543,383,149,171]
Middle_Good = [11,17,35,221,241,425,431,71,257,279,459,99,343,541,559,563,603,353,357,377,399]
Very_Bad = [103,33,47,209,215,233,403,417,429,51,65,85,87,261,267,273,495,109,111,131,347,501,503,521,529,533,555,565,577,361,155,169]
Very_Good = [5,39,45,203,205,415,421,55,67,77,249,253,263,291,293,449,477,483,489,127,307,309,313,331,335,339,499,515,537,547,553,575,593,597,599,601,367,151,165,177,189,191,247]
Very_Very_Bad = [231,277,287,485,557,569,187]
Very_Very_Good = [411,305,511,535,539,545,579,583,355,375]

Answer = random.choice(All)
result_message = ""
if Answer in Bad:
    b = f"""{Answer} صفحه
    بد"""
    result_message = b
elif Answer in Good:
    g = f"""{Answer} صفحه
    خوب"""
    result_message = g   
elif Answer in Middle:
    m = f"""{Answer} صفحه
    میانه"""
    result_message = m    
elif Answer in Middle_Bad:
    mb= f"""{Answer} صفحه
    میانه بد"""
    result_message = mb 
elif Answer in Middle_Good:
    mg = f"""{Answer} صفحه
    میانه خوب"""
    result_message = mg 
elif Answer in Very_Bad:
    vb = f"""{Answer} صفحه
    خیلی بد"""
    result_message = vb 
elif Answer in Very_Good:
    vg = f"""{Answer} صفحه
    خیلی خوب"""
    result_message = vg 
elif Answer in Very_Very_Bad:
    vvb = f"""{Answer} صفحه
    خیلی خیلی بد"""
    result_message = vvb 
else:
    vvg = f"""{Answer} صفحه
    خیلی خیلی خوب"""
    result_message = vvg 

def fetch_details(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract the required details with error handling
        overall_result = soup.find("span", id="L_Result_General")
        marriage_result = soup.find("span", id="L_Result_Marriage")
        trade_result = soup.find("span", id="L_Result_Trade")
        surah = soup.find("span", id="L_Chapter_Name")
        verse = soup.find("span", id="L_Ayeh")
        
        # Use default values if elements are not found
        overall_result = overall_result.text.strip() if overall_result else "نامشخص"
        marriage_result = marriage_result.text.strip() if marriage_result else "نامشخص"
        trade_result = trade_result.text.strip() if trade_result else "نامشخص"
        surah = surah.text.strip() if surah else "نامشخص"
        verse = verse.text.strip() if verse else "نامشخص"
        
        return overall_result, marriage_result, trade_result, surah, verse
    except Exception as e:
        return "خطا در دریافت اطلاعات", "خطا در دریافت اطلاعات", "خطا در دریافت اطلاعات", "خطا در دریافت اطلاعات", "خطا در دریافت اطلاعات"

def open_webpage(url):
    webbrowser.open(url)

Webpage = f"https://old.aviny.com/quran/estekhareh/index2.aspx?page={Answer}"    

# Fetch details from the webpage
overall_result, marriage_result, trade_result, surah, verse = fetch_details(Webpage)

root = tk.Tk()
root.title("استخاره")

# Create a label for the result message
result_label = tk.Label(root, text=result_message, font=("Arial", 10), padx=100, pady=15)
result_label.pack()

# Display the fetched details
details = f"""
نتیجه کلی: {overall_result}
نتیجه ازدواج: {marriage_result}
نتیجه معامله: {trade_result}
سوره: {surah}
آیه: {verse}
"""
details_label = tk.Label(root, text=details, font=("Arial", 10), justify="right", padx=10, pady=10)
details_label.pack()

# Create a clickable hyperlink
link = tk.Label(root, text="لینک: باز کردن صفحه", font=("Arial", 10), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e: open_webpage(Webpage))

# Run the tkinter main loop
root.mainloop()
