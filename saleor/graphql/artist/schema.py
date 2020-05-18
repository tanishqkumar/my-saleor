import graphene
from graphene_django import DjangoObjectType
from ...artist.models import Artist
from .mutations.artists import CreateArtist
# this file has the actual query schema definition as well as pulling
# the mutations definitions from mutations/artists
# need to write a query for all artists first so that you can write the
# query alongside the mutation to return the data

# these can do in types.py when they get too large, like in orders
class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist

class ArtistQueries(graphene.ObjectType):
    artists = graphene.List(
        ArtistType,
        # search=graphene.String(),
        # first=graphene.Int(),
        # skip=graphene.Int(),
    )
    # this is the function that is called when you send a query with a field links in there and
    # it returns all the links in the db

    def resolve_artists(self,
                      info, 
                    #   search=None, 
                    #   first=None, 
                    #   skip=None, 
                      **kwargs):
        qs = Artist.objects.all()

        # if search:
        #         filter = (
        #             Q(url__icontains=search) |
        #             Q(description__icontains=search)
        #         )
        #         return qs.filter(filter)
        # if first:
        #         return qs[:first]
        # if skip:
        #         return qs[skip:]
        return qs


class ArtistMutations(graphene.ObjectType):
    create_artist = CreateArtist.Field()
