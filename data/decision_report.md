# Decision Report

- generated_at: 2026-07-19T17:11:08.691172+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9058**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.98% / filled 20/20。**
- 全期間 MARKET基準: n=9058, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.02% | **+1.41%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +4.99% | **+0.75%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +4.31% | **+1.51%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +2.59% | **+1.43%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.18% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$110.25** / 初期 $100.00 (+10.25%)
- 確定トレード: 118件 (TP 43 / SL 70 / EXP 5)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $110.25
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$399.27** / 初期 $100.00 (+299.27%)
- 確定: 3120件 (Win 980 / Loss 998 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $399.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.46** / 初期 $100.00 (+25.46%)
- 確定: 1019件 (Win 263 / Loss 218 / Flat 538) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0582 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.81** / 初期 $100.00 (+0.81%)
- 確定: 258件 (Win 89 / Loss 129 / Flat 40) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000239 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $100.81

## 6. Latest Market Context

- 更新: 2026-07-19T17:11:03.634707+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=64556.6
- Funnel: target 885 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +16.04% | $56,932,168.79 |
| TLM/USDT:USDT | +8.80% | $11,872,089.25 |
| ESPORTS/USDT:USDT | +8.64% | $63,715,683.64 |
| SYN/USDT:USDT | +6.46% | $3,517,920.18 |
| DEXE/USDT:USDT | +6.43% | $1,415,271.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +1.97% | +1.90% |
| EVAA/USDT:USDT | below_1h_threshold | +1.96% | +1.88% |
| B/USDT:USDT | below_1h_threshold | +1.83% | +1.76% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.14% | +1.07% |
| BEAT/USDT:USDT | below_1h_threshold | +0.94% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
