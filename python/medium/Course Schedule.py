class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        study_first = {}
        study_later = {}
        all_courses = set()
        for i in prerequisites:
            v, u = i
            all_courses.add(u)
            all_courses.add(v)
            if u in study_first:
                study_first[u].add(v)
            else:
                study_first[u] = set()
                study_first[u].add(v)
            if v in study_later:
                study_later[v].add(u)
            else:
                study_later[v] = set()
                study_later[v].add(u)
        study = all_courses.difference(study_later.keys())
        can_study = set()
        
        for sl in study_later:
            if all([c in study for c in study_later[sl]]):
                can_study.add(sl)
        for cs in can_study:     
            study_later.pop(cs)
        while can_study:
            study.update(can_study)
            if len(study) == len(all_courses):
                return True
            can_study = set()
            for sl in study_later:
                if all([c in study for c in study_later[sl]]):
                    can_study.add(sl)
            for cs in can_study:     
                study_later.pop(cs)
        return False
