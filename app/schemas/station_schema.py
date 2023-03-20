from app.utils.schemas import ma

class StationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'temperature', 'humidity', 'created_at')