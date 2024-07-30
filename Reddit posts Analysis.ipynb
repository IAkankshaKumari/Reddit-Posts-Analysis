{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "316ee15a",
   "metadata": {},
   "source": [
    "A quick and easy analysis of this dataset to answer the following:\n",
    "\n",
    "1. Who removed the most number of posts from the website?\n",
    "2. A pie chart of who removes the post from the website\n",
    "3. Whose posts were removed most frequently?\n",
    "4. Most Popular posts, by awards received\n",
    "5. Comments distribution d) Conclusion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7371bc46",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c5568efc",
   "metadata": {},
   "outputs": [],
   "source": [
    "df= pd.read_csv(\"C:\\kaggle datasets\\Reddit Data.csv\",low_memory=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "10cc3662",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 190853 entries, 0 to 190852\n",
      "Data columns (total 12 columns):\n",
      " #   Column                 Non-Null Count   Dtype  \n",
      "---  ------                 --------------   -----  \n",
      " 0   id                     190853 non-null  object \n",
      " 1   title                  190852 non-null  object \n",
      " 2   score                  190853 non-null  int64  \n",
      " 3   author                 190853 non-null  object \n",
      " 4   author_flair_text      28845 non-null   object \n",
      " 5   removed_by             20744 non-null   object \n",
      " 6   total_awards_received  65146 non-null   float64\n",
      " 7   awarders               54478 non-null   object \n",
      " 8   created_utc            190853 non-null  int64  \n",
      " 9   full_link              190853 non-null  object \n",
      " 10  num_comments           190853 non-null  int64  \n",
      " 11  over_18                190853 non-null  bool   \n",
      "dtypes: bool(1), float64(1), int64(3), object(7)\n",
      "memory usage: 16.2+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f15296a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>title</th>\n",
       "      <th>score</th>\n",
       "      <th>author</th>\n",
       "      <th>author_flair_text</th>\n",
       "      <th>removed_by</th>\n",
       "      <th>total_awards_received</th>\n",
       "      <th>awarders</th>\n",
       "      <th>created_utc</th>\n",
       "      <th>full_link</th>\n",
       "      <th>num_comments</th>\n",
       "      <th>over_18</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ll1p9h</td>\n",
       "      <td>Wordcloud of trending video titles on YouTube ...</td>\n",
       "      <td>1</td>\n",
       "      <td>OmarZiada</td>\n",
       "      <td>OC: 1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.0</td>\n",
       "      <td>[]</td>\n",
       "      <td>1613473961</td>\n",
       "      <td>https://www.reddit.com/r/dataisbeautiful/comme...</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ll1o4h</td>\n",
       "      <td>Wordcloud of trending videos on YouTube in the...</td>\n",
       "      <td>1</td>\n",
       "      <td>OmarZiada</td>\n",
       "      <td>OC: 1</td>\n",
       "      <td>moderator</td>\n",
       "      <td>0.0</td>\n",
       "      <td>[]</td>\n",
       "      <td>1613473829</td>\n",
       "      <td>https://www.reddit.com/r/dataisbeautiful/comme...</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ll15gx</td>\n",
       "      <td>Immunization in India. Source: https://niti.go...</td>\n",
       "      <td>1</td>\n",
       "      <td>Professional_Napper_</td>\n",
       "      <td>NaN</td>\n",
       "      <td>moderator</td>\n",
       "      <td>0.0</td>\n",
       "      <td>[]</td>\n",
       "      <td>1613471541</td>\n",
       "      <td>https://www.reddit.com/r/dataisbeautiful/comme...</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ll0iup</td>\n",
       "      <td>How to quickly estimate the impact of players ...</td>\n",
       "      <td>1</td>\n",
       "      <td>Viziball</td>\n",
       "      <td>NaN</td>\n",
       "      <td>automod_filtered</td>\n",
       "      <td>0.0</td>\n",
       "      <td>[]</td>\n",
       "      <td>1613468624</td>\n",
       "      <td>https://www.reddit.com/r/dataisbeautiful/comme...</td>\n",
       "      <td>0</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ll0g9a</td>\n",
       "      <td>How to quickly estimate the impact of players ...</td>\n",
       "      <td>1</td>\n",
       "      <td>Viziball</td>\n",
       "      <td>NaN</td>\n",
       "      <td>moderator</td>\n",
       "      <td>0.0</td>\n",
       "      <td>[]</td>\n",
       "      <td>1613468281</td>\n",
       "      <td>https://www.reddit.com/r/dataisbeautiful/comme...</td>\n",
       "      <td>2</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       id                                              title  score  \\\n",
       "0  ll1p9h  Wordcloud of trending video titles on YouTube ...      1   \n",
       "1  ll1o4h  Wordcloud of trending videos on YouTube in the...      1   \n",
       "2  ll15gx  Immunization in India. Source: https://niti.go...      1   \n",
       "3  ll0iup  How to quickly estimate the impact of players ...      1   \n",
       "4  ll0g9a  How to quickly estimate the impact of players ...      1   \n",
       "\n",
       "                 author author_flair_text        removed_by  \\\n",
       "0             OmarZiada             OC: 1               NaN   \n",
       "1             OmarZiada             OC: 1         moderator   \n",
       "2  Professional_Napper_               NaN         moderator   \n",
       "3              Viziball               NaN  automod_filtered   \n",
       "4              Viziball               NaN         moderator   \n",
       "\n",
       "   total_awards_received awarders  created_utc  \\\n",
       "0                    0.0       []   1613473961   \n",
       "1                    0.0       []   1613473829   \n",
       "2                    0.0       []   1613471541   \n",
       "3                    0.0       []   1613468624   \n",
       "4                    0.0       []   1613468281   \n",
       "\n",
       "                                           full_link  num_comments  over_18  \n",
       "0  https://www.reddit.com/r/dataisbeautiful/comme...             0    False  \n",
       "1  https://www.reddit.com/r/dataisbeautiful/comme...             1    False  \n",
       "2  https://www.reddit.com/r/dataisbeautiful/comme...             1    False  \n",
       "3  https://www.reddit.com/r/dataisbeautiful/comme...             0    False  \n",
       "4  https://www.reddit.com/r/dataisbeautiful/comme...             2    False  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d85c2624",
   "metadata": {},
   "outputs": [],
   "source": [
    "# !pip install pandasql"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8a509a1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandasql as ps"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd1829fa",
   "metadata": {},
   "source": [
    "Let's check the missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "fb75a319",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "removed_by               170109\n",
       "author_flair_text        162008\n",
       "awarders                 136375\n",
       "total_awards_received    125707\n",
       "title                         1\n",
       "id                            0\n",
       "score                         0\n",
       "author                        0\n",
       "created_utc                   0\n",
       "full_link                     0\n",
       "num_comments                  0\n",
       "over_18                       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1b9619b",
   "metadata": {},
   "source": [
    "We can see that there are a lot of missing values in this dataset. However, because the data is being used for Exploratory Purposes, the missing values do not bother us much."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0867b3a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Basic Data Exploration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d697dcf9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>score</th>\n",
       "      <th>total_awards_received</th>\n",
       "      <th>created_utc</th>\n",
       "      <th>num_comments</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>190853.000000</td>\n",
       "      <td>65146.000000</td>\n",
       "      <td>1.908530e+05</td>\n",
       "      <td>190853.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>176.016159</td>\n",
       "      <td>0.013109</td>\n",
       "      <td>1.512494e+09</td>\n",
       "      <td>27.604732</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1951.936524</td>\n",
       "      <td>0.589425</td>\n",
       "      <td>6.822624e+07</td>\n",
       "      <td>213.236378</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.329263e+09</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.463862e+09</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.518662e+09</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.576576e+09</td>\n",
       "      <td>5.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>116226.000000</td>\n",
       "      <td>93.000000</td>\n",
       "      <td>1.613474e+09</td>\n",
       "      <td>18801.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               score  total_awards_received   created_utc   num_comments\n",
       "count  190853.000000           65146.000000  1.908530e+05  190853.000000\n",
       "mean      176.016159               0.013109  1.512494e+09      27.604732\n",
       "std      1951.936524               0.589425  6.822624e+07     213.236378\n",
       "min         0.000000               0.000000  1.329263e+09       0.000000\n",
       "25%         1.000000               0.000000  1.463862e+09       1.000000\n",
       "50%         1.000000               0.000000  1.518662e+09       2.000000\n",
       "75%         4.000000               0.000000  1.576576e+09       5.000000\n",
       "max    116226.000000              93.000000  1.613474e+09   18801.000000"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "da730985",
   "metadata": {},
   "source": [
    "Based on the information provided, we can conclude that the \"score\" variable is heavily skewed towards the lower values, based on the quartile distribution.\n",
    "\n",
    "This suggests that the majority of the data points have very low scores, with only a small number of data points having high scores. The presence of outliers with a very high score may also suggest that there are some extreme values that are skewing the distribution."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "6b090977",
   "metadata": {},
   "outputs": [],
   "source": [
    "# *Checking who removed the most Posts*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "cdb6e02f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>removed_by</th>\n",
       "      <th>posts_removed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>author</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>automod_filtered</td>\n",
       "      <td>1553</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>deleted</td>\n",
       "      <td>2948</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>moderator</td>\n",
       "      <td>14789</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>reddit</td>\n",
       "      <td>1453</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         removed_by  posts_removed\n",
       "0            author              1\n",
       "1  automod_filtered           1553\n",
       "2           deleted           2948\n",
       "3         moderator          14789\n",
       "4            reddit           1453"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "removed_posts = \"\"\"SELECT removed_by, count(distinct id) as posts_removed \n",
    "                    FROM df\n",
    "                    WHERE removed_by is not null\n",
    "                    GROUP BY removed_by\"\"\"\n",
    "df_removed_posts = ps.sqldf(removed_posts, locals())\n",
    "df_removed_posts"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79325d1a",
   "metadata": {},
   "source": [
    "Making a bar graph for the table above"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "a2fa2796",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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eu7x48fDzc0N999/PyIiIrBx40Y88cQTmDBhgm3+nr1ztj0IMzMzMW3aNDz33HOIj4/HI488gpkzZ2L9+vXXvA/LFjkSFj6iatKvXz9MmzYN06dPR61atTB06FBERETglltugZeXF0JCQjBhwgQkJyfb7pOTk4OJEyfCy8sLtWvXvqpwAMDFixcxcuRIuLu7o2HDhli6dOlVt7n8kG7Dhg0BAB07doSiKOjXr1+VvF57ZzAY8MMPP2Dfvn1o06YNZsyYgdmzZ9uuN5vN+P7773HixAm0a9cO77zzDl5//fVij9GjRw9MmTIFd911F4KCgvDuu++W6bk9PDywZs0apKamomvXrhg7diwGDhyIuXPnVuprpLKLjY2FxWLBiBEjULt2bXh4eMDLywuBgYFV/tzcY5GqhSCiatG3b1/h5eUlnn32WXHixAmxc+dOERQUJP773/+K48ePi/3794vBgweL/v372+7z2GOPifr164t169aJw4cPi1tvvVV4e3uLp556ynabW265RbRv317s2LFD7N27V/To0UO4u7uLDz/80HYbAGL58uVCCCF2794tAIh169aJhIQEkZKSUk3fAbInf/31l+jZs6fw9fUVAQEBYsSIESIyMlIIIcTGjRsFAJGWlma7/YEDBwQAERUVZbv+8q+XX35ZCCFEamqqmDBhgvDz8xPu7u5i2LBh4tSpU7bHWbRokfD19RW///67aNasmXB3dxd33HGHyMnJEYsXLxYNGjQQfn5+4oknnhCqqtruV9rjFj12vXr1hLu7uxg9erR47733hK+vb6nfi0WLFl31eqKiosTLL78s2rdvb7vd/fffL0aNGmX7c0n3EUKII0eOiGHDhglPT08RHBws7rvvPpGUlGR7nL59+4qpU6eKp556SgQGBop+/fqV6X7Z2dliwoQJwtPTU4SGhor33ntP9O3bt9jvA6JrYeEjqiZ9+/YVHTt2tP39tddeE0OGDCl2m7i4OAFAnDx5UmRlZQkXFxfx008/2a5PSUkR7u7utl/wJ0+eFADE7t27bbc5fvy4AHDNwhcVFSUAiAMHDlT6ayTH8csvv4hly5aJ06dPiwMHDoiRI0eKtm3bCk3TSi18BQUF4qOPPhI+Pj4iISFBJCQkiKysLCGEELfddpto2bKl+Oeff8TBgwfF0KFDRZMmTURhYaEQwlquzGazGDx4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7dvjhx9+QEJCAtLT05Gfnw8XFxd07doV8+fPv6e6li1bBrVajfXr16OsrAyBgYHYuXNntXGBrVq1wrvvvotFixZhwoQJ0Ol02L17N1xcXBAfHw9nZ2esWLECM2fOhIODAyIjI/Haa68ZzcFHRNRQJFFfI6iJCGVlZcjKyoKPjw/Mzc3lLoeoUeLnhKj+cQwfERERkcIx8BEREREpHAMfERERkcIx8BEREREpHAMfERERkcIx8BEREREpHAMfERERkcIx8BEREREpHAMfERERkcIx8BEREREpHAMfERERkcIx8BFRoxMcHIzg4OC7ttuzZw8kScKePXsMy8aNGwdvb+96q42IqCli4CMiRSspKUF8fLxRKCQiam5M5C6AqDnT6wVUKqnZ11CX3nvvPej1esPrkpISJCQkAMA99RoSESkRAx+RjFQqCf9bfRx/XiiWZf8OrlYY+FyHOt1mcXExrKys6nSb90Oj0ci2byKixoqXdIlk9ueFYlw+VyTLV22DZnx8PCRJwokTJ/D000/D3t4effr0AQCsW7cO3bp1g4WFBRwcHDB69GicO3eu2jZWrVqFNm3awMLCAj169MDXX399y339/vvvCA0NhZWVFVxcXDBz5kxcv369Wrsbx/BlZ2fD2dkZAJCQkABJkiBJEuLj42t13ERETQ17+Iio1kaNGoW2bdvitddegxACCxcuxLx58xAeHo6JEyciLy8PycnJ6NevH44cOQI7OzsAwAcffIDJkyejd+/eiI6OxpkzZzBixAg4ODjAw8PDsP3S0lL84x//wNmzZzFjxgy0bt0aa9euxVdffXXHupydnZGamoqpU6di5MiReOKJJwAAnTt3rrdzQUTUGDHwEVGtdenSBR999BEAICcnB23atEFiYiLi4uIMbZ544gl07doVKSkpiIuLQ0VFBeLi4vDggw9i9+7dMDU1BQC0b98ekZGRRoFv1apVOH36ND755BOMGjUKADBp0iR06dLljnVZWVkhLCwMU6dORefOnTFmzJi6PnQioiaBl3SJqNamTJli+P7TTz+FXq9HeHg4Ll++bPhq1aoV2rZti927dwMAfvjhB+Tm5mLKlCmGsAdUXpK1tbU12v727dvh6uqKsLAwwzJLS0tERkbW85ERESkDe/iIqNZ8fHwM32dmZkIIgbZt296ybdVNFTk5OQBQrZ1Go4Gvr6/RspycHPj5+UGSjO8mDggIqHXtRETNAQMfEdWahYWF4Xu9Xg9JkrBjxw6o1epqba2trRuyNCIiAgMfEdWxNm3aQAgBHx8f+Pv737adl5cXgMoewQEDBhiWV1RUICsry2h8npeXF3755RcIIYx6+TIyMu5az829gkREzRHH8BFRnXriiSegVquRkJAAIYTROiEE8vPzAQDdu3eHs7Mz3n33XZSXlxvapKeno6CgwOh9Q4cOxR9//IFNmzYZlpWUlGDVqlV3rcfS0hIAqm2TiKg5YQ8fkcwcXOWbpLg+9l11h+7cuXORnZ2N0NBQ2NjYICsrC1u2bEFkZCRmz54NjUaDxMRETJ48GQMGDMBTTz2FrKwspKWlVRvDN2nSJKxYsQJjx47Fjz/+CFdXV6xdu9YQ5u7EwsIC7du3x4YNG+Dv7w8HBwd07NgRHTt2rPNjJyJqrBj4iGSk14s6f9JFTWqo60erxcbGwt/fH0uXLjU81szDwwODBg3CiBEjDO0iIyOh0+mwePFixMTEoFOnTti6dSvmzZtntD1LS0vs2rULUVFRSE5OhqWlJZ555hk8+uijGDJkyF3ref/99xEVFYWZM2eivLwcCxYsYOAjomZFEjdfcyGiOlNWVoasrCz4+PjA3Nxc7nKIGiV+TojqH8fwERERESkcAx8RERGRwjHwERERESkcAx8RERGRwjHwERERESkcAx8RERGRwjHwETUAzn5EdHv8fBDVPwY+onqk0WggSRKKi4vlLoWo0SouLoYkSdBoNHKXQqRYfNIGUT1Sq9WwtbVFXl4erl+/jhYtWsDExASSVLdPtiBqaoQQ0Gq1uHr1Kq5evQo7Ozuo1Wq5yyJSLD5pg6ieCSFQWFiI3Nxc6HQ6ucshalTUajVcXFxga2vL/wgR1SMGPqIGIoSATqeDVquVuxSiRsHExARqtZpBj6gBMPARERERKRxv2iAiIiJSOAY+IiIiIoVj4CMiIiJSOAY+IiIiIoVj4CMiIiJSOAY+IiIiIoVj4CMiIiJSuP8HaBj9hvO40twAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 800x800 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "removed_by = df_removed_posts['removed_by'].tolist()\n",
    "number_of_removed_posts = df_removed_posts['posts_removed'].tolist()\n",
    "\n",
    "# Create pie chart\n",
    "fig, ax = plt.subplots(figsize=(8, 8))\n",
    "ax.pie(number_of_removed_posts, labels=removed_by, autopct='%1.1f%%', startangle=90,\n",
    "       counterclock=False, wedgeprops=dict(width=0.4, edgecolor='w'))\n",
    "\n",
    "# Add title and legend\n",
    "ax.set_title('Post Removal', fontsize=20)\n",
    "ax.legend(title='User', loc='center', bbox_to_anchor=(0.5, -0.1), fontsize=12)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d0935455",
   "metadata": {},
   "source": [
    "We can see that most posts are removed by the moderator, showing that Reddit Moderators, who are generally unpaid, are actively enforcing subreddit rules to regulate their subreddit. The next question is, whose posts were removed most frequently?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "364fe4f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>author</th>\n",
       "      <th>number_of_removed_posts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>[deleted]</td>\n",
       "      <td>2955</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>hornedviper9</td>\n",
       "      <td>235</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>RohanBAbu150</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mostafa_Dahroug</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>peter_mladenov</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>PerfctSmile</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Lifeinsider123</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>licensecrack</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>elizabeth010258</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Lisa580</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            author  number_of_removed_posts\n",
       "0        [deleted]                     2955\n",
       "1     hornedviper9                      235\n",
       "2     RohanBAbu150                       62\n",
       "3  Mostafa_Dahroug                       45\n",
       "4   peter_mladenov                       35\n",
       "5      PerfctSmile                       31\n",
       "6   Lifeinsider123                       28\n",
       "7     licensecrack                       26\n",
       "8  elizabeth010258                       24\n",
       "9          Lisa580                       22"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_removed = \"\"\"SELECT author, count(id) as number_of_removed_posts\n",
    "FROM df  \n",
    "WHERE removed_by is not null\n",
    "GROUP BY author \n",
    "ORDER BY 2 desc \n",
    "limit 10\"\"\"\n",
    "df_top_removed = ps.sqldf(top_removed, locals())\n",
    "df_top_removed"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9ef6c168",
   "metadata": {},
   "source": [
    "We can safely omit the first row, as the database categorises \"deleted\" as an author when it cannot directly attribute a post to an individual."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "73cb3a1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_top_removed = df_top_removed.drop([0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "4ec91e2c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>author</th>\n",
       "      <th>number_of_removed_posts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>hornedviper9</td>\n",
       "      <td>235</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>RohanBAbu150</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mostafa_Dahroug</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>peter_mladenov</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>PerfctSmile</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Lifeinsider123</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>licensecrack</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>elizabeth010258</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Lisa580</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            author  number_of_removed_posts\n",
       "1     hornedviper9                      235\n",
       "2     RohanBAbu150                       62\n",
       "3  Mostafa_Dahroug                       45\n",
       "4   peter_mladenov                       35\n",
       "5      PerfctSmile                       31\n",
       "6   Lifeinsider123                       28\n",
       "7     licensecrack                       26\n",
       "8  elizabeth010258                       24\n",
       "9          Lisa580                       22"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_top_removed"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d97b588",
   "metadata": {},
   "source": [
    "Now, lets see the most popular posts, by total_awards_received"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6fad0b23",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>awards_received</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Robinhood is getting wrecked in the App Store ...</td>\n",
       "      <td>93.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>How many leaders the Queen saw coming and goin...</td>\n",
       "      <td>55.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Citadel paid $88 million to Robinhood in Q3 20...</td>\n",
       "      <td>54.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>[OC] Vegetation of Africa 2019</td>\n",
       "      <td>38.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Number of Wilhelm Screams per Lord of the Ring...</td>\n",
       "      <td>31.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>[OC] Most Popular Programming Languages accord...</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Race and Hispanic origin by county [OC]</td>\n",
       "      <td>27.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>[OC] Fails-To-Deliver data on GameStop (GME)</td>\n",
       "      <td>24.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Highest Grossing Box Office Bald Actors of Hol...</td>\n",
       "      <td>21.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>The best (&amp;amp; worst) countries for raising a...</td>\n",
       "      <td>18.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title  awards_received\n",
       "0  Robinhood is getting wrecked in the App Store ...             93.0\n",
       "1  How many leaders the Queen saw coming and goin...             55.0\n",
       "2  Citadel paid $88 million to Robinhood in Q3 20...             54.0\n",
       "3                     [OC] Vegetation of Africa 2019             38.0\n",
       "4  Number of Wilhelm Screams per Lord of the Ring...             31.0\n",
       "5  [OC] Most Popular Programming Languages accord...             30.0\n",
       "6            Race and Hispanic origin by county [OC]             27.0\n",
       "7       [OC] Fails-To-Deliver data on GameStop (GME)             24.0\n",
       "8  Highest Grossing Box Office Bald Actors of Hol...             21.0\n",
       "9  The best (&amp; worst) countries for raising a...             18.0"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "popular_posts = \"\"\"SELECT title, total_awards_received as awards_received \n",
    "FROM df  \n",
    "where title != 'data_irl'\n",
    "order by 2 desc \n",
    "limit 10\"\"\"\n",
    "df_popular_posts = ps.sqldf(popular_posts, locals())\n",
    "df_popular_posts"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "038199b1",
   "metadata": {},
   "source": [
    "# Comments Distribution\n",
    "As seen in our quick statistics, an average reddit post has 28 comments. Lets see how the comments are distributed using a bar chart"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "f12f4f60",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings('ignore', category=FutureWarning)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "77d3fab9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk0AAAHHCAYAAACiOWx7AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuNSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/xnp5ZAAAACXBIWXMAAA9hAAAPYQGoP6dpAABL60lEQVR4nO3deVxV1f7/8fcBZRAERQQ0Fch59oqKpJkmiUNeTS0bzCGtqxcs5WbqzetYOV2nlKLJocFSm9NyyLEStVDLCTTTiyU4pZITKKzfH/04X484bPHkAX09H4/zeLD3Xnvtz1ns4u0+a+9jM8YYAQAA4KrcXF0AAABAUUBoAgAAsIDQBAAAYAGhCQAAwAJCEwAAgAWEJgAAAAsITQAAABYQmgAAACwgNAEAAFhAaAJuEWvWrJHNZtOHH37o6lIsOXTokLp166YyZcrIZrNp+vTpri4JAK6K0ARch7lz58pms8nLy0u//fZbvu0tW7ZUnTp1XFBZ0TN48GAtW7ZMw4cP1zvvvKO2bdtetf25c+c0bdo0RUZGyt/fX15eXqpWrZri4uK0e/fum1R14Xbw4EGNHj1aW7dudXUpTtWyZUvZbDb7KyAgQI0bN9bs2bOVm5vr9OOtX79eo0eP1okTJ5zeN4q2Yq4uACiKsrKyNGHCBM2cOdPVpRRZq1atUqdOnfTss89es+3Ro0fVtm1bJScn6/7779ejjz4qX19fpaam6oMPPtDrr7+u7Ozsm1B14Xbw4EGNGTNGYWFhatCggavLcaoKFSpo/PjxkqQjR47o7bffVt++fbV7925NmDDBqcdav369xowZo969e6tUqVJO7RtFG6EJKIAGDRrojTfe0PDhw1W+fHlXl3NTnT59Wj4+Pjfcz+HDhy3/Qerdu7e2bNmiDz/8UF27dnXYNm7cOD3//PM3XA9cJzc3V9nZ2fLy8rpiG39/f/Xo0cO+/I9//EPVq1fXrFmzNG7cOBUvXvxmlIrbHB/PAQXw73//Wzk5Odf8F+7+/ftls9k0d+7cfNtsNptGjx5tXx49erRsNpt2796tHj16yN/fX2XLltV//vMfGWN04MABderUSX5+fgoJCdGUKVMue8ycnBz9+9//VkhIiHx8fPT3v/9dBw4cyNdu48aNatu2rfz9/VWiRAndc889+u677xza5NW0c+dOPfrooypdurSaN29+1ff8yy+/6MEHH1RAQIBKlCihpk2basmSJfbteR9xGmOUkJBg/8jlSjZu3KglS5aob9+++QKTJHl6euq///2vw7pVq1bp7rvvlo+Pj0qVKqVOnTpp165dl31vBR3vvDlkCxcu1JgxY3THHXeoZMmS6tatm06ePKmsrCwNGjRIQUFB8vX1VZ8+fZSVlZWv/nfffVcRERHy9vZWQECAHn744Xy/r7yPfXfu3KlWrVqpRIkSuuOOOzRp0iSHeho3bixJ6tOnj31c8869PXv2qGvXrgoJCZGXl5cqVKighx9+WCdPnrzi2F987OTkZN11113y9vZWeHi4EhMT87XNysrSqFGjVKVKFXl6eqpixYp67rnn8r1vm82muLg4vffee6pdu7Y8PT21dOnSq9Zxqbxz6/Tp0zpy5Iika597eWbOnKnatWurRIkSKl26tBo1aqT58+dL+vO8GDJkiCQpPDzcPo779++/rvpwa+JKE1AA4eHh6tmzp9544w0NGzbMqVebunfvrpo1a2rChAlasmSJXnjhBQUEBOi1117Tvffeq4kTJ+q9997Ts88+q8aNG6tFixYO+7/44ouy2WwaOnSoDh8+rOnTpys6Olpbt26Vt7e3pD9DRbt27RQREaFRo0bJzc1Nc+bM0b333qtvvvlGTZo0cejzwQcfVNWqVfXSSy/JGHPF2g8dOqS77rpLZ86c0dNPP60yZcpo3rx5+vvf/64PP/xQDzzwgFq0aKF33nlHjz/+uO677z717NnzquPx+eefS5Ief/xxS+P39ddfq127drrzzjs1evRonT17VjNnzlSzZs20efNmhYWFOXW8x48fL29vbw0bNkw///yzZs6cqeLFi8vNzU3Hjx/X6NGjtWHDBs2dO1fh4eEaOXKkfd8XX3xR//nPf/TQQw+pX79+OnLkiGbOnKkWLVpoy5YtDlfijh8/rrZt26pLly566KGH9OGHH2ro0KGqW7eu2rVrp5o1a2rs2LEaOXKknnrqKd19992SpLvuukvZ2dmKiYlRVlaWBg4cqJCQEP32229avHixTpw4IX9//6uO6fHjx9W+fXs99NBDeuSRR7Rw4UINGDBAHh4eeuKJJyT9ebXo73//u7799ls99dRTqlmzprZt26Zp06Zp9+7d+vTTTx36XLVqlRYuXKi4uDgFBgbm+71Y8csvv8jd3V2lSpWydO5J0htvvKGnn35a3bp10zPPPKNz587pp59+0saNG/Xoo4+qS5cu2r17t95//31NmzZNgYGBkqSyZcted324BRkAls2ZM8dIMt9//73Zu3evKVasmHn66aft2++55x5Tu3Zt+/K+ffuMJDNnzpx8fUkyo0aNsi+PGjXKSDJPPfWUfd2FCxdMhQoVjM1mMxMmTLCvP378uPH29ja9evWyr1u9erWRZO644w6TmZlpX79w4UIjycyYMcMYY0xubq6pWrWqiYmJMbm5ufZ2Z86cMeHh4ea+++7LV9MjjzxiaXwGDRpkJJlvvvnGvu6PP/4w4eHhJiwszOTk5Di8/9jY2Gv2+cADDxhJ5vjx45ZqaNCggQkKCjLHjh2zr/vxxx+Nm5ub6dmzp32ds8a7Tp06Jjs7277+kUceMTabzbRr186hrqioKBMaGmpf3r9/v3F3dzcvvviiQ7tt27aZYsWKOay/5557jCTz9ttv29dlZWWZkJAQ07VrV/u677///rLn25YtW4wks2jRoisN2xXlHXvKlCkOx84b57z3/s477xg3NzeH370xxiQmJhpJ5rvvvrOvk2Tc3NzMjh07LNdQo0YNc+TIEXPkyBGza9cu8/TTTxtJpmPHjsYY6+dep06dHP4bvZzJkycbSWbfvn2W6sPtg4/ngAK688479fjjj+v1119Xenq60/rt16+f/Wd3d3c1atRIxhj17dvXvr5UqVKqXr26fvnll3z79+zZUyVLlrQvd+vWTeXKldOXX34pSdq6dav27NmjRx99VMeOHdPRo0d19OhRnT59Wq1bt9a6devy3ZHUv39/S7V/+eWXatKkicNHeL6+vnrqqae0f/9+7dy509ogXCQzM1OSHN7TlaSnp2vr1q3q3bu3AgIC7Ovr1aun++67zz4GF3PGeF88nyYyMlLGGPsVmIvXHzhwQBcuXJAkffzxx8rNzdVDDz1k/x0cPXpUISEhqlq1qlavXu2wv6+vr8OcHg8PDzVp0uSyNV0q70rSsmXLdObMmWu2v1SxYsX0j3/8w+HY//jHP3T48GElJydLkhYtWqSaNWuqRo0aDu/n3nvvlaR87+eee+5RrVq1LNeQkpKismXLqmzZsqpZs6ZmzpypDh06aPbs2ZKsn3ulSpXSr7/+qu+///66xwEgNAE3YMSIEbpw4YJT796pVKmSw3Le7fV5HxNcvP748eP59q9atarDss1mU5UqVexzMvbs2SNJ6tWrl/2PUN7rzTffVFZWVr55LuHh4ZZq/9///qfq1avnW1+zZk379uvl5+cnSfrjjz8sHV/SFWvIC4cXu9Hxvtz+klSxYsV863Nzc+1ju2fPHhljVLVq1Xy/h127dunw4cMO+1eoUCHf3K/SpUtftqZLhYeHKz4+Xm+++aYCAwMVExOjhISEa85nylO+fPl8k/+rVasmSQ7n1Y4dO/K9l7x2l74fq+dUnrCwMK1YsUJff/21vv32W2VkZGjx4sX235PVc2/o0KHy9fVVkyZNVLVqVcXGxuabywdcCXOagBtw5513qkePHnr99dc1bNiwfNuvNME5Jyfnin26u7tbWifpqvOLriTvKtLkyZOveFu6r6+vw3LeXChXqFGjhiRp27Zt9nk6znSj432lttfqIzc3VzabTV999dVl2176O7jRc2DKlCnq3bu3PvvsMy1fvlxPP/20xo8frw0bNqhChQqW+ria3Nxc1a1bV1OnTr3s9ktD5PWeUz4+PoqOji5wfXlq1qyp1NRULV68WEuXLtVHH32kV155RSNHjtSYMWNuuH/c2ghNwA0aMWKE3n33XU2cODHfttKlS0tSvofkFeSKi1V5V5LyGGP0888/q169epKkypUrS/rzCo4z/ghdLDQ0VKmpqfnWp6Sk2Ldfr44dO2r8+PF69913rxma8vq/Ug2BgYFOeVyCM1SuXFnGGIWHh9uvxtyoq92FKEl169ZV3bp1NWLECK1fv17NmjVTYmKiXnjhhavud/DgwXyPmsh7oGjeBO7KlSvrxx9/VOvWra9Zx1/hes49Hx8fde/eXd27d1d2dra6dOmiF198UcOHD5eXl5dL6kfRwMdzwA2qXLmyevTooddee00ZGRkO2/z8/BQYGKh169Y5rH/llVf+snrefvtth4+yPvzwQ6Wnp6tdu3aSpIiICFWuXFn//e9/derUqXz7592+XRDt27fXpk2blJSUZF93+vRpvf766woLC7uuOSx5oqKi1LZtW7355pv57sCSpOzsbPsDMsuVK6cGDRpo3rx5DkF1+/btWr58udq3b3/dx/+rdOnSRe7u7hozZky+q0XGGB07duy6+8wLNZeG9MzMTPtcqjx169aVm5vbZR+DcKkLFy7otddesy9nZ2frtddeU9myZRURESFJeuihh/Tbb7/p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acKECQ7rP/30U9lsNhdV5VqjRo2Sj4+PUlNTHb6z7FIZGRkaOHCg7rzzTnl6eqpixYrq2LHjVfcp6tasWSObzZbvC3CB2wWhCbjNeXl5aeLEiTp+/LirS3Ga7OzsAu+7d+9eNW/eXKGhoSpTpsxl2+zfv18RERFatWqVJk+erG3btmnp0qVq1aqVYmNjC3xsAIUboQm4zUVHRyskJETjx4+/YpvRo0fn+6hq+vTpCgsLsy/37t1bnTt31ksvvaTg4GCVKlVKY8eO1YULFzRkyBAFBASoQoUKmjNnTr7+U1JSdNddd8nLy0t16tTR2rVrHbZv375d7dq1k6+vr4KDg/X444/r6NGj9u0tW7ZUXFycBg0apMDAwCt+uW1ubq7Gjh2rChUqyNPTUw0aNNDSpUvt2202m5KTkzV27FjZbDaNHj36sv3885//lM1m06ZNm9S1a1dVq1ZNtWvXVnx8vDZs2GBvl5aWpk6dOsnX11d+fn566KGHdOjQoXzjOnv2bFWqVEm+vr765z//qZycHE2aNEkhISEKCgrSiy++6HB8m82m1157Tffff79KlCihmjVrKikpST///LNatmwpHx8f3XXXXdq7d6/Dfp999pkaNmwoLy8v3XnnnRozZowuXLjg0O+bb76pBx54QCVKlFDVqlX1+eefS/ozKLZq1UqSVLp0adlsNvXu3VuS9OGHH6pu3bry9vZWmTJlFB0drdOnT1927IAizdVffgfAdXr16mU6depkPv74Y+Pl5WUOHDhgjDHmk08+MRf/72HUqFGmfv36DvtOmzbNhIaGOvRVsmRJExsba1JSUsxbb71lJJmYmBjz4osvmt27d5tx48aZ4sWL24+zb98+I8lUqFDBfPjhh2bnzp2mX79+pmTJkubo0aPGGGOOHz9uypYta4YPH2527dplNm/ebO677z7TqlUr+7Hvuece4+vra4YMGWJSUlJMSkrKZd/v1KlTjZ+fn3n//fdNSkqKee6550zx4sXN7t27jTHGpKenm9q1a5t//etfJj093fzxxx/5+jh27Jix2WzmpZdeuurY5uTkmAYNGpjmzZubH374wWzYsMFERESYe+65x2FcfX19Tbdu3cyOHTvM559/bjw8PExMTIwZOHCgSUlJMbNnzzaSHL6sW5K54447zIIFC0xqaqrp3LmzCQsLM/fee69ZunSp2blzp2natKlp27atfZ9169YZPz8/M3fuXLN3716zfPlyExYWZkaPHu3Qb4UKFcz8+fPNnj17zNNPP218fX3NsWPHzIULF8xHH31kJJnU1FSTnp5uTpw4YQ4ePGiKFStmpk6davbt22d++uknk5CQcNmxA4o6QhNwG8sLTcYY07RpU/PEE08YYwoemkJDQ01OTo59XfXq1c3dd99tX75w4YLx8fEx77//vjHm/0LThAkT7G3Onz9vKlSoYCZOnGiMMWbcuHGmTZs2Dsc+cOCA/Y+3MX+Gpr/97W/XfL/ly5c3L774osO6xo0bm3/+85/25fr165tRo0ZdsY+NGzcaSebjjz++6rGWL19u3N3dTVpamn3djh07jCSzadMmY8yf41qiRAmTmZlpbxMTE2PCwsLyjeP48ePty5LMiBEj7MtJSUlGknnrrbfs695//33j5eVlX27dunW+oPfOO++YcuXKXbHfU6dOGUnmq6++MsYYs3r1aiPJHD9+3N4mOTnZSDL79++/6ngAtwI+ngMgSZo4caLmzZunXbt2FbiP2rVry83t//63EhwcrLp169qX3d3dVaZMGR0+fNhhv6ioKPvPxYoVU6NGjex1/Pjjj1q9erV8fX3trxo1akiSw8dPERERV60tMzNTBw8eVLNmzRzWN2vW7LreszHGUrtdu3apYsWKqlixon1drVq1VKpUKYfjhYWFqWTJkvbl4OBg1apVK984Xjpm9erVc9guyWGsg4ODde7cOWVmZkr6cxzHjh3rMI5PPvmk0tPTdebMmcv26+PjIz8/v3zHvlj9+vXVunVr1a1bVw8++KDeeOONW2p+HHCxYq4uAEDh0KJFC8XExGj48OH2uSp53Nzc8oWF8+fP5+ujePHiDss2m+2y63Jzcy3XderUKXXs2FETJ07Mt61cuXL2n318fCz3eSOqVq0qm82mlJQUp/RX0DG7uE3enY6XW5e336lTpzRmzBh16dIlXw1eXl5Xredqvy93d3etWLFC69ev1/LlyzVz5kw9//zz2rhxo8LDw6+4H1AUcaUJgN2ECRP0xRdfKCkpyWF92bJllZGR4RCcnPlspYsnT1+4cEHJycmqWbOmJKlhw4basWOHwsLCVKVKFYfX9QQlPz8/lS9fXt99953D+u+++061atWy3E9AQIBiYmKUkJBw2cnOebfj16xZUwcOHNCBAwfs23bu3KkTJ05c1/GcpWHDhkpNTc03hlWqVHG4qnU1Hh4ekqScnByH9TabTc2aNdOYMWO0ZcsWeXh46JNPPnH6ewBcjdAEwK5u3bp67LHH9PLLLzusb9mypY4cOaJJkyZp7969SkhI0FdffeW04yYkJOiTTz5RSkqKYmNjdfz4cT3xxBOSpNjYWP3+++965JFH9P3332vv3r1atmyZ+vTpk++P97UMGTJEEydO1IIFC5Samqphw4Zp69ateuaZZ6673pycHDVp0kQfffSR9uzZo127dunll1+2f9QYHR1tH8/Nmzdr06ZN6tmzp+655x41atTouo7nDCNHjtTbb7+tMWPGaMeOHdq1a5c++OADjRgxwnIfoaGhstlsWrx4sY4cOaJTp05p48aNeumll/TDDz8oLS1NH3/8sY4cOWIPvcCthNAEwMHYsWPzfRxTs2ZNvfLKK0pISFD9+vW1adMmPfvss0475oQJEzRhwgTVr19f3377rT7//HMFBgZKkv3qUE5Ojtq0aaO6detq0KBBKlWqlOUrJHmefvppxcfH61//+pfq1q2rpUuX6vPPP1fVqlWvq58777xTmzdvVqtWrfSvf/1LderU0X333aeVK1fq1VdflfTn1ZfPPvtMpUuXVosWLRQdHa0777xTCxYsuK5jOUtMTIwWL16s5cuXq3HjxmratKmmTZum0NBQy33ccccdGjNmjIYNG6bg4GDFxcXJz89P69atU/v27VWtWjWNGDFCU6ZMUbt27f7CdwO4hs1YndUIAABwG+NKEwAAgAWEJgAAAAsITQAAABYQmgAAACwgNAEAAFhAaAIAALCA0AQAAGABoQkAAMACQhMAAIAFhCYAAAALCE0AAAAWEJoAAAAs+H/WmMYCjAAIfAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "subset = df[df['num_comments'] < 28]\n",
    "sns.histplot(data=subset, x='num_comments', binwidth=1)\n",
    "\n",
    "# set the plot title and axis labels\n",
    "plt.title('Number of Comments per Post')\n",
    "plt.xlabel('Number of Comments')\n",
    "plt.ylabel('Frequency')\n",
    "\n",
    "# display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f5e3d00",
   "metadata": {},
   "source": [
    "As we can see, most posts still have less than 5 comments per post. From this, we can conclude that there are posts with an extremely high number of post which takes the mean to a very high value."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab824e05",
   "metadata": {},
   "source": [
    "# CONCLUSION\n",
    "As we can see from the beginning, the dataset has a lot of outliers. The data, although heavily skewed, is consistent with what we should expect from a social media dataset, as there are very few posts with a lot of likes/awards or comments, while others garner very few peoples eye."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
