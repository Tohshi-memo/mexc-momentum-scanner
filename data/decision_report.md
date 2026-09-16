# Decision Report

- generated_at: 2026-09-16T08:46:25.988800+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14653**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=14653, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/12 | 41.7% | +2.45% | **+1.02%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.50% | **+0.15%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.24% | **+0.13%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +2.64% | **+1.65%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,045.47** / 初期 $100.00 (+945.47%)
- 確定: 5531件 (Win 1647 / Loss 1788 / Flat 2096) / skip 5683件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,045.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.81** / 初期 $100.00 (+128.81%)
- 確定: 3059件 (Win 839 / Loss 721 / Flat 1499) / skip 5005件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $228.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.30** / 初期 $100.00 (+25.30%)
- 確定: 2942件 (Win 876 / Loss 1153 / Flat 913) / pending 2件 / skip 3179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000414 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CVC/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $125.30

## 6. Latest Market Context

- 更新: 2026-09-16T08:46:18.355333+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=75508.4
- Funnel: target 1054 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +117.76% | $12,521,126.95 |
| LSK/USDT:USDT | +27.74% | $19,850,407.43 |
| USELESS/USDT:USDT | +18.73% | $6,254,926.04 |
| LONGXIA/USDT:USDT | +12.99% | $2,603,850.21 |
| BTW/USDT:USDT | +10.18% | $4,907,804.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +3.45% | +3.73% |
| 4/USDT:USDT | below_1h_threshold | +1.68% | +1.96% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.52% | +1.81% |
| USELESS/USDT:USDT | below_1h_threshold | +1.08% | +1.37% |
| IOST/USDT:USDT | below_1h_threshold | +1.03% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
