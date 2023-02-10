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


# CONTACT

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
    
    

# PRODUIT

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
    
    
# ARTICLE

class ArticleInput(graphene.InputObjectType):
    title = graphene.String()
    author = graphene.String()
    description = graphene.String()
    date_created = graphene.String()
    image = graphene.String()
    status = graphene.String()
    date_add = graphene.String()
    date_update = graphene.String()

class CreateArticle(graphene.Mutation):
    class Arguments:
        input = ArticleInput(required=True)

    article = graphene.Field(ArticleType)
    
    @classmethod
    def mutate(cls, root, info, input):
        article = Article()
        article.title = input.title
        article.author = input.author
        article.description = input.description
        article.date_created = input.date_created
        article.image = input.image
        article.status = input.status
        article.date_add = input.date_add
        article.date_update = input.date_update
          
        article.save()
        return CreateArticle(article=article)

class UpdateArticle(graphene.Mutation):
    class Arguments:
        input = ArticleInput(required=True)
        id = graphene.ID()

    article = graphene.Field(ArticleType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        article = Article.objects.get(pk=id)
        article.title = input.title
        article.author = input.author
        article.description = input.description
        article.date_created = input.date_created
        article.image = input.image
        article.status = input.status
        article.date_add = input.date_add
        article.date_update = input.date_update
        
        article.save()
        return UpdateArticle(article=article)
    
    
# COMMENT

class CommentInput(graphene.InputObjectType):
    name = graphene.String()
    email = graphene.String()
    comment = graphene.String()
    status = graphene.String()
    date_add = graphene.String()
    date_update = graphene.String()

class CreateComment(graphene.Mutation):
    class Arguments:
        input = CommentInput(required=True)

    comment = graphene.Field(CommentType)
    
    @classmethod
    def mutate(cls, root, info, input):
        comment = Comment()
        comment.name = input.name
        comment.email = input.email
        comment.comment = input.comment
        comment.status = input.status
        comment.date_add = input.date_add
        comment.date_update = input.date_update
          
        comment.save()
        return CreateComment(comment=comment)

class UpdateComment(graphene.Mutation):
    class Arguments:
        input = CommentInput(required=True)
        id = graphene.ID()

    comment = graphene.Field(CommentType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        comment = Comment.objects.get(pk=id)
        comment.name = input.name
        comment.email = input.email
        comment.comment = input.comment
        comment.status = input.status
        comment.date_add = input.date_add
        comment.date_update = input.date_update
        
        comment.save()
        return UpdateComment(comment=comment)
    

# REPLY

class ReplyInput(graphene.InputObjectType):
    nom = graphene.String()
    message = graphene.String()
    comment = graphene.ID()
    status = graphene.String()
    date_add = graphene.String()
    date_update = graphene.String()

class CreateReply(graphene.Mutation):
    class Arguments:
        input = ReplyInput(required=True)

    reply = graphene.Field(ReplyType)
    
    @classmethod
    def mutate(cls, root, info, input):
        comment = Comment.objects.get(pk=input.comment)
        reply = Reply(comment=comment)
        reply.nom = input.nom
        reply.message = input.message
        reply.status = input.status
        reply.date_add = input.date_add
        reply.date_update = input.date_update
          
        reply.save()
        return CreateReply(reply=reply)

class UpdateReply(graphene.Mutation):
    class Arguments:
        input = ReplyInput(required=True)
        id = graphene.ID()

    reply = graphene.Field(ReplyType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        reply = Reply.objects.get(pk=id)
        reply.nom = input.nom
        reply.message = input.message
        reply.status = input.status
        reply.date_add = input.date_add
        reply.date_update = input.date_update
        
        reply.save()
        return UpdateReply(reply=reply)
    
    

# TEAM MEMBER

class TeamMemberInput(graphene.InputObjectType):
    name = graphene.String()
    profession = graphene.String()
    facebook_link = graphene.String()
    instagram_link = graphene.String()
    photo = graphene.String()
    description = graphene.String()
    status = graphene.String()
    date_add = graphene.String()
    date_update = graphene.String()

class CreateTeamMember(graphene.Mutation):
    class Arguments:
        input = TeamMemberInput(required=True)

    team_member = graphene.Field(TeamMemberType)
    
    @classmethod
    def mutate(cls, root, info, input):
        team_member = TeamMember()
        team_member.name = input.name 
        team_member.profession = input.profession  
        team_member.facebook_link = input.facebook_link
        team_member.instagram_link = input.instagram_link
        team_member.photo = input.photo 
        team_member.description = input.description 
        team_member.status = input.status  
        team_member.date_add = input.date_add 
        team_member.date_update = input.date_update 
          
        team_member.save()
        return CreateTeamMember(team_member=team_member)

class UpdateTeamMember(graphene.Mutation):
    class Arguments:
        input = TeamMemberInput(required=True)
        id = graphene.ID()

    team_member = graphene.Field(TeamMemberType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        team_member = TeamMember.objects.get(pk=id)
        team_member.name = input.name 
        team_member.profession = input.profession  
        team_member.facebook_link = input.facebook_link
        team_member.instagram_link = input.instagram_link
        team_member.photo = input.photo 
        team_member.description = input.description 
        team_member.status = input.status  
        team_member.date_add = input.date_add 
        team_member.date_update = input.date_update  
        
        team_member.save()
        return UpdateTeamMember(team_member=team_member)





# MUTATION


class Mutation(graphene.ObjectType):
    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()
    create_produit = CreateProduit.Field()
    update_produit = UpdateProduit.Field()
    create_article = CreateArticle.Field()
    update_article = UpdateArticle.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
    create_reply = CreateReply.Field()
    update_reply = UpdateReply.Field()
    create_teammember = CreateTeamMember.Field()
    Update_teammember = UpdateTeamMember.Field()

    
schema = graphene.Schema(query=Query, mutation=Mutation)