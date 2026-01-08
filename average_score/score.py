#!/usr/bin/env python
import sys
import csv


def load_from_csv(filepath):
    """
    Read students' names and scores from given 
    csv file and return it in dict with list of subjects.
    """
    student_scores = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)

        # Readout the header
        # 이름, 국어, 수학, 영어, 과학, 사회
        header = next(csv_reader)

        for row in csv_reader:
            student_scores[row[0]] = row[1:]
    return student_scores, header[1:]


def subject_average(student_scores: dict, subjects: list):
    """
    이 반의 각 과목별 평균을 구해서 딕셔너리로 반환
    예) {"국어": 80.8, "수학": 35.3, "영어": 96.6, "과학": 85.3, "사회": 38.8}
    """
    sub_kor = 0
    sub_math = 0
    sub_eng = 0
    sub_sci = 0
    sub_soc = 0
    
    for name in student_scores:
        l = []
        for score in student_scores[name]:
            l.append(int(score))
        sub_kor += l[0]
        sub_math += l[1]
        sub_eng += l[2]
        sub_sci += l[3]
        sub_soc += l[4]
    mean_kor = sub_kor / len(student_scores.keys())
    mean_math = sub_math / len(student_scores.keys())
    mean_eng = sub_eng / len(student_scores.keys())
    mean_sci = sub_sci / len(student_scores.keys())
    mean_soc = sub_soc / len(student_scores.keys())
    score_mean = {}
    score_mean[subjects[0]] = mean_kor
    score_mean[subjects[1]] = mean_math
    score_mean[subjects[2]] = mean_eng
    score_mean[subjects[3]] = mean_sci
    score_mean[subjects[4]] = mean_soc
    return score_mean
        


def student_average(student_scores: dict):
    """
    각 학생별 전과목 평균 점수를 정렬된 튜플의 리스트로 반환
    예) [("이영희", 89.8), ("김철수", 86.6), ("박민수", 84.8)]
    """
    l = []
    for name in student_scores:
        summ = 0
        for score in student_scores[name]:
            summ += int(score)
        mean = summ / len(student_scores[name])
        l.append((name, mean))
        l.sort(key=lambda x : x[1], reverse=True)
    return l


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"USAGE: {sys.argv[0]} <csv_file>")
        sys.exit()

    student_scores, subjects = load_from_csv(sys.argv[1])
    sub_avg = subject_average(student_scores, subjects)
    stud_avg = student_average(student_scores)

    print("과목 평균:")
    for sub, avg in sub_avg.items():
        print(f"\t{sub}: {avg:.2f}")

    print("학생 점수:")
    for avg in stud_avg:
        print(f"\t{avg[0]}: {avg[1]:.2f}")
