class Ricky:
    def __init__(self,id,name,status,species,typee,gender,origin_name,location_name,
    image,created,dimension,episode_id,episode_name,episode_air_date,episode):
        self.id=id
        self.name=name
        self.status=status
        self.species=species
        self.typee=typee
        self.gender=gender
        self.origin_name=origin_name
        self.location_name=location_name
        self.image=image
        self.created=created
        self.dimension=dimension
        self.episode_id=episode_id  
        self.episode_name=episode_name
        self.episode_air_date=episode_air_date
        self.episode=episode
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'species': self.species,
            'typee': self.typee,
            'gender': self.gender,
            'origin_name': self.origin_name,
            'location_name': self.location_name,
            'image': self.image,
            'created': self.created,
            'dimension': self.dimension,
            'episode_id': self.episode_id,
            'episode_name': self.episode_name,
            'episode_air_date': self.episode_air_date,
            'episode': self.episode
        }