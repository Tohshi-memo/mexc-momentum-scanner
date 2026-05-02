# Decision Report

- generated_at: 2026-05-02T18:17:03.608983+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2965**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=2965, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.88% | **+1.78%** |
| ASK | 20/20 | 100.0% | +1.36% | **+1.36%** |
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.55% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.64% | **+0.61%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.93% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T18:16:59.376704+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=78299.1
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XNY/USDT:USDT | +8.61% | $1,256,292.60 |
| BSB/USDT:USDT | +8.33% | $7,194,649.81 |
| TAC/USDT:USDT | +7.67% | $2,596,598.05 |
| BIANRENSHENG/USDT:USDT | +6.96% | $1,027,234.74 |
| BASED/USDT:USDT | +5.06% | $1,303,831.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RLS/USDT:USDT | below_1h_threshold | +4.98% | +5.06% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.81% | +2.89% |
| XNY/USDT:USDT | below_1h_threshold | +1.30% | +1.38% |
| H/USDT:USDT | below_1h_threshold | +0.97% | +1.05% |
| LUNC/USDT:USDT | below_1h_threshold | +0.86% | +0.94% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
