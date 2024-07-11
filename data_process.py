import pandas as pd
import numpy as np

class GeneratePrompt:
    def __init__(self, type) -> None:
        self.type = type
        self.question_template = ["我想在[YY年MM月DD日]买一注[NN]彩票，哪个号码中奖概率最高？",
                    "我计划在[YY年MM月DD日]购买一注[NN]彩票，哪些号码中奖的几率最大？",
                    "在[YY年MM月DD日]，我想买一注[NN]彩票，应该选择哪些号码？",
                    "如果我在[YY年MM月DD日]买一注[NN]彩票，哪些号码最有可能中奖？",
                    "请告诉我在[YY年MM月DD日]购买[NN]彩票时，哪些号码中奖概率最高？",
                    "我打算在[YY年MM月DD日]买一注[NN]彩票，哪些号码最有可能中奖？", 
                    "在[YY年MM月DD日]，我想买一注[NN]彩票，中奖概率最高的号码是什么？",
                    "如果我在[YY年MM月DD日]购买一注[NN]彩票，哪些号码最有希望中奖？",
                    "请预测在[YY年MM月DD日]购买[NN]彩票时，哪些号码中奖的几率最大？",
                    "预测一下[YY年MM月DD日]的[NN]彩票开奖号码。",
                    "请预测[YY年MM月DD日]的[NN]彩票中奖号码。",
                    "你能告诉我[YY年MM月DD日]的[NN]彩票可能的中奖号码吗？",
                    "预测一下在[YY年MM月DD日]，[NN]彩票的中奖号码会是什么？",
                    "请预测[YY年MM月DD日]的[NN]彩票号码。",
                    "你能预测[YY年MM月DD日]的[NN]彩票中奖号码吗？",
                    "请告诉我[YY年MM月DD日]的[NN]彩票可能的中奖号码。",
                    "预测一下[YY年MM月DD日]，[NN]彩票的中奖号码。",
                    "你能预测一下[YY年MM月DD日]的[NN]彩票号码吗？"]
        
        self.answer_template = ["我预测的号码是：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "根据我的分析，红球为 {red_balls_str}，蓝球为 {blue_balls}。",
                                "我的模型预测结果：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "本次预测的号码是：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "经过计算，我的预测是：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "预测结果如下：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "我认为这次的中奖号码是：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "根据数据分析，红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "我的预测结果是：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "预测号码：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "我推测的号码是：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "根据我的预测，红球为 {red_balls_str}，蓝球为 {blue_balls}。",
                                "我的分析结果：红球 {red_balls_str}，蓝球 {blue_balls}。"
                                "本次预测的结果是：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "经过模型计算，我的预测是：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "预测结果显示：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "我认为这次的号码是：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "根据数据分析，预测结果为红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "我的预测结果是：红球 {red_balls_str}，蓝球 {blue_balls}。",
                                "预测号码如下：红球 {red_balls_str}，蓝球 {blue_balls}。"]
        
        self.use_answer_prompt = True

    def input_prompt(self, date: pd.Timestamp):
        prompt_idx = np.random.randint(len(self.question_template))
        prompt = self.question_template[prompt_idx]
        date_text = f"{date.year}年{date.month}月{date.day}日"
        new_input = prompt.replace("[YY年MM月DD日]", date_text)
        new_input = new_input.replace("[NN]",self.type)
        return new_input
    
    def output_prompt(self, red_balls, blue_balls):
        prompt_idx = np.random.randint(len(self.answer_template))
        prompt = self.answer_template[prompt_idx]
        if self.type == "双色球":
            red_balls_str = str(f"{red_balls[0]}, {red_balls[1]}, {red_balls[2]}, {red_balls[3]}, {red_balls[4]}, {red_balls[5]}")
            blue_balls_str = str(f"{blue_balls}")
        else:
            red_balls_str = str(f"{red_balls[0]}, {red_balls[1]}, {red_balls[2]}, {red_balls[3]}, {red_balls[4]}")
            blue_balls_str = str(f"{blue_balls[0]}, {blue_balls[1]}")
        if self.use_answer_prompt:
            new_output = prompt.replace("{red_balls_str}", red_balls_str)
            new_output = new_output.replace("{blue_balls}", str(blue_balls_str))
        else:
            new_output = f"我的预测是：红球为{red_balls_str}，蓝球为{blue_balls}"
        return new_output

# gp = GeneratePrompt()

# input_1 = gp.input_prompt(date_data[2])
# print(input_1)

