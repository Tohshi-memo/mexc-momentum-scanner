# Decision Report

- generated_at: 2026-09-14T01:21:43.464618+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14472**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=14472, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.43% | **+1.36%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.08% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.82% | **+0.57%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.74% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.90% | **+3.90%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.17% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,072.66** / 初期 $100.00 (+972.66%)
- 確定: 5434件 (Win 1635 / Loss 1762 / Flat 2037) / skip 5599件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.22% 残高後 $1,072.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.42** / 初期 $100.00 (+128.42%)
- 確定: 2990件 (Win 830 / Loss 715 / Flat 1445) / skip 4893件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0649 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STEEM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $228.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.50** / 初期 $100.00 (+26.50%)
- 確定: 2859件 (Win 850 / Loss 1106 / Flat 903) / pending 4件 / skip 3082件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000261 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STEEM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $126.50

## 6. Latest Market Context

- 更新: 2026-09-14T01:21:25.779910+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=76677.2
- Funnel: target 1068 → liquid 144 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +45.65% | $1,054,762.74 |
| POWER/USDT:USDT | +21.12% | $3,964,397.20 |
| BR/USDT:USDT | +7.20% | $2,296,269.55 |
| MAGMA/USDT:USDT | +5.35% | $1,805,379.17 |
| FILECOIN/USDT:USDT | +5.15% | $40,819,920.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +4.03% | +4.15% |
| POWR/USDT:USDT | below_1h_threshold | +2.89% | +3.02% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.06% | +2.18% |
| UAI/USDT:USDT | below_1h_threshold | +1.52% | +1.64% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
