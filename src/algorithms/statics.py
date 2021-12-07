N_GRAM_LOWER_LIM = 1
N_GRAM_UPPER_LIM = 2
SERVER_URL = 'http://localhost:9000'
DB_CONNECTION = 'mongodb://localhost:27017'
HEADER_ROW =    [
                    "PS_TERM_ID",
                    "INSTRUCTOR_NAME",
                    "COURSE_UNIQUE_ID",
                    "RESPONSE_UNIQUE_ID",
                    "QUESTION_ID",
                    "RESPONSE_TEXT",
                    "RESPONSE_NUM",
                    "INSTRUCTOR_ENROLLMENTS",
                    "STUDENT_ENROLLMENTS",
                    "STUDENT_RESPONDENTS",
                    "COURSE_RESPONSE_RATE","OPTOUTS",
                    "OPTOUT_RATE",
                    "RESPONDENTS_COMPLETE",
                    "RESPONDENTS_COMPLETE_RATE",
                    "COURSE_TITLE",
                    "PS_COURSE_ID",
                    "PS_CLASS_ID",
                    "PS_COMBINED_SECTION_ID",
                    "CLASS_TYPE",
                    "CLASS_LEVEL",
                    "DEPT_CODE",
                    "SCHOOL_CODE",
                    "SCHOOL_NAME",
                    "DEPT_NAME",
                    "CLASS_LOCATION",
                    "INSTRUCTION_MODE",
                    "QUESTION_TEXT",
                    "ANSWER_SET_TEXT",
                    "ANSWER_SET_NUM"
                ]
                
RELEVANT_ROWS = [
                    "COURSE_UNIQUE_ID",
                    "COURSE_TITLE",
                    "INSTRUCTOR_NAME",
                    "QUESTION_ID",
                    "QUESTION_TEXT",
                    "RESPONSE_TEXT"
                ]
                