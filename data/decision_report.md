# Decision Report

- generated_at: 2026-06-03T13:12:12.874404+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5545**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=5545, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.29% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.53% | **+0.42%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.39% | **+0.37%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.63% | **+0.47%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| MARKET_LONG | 20/20 | 100.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.19** / 初期 $100.00 (+33.19%)
- 確定: 999件 (Win 239 / Loss 309 / Flat 451) / skip 1107件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $133.19

## 4. Latest Market Context

- 更新: 2026-06-03T13:12:10.949784+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=67085.7
- Funnel: target 771 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +42.44% | $1,220,370.34 |
| CLO/USDT:USDT | +39.49% | $5,188,185.58 |
| BP/USDT:USDT | +33.90% | $1,124,925.76 |
| EPIC/USDT:USDT | +31.32% | $3,059,715.61 |
| WLD/USDT:USDT | +31.16% | $198,319,256.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +2.82% | +2.77% |
| JTO/USDT:USDT | below_1h_threshold | +2.37% | +2.32% |
| ARKM/USDT:USDT | below_1h_threshold | +1.47% | +1.42% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.14% | +1.09% |
| ENA/USDT:USDT | below_1h_threshold | +1.14% | +1.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
