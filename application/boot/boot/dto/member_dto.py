from boot.model.member import Member
from pweb_form_rest import fields, PWebRestDTO


class MemberDetailsDTO(PWebRestDTO):
    class Meta:
        model = Member
        load_instance = True

    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    roll = fields.String(required=True, error_messages={"required": "Please enter roll"})
    technology = fields.String(required=True, error_messages={"required": "Please enter technology"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    address = fields.String(allow_none=True)


class MemberCreateDTO(MemberDetailsDTO):
    class Meta:
        model = Member
        load_instance = True

    password = fields.String(required=True, error_messages={"required": "Please enter password"})


class MemberUpdateDTO(MemberDetailsDTO):
    class Meta:
        model = Member
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"})