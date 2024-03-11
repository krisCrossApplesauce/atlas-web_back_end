const { GraphQLObjectType, GraphQLString, GraphQLInt, GraphQLSchema } = require('graphql');

const TaskType = new GraphQLObjectType({
  name: 'Type',
  fields: {
    id: GraphQLString,
    title: GraphQLString,
    weight: GraphQLInt,
    description: GraphQLString
  }
});

const RootQuery = new GraphQLObjectType({
  name: 'RootQueryType',
  fields: {
    task: {
      name: TaskType,
      args: {
        id: {type: GraphQLString}
      },
      resolve(parent, args) {}
    }
  }
});

module.exports = new GraphQLSchema({
  query: RootQuery
});
