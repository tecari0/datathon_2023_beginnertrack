import math
# read the file, collect data; 2010-2019 National && State population
with open("female_populationSet_2019.txt", "r") as P_Set:
    Total_population = [line.strip().split(',')
                        for line in P_Set if (line.strip().split(',')[5] == "2")]

# read the file, collect data; female morbidity rate and age range
with open("female_morbidity_rate.txt", "r") as F_morbidity:
    female_mor = [line.strip().split(',') for line in F_morbidity]
    # print(female_mor)

with open("Each_State_Facility.txt", "r") as Facility_num:
    each_fac = [line.strip().split(' ') for line in Facility_num]
for inner_list in each_fac:
    for index, value in enumerate(inner_list):
        if value.strip():
            inner_list[index] = value.strip()
        else:
            inner_list[index] = None
facility_num = [[value for value in inner_list if value]
                for inner_list in each_fac]


def each_state_ppl_age(Total_population, female_mor):  # 按照年龄阶段收集各个州的人口数-2019
    # get the age range from female-morbidity group
    age_range = [elem[0].strip().split("-") for elem in female_mor]
    age_range.pop(0)
    All_State_Age_Range = {}
    State_Name = []

    count_state = 0  # count how many States exist
    # print(len(Total_population))
    for i in range(0, len(Total_population)):
        if(i < len(Total_population)-1 and Total_population[i][4] == Total_population[i+1][4]):
            # print(i)
            continue
        elif(i == len(Total_population)-1):
            # print(i,"第二")
            count_state += 1
            State_Name.append(Total_population[i][4])
            break
        else:
            count_state += 1
            State_Name.append(Total_population[i][4])

    # print(State_Name)
    for num_S in range(count_state):  # 把每个州的年龄段总人数输入成一个dic并输出
        #State_total_pop = 0
        All_State_Age_Range[State_Name[num_S]] = {}
        for i in range(len(age_range)):  # age_range 是female_mor的年龄段，in string
            check_age = age_range[i]  # 把female_mor的年龄段打出来
            # print(check_age,"看")
            # 把["1","4"]的年龄段形式变成[1,2,3,4]，方便后续计算total值
            if(len(check_age) == 2):
                State_total_pop = 0
                comput_range = list(
                    range(int(check_age[0]), int(check_age[1])+1))
                # print(comput_range)
                for cal in range(len(Total_population)):  # 把每一个年龄段的population 总数计算出来了
                    # print(Total_population)
                    if(int(Total_population[0][6]) in comput_range):
                        State_total_pop += int(Total_population[0][-1])
                        # print(State_total_pop)
                        Total_population.pop(0)
                        cal -= 1
                    elif(int(Total_population[0][6]) > comput_range[-1]):
                        break
                #All_State_Age_Range[State_Name[num_S]] = {}
                All_State_Age_Range[State_Name[num_S]
                                    ][female_mor[i+1][0]] = State_total_pop
                # print(All_State_Age_Range)
                # for age in range
                # print(age1,age2)
            elif(len(check_age) == 1 and check_age[0] == "0"):
                age1 = check_age[0]
                All_State_Age_Range[State_Name[num_S]][age1] = int(
                    Total_population[0][-1])
                #print(Total_population[0], "我进来了")
                Total_population.pop(0)
            elif(len(check_age) == 1 and check_age[0] == "85"):
                age1 = check_age[0]
                All_State_Age_Range[State_Name[num_S]]["85"] = int(
                    Total_population[0][-1])
                Total_population.pop(0)
                Total_population.pop(0)
                # print(Total_population[0],"我进来了")
                # All_State_Age_Range[State_Name[num_S]][age1] =
            # All_State_Age_Range[State_Name[num_S]][female_mor[i][0]]
        # print(All_State_Age_Range)
    #print(All_State_Age_Range["United States"])
    return All_State_Age_Range, State_Name, female_mor
    # print(All_State_Age_Range)


def delete_rows(All_State_Age_Range, State_Name, female_mor):
    for i in range(len(State_Name)):
        for j in range(0, 4):
            del All_State_Age_Range[State_Name[i]][female_mor[j+1][0]]
    # print(All_State_Age_Range)
    return All_State_Age_Range


def sum_up(All_State_Age_Range, State_Name, female_mor):  # 求每个州的发病率
    morbidity = []
    sick_rate = [elem[1] for elem in female_mor]
    for i in range(0, 5):
        sick_rate.pop(0)

    for i in range(len(sick_rate)):  # 发病率的小数形式，len = 15
        sick_rate[i] = float(sick_rate[i])*0.00001

    for i in range(len(All_State_Age_Range)):
        sum = 0
        curr = 5  # 年龄阶段从15开始，index为5
        for j in range(len(sick_rate)):
            population = All_State_Age_Range[State_Name[i]
                                             ][female_mor[curr][0]]
            possi = sick_rate[j]
            curr += 1
            sum += population * possi
        morbidity.append(sum)
    return morbidity  # the sum of 发病率 in each State


All_State_Age_Range, State_Name, age_range = each_state_ppl_age(
    Total_population, female_mor)
All_State_Age_Range = delete_rows(All_State_Age_Range, State_Name, age_range)
morbidity = sum_up(All_State_Age_Range, State_Name, female_mor)
for i in range(len(morbidity)):
    print(morbidity[i])
# print(All_State_Age_Range)
# print(All_State_Age_Range)
# def age_sum_state():
