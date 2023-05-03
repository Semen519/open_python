import telebot as tb
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


# dict with user_id key
# one user have "complete", "language", "age", "gender", "answer_1", "answer_2"
database = {}
bot = tb.TeleBot(os.environ.get('TOKEN'))

# questions 1-10, man, woman
items = {}

items['introduction_RU'] = 'Здравствуйте и добро пожаловать! Мы проводим социологический опрос для изучения релокантов 2022 и 2023 годов. Опрос состоит из 15 вопросов и должен занять около 7 минут. \n \
    Мы хотели бы заверить вас, что все ответы, данные в этом опросе, будут анонимизированы и сохранены только на одном носителе. Мы серьезно относимся к конфиденциальности и не будем передавать никакую личную информацию третьим лицам. Ваше участие высоко ценится и поможет нам получить ценные сведения по рассматриваемой теме. Спасибо за ваше время \n \
    Пожалуйста, помните, что при необходимости вы можете использовать команду /back для возврата к предыдущему вопросу. \n \
    Также с помощью команды /start вы можете полностью заново пройти \n \
    Согласны ли вы пройти опрос?'
items['introduction_EN'] = 'Hello and welcome! We are conducting a sociological survey to study the 2022 and 2023 relocations. The survey consists of 15 questions and should take about 7 minutes to complete. \n \
    We would like to assure you that all responses given in this survey will be anonymized and saved on one medium only. We take privacy seriously and will not share any personal information with third parties. Your participation is greatly appreciated and will help us gain valuable insights into the topic at hand. Thank you for your time. \n \
    Please remember that, if necessary, you can use the /back command to go back to the previous question. \n \
    You can also use the /start command to completely re-take \n \
Do you agree to take the survey?'
items['introduction_CN'] = '你好，欢迎! 我们正在进行一项社会学调查，以研究2022年和2023年的搬迁工作。该调查由15个问题组成，大约需要7分钟完成。\n \
    我们向您保证，在本次调查中给出的所有答案将被匿名化，并只保存在一个媒介上。我们非常重视保密性，不会与第三方分享任何个人信息。我们非常感谢您的参与，这将有助于我们获得对当前主题的宝贵见解。谢谢您的时间 \n \
    请记住，如果有必要，你可以使用/back命令返回到你之前的问题。\n \
    你也可以使用/start命令来完全重考。\n \
你是否同意接受调查？'
items['introduction_UA'] = "    Доброго дня і ласкаво просимо! Ми проводимо соціологічне опитування для вивчення релокантів 2022 і 2023 років. Опитування складається з 15 запитань і має зайняти близько 7 хвилин. \n \
    Ми хотіли б запевнити вас, що всі відповіді, дані в цьому опитуванні, будуть анонімізовані та збережені тільки на одному носії. Ми серйозно ставимося до конфіденційності та не передаватимемо жодної особистої інформації третім особам. Ваша участь високо цінується і допоможе нам отримати цінні відомості з даної теми. Дякуємо за ваш час \n \
    Будь ласка, пам'ятайте, що за необхідності ви можете використовувати команду /back для повернення до попереднього запитання. \n \
    Також за допомогою команди /start ви можете повністю заново пройти \n \
    Чи згодні ви пройти опитування?"
items['introduction_FR'] = "    Bonjour et bienvenue ! Nous menons une enquête sociologique pour étudier les délocalisations de 2022 et 2023. L'enquête se compose de 15 questions et devrait prendre environ 7 minutes à remplir. \n \
    Nous tenons à vous assurer que toutes les réponses données dans le cadre de cette enquête seront anonymisées et sauvegardées sur un seul support. Nous prenons la confidentialité au sérieux et ne partagerons aucune information personnelle avec des tiers. Votre participation est très appréciée et nous aidera à obtenir des informations précieuses sur le sujet en question. Merci de nous avoir accordé votre temps \n \
    N'oubliez pas que, si nécessaire, vous pouvez utiliser la commande /back pour revenir à votre question précédente. \n \
    Vous pouvez également utiliser la commande /start pour reprendre complètement l'enquête. \n \
Acceptez-vous de répondre à l'enquête ?"

items['question_1_RU'] = 'Вы релоцировались в 2022 или 2023 годах?'
items['question_1_EN'] = 'Did you relocate in 2022 or 2023?'
items['question_1_CN'] = '你在2022年或2023年搬迁了吗?'
items['question_1_UA'] = 'Ви релокувалися у 2022 чи 2023 роках?'
items['question_1_FR'] = 'Vous avez déménagé en 2022 ou 2023 ?'

