###############################################################################
#### DO NOT EDIT THIS SECTION
###############################################################################
from typing import Dict, Any, List, Tuple, Optional
from shared_utils import set_weighted_score_data
from scaffolded_writing.cfg import ScaffoldedWritingCFG
from scaffolded_writing.student_submission import StudentSubmission
from shared_utils import grade_question_parameterized

def generate(data: Dict[str, Any]) -> None:
    data["params"]["subproblem_definition_cfg"] = PROBLEM_CONFIG.to_json_string()

def grade(data: Dict[str, Any]) -> None:
    grade_question_parameterized(data, "subproblem_definition", grade_statement)
    set_weighted_score_data(data)

###############################################################################
#### DO NOT EDIT ABOVE HERE, ONLY EDIT BELOW
###############################################################################

statement = 'You want to play a song. How will you go about doing so?'

PROBLEM_CONFIG = ScaffoldedWritingCFG.fromstring(f"""
    START -> "Play" PLAY
    PLAY -> ARTIST PLAY_LOCATION INSTRUMENT | EPSILON
    ARTIST -> "Vulfpeck" | "Janice Kapp Perry" | "Taylor Swift"
    PLAY_LOCATION -> "in church" | "at the quad" | "at home"
    INSTRUMENT -> "with a trombone" | "with a violin" | "with a guitar"
    EPSILON ->
""")

def grade_statement(tokens: List[str]) -> Tuple[bool, Optional[str]]:
    submission = StudentSubmission(tokens, PROBLEM_CONFIG)

    if submission.does_path_exist("ARTIST", "Vulfpeck") and \
        submission.does_path_exist('PLAY_LOCATION', 'in church'):
        return False, 'Vulfpeck is great, but not in the context of church. consider playing somewhere else.'

    if submission.does_path_exist("ARTIST", "Taylor Swift"):
        return False, 'It\'s best to sing Taylor Swift songs rather than play them. Try again.'

    if submission.does_path_exist("ARTIST", "Vulfpeck") and \
        submission.does_path_exist('INSTRUMENT', 'with a violin'):
        return False, 'Yeah that doesn\'t really work. You\'d better use a different instrument if you want to play Vulfpeck'

    if submission.does_path_exist("PLAY_LOCATION", "at home"):
        return False, 'No need to play at home anymore. You\'ve practiced. Go out and play!'

    if submission.does_path_exist("ARTIST", "Janice Kapp Perry") and \
        submission.does_path_exist('PLAY_LOCATION', 'at the quad'):
        return False, 'Her music is a bit soft. Not many people will be able to hear it'
    

    if submission.does_path_exist("ARTIST", "Vulfpeck") and \
        submission.does_path_exist('PLAY_LOCATION', 'at the quad') and \
            submission.does_path_exist('INSTRUMENT', 'with a guitar'):
        return True, 'Yep. That\'s the ultimate combo.'
    
    


    return True, None


