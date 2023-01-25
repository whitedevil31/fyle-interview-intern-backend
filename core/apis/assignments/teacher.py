from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema,GradeAssignmentSchema
teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)


@teacher_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.auth_principal
def list_assignments(p):
    """Returns list of assignments assigned to a teacher """
    teachers_assignment  = Assignment.get_assignments_of_teacher(p.teacher_id)
    teachers_assignment_dump = AssignmentSchema().dump(teachers_assignment, many=True)
    return APIResponse.respond(data=teachers_assignment_dump)


@teacher_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.auth_principal
def grade_assignment(p,payload_data):
    """Grading an assignment by teacher """
    assignment = GradeAssignmentSchema().load(payload_data)
    graded_assignment = Assignment.grade_assignment(assignment,p)
    db.session.commit()
    graded_assignment_dump =AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)