items['yes_RU'] = 'Да'
items['yes_EN'] = 'Yes'
items['yes_CN'] = '是'
items['yes_UA'] = 'Так'
items['yes_FR'] = 'Oui'

items['no_RU'] = 'Нет'
items['no_EN'] = 'No'
items['no_CN'] = '没有'
items['no_UA'] = 'Ні'
items['no_FR'] = 'Non'

items['question_2_RU'] = 'Выберите ваш пол:'
items['question_2_EN'] = 'Choose your gender:'
items['question_2_CN'] = '指定你的性别:'
items['question_2_UA'] = 'Вкажіть вашу стать:'
items['question_2_FR'] = 'Précisez votre sexe:'

items['man_RU'] = 'Мужчина'
items['man_EN'] = 'Man'
items['man_CN'] = '侠'
items['man_UA'] = 'Чоловік'
items['man_FR'] = "L'homme"

items['woman_RU'] = 'Женщина'
items['woman_EN'] = 'Woman'
items['woman_CN'] = '妇人'
items['woman_UA'] = 'Жінка'
items['woman_FR'] = 'Femme'

items['question_3_RU'] = 'Укажите сколько вам лет:'
items['question_3_EN'] = 'State how old you are:'
items['question_3_CN'] = '说明你的年龄是多少:'
items['question_3_UA'] = 'Вкажіть скільки вам років:'
items['question_3_FR'] = 'Indiquez votre âge:'

items['question_4_RU'] = 'В каком городе вы проживали до релокации?'
items['question_4_EN'] = 'What city did you live in before your relocation?'
items['question_4_CN'] = '在搬迁之前，你住在哪个城市？'
items['question_4_UA'] = 'У якому місті ви жили до релокації?'
items['question_4_FR'] = 'Dans quelle ville habitiez-vous avant la délocalisation?'

items['question_5_RU'] = 'Кем вы работаете?'
items['question_5_EN'] = 'What is your job?'
items['question_5_CN'] = '你的工作是什么？'
items['question_5_UA'] = 'Ким ви працюєте?'
items['question_5_FR'] = 'Quel type de travail faites-vous ?'

items['question_6_RU'] = 'Какие из следующих категорий людей присутствуют в вашей семье? Пожалуйста, выберите все применимые варианты '
items['question_6_EN'] = 'Which of the following categories of people are present in your family? Please select all applicable options'
items['question_6_CN'] = ' 在你面前的是一份人的类别清单。如果你的家人有的话，请列出他们：'
items['question_6_UA'] = 'Перед вами знаходиться список категорій людей. Вкажіть їх, якщо у вас є такі в родині:'
items['question_6_FR'] = 'Quel type de travail faites-vous ?'

items['siblings_RU'] = 'Близкие пожилые родственики'
items['siblings_EN'] = 'Close elderly relatives'
items['siblings_CN'] = '密切的老年亲属'
items['siblings_UA'] = 'Близькі літні родичі'
items['siblings_FR'] = 'Parents âgés proches'

items['children_RU'] = 'Несовершеннолетние дети'
items['children_EN'] = 'Non-adolescent children'
items['children_CN'] = '非青少年儿童'
items['children_UA'] = 'Неповнолітні діти'
items['children_FR'] = 'Enfants non adolescents'

items['disabled_person_RU'] = 'Люди с ограниченными возможностями здоровья'
items['disabled_person_EN'] = 'People with disabilities'
items['disabled_person_CN'] = '残疾人士'
items['disabled_person_UA'] = "Люди з обмеженими можливостями здоров'я"
items['disabled_person_FR'] = 'Personnes handicapées'

items['check_question_RU'] = "Верно ли введены данны?"
items['check_question_EN'] = "Are the data entered correctly?"
items['check_question_CN'] = "输入的数据是否正确？"
items['check_question_UA'] = "Чи правильно введені дані?"
items['check_question_FR'] = "Les données sont-elles correctement saisies ?"

items['question_7_RU'] = 'Выберите количество успешных, по вашему мнению, кейсов релокации среди ваших знакомых до вашей релокации'
items['question_7_EN'] = 'Select the number of successful relocation cases among your acquaintances before your relocation'
items['question_7_CN'] = '选择在你搬迁前，你的熟人中成功搬迁的案例数量'
items['question_7_UA'] = 'Оберіть кількість успішних на вашу думку кейсів релокації серед ваших знайомих до вашої релокації'
items['question_7_FR'] = 'Sélectionnez le nombre de cas de relocalisation réussis parmi vos connaissances avant votre relocalisation'

