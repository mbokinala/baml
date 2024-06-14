###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ bundle add baml sorbet-runtime sorbet-struct-comparable
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# frozen_string_literal: true
# rubocop: disable
# formatter:off
# typed: false
require "sorbet-runtime"
require "sorbet-struct-comparable"

require_relative "types"

module Baml
  
  module PartialTypes
    class Blah < T::Struct; end
    class ClassOptionalOutput < T::Struct; end
    class ClassOptionalOutput2 < T::Struct; end
    class ClassWithImage < T::Struct; end
    class DynamicClassOne < T::Struct; end
    class DynamicClassTwo < T::Struct; end
    class DynamicOutput < T::Struct; end
    class Education < T::Struct; end
    class Email < T::Struct; end
    class Event < T::Struct; end
    class FakeImage < T::Struct; end
    class InnerClass < T::Struct; end
    class InnerClass2 < T::Struct; end
    class NamedArgsSingleClass < T::Struct; end
    class OptionalTest_Prop1 < T::Struct; end
    class OptionalTest_ReturnType < T::Struct; end
    class OrderInfo < T::Struct; end
    class Person < T::Struct; end
    class RaysData < T::Struct; end
    class Resume < T::Struct; end
    class SearchParams < T::Struct; end
    class SomeClassNestedDynamic < T::Struct; end
    class TestClassAlias < T::Struct; end
    class TestClassNested < T::Struct; end
    class TestClassWithEnum < T::Struct; end
    class TestOutputClass < T::Struct; end
    class UnionTest_ReturnType < T::Struct; end
    class WithReasoning < T::Struct; end
    class Blah < T::Struct
      include T::Struct::ActsAsComparable
      const :prop4, T.nilable(String)
    end
    class ClassOptionalOutput < T::Struct
      include T::Struct::ActsAsComparable
      const :prop1, T.nilable(String)
      const :prop2, T.nilable(String)
    end
    class ClassOptionalOutput2 < T::Struct
      include T::Struct::ActsAsComparable
      const :prop1, T.nilable(String)
      const :prop2, T.nilable(String)
      const :prop3, Baml::PartialTypes::Blah
    end
    class ClassWithImage < T::Struct
      include T::Struct::ActsAsComparable
      const :myImage, T.nilable(Baml::Image)
      const :param2, T.nilable(String)
      const :fake_image, Baml::PartialTypes::FakeImage
    end
    class DynamicClassOne < T::Struct
      include T::Struct::ActsAsComparable
    end
    class DynamicClassTwo < T::Struct
      include T::Struct::ActsAsComparable
      const :hi, T.nilable(String)
      const :some_class, Baml::PartialTypes::SomeClassNestedDynamic
      const :status, T.nilable(Baml::Types::DynEnumOne)
    end
    class DynamicOutput < T::Struct
      include T::Struct::ActsAsComparable
    end
    class Education < T::Struct
      include T::Struct::ActsAsComparable
      const :institution, T.nilable(String)
      const :location, T.nilable(String)
      const :degree, T.nilable(String)
      const :major, T::Array[T.nilable(String)]
      const :graduation_date, T.nilable(String)
    end
    class Email < T::Struct
      include T::Struct::ActsAsComparable
      const :subject, T.nilable(String)
      const :body, T.nilable(String)
      const :from_address, T.nilable(String)
    end
    class Event < T::Struct
      include T::Struct::ActsAsComparable
      const :title, T.nilable(String)
      const :date, T.nilable(String)
      const :location, T.nilable(String)
      const :description, T.nilable(String)
    end
    class FakeImage < T::Struct
      include T::Struct::ActsAsComparable
      const :url, T.nilable(String)
    end
    class InnerClass < T::Struct
      include T::Struct::ActsAsComparable
      const :prop1, T.nilable(String)
      const :prop2, T.nilable(String)
      const :inner, Baml::PartialTypes::InnerClass2
    end
    class InnerClass2 < T::Struct
      include T::Struct::ActsAsComparable
      const :prop2, T.nilable(Integer)
      const :prop3, T.nilable(Float)
    end
    class NamedArgsSingleClass < T::Struct
      include T::Struct::ActsAsComparable
      const :key, T.nilable(String)
      const :key_two, T.nilable(T::Boolean)
      const :key_three, T.nilable(Integer)
    end
    class OptionalTest_Prop1 < T::Struct
      include T::Struct::ActsAsComparable
      const :omega_a, T.nilable(String)
      const :omega_b, T.nilable(Integer)
    end
    class OptionalTest_ReturnType < T::Struct
      include T::Struct::ActsAsComparable
      const :omega_1, Baml::PartialTypes::OptionalTest_Prop1
      const :omega_2, T.nilable(String)
      const :omega_3, T::Array[T.nilable(Baml::Types::OptionalTest_CategoryType)]
    end
    class OrderInfo < T::Struct
      include T::Struct::ActsAsComparable
      const :order_status, T.nilable(Baml::Types::OrderStatus)
      const :tracking_number, T.nilable(String)
      const :estimated_arrival_date, T.nilable(String)
    end
    class Person < T::Struct
      include T::Struct::ActsAsComparable
      const :name, T.nilable(String)
      const :hair_color, T.nilable(Baml::Types::Color)
    end
    class RaysData < T::Struct
      include T::Struct::ActsAsComparable
      const :dataType, T.nilable(Baml::Types::DataType)
      const :value, T.nilable(T.any(Baml::PartialTypes::Resume, Baml::PartialTypes::Event))
    end
    class Resume < T::Struct
      include T::Struct::ActsAsComparable
      const :name, T.nilable(String)
      const :email, T.nilable(String)
      const :phone, T.nilable(String)
      const :experience, T::Array[Baml::PartialTypes::Education]
      const :education, T::Array[T.nilable(String)]
      const :skills, T::Array[T.nilable(String)]
    end
    class SearchParams < T::Struct
      include T::Struct::ActsAsComparable
      const :dateRange, T.nilable(Integer)
      const :location, T::Array[T.nilable(String)]
      const :jobTitle, Baml::PartialTypes::WithReasoning
      const :company, Baml::PartialTypes::WithReasoning
      const :description, T::Array[Baml::PartialTypes::WithReasoning]
      const :tags, T::Array[T.nilable(T.any(T.nilable(Baml::Types::Tag), T.nilable(String)))]
    end
    class SomeClassNestedDynamic < T::Struct
      include T::Struct::ActsAsComparable
      const :hi, T.nilable(String)
    end
    class TestClassAlias < T::Struct
      include T::Struct::ActsAsComparable
      const :key, T.nilable(String)
      const :key2, T.nilable(String)
      const :key3, T.nilable(String)
      const :key4, T.nilable(String)
      const :key5, T.nilable(String)
    end
    class TestClassNested < T::Struct
      include T::Struct::ActsAsComparable
      const :prop1, T.nilable(String)
      const :prop2, Baml::PartialTypes::InnerClass
    end
    class TestClassWithEnum < T::Struct
      include T::Struct::ActsAsComparable
      const :prop1, T.nilable(String)
      const :prop2, T.nilable(Baml::Types::EnumInClass)
    end
    class TestOutputClass < T::Struct
      include T::Struct::ActsAsComparable
      const :prop1, T.nilable(String)
      const :prop2, T.nilable(Integer)
    end
    class UnionTest_ReturnType < T::Struct
      include T::Struct::ActsAsComparable
      const :prop1, T.nilable(T.any(T.nilable(String), T.nilable(T::Boolean)))
      const :prop2, T::Array[T.nilable(T.any(T.nilable(Float), T.nilable(T::Boolean)))]
      const :prop3, T.nilable(T.any(T::Array[T.nilable(T::Boolean)], T::Array[T.nilable(Integer)]))
    end
    class WithReasoning < T::Struct
      include T::Struct::ActsAsComparable
      const :value, T.nilable(String)
      const :reasoning, T.nilable(String)
    end
  end
end