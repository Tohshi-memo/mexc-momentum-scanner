# Decision Report

- generated_at: 2026-09-16T05:11:25.706172+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14638**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=14638, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.84% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.70% | **+0.56%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.57% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,045.55** / 初期 $100.00 (+945.55%)
- 確定: 5519件 (Win 1646 / Loss 1786 / Flat 2087) / skip 5680件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,045.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3054件 (Win 839 / Loss 719 / Flat 1496) / skip 4995件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0176 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.12** / 初期 $100.00 (+25.12%)
- 確定: 2928件 (Win 871 / Loss 1144 / Flat 913) / pending 6件 / skip 3179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000336 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $125.12

## 6. Latest Market Context

- 更新: 2026-09-16T05:11:15.097019+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=75747.9
- Funnel: target 1064 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +31.86% | $3,270,123.75 |
| LSK/USDT:USDT | +29.71% | $18,226,762.88 |
| LONGXIA/USDT:USDT | +19.41% | $2,156,144.64 |
| USELESS/USDT:USDT | +12.32% | $5,120,792.88 |
| ON/USDT:USDT | +11.16% | $3,261,656.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +0.49% | +0.59% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.22% | +0.33% |
| BTW/USDT:USDT | below_1h_threshold | +0.11% | +0.22% |
| MUU/USDT:USDT | below_1h_threshold | +0.11% | +0.21% |
| FCXSTOCK/USDT:USDT | below_1h_threshold | +0.09% | +0.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
