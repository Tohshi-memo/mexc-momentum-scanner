# Decision Report

- generated_at: 2026-09-16T09:56:30.218653+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14657**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14657, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/13 | 38.5% | +2.22% | **+0.85%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.10% | **+0.08%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +4.30% | **+2.46%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.61% | **+1.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,038.92** / 初期 $100.00 (+938.92%)
- 確定: 5535件 (Win 1648 / Loss 1790 / Flat 2097) / skip 5683件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,038.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.53** / 初期 $100.00 (+128.53%)
- 確定: 3063件 (Win 840 / Loss 722 / Flat 1501) / skip 5005件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0070 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $228.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.42** / 初期 $100.00 (+24.42%)
- 確定: 2946件 (Win 876 / Loss 1157 / Flat 913) / pending 4件 / skip 3179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000360 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.42

## 6. Latest Market Context

- 更新: 2026-09-16T09:56:15.562930+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=75934.8
- Funnel: target 1058 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +104.16% | $15,425,081.65 |
| LSK/USDT:USDT | +33.18% | $21,236,332.55 |
| USELESS/USDT:USDT | +16.66% | $7,080,064.21 |
| LONGXIA/USDT:USDT | +12.69% | $2,638,376.79 |
| BTW/USDT:USDT | +11.65% | $4,732,802.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_relative_strength | +5.13% | +4.81% |
| LSK/USDT:USDT | below_1h_threshold | +4.71% | +4.40% |
| NEAR/USDT:USDT | below_1h_threshold | +3.19% | +2.88% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.13% | +2.82% |
| ARB/USDT:USDT | below_1h_threshold | +2.70% | +2.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