# output_1 = gp.output_prompt(red_balls[2],blue_balls[2])
# print(output_1)
# date_data = file["Date"]
# date_data = np.datetime64(date_data)
# date1 = date_data[0]
# year1 = date1.year()

class LotteryDataLoader:
    def __init__(self) -> None:
        type_list = ["双色球", "大乐透"]
        self.enquire_list, self.answer_list = [],[]

        for type in type_list:
            if type == "双色球":
                path = "./data/ssq_asc.txt"
                file = pd.read_csv(path,delimiter=" ")
                file.columns = ['ID', 'Date', 'Red1', 'Red2', 'Red3', 'Red4', 'Red5',
                'Red6', 'Blue', 'Out1', 'Out2', 'Out3', 'Out4', 'Out5',
                  'Out6', 'Num13', 'Num14', 'Num15', 'Num16', 'Num17',
                    'Num18', 'Num19', 'Num20', 'Num21', 'Num22', 'Num23',
                      'Num24', 'Num25', 'Num26']
            else:
                path = "./data/dlt_asc.txt"
                file = pd.read_csv(path,delimiter=" ")
                file.columns = ['ID', 'Date', 'Red1', 'Red2', 'Red3', 'Red4', 'Red5',
                    'Red6', 'Blue', 'Out1', 'Out2', 'Out3', 'Out4', 'Out5',
                     'Out6', 'Num13', 'Num14', 'Num15', 'Num16', 'Num17',
                    'Num18', 'Num19', 'Num20', 'Num21', 'Num22', 'Num23',
                      'Num24', 'Num25', 'Num26', 'n27', 'n28','29','30','31','32',
                      '33','34','35','36','37','38','39','40','41','42']
            self.type = type
            self.prompter = GeneratePrompt(self.type)
            
            self.date_data_interp = []
            self.issue_data_interp = []
            self.red_balls_data_interp = []
            self.blue_balls_data_interp = []
            self._interpolate(file)
            enquire_list, answer_list = self._prompt()
            self.enquire_list.extend(enquire_list)
            self.answer_list.extend(answer_list)


    def _interpolate(self,file) -> None:

        date_data = pd.to_datetime(file["Date"])
        # interpolate with date
        if self.type == "大乐透":
            red_balls = np.column_stack([np.array(file["Red1"]), 
                        np.array(file["Red2"]),
                        np.array(file["Red3"]),
                        np.array(file["Red4"]),
                        np.array(file["Red5"])])
            blue_balls = np.column_stack([np.array(file["Red6"]),
                                          np.array(file["Blue"])])
        else:
            red_balls = np.column_stack([np.array(file["Out1"]), 
                        np.array(file["Out2"]),
                        np.array(file["Out3"]),
                        np.array(file["Out4"]),
                        np.array(file["Out5"]),
                        np.array(file["Out6"])])
            blue_balls = np.array(file["Blue"])

        for idx in range(len(date_data)-1):
            date_now = date_data[idx]
            date_next = date_data[idx+1]
            issue_next = file["ID"][idx+1]
            red_balls_next = red_balls[idx+1]
            blue_balls_next = blue_balls[idx+1]
            delta_date = date_next - date_now
            # print(type(delta_date))
            delta_date_days = delta_date.days
            # print(int(delta_date_days))
            interpolated_date = [date_now + pd.Timedelta(days=day) for day in range(delta_date_days) ]
            interpolated_issue = [issue_next for day in range(delta_date_days)]
            interpolated_red_ball = [red_balls_next for day in range(delta_date_days)]
            interpolated_blue_ball = [blue_balls_next for day in range(delta_date_days)]
            self.date_data_interp.extend(interpolated_date)
            self.issue_data_interp.extend(interpolated_issue)
            self.red_balls_data_interp.extend(interpolated_red_ball)
            self.blue_balls_data_interp.extend(interpolated_blue_ball)

    def _prompt(self):
        enquire_list = []
        answer_list = []
        for idx,_ in enumerate(self.date_data_interp):
            enquire = self.prompter.input_prompt(self.date_data_interp[idx])
            answer = self.prompter.output_prompt(self.red_balls_data_interp[idx],self.blue_balls_data_interp[idx])
            enquire_list.append(enquire)
            answer_list.append(answer)    

        return enquire_list, answer_list
    
    def __getitem__(self, index):
        return self.enquire_list[index], self.answer_list[index]
    
    def __len__(self):
        return len(self.answer_list)