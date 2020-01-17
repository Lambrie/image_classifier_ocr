import pickle
import nltk
from googletrans import Translator
from __pickle_processing__ import checkFile, readFile

translator = Translator()
tc = nltk.classify.textcat.TextCat()

def split_words_in_english(inOCR_img):
    if not inOCR_img: {}
    resumeDD = None
    if checkFile("ocr_nlp_trained_data.pickle","pickles\\"):
        resumeDD = readFile("ocr_nlp_trained_data.pickle","pickles\\")

    ocr_nltk_output = {}
    count = 0
    for key, value in inOCR_img.items():
        if resumeDD:
            if key in resumeDD:
                ocr_nltk_output[key] = resumeDD[key]
                count += 1
                print(count)
                continue

        tokenized_word = nltk.tokenize.word_tokenize(value[0])
        tokenized_word = [''.join(e for e in str if e.isalnum()) for str in tokenized_word]

        fdist_tokenized_word = nltk.probability.FreqDist(tokenized_word)

        stop_words = set(nltk.corpus.stopwords.words("english"))
        stop_words.add("")
        filtered_word = []
        for w in tokenized_word:
            if w not in stop_words:
                filtered_word.append(w)

        # try:
        #     eng_filtered_word = google_translate(filtered_word)
        # except Exception as e:
        #     eng_filtered_word = filtered_word
        #     print(e)
        # eng_fdist_filtered_word = nltk.probability.FreqDist(eng_filtered_word)

        eng_fdist_filtered_word = nltk.probability.FreqDist(filtered_word)

        eng_filtered_word = []
        for w in eng_fdist_filtered_word:
            if w not in stop_words:
                eng_filtered_word.append(w)
        ocr_nltk_output[key] = eng_filtered_word

        count += 1
        print(count)

        if ocr_nltk_output:
            with open("ocr_nlp_trained_data.pickle", "wb") as handle:
                pickle.dump(ocr_nltk_output, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('ocr_nlp_trained_data.pickle', 'wb') as handle:
        pickle.dump(ocr_nltk_output, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return ocr_nltk_output

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def google_translate(inDist_filtered_word):
    language_detect_count = {}
    eng_dist_filtered_word = {}

    wordList = []
    for word in inDist_filtered_word:
        if not is_number(word) and len(str(word)) > 1:
            wordList.append(word)
    text = ",".join(wordList)
    language_detect_bulk = translator.translate(text=text, src='auto', dest='en')

    language_detect_cde = str(language_detect_bulk.src)
    translated_text_list = str(language_detect_bulk.text).split(",")
    orig_text_list = str(language_detect_bulk.origin).split(",")

    eng_dist_filtered_word = []
    if language_detect_cde in ["it", "ita", "es" , "spa" , "fr" , "fra", "fre", "de", "deu", "ger"]:
        # if len(orig_text_list) == len(translated_text_list):
        #     for i in range(len(orig_text_list)):
        #         eng_dist_filtered_word.append({"original_text":str(orig_text_list[i])\
        #                                           , "translated_text":str(translated_text_list[i])\
        #                                           , "count":int(inDist_filtered_word[orig_text_list[i]])})
        # elif len(orig_text_list) > len(translated_text_list):
        #     for i in range(len(translated_text_list)):
        #         eng_dist_filtered_word.append({"original_text":str(orig_text_list[i])\
        #                                           , "translated_text":str(translated_text_list[i])\
        #                                           , "count":int(inDist_filtered_word[orig_text_list[i]])})
        # elif len(orig_text_list) < len(translated_text_list):
        #     for i in range(len(orig_text_list)):
        #         eng_dist_filtered_word.append({"original_text":str(orig_text_list[i])\
        #                                           , "translated_text":str(translated_text_list[i])\
        #                                           , "count":int(inDist_filtered_word[orig_text_list[i]])})
        # else:
        #     for i in range(len(orig_text_list)):
        #         eng_dist_filtered_word.append({"original_text": "" \
        #                                           , "translated_text": str(translated_text_list[i]) \
        #                                           , "count": 0})
        return translated_text_list
    elif language_detect_cde in ["en","eng"]:
        return wordList
    else:
        return eng_dist_filtered_word





# def google_translate(inDist_filtered_word):
#     language_detect_count = {}
#     eng_dist_filtered_word = {}
#     for word, value in inDist_filtered_word.items():
#         if not str(word).isnumeric():
#             language_detect = translator.translate(text=word, src='auto', dest='en')
#             if language_detect:
#                 language_detect_cde = str(language_detect.src)
#                 if language_detect_cde in ["it", "ita", "en" , "es" , "spa" , "fr" , "fra", "fre", "de", "deu", "ger"]:
#                     if language_detect.extra_data["confidence"] >= 0.8:
#                         if language_detect_cde in language_detect_count:
#                             language_detect_count[language_detect_cde] = int(language_detect_count[language_detect_cde]) + 1
#                             eng_dist_filtered_word[language_detect.text] = value
#                         else:
#                             language_detect_count[language_detect_cde] = 1
#                             eng_dist_filtered_word[language_detect.text] = value
#                     else:
#                         inDist_filtered_word[word] = 0
#                 else:
#                     inDist_filtered_word[word] = 0
#     return eng_dist_filtered_word


