# Decision Report

- generated_at: 2026-09-08T17:06:16.950890+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14014**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14014, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.96% | **-0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.99% | **+0.35%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.05% | **+0.04%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.43% | **-0.11%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.92% | **-0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.96% | **+1.96%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.17% | **+1.74%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.52% | **+0.84%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.71% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,012.19** / 初期 $100.00 (+912.19%)
- 確定: 5278件 (Win 1587 / Loss 1707 / Flat 1984) / skip 5297件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.14% 残高後 $1,012.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.50** / 初期 $100.00 (+90.50%)
- 確定: 2617件 (Win 725 / Loss 622 / Flat 1270) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0467 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $190.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.92** / 初期 $100.00 (+19.92%)
- 確定: 2598件 (Win 761 / Loss 985 / Flat 852) / pending 6件 / skip 2884件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $119.92

## 6. Latest Market Context

- 更新: 2026-09-08T17:06:08.957678+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78771.4
- Funnel: target 1070 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +11.05% | $2,175,237.67 |
| MARSCOIN/USDT:USDT | +5.18% | $2,662,481.08 |
| LIT/USDT:USDT | +3.72% | $5,554,537.99 |
| BTR/USDT:USDT | +3.05% | $1,243,491.61 |
| UAI/USDT:USDT | +2.60% | $14,489,231.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +2.00% | +1.91% |
| SOXS/USDT:USDT | below_1h_threshold | +1.98% | +1.89% |
| FLOCK/USDT:USDT | below_1h_threshold | +1.92% | +1.83% |
| BNCSTOCK/USDT:USDT | below_1h_threshold | +1.35% | +1.26% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.18% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
