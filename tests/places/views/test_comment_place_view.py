from tests.base.utils import PlaceTestUtils, UserTestUtils
from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.models import Comment


class CommentPlaceViewTests(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_commentPlace__whenNotIsOwner_expectToCreateComment(self):
        self.client.force_login(self.user)
        place_user = self.create_user(email='email_test2', password='password_test2')
        place = self.create_place_with_comment(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place Description',
            image='path/to/image.png',
            user=place_user,
            comment_user=self.user,
        )

        comment_exists = Comment.objects.filter(
            user_id=self.user.id,
            place_id=place.id,
        ) \
            .exists()

        self.assertTrue(comment_exists)


