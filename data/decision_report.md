# Decision Report

- generated_at: 2026-11-15T00:21:30.972951+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18922**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=18922, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +2.52% | **+1.13%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.58% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.32% | **+0.92%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.19% | **+0.72%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.71% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,746.38** / 初期 $100.00 (+1646.38%)
- 確定: 7326件 (Win 2106 / Loss 2344 / Flat 2876) / skip 8157件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARIA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,746.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$427.10** / 初期 $100.00 (+327.10%)
- 確定: 4930件 (Win 1317 / Loss 1080 / Flat 2533) / skip 7403件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0275 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARIA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $427.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7082件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-15T00:21:14.858258+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64182.5
- Funnel: target 1071 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +20.32% | $3,811,705.46 |
| ARIA/USDT:USDT | +9.46% | $2,258,080.50 |
| JCT/USDT:USDT | +8.75% | $4,952,549.01 |
| SHELL/USDT:USDT | +8.35% | $2,433,007.19 |
| BTW/USDT:USDT | +5.01% | $5,236,185.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHELL/USDT:USDT | below_1h_threshold | +4.84% | +4.76% |
| JCT/USDT:USDT | below_1h_threshold | +2.72% | +2.64% |
| BTW/USDT:USDT | below_1h_threshold | +2.14% | +2.06% |
| INIT/USDT:USDT | below_1h_threshold | +1.89% | +1.81% |
| SOXL/USDT:USDT | below_1h_threshold | +1.73% | +1.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
