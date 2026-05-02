# Decision Report

- generated_at: 2026-05-02T17:52:04.098260+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2963**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=2963, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.25% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |
| ASK | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.41% | **+0.34%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.54% | **+0.46%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.32% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T17:52:02.059585+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78362.3
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +8.12% | $2,607,556.59 |
| XNY/USDT:USDT | +5.46% | $1,274,382.28 |
| ORDI/USDT:USDT | +5.44% | $29,099,447.91 |
| BASED/USDT:USDT | +4.98% | $1,297,011.26 |
| TAG/USDT:USDT | +4.86% | $15,068,753.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AT/USDT:USDT | below_1h_threshold | +4.96% | +5.03% |
| SPACE/USDT:USDT | below_1h_threshold | +3.40% | +3.48% |
| H/USDT:USDT | below_1h_threshold | +2.41% | +2.48% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.33% | +2.40% |
| WLFI/USDT:USDT | below_1h_threshold | +1.66% | +1.73% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
