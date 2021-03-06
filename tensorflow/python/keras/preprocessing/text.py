# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Utilities for text input preprocessing.
"""
# pylint: disable=invalid-name
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from keras_preprocessing import text

from tensorflow.python.util.tf_export import keras_export

text_to_word_sequence = text.text_to_word_sequence
one_hot = text.one_hot
hashing_trick = text.hashing_trick
Tokenizer = text.Tokenizer

keras_export(
    'keras.preprocessing.text.text_to_word_sequence')(text_to_word_sequence)
keras_export('keras.preprocessing.text.one_hot')(one_hot)
keras_export('keras.preprocessing.text.hashing_trick')(hashing_trick)
keras_export('keras.preprocessing.text.Tokenizer')(Tokenizer)

# text.tokenizer_from_json is only available if keras_preprocessing >= 1.1.0
try:
  tokenizer_from_json = text.tokenizer_from_json
  keras_export('keras.preprocessing.text.tokenizer_from_json')(
      tokenizer_from_json)
except AttributeError:
  pass
