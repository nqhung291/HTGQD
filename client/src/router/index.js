import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index')
  },
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [
      {
        path: 'dashboard',
        component: () => import('@/views/dashboard/index'),
        name: 'Dashboard',
        meta: { title: 'Trang chủ', icon: 'dashboard', affix: true }
      }
    ]
  },
  {
    path: '/repository',
    component: Layout,
    children: [
      {
        path: '',
        component: () => import('@/views/repository'),
        name: 'Icon',
        meta: { title: 'Tủ đồ', icon: 'theme', noCache: true }
      }
    ]
  },
  {
    path: '/history',
    component: Layout,
    children: [
      {
        path: '',
        component: () => import('@/views/history'),
        name: 'History',
        meta: { title: 'Lịch sử giao dịch', icon: 'list', noCache: true }
      }
    ]
  }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
