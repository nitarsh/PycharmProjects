# -*- coding: utf-8 -*-
import random
from flask import Blueprint, request, jsonify
from flask_login import current_user
from injector import inject
import math

from smartcook.advertisement.interfaces import AdRepository
from smartcook.advertisement.models import UserAdInterest, ShownAdvertisement
from smartcook.advertisement.schemas import AdvertisementSchema
from smartcook.extensions import user_login_manager, db
from smartcook.fuelpoint.interfaces import FuelPointRepository


blueprint = Blueprint("advertisement", __name__, url_prefix='/advertisements', static_folder="../static")


@blueprint.route("/in-purchase-ad-interest", methods=['POST'])
@user_login_manager.login_required
def in_purchase_ad_interest():
    data = request.json

    try:
        ad_id = data['ad_id']
        fp_id = data['fuel_point_id']
    except KeyError as e:
        return jsonify({'message': 'Missing key: {}'.format(str(e))}), 400

    db.add(UserAdInterest(
        ad_id=ad_id,
        fuel_point_id=fp_id,
        user=current_user))

    return jsonify({}), 201


@blueprint.route("/broadcast-ad-interest", methods=['POST'])
def broadcast_ad_interest():
    data = request.json

    try:
        ad_id = data['ad_id']
        fp_id = data['fuel_point_id']
        phone_number = data['phone_number']
    except KeyError as e:
        return jsonify({'message': 'Missing key: {}'.format(str(e))}), 400

    db.add(UserAdInterest(
        ad_id=ad_id,
        fuel_point_id=fp_id,
        phone_number=phone_number
    ))

    return jsonify({}), 201


@blueprint.route("/for-fuel-point/<fp_id>")
@inject(ad_repo=AdRepository, fp_repo=FuelPointRepository)
def ads_for_fuel_point(ad_repo, fp_repo, fp_id):
    fp = fp_repo.with_id(fp_id)
    ads_for_fp = [a for a in ad_repo.query
                  if (a.inpurchase_criteria or a.broadcast_criteria)
                  and (a.inpurchase_criteria or a.broadcast_criteria).sub_region_id == fp.sub_region_id]

    if not ads_for_fp:
        return jsonify({'message': 'No ads!'}), 404
    else:
        return jsonify({
            'ads': AdvertisementSchema(many=True).dump(ads_for_fp).data
        }), 200


@blueprint.route("/broadcast-ads-for-fuel-point/<fp_id>")
@inject(ad_repo=AdRepository, fp_repo=FuelPointRepository)
def broadcast_ads_for_fuel_point(ad_repo, fp_repo, fp_id):
    fp = fp_repo.with_id(fp_id)

    all_broadcast_ads = [a for a in ad_repo.all() if a.broadcast_criteria]
    ads_for_fp = [ad for ad in all_broadcast_ads if ad.broadcast_criteria.sub_region_id == fp.sub_region_id]

    no_of_time_slots = 24 * 60 * 60 / 30
    curr_slot = 0
    ads_with_time_slots = {}
    while curr_slot < no_of_time_slots:
        random_ad = random.choice(ads_for_fp)
        ads_with_time_slots[curr_slot] = AdvertisementSchema().dump(random_ad).data
        curr_slot += int(math.ceil(random_ad.duration / 30.0))

    if not ads_for_fp:
        return jsonify({'message': 'No ads!'}), 404
    else:
        return jsonify(ads_with_time_slots), 200


@blueprint.route("/inpurchase-ads-for-fuel-point/<fp_id>")
@inject(ad_repo=AdRepository, fp_repo=FuelPointRepository)
def inpurchase_ads_for_fuel_point(ad_repo, fp_repo, fp_id):
    fp = fp_repo.with_id(fp_id)

    all_inpurchase_ads = [a for a in ad_repo.all() if a.inpurchase_criteria]
    ads_for_fp = [ad for ad in all_inpurchase_ads if ad.inpurchase_criteria.sub_region_id == fp.sub_region_id]

    if not ads_for_fp:
        return jsonify({'message': 'No ads!'}), 404
    else:
        return jsonify({
            'inpurchase_ads': AdvertisementSchema(many=True).dump(ads_for_fp).data
        }), 200


@blueprint.route("/ads-played-by-fuel-point/")
def ads_played_by_fuel_point():
    data = request.args

    ad_ids = data['ad_ids']
    fuel_point_id = data['fuel_point_id']

    for id in ad_ids:
        shown_ad = ShownAdvertisement(fuel_point_id=fuel_point_id, ad_id=id)
        db.add(shown_ad)

    return jsonify({}), 201