items['variant_1'] = '0'
items['variant_2'] = '1-2'
items['variant_3'] = '3-5'
items['variant_4'] = '5-7'
items['variant_5'] = '7-10'
items['variant_6'] = '>10'

items['question_8_RU'] = 'В какую страну вы релоцировались?'
items['question_8_EN'] = 'Which country did you relocate to? '
items['question_8_CN'] = '您迁居到哪个国家？'
items['question_8_UA'] = 'У яку країну ви релоціювалися?'
items['question_8_FR'] = 'Dans quel pays avez-vous déménagé ?'

items['question_9_RU'] = 'Выберите количество неуспешных по вашему мнению кейсов релокации среди ваших знакомых'
items['question_9_EN'] = 'Select the number of unsuccessful relocation cases among your acquaintances'
items['question_9_CN'] = '选择你的熟人中不成功的搬迁案例的数量'
items['question_9_UA'] = 'Оберіть кількість неуспішних на вашу думку кейсів релокації серед ваших знайомих'
items['question_9_FR'] = 'Sélectionnez le nombre de cas de relocalisation infructueux parmi vos connaissances'

items['variant_1'] = '0'
items['variant_2'] = '1-2'
items['variant_3'] = '3-5'
items['variant_4'] = '5-7'
items['variant_5'] = '7-10'
items['variant_6'] = '>10'

items['question_10_RU'] = 'Представьте себе что Вы можете продолжать работать в России как обычно, а можете ' \
                          'эмигрировать за границу, где вы с вероятностью Q сможете найти работу с таким же уровнем ' \
                          'реального располагаемого дохода, что и в России, а с вероятностью 1-Q можете найти работу ' \
                          'только с реальным располагаемым доходов вдвое ниже. При каком минимальном значении ' \
                          'вероятности Q предпочтете Вы же выехать за пределы России и работать на тех условиях, ' \
                          'которые сможете найти?'
items['question_10_EN'] = 'Imagine that you can continue to work in Russia as usual, or you can emigrate abroad, ' \
                          'where with probability Q you can find a job with the same level of real disposable income ' \
                          'as in Russia, and with probability 1-Q you can find a job with only half as much real ' \
                          'disposable income. At what minimum value of probability Q would you prefer to leave Russia ' \
                          'and work under the conditions you can find?'
items['question_10_CN'] = '想象一下，你可以像往常一样在俄罗斯工作，也可以移民国外，在那里你有可能找到一份与俄罗斯实际可支配收入水平相同的工作，也有可能找到一份实际可支配收入只有一半的工作，概率为Q。在概率Q' \
                          '的哪个最小值上，你会选择离开俄罗斯，在你能找到的条件下工作？'
items['question_10_UA'] = 'Уявіть собі, що Ви можете продовжувати працювати в Росії, як зазвичай, а можете емігрувати ' \
                          'за кордон, де ви з імовірністю Q зможете знайти роботу з таким самим рівнем реального ' \
                          'наявного доходу, що й у Росії, а з імовірністю 1-Q можете знайти роботу тільки з реальним ' \
                          'наявним доходом, що вдвічі нижчий. За якого мінімального значення ймовірності Q віддасте ' \
                          'перевагу Ви ж виїхати за межі Росії і працювати на тих умовах, які зможете знайти?'
items['question_10_FR'] = "Imaginez que vous puissiez continuer à travailler en Russie comme d'habitude, ou que vous " \
                          "puissiez émigrer à l'étranger, où, avec une probabilité Q, vous pourriez trouver un emploi " \
                          "avec le même niveau de revenu disponible réel qu'en Russie, et avec une probabilité 1-Q, " \
                          "vous pourriez trouver un emploi avec seulement la moitié du revenu disponible réel. À " \
                          "partir de quelle valeur minimale de la probabilité Q préféreriez-vous quitter la Russie et " \
                          "travailler dans les conditions que vous pouvez trouver ?"

items['question_11_RU'] = 'Представьте себе что Вы можете работать в России как обычно, и получать обычный доход с ' \
                          'вероятностью P, и можете быть призваны в армию с вероятностью 1-P. При каком минимальном ' \
                          'значении вероятности P Вы предпочтете выехать за пределы России?'
