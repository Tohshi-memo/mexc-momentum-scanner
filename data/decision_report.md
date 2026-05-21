# Decision Report

- generated_at: 2026-05-21T04:09:15.825477+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4604**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.71% / filled 20/20。**
- 全期間 MARKET基準: n=4604, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +1.44% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.64% | **+1.64%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.22% | **+1.00%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.17% | **+0.97%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.89% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 545件 (Win 138 / Loss 185 / Flat 222) / skip 620件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T04:09:10.744456+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=78040.6
- Funnel: target 765 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +73.03% | $1,430,776.62 |
| EDEN/USDT:USDT | +41.98% | $29,648,990.07 |
| SATO/USDT:USDT | +21.18% | $3,550,618.07 |
| NIL/USDT:USDT | +20.11% | $3,409,331.33 |
| JTO/USDT:USDT | +14.81% | $3,286,842.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +4.37% | +4.37% |
| ROAM/USDT:USDT | below_1h_threshold | +4.20% | +4.20% |
| BSB/USDT:USDT | below_1h_threshold | +2.04% | +2.04% |
| DASH/USDT:USDT | below_1h_threshold | +1.07% | +1.07% |
| LIT/USDT:USDT | below_1h_threshold | +1.04% | +1.04% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
