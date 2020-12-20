import {
  Button,
  Select,
  Option,
  Radio,
  RadioGroup,
  RadioButton,
  Row,
  Col,
  Dialog,
  Message,
  Form,
  FormItem,
  Input,
  Card,
  Autocomplete,
  DatePicker,
  TimePicker,
  Dropdown,
  DropdownItem,
  DropdownMenu,
  Tabs,
  TabPane,
  Carousel,
  CarouselItem,
  Divider
} from 'element-ui'

const element = {
  install: function (Vue) {
    Vue.use(Button)
    Vue.use(Select)
    Vue.use(Option)
    Vue.use(Radio)
    Vue.use(RadioGroup)
    Vue.use(RadioButton)
    Vue.use(Row)
    Vue.use(Col)
    Vue.use(Dialog)
    Vue.use(Form)
    Vue.use(FormItem)
    Vue.use(Input)
    Vue.use(Card)
    Vue.use(Autocomplete)
    Vue.use(DatePicker)
    Vue.use(TimePicker)
    Vue.use(Dropdown)
    Vue.use(DropdownItem)
    Vue.use(DropdownMenu)
    Vue.use(Tabs)
    Vue.use(TabPane)
    Vue.use(Carousel)
    Vue.use(CarouselItem)
    Vue.use(Divider)
    Vue.prototype.$message = Message
  }
}

export default element
