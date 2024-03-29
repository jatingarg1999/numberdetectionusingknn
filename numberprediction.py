{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('mnist_train.csv')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(60000, 785)\n"
     ]
    }
   ],
   "source": [
    "print(df.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['label', '1x1', '1x2', '1x3', '1x4', '1x5', '1x6', '1x7', '1x8', '1x9',\n",
      "       ...\n",
      "       '28x19', '28x20', '28x21', '28x22', '28x23', '28x24', '28x25', '28x26',\n",
      "       '28x27', '28x28'],\n",
      "      dtype='object', length=785)\n"
     ]
    }
   ],
   "source": [
    "print(df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<bound method NDFrame.head of        label  1x1  1x2  1x3  1x4  1x5  1x6  1x7  1x8  1x9  ...  28x19  28x20  \\\n",
      "0          5    0    0    0    0    0    0    0    0    0  ...      0      0   \n",
      "1          0    0    0    0    0    0    0    0    0    0  ...      0      0   \n",
      "2          4    0    0    0    0    0    0    0    0    0  ...      0      0   \n",
      "3          1    0    0    0    0    0    0    0    0    0  ...      0      0   \n",
      "4          9    0    0    0    0    0    0    0    0    0  ...      0      0   \n",
      "...      ...  ...  ...  ...  ...  ...  ...  ...  ...  ...  ...    ...    ...   \n",
      "59995      8    0    0    0    0    0    0    0    0    0  ...      0      0   \n",
      "59996      3    0    0    0    0    0    0    0    0    0  ...      0      0   \n",
      "59997      5    0    0    0    0    0    0    0    0    0  ...      0      0   \n",
      "59998      6    0    0    0    0    0    0    0    0    0  ...      0      0   \n",
      "59999      8    0    0    0    0    0    0    0    0    0  ...      0      0   \n",
      "\n",
      "       28x21  28x22  28x23  28x24  28x25  28x26  28x27  28x28  \n",
      "0          0      0      0      0      0      0      0      0  \n",
      "1          0      0      0      0      0      0      0      0  \n",
      "2          0      0      0      0      0      0      0      0  \n",
      "3          0      0      0      0      0      0      0      0  \n",
      "4          0      0      0      0      0      0      0      0  \n",
      "...      ...    ...    ...    ...    ...    ...    ...    ...  \n",
      "59995      0      0      0      0      0      0      0      0  \n",
      "59996      0      0      0      0      0      0      0      0  \n",
      "59997      0      0      0      0      0      0      0      0  \n",
      "59998      0      0      0      0      0      0      0      0  \n",
      "59999      0      0      0      0      0      0      0      0  \n",
      "\n",
      "[60000 rows x 785 columns]>\n"
     ]
    }
   ],
   "source": [
    "print(df.head)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "data=df.values\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(60000, 785)\n"
     ]
    }
   ],
   "source": [
    "print(data.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "X=data[:,1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "Y=data[:,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(60000,)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(60000, 784)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "split=(int)(0.8*X.shape[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train=X[:split,:]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "Y_train=Y[:split]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test=X[split:,:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "Y_test=Y[split:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "def drawimage(sample):\n",
    "    data=sample.reshape((28,28))\n",
    "    plt.imshow(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "drawimage(X[15000,:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "def dist(x1,x2):\n",
    "    return np.sqrt(sum((x1-x2)**2))\n",
    "    \n",
    "                   \n",
    "def knn(X,Y,querypoint,k=100):\n",
    "    vals=[]\n",
    "    m=X.shape[0]\n",
    "    for i in range(m):\n",
    "        d=dist(querypoint,X[i])\n",
    "        vals.append((d,Y[i]))\n",
    "    vals=sorted(vals)\n",
    "    vals=vals[:k]\n",
    "    vals=np.array(vals)\n",
    "    newvals=np.unique(vals[:,1],return_counts=True)\n",
    "    index=newvals[1].argmax()\n",
    "    pred=newvals[0][index]\n",
    "    return pred\n",
    "    \n",
    "                   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "pred=knn(X_train,Y_train,X_test[4000])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "print(int(pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "drawimage(X_test[4000])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print(Y_test[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
