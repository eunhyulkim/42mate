from apscheduler.schedulers.blocking import BlockingScheduler
from blocks import get_invitation_blocks
from app import db, slack
from models import User
from datetime import datetime
import json
from make_match_and_evaluation_schedule_functions import create_evaluations,\
    is_match_enable_day, get_matched_groups, create_matches_of, update_user_field,\
    let_matched_users_meet, send_match_fail_message
from send_evaluation_schedule_functions import get_target_matches, send_evaluation_message


def make_match_and_evaluation_schedule():
    """
    make match and evaluation at 00:01 for users who joined on the yesterday
    if there is a unmatched user in the end, restore the match count that was increased
    """
    print("MAKE_MATCH_AND_EVALUATION_SCHEDULE_START")
    unmatched_users = db.session.query(User).filter_by(joined=True).order_by('match_count').all()
    update_user_field(unmatched_users)
    if is_match_enable_day(unmatched_users):
        matched_groups = get_matched_groups(unmatched_users)
        matches = create_matches_of(matched_groups=matched_groups)
        let_matched_users_meet(matches)
        db.session.add_all(matches)
        evaluations = create_evaluations(matches)
        db.session.add_all(evaluations)
    if unmatched_users:
        send_match_fail_message(unmatched_users[0])
        unmatched_users[0].match_count -= 1
    print("MATCH_MAKE_SCHEDULE_ADD_AND_COMMIT_START")
    db.session.commit()
    print("MATCH_MAKE_SCHEDULE_END")


def send_evaluation_schedule():
    """
    send messages requesting evaluation of yesterday's match at 10:00 KST
    """
    target_matches = get_target_matches()
    if target_matches is None:
        return
    for match in target_matches:
        for evaluation in match.evaluations:
            send_evaluation_message(evaluation)
            evaluation.send_time = datetime.utcnow()
    db.session.commit()


def send_join_invitation_schedule():
    """
    send messages asking join of tomorrow's match at 18:00 KST
    """
    blocks = get_invitation_blocks()
    unjoined_users = db.session.query(User).filter(User.register == True, User.joined == False).all()
    for user in unjoined_users:
        slack_id = user.slack_id
        response = slack.conversations.open(users=slack_id, return_im=True)
        channel = response.body['channel']['id']
        slack.chat.post_message(channel=channel, blocks=json.dumps(blocks))


if __name__ == "__main__":
    make_match_and_evaluation_schedule()
    # sched = BlockingScheduler()
    # sched.add_job(send_evaluation_schedule, 'cron', hour=1)
    # sched.add_job(send_join_invitation_schedule, 'cron', hour=9)
    # sched.add_job(make_match_and_evaluation_schedule, 'cron', hour=15, minute=1)
    # sched.start()