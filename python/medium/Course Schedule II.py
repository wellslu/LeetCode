class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        study_first = {}
        courses = set([i for i in range(numCourses)])
        for course, ex_course in prerequisites:
            if course in study_first:
                study_first[course].add(ex_course)
            else:
                study_first[course] = set([ex_course])
        
        already_study_set = courses.difference(study_first.keys())
        already_study = list(already_study_set)
        while study_first:
            study = set()
            for course in study_first:
                if study_first[course].issubset(already_study_set):
                    study.add(course)
            if len(study) == 0:
                return []
            already_study_set.update(study)
            already_study+=list(study)
            for k in study:
                study_first.pop(k)
        return already_study
