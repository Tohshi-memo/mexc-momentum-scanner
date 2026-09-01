# Decision Report

- generated_at: 2026-09-01T23:01:20.963087+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13277**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13277, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.11% | **-1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +5.85% | **+1.76%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.96% | **+1.48%** |
| LIMIT_6PCT | 8/20 | 40.0% | +3.42% | **+1.37%** |
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.53% | **+1.76%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.83% | **+1.65%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.39% | **+1.55%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.81% | **+1.53%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.65% | **+1.46%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$828.47** / 初期 $100.00 (+728.47%)
- 確定: 4912件 (Win 1497 / Loss 1615 / Flat 1800) / skip 4926件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $828.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$176.54** / 初期 $100.00 (+76.54%)
- 確定: 2256件 (Win 632 / Loss 541 / Flat 1083) / skip 4432件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1049 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $176.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2659件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000289 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-01T23:01:11.542333+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77215.1
- Funnel: target 1036 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +23.75% | $3,167,795.43 |
| UAI/USDT:USDT | +19.46% | $14,412,590.15 |
| ACE/USDT:USDT | +12.89% | $8,441,499.02 |
| BONER/USDT:USDT | +12.42% | $2,175,454.66 |
| FONE/USDT:USDT | +10.08% | $1,257,032.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +1.13% | +1.16% |
| CASHCAT/USDT:USDT | below_1h_threshold | +0.94% | +0.97% |
| PONS/USDT:USDT | below_1h_threshold | +0.88% | +0.91% |
| USOIL/USDT:USDT | below_1h_threshold | +0.32% | +0.35% |
| FONE/USDT:USDT | below_1h_threshold | +0.29% | +0.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
