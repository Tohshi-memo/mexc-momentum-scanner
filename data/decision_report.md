# Decision Report

- generated_at: 2026-05-27T00:39:23.044346+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4911**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.01% / filled 20/20。**
- 全期間 MARKET基準: n=4911, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.01% | **+1.01%** |
| ASK | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.65% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.38% | **+1.10%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.23% | **+0.98%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.81% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.48% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.36** / 初期 $100.00 (+29.36%)
- 確定: 679件 (Win 172 / Loss 216 / Flat 291) / skip 793件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $129.36

## 4. Latest Market Context

- 更新: 2026-05-27T00:39:20.638966+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=75886.8
- Funnel: target 768 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNC/USDT:USDT | +13.08% | $6,431,430.67 |
| REQ/USDT:USDT | +12.16% | $1,075,809.71 |
| MUSTOCK/USDT:USDT | +8.16% | $24,138,649.03 |
| PLAY/USDT:USDT | +6.20% | $7,765,315.40 |
| PHA/USDT:USDT | +5.64% | $6,967,034.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHA/USDT:USDT | below_1h_threshold | +4.19% | +4.20% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +3.30% | +3.31% |
| FET/USDT:USDT | below_1h_threshold | +2.68% | +2.70% |
| JTO/USDT:USDT | below_1h_threshold | +1.92% | +1.93% |
| BILL/USDT:USDT | below_1h_threshold | +1.74% | +1.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
