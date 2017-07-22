#!/bin/sh

#WorkingDirectory
WORK_DIR=/usr/local/work

function passwd_root() {
  echo "管理者パスワードを変更してください。必ずメモしてください。忘れた場合は復旧できません。"
  passwd
}

function adduser_develop() {
  echo "開発者用アカウント(dev)を追加します。パスワードを変更してください。必ずメモしてください。"
  adduser dev
  id dev
  passwd dev
}

function chef_install() {

  mkdir $WORK_DIR
  cd $WORK_DIR
  wget https://packages.chef.io/stable/el/6/chef-12.12.15-1.el6.x86_64.rpm
  rpm -ivh chef-12.12.15-1.el6.x86_64.rpm
  mkdir /var/chef
  cd /var/chef/
  git clone https://github.com/shannonlab-publication/cookbooks.git
  chef-solo -o base
  chef-solo -o Python-3.5.2
  chef-solo -o httpd
  chef-solo -o redis-2.8.17
  chef-solo -o pip-modules

}

function clone_firstDjango() {

  cd /var/www/
  git clone https://github.com/shannonlab-publication/django.git
  chown -R dev:dev /var/www/django

}

passwd_root
adduser_develop
chef_install
clone_firstDjango
