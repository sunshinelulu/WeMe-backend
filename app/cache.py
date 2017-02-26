import redis

redis_store = redis.Redis(password="rediscacheserver")

KEY_PREFIX = 'WEME'

#community
COMMUNITY_KEY_PREFIX = "{}:community".format(KEY_PREFIX)
COMMUNITY_TOPIC_HOTINDEX_KEY = "{}:topic_hotindex".format(COMMUNITY_KEY_PREFIX)

#USER
USER_KEY_PREFIX = "{}:user".format(KEY_PREFIX)
RECOMMEND_USER_KEY = "{}:recommend_user".format(USER_KEY_PREFIX)
RECOMMEND_USER_MALE_KEY = "{}:recommend_user_male".format(USER_KEY_PREFIX)
RECOMMEND_USER_FEMALE_KEY = "{}:recommend_user_female".format(USER_KEY_PREFIX)
RECOMMEND_USER_NEW_REGISTERED_MALE_KEY = "{}:recommend_new_registered_male".format(USER_KEY_PREFIX)
RECOMMEND_USER_NEW_REGISTERED_FEMALE_KEY = "{}:recommend_new_registered_female".format(USER_KEY_PREFIX)
RECOMMEND_USER_PREF_KEY = "{}:recommend_user_preference".format(USER_KEY_PREFIX)
RECOMMEND_USER_FLAG = "{}:recommend_user_flag".format(USER_KEY_PREFIX)

def clear_redis():
	redis_store.delete(COMMUNITY_TOPIC_HOTINDEX_KEY, RECOMMEND_USER_KEY, 
					RECOMMEND_USER_MALE_KEY, RECOMMEND_USER_FEMALE_KEY, RECOMMEND_USER_NEW_REGISTERED_FEMALE_KEY,
					RECOMMEND_USER_NEW_REGISTERED_MALE_KEY, RECOMMEND_USER_PREF_KEY, RECOMMEND_USER_FLAG)
