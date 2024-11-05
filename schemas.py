from marshmallow import Schema, fields, validate, EXCLUDE

class TranscriptSchema(Schema):
    company_name = fields.Str(required=True, validate=validate.Length(min=1))
    transcript_text = fields.Str(required=True, validate=validate.Length(min=1))

    class Meta:
        unknown = EXCLUDE  # Exclude any fields not explicitly defined
