# Decision Report

- generated_at: 2026-05-31T09:15:14.711598+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5180**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.16% / filled 20/20。**
- 全期間 MARKET基準: n=5180, expectancy=-0.05%
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
| LIMIT_1PCT | 15/20 | 75.0% | +1.23% | **+0.92%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.18% | **+0.82%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

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

- 残高: **$121.68** / 初期 $100.00 (+21.68%)
- 確定: 815件 (Win 184 / Loss 245 / Flat 386) / skip 926件
- 成長率目線: 平均log +0.000241 / 幾何平均 +0.024% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.50% 残高後 $121.68

## 4. Latest Market Context

- 更新: 2026-05-31T09:15:09.624587+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=73886.7
- Funnel: target 773 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +34.38% | $1,814,857.58 |
| PLAY/USDT:USDT | +31.39% | $2,493,469.80 |
| TA/USDT:USDT | +23.03% | $2,498,085.70 |
| MYX/USDT:USDT | +17.08% | $3,160,488.79 |
| PORTAL/USDT:USDT | +16.75% | $12,291,766.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +1.53% | +1.57% |
| LAB/USDT:USDT | below_1h_threshold | +1.49% | +1.53% |
| STG/USDT:USDT | below_1h_threshold | +1.36% | +1.40% |
| TA/USDT:USDT | below_1h_threshold | +1.35% | +1.39% |
| BILL/USDT:USDT | below_1h_threshold | +0.88% | +0.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
