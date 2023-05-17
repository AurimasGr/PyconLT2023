import pickle


class Preprocessor:

    def __init__(self):

        with open("src/data/PU_DO_map.pkl", 'rb') as f:
            self.pu_do_map = pickle.load(f)

    def preprocess(self, payload):

        feature_set = {"PULocationID": payload.get("PULocationID"),
                       "DOLocationID": payload.get("DOLocationID"),
                       "trip_distance": payload.get("TripDistance"),
                       "pickup_month": payload.get("PickupDatetime").month,
                       "pickup_day": payload.get("PickupDatetime").day,
                       "pickup_hour": payload.get("PickupDatetime").hour,
                       "pickup_minute": payload.get("PickupDatetime").minute,
                       "pickup_dow": payload.get("PickupDatetime").weekday(),
                       "PU_DO_num": self.pu_do_map.get(f'{payload.get("PULocationID")}_{payload.get("DOLocationID")}', 10000)}

        feature_vector = [feature_set[k] for k in feature_set]

        return [feature_vector]
