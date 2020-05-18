import graphene
from graphql import GraphQLError
from graphene_django import DjangoObjectType
from ....artist.models import Artist


class CreateArtist(graphene.Mutation):

        # first we define the output of the mutation 
        name = graphene.String()
        email = graphene.String()
        type = graphene.String()
        bio = graphene.String()

# second we define data to send to the server as args of CreateArtist
        class Arguments:
            name = graphene.String()
            email = graphene.String()
            type = graphene.String()
            bio = graphene.String()

# third we define what happens on the server with the url, desc that we passed to it as args from the front end as per graphene spec
# when you run mutate you want the whole thing to return a new artist, where you pass in the args into self() with vars
# that you instantiated in the beginning for that reason
        def mutate(self, info, name, email, type, bio):
                artist = Artist(name=name, email=email, type=type, bio=bio)
                artist.save()

                return CreateArtist(
                    name=artist.name,
                    email=artist.email,
                    type=artist.type,
                    bio=artist.bio,
                )

