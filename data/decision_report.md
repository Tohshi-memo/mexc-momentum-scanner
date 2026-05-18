# Decision Report

- generated_at: 2026-05-18T02:18:29.462419+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4429**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=4429, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.99% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.91% | **+0.69%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.72% | **+0.54%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.64% | **+0.48%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.35% | **+0.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.15** / 初期 $100.00 (+20.15%)
- 確定: 426件 (Win 110 / Loss 145 / Flat 171) / skip 564件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $120.15

## 4. Latest Market Context

- 更新: 2026-05-18T02:18:27.090904+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=77030.0
- Funnel: target 765 → liquid 131 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +30.96% | $5,785,208.15 |
| AIGENSYN/USDT:USDT | +10.18% | $3,050,336.26 |
| UB/USDT:USDT | +6.57% | $15,496,691.22 |
| BSB/USDT:USDT | +6.05% | $19,393,645.78 |
| HYPE/USDT:USDT | +5.21% | $312,974,973.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +1.40% | +1.47% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.26% | +1.32% |
| SIREN/USDT:USDT | below_1h_threshold | +1.13% | +1.19% |
| POL/USDT:USDT | below_1h_threshold | +0.99% | +1.06% |
| GUA/USDT:USDT | below_1h_threshold | +0.99% | +1.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
