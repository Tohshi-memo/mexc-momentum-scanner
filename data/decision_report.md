# Decision Report

- generated_at: 2026-09-25T03:41:31.920746+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15513**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=15513, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +3.44% | **+1.38%** |
| LIMIT_5PCT | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.56% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.62% | **+1.18%** |
| LIMIT_BB3S_LONG | 8/10 | 80.0% | +0.79% | **+0.63%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.75% | **+0.56%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.93% | **+0.56%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.71% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5900件 (Win 1739 / Loss 1890 / Flat 2271) / skip 6174件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.66** / 初期 $100.00 (+152.66%)
- 確定: 3447件 (Win 949 / Loss 793 / Flat 1705) / skip 5477件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0449 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $252.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.99** / 初期 $100.00 (+19.99%)
- 確定: 3170件 (Win 933 / Loss 1254 / Flat 983) / pending 1件 / skip 3812件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000129 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.99

## 6. Latest Market Context

- 更新: 2026-09-25T03:41:14.725276+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=84305.3
- Funnel: target 1069 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +13.62% | $2,610,141.94 |
| QNT/USDT:USDT | +11.70% | $3,991,127.35 |
| XPL/USDT:USDT | +10.27% | $17,190,057.05 |
| ONE/USDT:USDT | +9.47% | $8,907,891.49 |
| SOXL/USDT:USDT | +6.79% | $26,463,217.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QNT/USDT:USDT | below_1h_threshold | +2.70% | +2.55% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.63% | +1.48% |
| ZRO/USDT:USDT | below_1h_threshold | +1.43% | +1.28% |
| AXS/USDT:USDT | below_1h_threshold | +1.34% | +1.19% |
| ZEC/USDT:USDT | below_1h_threshold | +1.25% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
