import BMM,FMM
import dic
#使用双向最大匹配算法实现中文分词
words_dict = dic.dic_list
 

 
#实现双向最大匹配算法中的切词方法
def cut_words(raw_sentence,words_dict):
    bmm_word_list = BMM.cut_words(raw_sentence,words_dict)
    fmm_word_list = FMM.cut_words(raw_sentence,words_dict)
    bmm_word_list_size = len(bmm_word_list)
    fmm_word_list_size = len(fmm_word_list)
    if bmm_word_list_size != fmm_word_list_size:
        if bmm_word_list_size < fmm_word_list_size:
            return bmm_word_list
        else:
            return fmm_word_list
    else:
        FSingle = 0
        BSingle = 0
        isSame = True
        for i in range(len(fmm_word_list)):
            if fmm_word_list[i] not in bmm_word_list:#如果fmm和bmm的分词结果是不相同的
                isSame = False
            if len(fmm_word_list[i]) == 1:
                FSingle = FSingle + 1#如果fmm列表里的词长度为1，也就是说是单个词，那么就把单个词的数量+1
            if len(bmm_word_list[i]) == 1:
                BSingle = BSingle + 1
        if isSame:
            return fmm_word_list
        elif BSingle > FSingle:
            return fmm_word_list
        else:
            return bmm_word_list
 
 
def main():
    """
    用于用户交互
    :return:
    """
    while True:
        print("请输入要分词的序列:")
        input_str = input()
        if not input_str:
            break
        result = cut_words(input_str,words_dict)
        print("分词结果:",result)
 
if __name__ == '__main__':
    main()