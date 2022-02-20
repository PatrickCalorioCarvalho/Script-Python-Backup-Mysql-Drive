Create database TestesBackup;
use TestesBackup;

create table TestesTabela
(
    IDTeste int not null auto_increment primary key,
    NomeTeste varchar(50)
);
insert into TestesTabela(NomeTeste) values('Teste01');
insert into TestesTabela(NomeTeste) values('Teste02');
insert into TestesTabela(NomeTeste) values('Teste03');
insert into TestesTabela(NomeTeste) values('Teste04');
insert into TestesTabela(NomeTeste) values('Teste05');