# import dic
# words_dict = dic.dic_list
 

ans_reverse=[]  #存放逆向匹配的结果
#实现逆向最大匹配算法中的切词方法
def cut_words(raw_sentence,words_dict):
    #max_length=5    #分词字典中最大长度字符串的长度
    #要是分词字典列表中最大长度字符串的长度一眼看不出来，可采用下一行的形式
    max_length=len(sorted(words_dict, key=lambda x: len(x))[-1])
    #1、正向最大匹配
    len_row=len(raw_sentence)
    while len_row>0 :
        divide = raw_sentence[-max_length:]
        while divide not in words_dict:
            if len(divide)==1:
                break
            divide=divide[1:]   #注意这里缩短截取字符串是缩短前部分，保留后部分
        ans_reverse.append(divide)
        raw_sentence = raw_sentence[0:len(raw_sentence)-len(divide)]
        len_row = len(raw_sentence)
    #print("\'逆向最大匹配\'的分词结果为：",ans_reverse[::-1])#注意是倒序输出
    return ans_reverse
 
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