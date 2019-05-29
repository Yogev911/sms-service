create schema sms collate utf8mb4_general_ci;

create table users
(
	id int auto_increment
		primary key,
	user varchar(255) not null,
	password varchar(255) not null,
	phone varchar(255) not null,
	balance int not null,
	pin int null,
	verify tinyint(1) not null,
	constraint users_user_uindex
		unique (user)
);

create table message_history
(
	id int auto_increment
		primary key,
	sender_id int null,
	dest_number varchar(255) null,
	time_stamp timestamp default current_timestamp() not null on update current_timestamp(),
	message varchar(1023) null,
	constraint message_history_users_id_fk
		foreign key (sender_id) references users (id)
);

create table puzzles
(
	question varchar(255) null,
	answer float null,
	user_id int null,
	reword int null,
	id int auto_increment
		primary key,
	constraint puzzles_users_id_fk
		foreign key (user_id) references users (id)
);
