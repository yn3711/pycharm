from googleapiclient.discovery import build

YOUTUBE_API_KEY = 'AIzaSyCuYF9plierj9IxVNAz_2j3yudHy-_CAuQ'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
part='snippet',
#検索したい文字列を指定
q='ボードゲーム',
#視聴回数が多い順に取得
order='viewCount',
type='video',
).execute()

search_response['items'][0]

#numに入れた数字×5件の情報を取得
#その他のパラメーターはAPIから情報を取得するパラメータと同じ
def get_video_info(part, q, order, type, num):
    dic_list = []
    search_response = youtube.search().list(part=part,q=q,order=order,type=type)
    output = youtube.search().list(part=part,q=q,order=order,type=type).execute()

    #一度に5件しか取得できないため何度も繰り返して実行
    for i in range(num):
        dic_list = dic_list + output['items']
        search_response = youtube.search().list_next(search_response, output)
        output = search_response.execute()


        print(dic_list)
'''
    df = pd.DataFrame(dic_list)
    #各動画毎に一意のvideoIdを取得
    df1 = pd.DataFrame(list(df['id']))['videoId']
    #各動画毎に一意のvideoIdを取得必要な動画情報だけ取得
    df2 = pd.DataFrame(list(df['snippet']))[['channelTitle','publishedAt','channelId','title','description']]
    ddf = pd.concat([df1,df2], axis = 1)

    return ddf
'''


get_video_info(part='snippet',q='ボードゲーム',order='viewCount',type='video',num = 20)