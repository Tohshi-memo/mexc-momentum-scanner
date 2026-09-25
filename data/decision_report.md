# Decision Report

- generated_at: 2026-09-25T02:11:26.909273+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15509**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=15509, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.69% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/10 | 70.0% | +1.47% | **+1.03%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.54% | **+0.77%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.69% | **+0.55%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.61% | **+0.49%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.50% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5900件 (Win 1739 / Loss 1890 / Flat 2271) / skip 6170件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.66** / 初期 $100.00 (+152.66%)
- 確定: 3444件 (Win 949 / Loss 793 / Flat 1702) / skip 5476件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0018 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $252.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.99** / 初期 $100.00 (+19.99%)
- 確定: 3170件 (Win 933 / Loss 1254 / Flat 983) / pending 1件 / skip 3808件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000129 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.99

## 6. Latest Market Context

- 更新: 2026-09-25T02:11:15.915281+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=84819.4
- Funnel: target 1069 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +42.33% | $14,315,955.89 |
| SYN/USDT:USDT | +13.05% | $2,108,778.37 |
| XPL/USDT:USDT | +11.05% | $16,814,647.79 |
| QNT/USDT:USDT | +8.64% | $3,687,666.10 |
| SOXL/USDT:USDT | +7.05% | $24,805,437.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +2.44% | +2.15% |
| MVLL/USDT:USDT | below_1h_threshold | +1.76% | +1.47% |
| SYN/USDT:USDT | below_1h_threshold | +1.64% | +1.35% |
| SNXX/USDT:USDT | below_1h_threshold | +1.62% | +1.34% |
| MUU/USDT:USDT | below_1h_threshold | +1.47% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
