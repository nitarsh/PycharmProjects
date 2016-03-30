import datetime

from flask_admin import expose
from injector import inject

from smartcook.admin import ScCustomAdminView, ScModelView
from smartcook.advertisement.interfaces import AdRepository
from smartcook.advertisement.models import Advertisement, Advertiser, BroadcastAdCriteria, InPurchaseAdCriteria
from smartcook.interfaces import Database
from smartcook.user.interfaces import UserRepository


class ManageAdvertisersView(ScModelView):

    form_excluded_columns = ['advertisements']

    def __init__(self, session, **kwargs):
        super(ManageAdvertisersView, self).__init__(Advertiser, session, **kwargs)


class ManageAdvertisementsView(ScModelView):
    can_create = True
    form_excluded_columns = ['created', 'updated',
                             'broadcast_criteria', 'inpurchase_criteria',
                             'shown_history', 'user_interests']

    def __init__(self, session, **kwargs):
        super(ManageAdvertisementsView, self).__init__(Advertisement, session, **kwargs)

    def on_model_change(self, form, model, is_created):
        file = self.edit_form().file.data

        if file:
            model.file = file.stream


class ManageBroadcastAdCriteriaView(ScModelView):
    can_create = True
    form_excluded_columns = ['created', 'updated']

    def __init__(self, session, **kwargs):
        super(ManageBroadcastAdCriteriaView, self).__init__(BroadcastAdCriteria, session, **kwargs)


class ManageInPurchaseAdCriteriaView(ScModelView):
    can_create = True
    form_excluded_columns = ['created', 'updated']

    def __init__(self, session, **kwargs):
        super(ManageInPurchaseAdCriteriaView, self).__init__(InPurchaseAdCriteria, session, **kwargs)


class ViewEngagementView(ScCustomAdminView):

    def __init__(self, session, ad_repo, user_repo, **kwargs):
        super(ViewEngagementView, self).__init__(**kwargs)
        self.user_repo = user_repo
        self.ad_repo = ad_repo
        self.session = session

    def ad_details(self):
        ad_details = []
        for ad in self.ad_repo.all():
            created = ad.created
            no_of_customers = 1
            days_existed = (datetime.datetime.today() - created).days
            min_broadcast_views = 0 if not ad.broadcast_criteria else ad.broadcast_criteria.min_repetition * days_existed
            inpurchase_views = 0 if not ad.inpurchase_criteria else ad.inpurchase_criteria.repetition * days_existed * no_of_customers

            ad_details.append(dict(
                name=str(ad.name), id=ad.id, uploaded=created.date(),
                min_broadcast_views=min_broadcast_views,
                inpurchase_views=inpurchase_views,
                customers=4,
                inpurchase_clicks=12
            ))
        return ad_details

    @expose('/')
    def index(self):
        return self.render('admin/view_engagement.html',
                           ads=self.ad_details())

    @expose('/<int:id>')
    def edit_ad(self, id):
        ad = self.ad_repo.with_id(id)
        ad_form = ManageAdvertisementsView(self.session).edit_form(ad)

        return self.render('admin/view_engagement.html',
                           ads=self.ad_details(),
                           ad_form=ad_form)


class AdsSetupView(ScCustomAdminView):

    def __init__(self, session, ad_repo, **kwargs):
        super(AdsSetupView, self).__init__(**kwargs)
        self.ad_repo = ad_repo
        self.session = session

    @expose('/')
    def index(self):
        create_form = ManageAdvertisementsView(self.session).create_form()
        broadcast_ad_form = ManageBroadcastAdCriteriaView(self.session).create_form()
        inpurchase_ad_form = ManageInPurchaseAdCriteriaView(self.session).create_form()
        ad_details = self.ad_repo.all()
        return self.render('admin/ads_setup.html',
                           create_form=create_form,
                           broadcast_ad_form=broadcast_ad_form,
                           inpurchase_ad_form=inpurchase_ad_form,
                           ad_details=ad_details)


@inject(db=Database, ad_repo=AdRepository, user_repo=UserRepository)
def register_views(admin, db, ad_repo, user_repo):
    session = db.session

    admin.add_view(
        ManageAdvertisersView(session, name='Manage Advertisers', category='Ad Operations', endpoint='manage-advertisers'))
    admin.add_view(
        AdsSetupView(session, ad_repo, name='Ads Setup', category='Ad Operations', endpoint='ads-setup'))
    admin.add_view(
        ManageAdvertisementsView(session, name='Manage Advertisements', category='Ad Operations', endpoint='manage-advertisements'))

    admin.add_view(
        ManageBroadcastAdCriteriaView(session, name='Manage Broadcast Ad Criteria', category='Ad Operations', endpoint='manage-broadcast-ad'))
    admin.add_view(
        ManageInPurchaseAdCriteriaView(session, name='Manage InPurchase Ad Criteria', category='Ad Operations', endpoint='manage-inpurchase-ad'))

    admin.add_view(
        ViewEngagementView(session, ad_repo, user_repo, name='View Engagement', category='Ad Operations', endpoint='view-engagement'))
