from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User,AbstractBaseUser,PermissionsMixin,UserManager


class Cliente(models.Model):
    nome        = models.CharField('Nome',max_length=100)
    cpf         = models.CharField('CPF',max_length=20,blank=True,null=True)
    rg          = models.CharField('RG',max_length=20,blank=True,null=True)
    data_nascimento = models.DateField('Data de Nascimento',blank=True,null=True)
    #Endereço
    logradouro  = models.CharField('Logradouro',max_length=100,blank=True,null=True)
    numero      = models.IntegerField('N°',blank=True,null=True)
    bairro      = models.CharField('Bairro',max_length=100,blank=True,null=True)
    cidade      = models.CharField('Cidade',max_length=100,blank=True,null=True)
    uf          = models.CharField('Estado UF',max_length=50,blank=True,null=True)
    observacoes = models.CharField('Observações',max_length=100,blank=True,null=True)

    def __str__(self):
        return self.nome

class CustomUser(PermissionsMixin,AbstractBaseUser):
    username = models.CharField('Usúario', max_length=20, unique=True)
    email = models.EmailField('E-mail', unique=True)

    first_name = models.CharField('Primeiro Nome', max_length=20, blank=True)
    last_name = models.CharField('Segundo Nome', max_length=20, blank=True)
    friends = models.ManyToManyField('self',blank=True)
    frase = models.TextField('Frase',max_length=200,blank=True,null=True)
    foto = models.ImageField('Foto Perfil',upload_to='user/perfil',blank='true',default='/user/perfil/avatar.png')
    cidade = models.CharField('Cidade',max_length=20,blank=True,null=True)
    uf = models.CharField('Estado',max_length=10,blank=True,null=True)


    is_staff = models.BooleanField('É da equipe', default=False, blank=True)
    is_active = models.BooleanField('É ativo', default=True, blank=True)
    #foto = models.ImageField(verbose_name='Foto', upload_to='user/perfil', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, blank=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username


    def convite(self,convidado):
        convite = Convite(convidante=self,convidado=convidado)
        convites = convidado.convites_recebidos.filter(convidante_id=self.id)

        if not len(convites) > 0:
            convite.save()

    def remove_friend(self,profile_id):
        friend = CustomUser.objects.filter(id=profile_id)[0]
        self.friends.remove(friend)

    class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Usuarios'
        ordering = ['-id']


class Convite(models.Model):
    convidante = models.ForeignKey(CustomUser,related_name='criador_convite',on_delete=models.CASCADE)
    convidado = models.ForeignKey(CustomUser,related_name='convites_recebidos',on_delete=models.CASCADE)
    created_at = models.DateTimeField('Data da solicitacao',auto_now_add=True,blank=True)


    def aceitar(self):
        #Convite sera passado na view do rest
        self.convidante.friends.add(self.convidado)
        self.convidado.friends.add(self.convidante)
        self.delete()



    def __str__(self):
        return str(self.convidante)





class Avaliacao(models.Model):
    professor     = models.ForeignKey(CustomUser,related_name="professor_ficha",on_delete=models.CASCADE)
    aluno     = models.ForeignKey(CustomUser,related_name="aluno_ficha",on_delete=models.CASCADE)
    data_create      = models.DateField('Data de criação')

    altura      = models.IntegerField('Altura',blank=True,null=True)
    peso        = models.DecimalField('Peso',max_digits=5,decimal_places=2,blank=True,null=True)

    torax    = models.DecimalField('Torax',max_digits=5,decimal_places=2,blank=True,null=True)
    peitoral    = models.DecimalField('Peitoral',max_digits=5,decimal_places=2,blank=True,null=True)
    axilar    = models.DecimalField('Axilar',max_digits=5,decimal_places=2,blank=True,null=True)
    cintura    = models.DecimalField('Cintura',max_digits=5,decimal_places=2,blank=True,null=True)
    abdomen    = models.DecimalField('Cintura',max_digits=5,decimal_places=2,blank=True,null=True)
    quadril    = models.DecimalField('Quadril',max_digits=5,decimal_places=2,blank=True,null=True)
    #Braço
    braco_esq = models.DecimalField('Braço esquerdo',max_digits=5,decimal_places=2,blank=True,null=True)
    braco_dir = models.DecimalField('Braço direito',max_digits=5,decimal_places=2,blank=True,null=True)
    antebraco_esq = models.DecimalField('Antebraço esquerdo',max_digits=5,decimal_places=2,blank=True,null=True)
    antebraco_dir = models.DecimalField('Antebraço direito',max_digits=5,decimal_places=2,blank=True,null=True)

    #Pernas
    coxa_esq    = models.DecimalField('Coxa esquerda',max_digits=5,decimal_places=2,blank=True,null=True)
    coxa_dir    = models.DecimalField('Coxa eireita',max_digits=5,decimal_places=2,blank=True,null=True)
    panturilha_esq    = models.DecimalField('Pantirrilha esquerda',max_digits=5,decimal_places=2,blank=True,null=True)
    panturilha_dir    = models.DecimalField('Pantirrilha direita',max_digits=5,decimal_places=2,blank=True,null=True)


    def __str__(self):
        return str(self.id)+ ' --'
    class Meta:
        verbose_name='Ficha Pessoal'
        verbose_name_plural ='Fichas Pessoais'

class Musculo(models.Model):
    nome = models.CharField('Nome',max_length=50)
    descricao = models.CharField('Descricao',max_length=100,blank=True,null=True)

    def __str__(self):
        return self.nome

class Exercicio(models.Model):
    nome = models.CharField('Nome do exercicio',max_length=100)
    musculo = models.ForeignKey(Musculo,on_delete=models.CASCADE)
    def __str__(self):
        return self.nome + '('+str(self.musculo)+')'

class Treino(models.Model):

    professor = models.ForeignKey(CustomUser,related_name='professor_treino', on_delete=models.CASCADE)
    aluno = models.ForeignKey(CustomUser,related_name='aluno_treino', on_delete=models.CASCADE)

    # cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    data_inicio     = models.DateField('Data Inicio')
    data_fim     = models.DateField('Data Fim',blank=True,null=True)

    def __str__(self):
        return str(self.id) + ' --- '

class ExercicioTreino(models.Model):
    DIA_CHOICES=(
        ('DOM','Domingo'),
        ('SEG','Segunda'),
        ('TER','Terça'),
        ('QUA','Quarta'),
        ('QUI','Quinta'),
        ('SEX','Sexta'),
        ('SAB','Sabado'),
    )
    treino = models.ForeignKey(Treino,on_delete=models.CASCADE)
    dia = models.CharField('Dia do exercicio',choices=DIA_CHOICES,max_length=20)
    exercicio = models.ForeignKey('Exercicio',on_delete=models.CASCADE)
    repeticoes = models.IntegerField('Repeticoes',blank=True,null=True)
    sequencias = models.IntegerField('Sequencias',blank=True,null=True)
    carga = models.DecimalField('Carga',blank=True,null=True,decimal_places=1,max_digits=4)
    duracao = models.TimeField('Duração',blank=True,null=True)
    descanso = models.TimeField('Tempo de descanso Entre Exercicio',blank=True,null=True)
    def __str__(self):
        return str(self.dia)+'-'+'-'+str(self.exercicio)




