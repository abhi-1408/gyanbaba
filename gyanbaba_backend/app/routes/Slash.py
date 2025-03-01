from ..services.joke import get_joke
from ..services.quote import get_quote
from ..services.meme import get_all_meme
from ..services.video import get_video
from ..services.resource import load_data,add_vote,load_meme_from_api
from ..services.user import load_user
from ..services.test import get_test
from ..services.schedule import getschedule,addschedule
import json
from . import slash
from flask import request


@slash.route('/')
def g_home():
    
    return json.dumps('slash Home')


@slash.route('/getschedule/<view_id>')
def g_res(view_id):
    data = getschedule(view_id)
    return json.dumps(data)

@slash.route('/addschedule',methods=['POST','GET'])
def p_res():
    data = request.form.to_dict()
    # view_id=request.json['view_id']
    # col_name=request.json['col_name']
    # col_val=request.json['col_value']
    view_id=data['view_id']
    col_name=data['col_name']
    col_val=data['col_value']
    data = addschedule(view_id,col_name,col_val)
    return json.dumps('added in schedule')


@slash.route('/joke')
def g_joke():
    # channel_id
    channel_id=request.args['channel_id']
    #print('****(((((((******<<<<<<<<JOKE>>>>>>>>>>**********',channel_id)
    joke=get_joke(channel_id)
    # print('in slash route',quote['payload'])

    # return json.dumps({'joke':[dict(row) for row in obj_joke]})
    return json.dumps(joke['payload'][0])
    # print('**********************',joke[0][1])


@slash.route('/getallmeme')
def g_meme():
    # channel_id
    
    meme=get_all_meme()
    # print('in slash route',quote['payload'])

    # return json.dumps({'joke':[dict(row) for row in obj_joke]})
    return json.dumps(meme['payload'])
    # print('**********************',joke[0][1])



@slash.route('/quote')
def g_quote():
    channel_id=request.args['channel_id']
    #print('****(((((((******<<<<<<<<QUOTE>>>>>>>>>>**********',channel_id)
    
    quote=get_quote(channel_id)
    #print('in slash route',quote['payload'])

    # return json.dumps({'joke':[dict(row) for row in obj_joke]})
    return json.dumps(quote['payload'][0])

    # quote=get_quote()
    # print('in slash route',quote['payload'])

    # # return json.dumps({'joke':[dict(row) for row in obj_joke]})
    # return (quote['payload'])
    

@slash.route('/video')
def g_video():
    channel_id=request.args['channel_id']
    #print('****(((((((******<<<<<<<<VIDEO>>>>>>>>>>**********',channel_id)
    video=get_video(channel_id)
    # print('in slash route',quote['payload'])

    # return json.dumps({'joke':[dict(row) for row in obj_joke]})
    # return json.dumps(video['payload'])
    #print('**********************',video)

    return json.dumps(video['payload'][0])



@slash.route('/addvote/<res_id>',methods=['POST'])
def g_add_vote(res_id):
    user_id=request.json['user_id']
    # user_id=2
    # vote=request.json['vote_value']

    # up_votes,down_votes
    vote_name=request.json['vote_name']

    dd=add_vote({'res_id':res_id,'user_id':user_id,'vote_name':vote_name})

    

    return json.dumps(dd['payload'][0])


@slash.route('/load')
def g_load():
    load_data()
    # load_user()
    return json.dumps('loaded data')


@slash.route('/test')
def g_test():
    # channel_id=request.json['channel_id']
    d=load_meme_from_api()
    return json.dumps(d)