items['question_11_EN'] = 'Imagine that you can work in Russia as usual and earn a regular income with probability P, ' \
                          'and you can be drafted into the army with probability 1-P. At what minimum value of ' \
                          'probability P would you prefer to leave Russia?'
items['question_11_CN'] = '想象一下，你可以像往常一样在俄罗斯工作并获得正常的收入，概率为P，而你可以被征召入伍，概率为1-P。在概率P的哪个最小值上，你会选择离开俄罗斯？'
items['question_11_UA'] = 'Уявіть собі, що Ви можете працювати в Росії як зазвичай, і отримувати звичайний дохід з ' \
                          'імовірністю P, і можете бути покликані в армію з імовірністю 1-P. За якого мінімального ' \
                          'значення ймовірності P Ви віддасте перевагу виїхати за межі Росії?'
items['question_11_FR'] = "Imaginez que vous puissiez travailler en Russie comme d'habitude et gagner un revenu " \
                          "régulier avec une probabilité P, et que vous puissiez être incorporé dans l'armée avec une " \
                          "probabilité 1-P. À partir de quelle valeur minimale de la probabilité P préféreriez-vous " \
                          "quitter la Russie ?"

items['question_12_RU'] = 'Когда вы  релоцировались? (Выехали из страны, приняв решение не возвращаться продолжительное время)'
items['question_12_EN'] = 'When did you relocate? (Left the country, having decided not to return for an extended period)'
items['question_12_CN'] = '你是什么时候搬迁的？(离开了这个国家，已决定长期不回国）'
items['question_12_UA'] = 'Коли ви релоціювалися? (Виїхали з країни, прийнявши рішення не повертатися тривалий час) '
items['question_12_FR'] = "Quand avez-vous déménagé ? (J'ai quitté le pays, ayant décidé de ne pas y retourner pour une longue période)"

items['question_13_RU'] = 'Остаются ли у вас источники дохода в России, включая удаленную работу?'
items['question_13_EN'] = 'Do you still have sources of income in Russia, including distance work? '
items['question_13_CN'] = '你在俄罗斯还有收入来源吗，包括远程工作？'
items['question_13_UA'] = 'Чи залишаються у вас джерела доходу в Росії, включно з віддаленою роботою?'
items['question_13_FR'] = 'Avez-vous encore des sources de revenus en Russie, y compris le travail à distance?'

items['question_14_RU'] = 'Были ли у вас документы других стран до того как вы приняли решение о релокации?'
items['question_14_EN'] = 'Did you have documentation before you made the decision to relocate?'
items['question_14_CN'] = '在你决定搬迁之前，你是否有文件？'
items['question_14_UA'] = 'Чи були у вас документи до того, як ви прийняли рішення про релокацію?'
items['question_14_FR'] = 'Disposiez-vous de documents avant de prendre la décision de déménager?'

items['question_15_RU'] = 'Были ли у вас источники дохода за пределами России, когда вы приняли решение о релокации?'
items['question_15_EN'] = 'Did you have any sources of income outside Russia before you decided to relocate?'
items['question_15_CN'] = '在你决定搬迁之前，你在俄罗斯之外是否有任何收入来源?'
items['question_15_UA'] = 'Чи були у вас джерела доходу за межами Росії, до того як ви прийняли рішення про релокацію?'
items['question_15_FR'] = 'Aviez-vous des sources de revenus en dehors de la Russie avant de décider de déménager ?'

items['rejection_RU'] = 'Спасибо за то, что уделили нам время. Если вы все-таки захотите пройти опрос позже, всегда вам рады.'
items['rejection_EN'] = 'Thank you for your time. If you do want to take the survey later, you are always welcome'
items['rejection_CN'] = '谢谢你的时间。如果你以后还想参加调查，我们随时欢迎你'
items['rejection_UA'] = 'Дякуємо за те, що приділили нам час. Якщо ви все-таки захочете пройти опитування пізніше, завжди вам раді'
items['rejection_FR'] = "Nous vous remercions pour le temps que vous nous avez consacré. Si vous souhaitez répondre à l'enquête ultérieurement, vous êtes toujours le bienve"

items['good_bye_RU'] = 'Выражаем глубокую признательность за прохождние опроса. Вы очень нам помогли. \
                       Если в вашем окружении есть релоканты, будем искренне благодарны, если вы поделитесь с ними ссылкой на наш опрос'
