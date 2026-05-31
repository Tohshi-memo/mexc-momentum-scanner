# Decision Report

- generated_at: 2026-05-31T09:04:56.008079+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5179**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.16% / filled 20/20。**
- 全期間 MARKET基準: n=5179, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |
| ASK | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.30% | **+0.97%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.32% | **+0.92%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.05% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.92% | **+0.14%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.08% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.29** / 初期 $100.00 (+22.29%)
- 確定: 814件 (Win 184 / Loss 244 / Flat 386) / skip 926件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +6.78%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $122.29

## 4. Latest Market Context

- 更新: 2026-05-31T09:04:50.507987+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=73842.6
- Funnel: target 773 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +33.71% | $1,758,866.24 |
| PLAY/USDT:USDT | +21.31% | $2,071,766.74 |
| TA/USDT:USDT | +20.66% | $2,492,121.31 |
| PORTAL/USDT:USDT | +18.73% | $12,148,333.88 |
| MYX/USDT:USDT | +15.76% | $3,074,913.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUNDIX/USDT:USDT | below_1h_threshold | +0.69% | +0.78% |
| STG/USDT:USDT | below_1h_threshold | +0.61% | +0.71% |
| GUA/USDT:USDT | below_1h_threshold | +0.59% | +0.69% |
| LAB/USDT:USDT | below_1h_threshold | +0.55% | +0.64% |
| AVNT/USDT:USDT | below_1h_threshold | +0.48% | +0.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
