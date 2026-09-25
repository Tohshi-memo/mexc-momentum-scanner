# Decision Report

- generated_at: 2026-09-25T04:31:26.136252+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15514**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15514, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +2.61% | **+1.44%** |
| LIMIT_6PCT | 8/20 | 40.0% | +3.44% | **+1.38%** |
| LIMIT_ATR | 17/20 | 85.0% | +1.08% | **+0.92%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.07% | **+0.85%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.53% | **+1.14%** |
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
- 確定: 5900件 (Win 1739 / Loss 1890 / Flat 2271) / skip 6175件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$254.39** / 初期 $100.00 (+154.39%)
- 確定: 3448件 (Win 950 / Loss 793 / Flat 1705) / skip 5477件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0449 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $254.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.99** / 初期 $100.00 (+19.99%)
- 確定: 3170件 (Win 933 / Loss 1254 / Flat 983) / pending 1件 / skip 3812件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000168 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.99

## 6. Latest Market Context

- 更新: 2026-09-25T04:31:15.312276+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=84120.4
- Funnel: target 1069 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +16.22% | $4,418,419.98 |
| XPL/USDT:USDT | +12.98% | $17,146,272.46 |
| SYN/USDT:USDT | +12.94% | $2,847,623.46 |
| SOXL/USDT:USDT | +6.60% | $27,931,149.88 |
| XLM/USDT:USDT | +6.30% | $16,239,003.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAI/USDT:USDT | below_1h_threshold | +3.64% | +3.73% |
| ONDO/USDT:USDT | below_1h_threshold | +2.34% | +2.43% |
| QNT/USDT:USDT | below_1h_threshold | +2.04% | +2.13% |
| BEAT/USDT:USDT | below_1h_threshold | +1.91% | +2.00% |
| SYN/USDT:USDT | below_1h_threshold | +1.73% | +1.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
