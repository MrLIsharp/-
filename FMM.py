import dic
words_dict = dic.dic_list
 

ans_forward=[]  #存放正向匹配的结果
#实现正向最大匹配算法中的切词方法
def cut_words(raw_sentence,words_dict):
#max_length=5    #分词字典中最大长度字符串的长度
#要是分词字典列表中最大长度字符串的长度一眼看不出来，可采用下一行的形式
    max_length=len(sorted(words_dict, key=lambda x: len(x))[-1])
    #1、正向最大匹配
    len_row=len(raw_sentence)  #len_orw为当前为划分句子的长度
    while len_row>0:       #当前待划分句子长度为0时，结束划分
        divide = raw_sentence[0:max_length]    #从前向后截取长度为max_length的字符串
        while divide not in words_dict:      #当前截取的字符串不在分词字典中，则进循环
            if len(divide)==1:             #当前截取的字符串长度为1时，说明分词字典无匹配项
                break                      #直接保留当前的一个字
            divide=divide[0:len(divide)-1] #当前截取的字符串长度减一
        ans_forward.append(divide)         #记录下当前截取的字符串
        raw_sentence = raw_sentence[len(divide):]  #截取未分词的句子
        len_row = len(raw_sentence)            #记录未分词的句子的长度
   # print("\'正向最大匹配\'的分词结果为：",ans_forward)
    return ans_forward
 
# def main():
    # """
    # 用于用户交互
    # :return:
    # """
    # #init()
    # while True:
        # print("请输入要分词的序列:")
        # input_str = input()
        # if not input_str:
            # break
        # result = cut_words(input_str,words_dict)
        # #print("词典:",words_dict)
        # print("分词结果:",result)
 
# if __name__ == '__main__':
    # main()