# 导航首页

- 路由导航守卫分为 **3 种**：
  - **全局路由守卫、路由独享的守卫、组件内的守卫**
    1. 全局路由守卫
       1. beforeEach
       2. beforeResolve
       3. afterEach
    2. 路由独享的守卫：beforeEnter
    3. 组件内的守卫：
       1. beforeRouteEnter
       2. beforeRouteUpdate
       3. beforeRouteLeave

<br/>

<br/>

# 生命周期

1. 路径改变，导航被触发🔓
2. 在跳转前的页面调用 `beforeRouteLeave` 守卫🚴‍♀️(唯一支持给 next 传递回调的守卫)
3. `beforeEach` (全)
4. `beforeRouteUpdate` --在在 `/users/1` 和 `/users/2` 之间跳转的时候，
5. `beforeEnter` --只在切换页面刚进去的时候触发
6. 解析异步路由组件 ???
7. 在跳转后的页面里调用 `beforeRouteEnter` 守卫🚴‍♂️
8. beforeResolve 守卫（全）
9. 导航被确认🔒
10. afterEach（全）
11. 触发 DOM 更新。
12. 调用 beforeRouteEnter 守卫中传给 next 的回调函数，创建好的组件实例会作为回调函数的参数传入。？？？

<br/>

### 在[官方文档](https://router.vuejs.org/zh/guide/advanced/navigation-guards.html#%E4%BD%BF%E7%94%A8%E7%BB%84%E5%90%88-api)里提到的词：

- 调用点
  - （失活、重用、激活的）组件
  - 全局
  - 路由配置
- 调用的东西
  - 守卫
  - 函数
  - 钩子
  - 回调函数
- 状态
  - 验证
  - 复用
  - 确认
