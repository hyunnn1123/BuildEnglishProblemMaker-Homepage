# -*- coding: utf-8 -*-
import gradio as gr
import random

def beVerbVariation(originalContent):
    if(originalContent == ""):
        return "본문을 입력하지 않았습니다"
    content = originalContent
    #beVerbList_simpleTense = ['is', 'am', 'are'] #am과 is의 구분은 너무 쉬워서 제외 함
    beVerbList_simpleTense = ['is', 'are']
    beVerbList_pastTense   = ['was', 'were']
    for verb in beVerbList_simpleTense:
        content = content.replace(" " + verb + " ", " ***" + beVerbList_simpleTense[random.randint(0, len(beVerbList_simpleTense) - 1)] + "*** ")
    for verb in beVerbList_pastTense:
        content = content.replace(" " + verb + " ", " ***" + beVerbList_pastTense[random.randint(0, len(beVerbList_pastTense) - 1)] + "*** ")
    return content

def orderVariation(originalContent):
    if(originalContent == ""):
        return "본문을 입력하지 않았습니다"
    content = originalContent.split(".")
    if "" in content:
        content.remove("")
    if(len(content) < 6):
        return "7개 이상의 문장으로 구성되어 있는 지문만 순서 문제를 제작할 수 있습니다"
    firstMassCut = round(len(content) / 3)
    secondMassCut = firstMassCut * 2
    firstMassContent = ""
    for firstIndex in range(0, firstMassCut):
        firstMassContent = firstMassContent + content[firstIndex] + "."
    secondMassContent = ""
    for secondIndex in range(firstMassCut + 1, secondMassCut):
        secondMassContent = secondMassContent + content[secondIndex] + "."
    thirdMassContent = ""
    for thirdIndex in range(secondMassCut + 1, len(content)):
        thirdMassContent = thirdMassContent + content[thirdIndex] + "."
    contentList = [firstMassContent, secondMassContent, thirdMassContent]
    shuffledList = contentList.copy()
    random.shuffle(shuffledList)
    firstOrder = 0
    secondOrder = 0
    thirdOrder = 0
    for i in range(len(shuffledList)):
        if shuffledList[i] == contentList[0]:
            firstOrder = ['A', 'B', 'C'][i]
        elif shuffledList[i] == contentList[1]:
            secondOrder = ['A', 'B', 'C'][i]
        else:
            thirdOrder = ['A', 'B', 'C'][i]

    return "[A] " + shuffledList[0] + "\n\n[B] " + shuffledList[1] + "\n\n[C] " + shuffledList[2] + "\n\n\n** 정답: " + firstOrder + " --> " + secondOrder + " --> " + thirdOrder

def blankVariation(originalContent):
    if(originalContent == ""):
        return "본문을 입력하지 않았습니다"
    content = originalContent.split(".")
    if "" in content:
        content.remove("")
    if(len(content) < 6):
        return "7개 이상의 문장으로 구성되어 있는 지문만 빈칸 문제를 제작할 수 있습니다"
    sentenceNumToRemove = random.randint(0, len(content)-1)
    removedSentence = content[sentenceNumToRemove]
    content[sentenceNumToRemove] = "________________"
    return "다음 빈칸에 들어갈 말로 가장 적절한 것을 고르시오.\n\n" + ". ".join(content) + "\n\n\n** 정답: " + removedSentence

def insert_shuffle(num):
    sentenceNum = num.copy()
    random.shuffle(sentenceNum)
    first = sentenceNum.pop()
    second = sentenceNum.pop()
    third = sentenceNum.pop()
    fourth = sentenceNum.pop()
    fifth = sentenceNum.pop()
    return [first, second, third, fourth, fifth]

def insertVariation(originalContent):
    if(originalContent == ""):
        return "본문을 입력하지 않았습니다"
    content = originalContent.split(".")
    if "" in content:
        content.remove("")
    if(len(content) < 6):
        return "7개 이상의 문장으로 구성되어 있는 지문만 삽입 문제를 제작할 수 있습니다"
    sentenceNum = [*range(0, len(content))]
    data = insert_shuffle(sentenceNum)
    error = 0
    while(True):
        if abs(data[0] - data[1]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)
        elif abs(data[0] - data[2]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)     
        elif abs(data[0] - data[3]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)
        elif abs(data[0] - data[4]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)
        elif abs(data[1] - data[2]) < 2:
            error = error + 1 
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)
        elif abs(data[1] - data[3]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)
        elif abs(data[1] - data[4]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)  
        elif abs(data[2] - data[3]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum) 
        elif abs(data[2] - data[4]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum) 
        elif abs(data[3] - data[4]) < 2:
            error = error + 1
            print("  [!] 삽입 문제 | 사용할 수 없는 경우의 수 ([" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]) 가 발생하여 새로운 경우의 수를 찾고 있습니다.. " + str(error) + "번째 시도중")
            data = insert_shuffle(sentenceNum)  
        else:
            print("  [!] 삽입 문제 | 사용할 수 있는 경우의 수를 찾았습니다: [" + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + "]")
            break
    first = data[0]
    second = data[1]
    third = data[2]
    fourth = data[3]
    fifth = data[4]
    removedSentence = content[first]
    content[first]  = "● ★"
    content[second] = "● " + content[second]
    content[third]  = "● " + content[third]
    content[fourth] = "● " + content[fourth]
    content[fifth]  = "● " + content[fifth]
    textedContent = ". ".join(content)
    textedContent = textedContent.replace("●", "①", 1)
    textedContent = textedContent.replace("●", "②", 1)
    textedContent = textedContent.replace("●", "③", 1)
    textedContent = textedContent.replace("●", "④", 1)
    textedContent = textedContent.replace("●", "⑤", 1)
    textedContent = textedContent.replace("★.", "")
    content = textedContent.split(".")
    if "" in content:
        content.remove("")
    return "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.\n\n[ " + removedSentence + " ]\n\n" + textedContent.replace("★", "") + "\n\n\n** 정답: " + content[first][0:3]


problem_type = ["빈칸 문제", "삽입 문제", "순서 배열 문제", "be 동사 변형 문제"]


def createProblems(context, problem):
    value = ["문제가 생성되지 않았습니다"] * len(problem_type)
    for i in range(len(problem)):
        if problem[i] == problem_type[0]:
            value[0] = blankVariation(context)
        elif problem[i] == problem_type[1]:
            value[1] = insertVariation(context)
        elif problem[i] == problem_type[2]:
            value[2] = orderVariation(context)
        elif problem[i] == problem_type[3]:
            value[3] = beVerbVariation(context)
        else:
            value = ["What The Fuck!"] * len(problem_type)
    return value[0], value[1], value[2], value[3]
        

component_context = gr.components.Textbox(interactive=True, label="영어 본문", placeholder="변형 문제를 제작할 영어 본문을 입력해주세요 (●'◡'●)\n\n참고: 최소 7줄의 본문을 입력해주세요")
component_problem_type = gr.components.CheckboxGroup(label="어떤 종류의 문제를 생성하시겠습니까?", type="value", choices=problem_type)

outputs=[]

for i in range(max(1, len(problem_type))):
    outputs.append(gr.outputs.components.Text(label="생성된 " + problem_type[i], placeholder="로딩 중..."))

demo = gr.Interface(
    fn=createProblems,
    inputs=[component_context, component_problem_type],
    outputs=outputs
)
demo.launch(share=True)


