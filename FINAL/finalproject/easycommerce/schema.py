import graphene
from graphene_django import DjangoObjectType
from .models import * 
from user.models import *
from blog.models import *

class ContactType(DjangoObjectType):
    class Meta: 
        model = Contact
        fields = (
            'nom',
            'email',
            'commentaire' ,
            'status',
            'date_add',
            'date_update',
        )

  
class ProduitType(DjangoObjectType):
    class Meta: 
        model = Produit
        fields = (
            'name',
            'price',
            'image',
            'description',
            'categorie', 
            'status',
            'date_add', 
            'date_update',
        ) 
        

class ArticleType(DjangoObjectType):
    class Meta: 
        model = Article
        fields = (
            'title',
            'author',
            'description',
            'date_created',
            'image', 
            'status',
            'date_add', 
            'date_update',
        ) 
        

class CommentType(DjangoObjectType):
    class Meta: 
        model = Comment
        fields = (
            'name',
            'email',
            'comment',
            'status',
            'date_add', 
            'date_update',
        ) 
        

class ReplyType(DjangoObjectType):
    class Meta: 
        model = Reply
        fields = (
            'nom',
            'message',
            'comment',
            'status',
            'date_add', 
            'date_update',
        ) 
        
class TeamMemberType(DjangoObjectType):
    class Meta: 
        model = TeamMember
        fields = (
            'name',
            'profession',
            'facebook_link',
            'instagram_link', 
            'photo',
            'description',
            'status',
            'date_add', 
            'date_update',
        ) 
        


        
class Query(graphene.ObjectType):
    contacts = graphene.List(ContactType)
    produits = graphene.List(ProduitType)
    articles = graphene.List(ArticleType)
    comments = graphene.List(CommentType)
    replys = graphene.List(ReplyType)
    teammembers = graphene.List(TeamMemberType)
    

    def resolve_contacts(root, info, **kwargs):
        # Querying a list
        return Contact.objects.all()

    def resolve_produits(root, info, **kwargs):
        # Querying a list
        return Produit.objects.all()

    def resolve_articles(root, info, **kwargs):
        # Querying a list
        return Article.objects.all()
    
    def resolve_comments(root, info, **kwargs):
        # Querying a list
         return Comment.objects.all()

    def resolve_replys(root, info, **kwargs):
        # Querying a list
         return Reply.objects.all()
     
    def resolve_teammembers(root, info, **kwargs):
            # Querying a list
        return TeamMember.objects.all()
    
    
    
schema = graphene.Schema(query=Query)



class ContactInput(graphene.InputObjectType):
    nom  = graphene.String()
    email  = graphene.String()
    commentaire  = graphene.String()
    status  = graphene.String()
    date_add  = graphene.String()
    date_update  = graphene.String()

class CreateContact(graphene.Mutation):
    class Arguments:
        input = ContactInput(required=True)

    contact = graphene.Field(ContactType)
    
    @classmethod
    def mutate(cls, root, info, input):
        contact = Contact()
        contact.nom = input.nom 
        contact.email = input.email  
        contact.commentaire = input.commentaire
        contact.status = input.status
        contact.date_add = input.date_add 
        contact.date_update = input.date_update 
          
        contact.save()
        return CreateContact(contact=contact)

class UpdateContact(graphene.Mutation):
    class Arguments:
        input = ContactInput(required=True)
        id = graphene.ID()

    book = graphene.Field(ContactType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        contact = Contact.objects.get(pk=id)
        contact.nom  = input.nom 
        contact.email  = input.email 
        contact.commentaire  = input.commentaire
        contact.status  = input.status  
        contact.date_add = input.date_add 
        contact.date_update = input.date_update  
        
        contact.save()
        return UpdateContact(contact=contact)



class ProduitInput(graphene.InputObjectType):
    name  = graphene.String()
    price  = graphene.String()
    image  = graphene.String()
    description = graphene.String()
    categorie = graphene.String()
    
    status  = graphene.String()
    date_add  = graphene.String()
    date_update  = graphene.String()

class CreateProduit(graphene.Mutation):
    class Arguments:
        input = ProduitInput(required=True)

    produit = graphene.Field(ProduitType)
    
    @classmethod
    def mutate(cls, root, info, input):
        produit = Produit()
        produit.name = input.name 
        produit.price = input.price  
        produit.image = input.image  
        produit.description = input.description
        produit.categorie = input.categorie
        
        
        produit.status = input.status
        produit.date_add = input.date_add 
        produit.date_update = input.date_update 
          
        produit.save()
        return CreateProduit(produit=produit)



class UpdateProduit(graphene.Mutation):
    class Arguments:
        input = ProduitInput(required=True)
        id = graphene.ID()

    produit = graphene.Field(ProduitType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        produit = Produit.objects.get(pk=id)
        produit.name  = input.name 
        produit.price  = input.price 
        produit.description  = input.description
        produit.categorie  = input.categorie
        
        produit.status  = input.status  
        produit.date_add = input.date_add 
        produit.date_update = input.date_update  
        
        Produit.save()
        return UpdateProduit(produit=produit)


class Mutation(graphene.ObjectType):
    # update_ = UpdateCategory.Field()
    # create_category = CreateCategory.Field()
    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()
    create_produit = CreateProduit.Field()
    update_produit = UpdateProduit.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)