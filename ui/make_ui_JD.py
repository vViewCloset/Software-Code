import cat_predict as cp
import att_predict as ap
import color_re as cr

def print_ui(cat, att,cat_score,att_score,color):
    att_len = 13; cat_len = 13;color_len = 30
    if len(att) % 2 == 0:
        att = att + ' '
    if len(cat) % 2 == 0:
        cat = cat + ' '

    att_blank = int((att_len - len(att))/2)
    cat_blank = int((cat_len - len(cat))/2)
    color_blank = int((color_len - len(color))/2)

    att_list = []; cat_list =[];color_list = []
    
    for i in range(att_blank):
        att_list.append(' ')

    att_list.append(att)
    
    for i in range(att_blank):
        att_list.append(' ')
 
    att_txt = ''.join(att_list)
    
    for i in range(cat_blank):
        cat_list.append(' ')
  
    cat_list.append(cat)

    for i in range(cat_blank):
        cat_list.append(' ')
 
    cat_txt = ''.join(cat_list)
    
    color_txt = '지금 고른 의상은 ' + color + ' 색상입니다.'

    print(' ----------------------------------')
    print('|        |  판단결과   |   정확도  |')
    print(' ----------------------------------')
    print('|  종류  |' + cat_txt + '|    ' + cat_score + '  |')
    print(' ----------------------------------')
    print('|  속성  |' + att_txt + '|    ' + att_score + '   |')
    print(' ----------------------------------')
    print('')
    print(color_txt)
    print('')
cat, cat_score = cp.category_total()
att, att_score = ap.attribute_total()
color = cr.color_total()

print_ui(cat, att, cat_score, att_score,color)