items['good_bye_EN'] = 'We are very grateful to you for taking the survey. You have been a great help to us.  If there are any relocatees in your community, we would sincerely appreciate it if you could share the link to our survey with them'
items['good_bye_CN'] = '我们非常感谢你参加调查。你对我们的帮助很大。 如果你的社区有任何搬迁者，如果你能与他们分享我们的调查链接，我们将真诚地感谢。'
items['good_bye_UA'] = 'Висловлюємо глибоку вдячність за проходження опитування. Ви дуже нам допомогли.  Якщо у вашому оточенні є релоканти, будемо щиро вдячні, якщо ви поділитеся з ними посиланням на наше опитування'
items['good_bye_FR'] = "Nous vous sommes très reconnaissants d'avoir répondu à l'enquête. Vous nous avez été d'une aide précieuse.  S'il y a des personnes relocalisées dans votre communauté, nous vous serions très reconnaissants de bien vouloir leur communiquer le lien vers notre enquête."

items['nonrelocant_RU'] = 'Спасибо, что согласились пройти опрос, но, к сожалению, наша выборка ограничивается релокантами. Если в вашем окружении есть такие люди, будем искренне благодарны, если вы поделитесь с ними ссылкой на наш опрос'
items['nonrelocant_EN'] = 'Thank you for agreeing to take the survey, but unfortunately our sample is limited to relocants. If you know someone who does, we would be very grateful if you could share the link to our survey with them.'
items['nonrelocant_CN'] = '感谢你同意参加调查，但不幸的是，我们的样本仅限于搬迁者。如果你知道有人这样做，如果你能与他们分享我们的调查链接，我们将非常感激。'
items['nonrelocant_UA'] = 'Дякуємо, що погодилися пройти опитування, але, на жаль, наша вибірка обмежується релокантами. Якщо у вашому оточенні є такі знайомі, будемо щиро вдячні, якщо ви поділитеся з ними посиланням на наше опитування'
items['nonrelocant_FR'] = "Nous vous remercions d'avoir accepté de participer à l'enquête, mais notre échantillon est malheureusement limité aux personnes qui déménagent. Si vous connaissez quelqu'un qui en fait partie, nous vous serions très reconnaissants de partager avec lui le lien vers notre enquête"

items['age_error_RU'] = 'Некорректная запись возраста. Пожалуйста, повторите ввод. Пример ввода: 24'
items['age_error_EN'] = 'Incorrect age entry. Please re-enter again. Example entry: 24'
items['age_error_CN'] = '年龄输入不正确。请重新输入。输入示例：24'
items['age_error_UA'] = 'Некоректний запис віку. Будь ласка, повторіть введення. Приклад введення: 24'
items['age_error_FR'] = "La saisie de l'âge est incorrecte. Veuillez le saisir à nouveau. Exemple de saisie : 24"

items['you_selected_RU'] = 'Вы выбрали: '
items['you_selected_EN'] = 'You have selected: '
items['you_selected_CN'] = '您已选择: '
items['you_selected_UA'] = 'Ви вибрали: '
items['you_selected_FR'] = 'Vous avez sélectionné: '

items['keyboard_error_RU'] = 'Вы ввели некоретные данные, пожалуйста, вводите данные с клавиатуры (Всплывающие окошки ниже)'
items['keyboard_error_EN'] = 'You have entered incorrect data, please enter data using the keypad (Pop-up boxes below)'
items['keyboard_error_CN'] = '您输入的数据不正确，请用小键盘输入数据（下面的弹出框）。'
items['keyboard_error_UA'] = 'Ви ввели некоретні дані, будь ласка, вводьте дані з клавіатури (Спливаючі віконця нижче)'
items['keyboard_error_FR'] = "Vous avez saisi des données incorrectes, veuillez saisir les données à l'aide du clavier (fenêtres contextuelles ci-dessous)."

items['selected_categories_RU'] = 'Выбрано : '
items['selected_categories_EN'] = 'Selected : '
items['selected_categories_CN'] = '选定 ：'
items['selected_categories_UA'] = 'Обрано :'
items['selected_categories_FR'] = 'Sélectionné :'

items['nobody_selected_RU'] = 'Никто не выбран'
items['nobody_selected_EN'] = 'No one has been selected'
items['nobody_selected_CN'] = '没有人被选中'
items['nobody_selected_UA'] = 'Ніхто не обраний'
items['nobody_selected_FR'] = "Personne n'a été sélectionné"