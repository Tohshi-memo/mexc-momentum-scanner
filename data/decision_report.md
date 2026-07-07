# Decision Report

- generated_at: 2026-07-07T18:08:06.264722+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8451**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8451, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.48% | **+0.70%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_BB3S | 4/16 | 25.0% | -0.03% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.64% | **+0.38%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.51% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$101.56** / 初期 $100.00 (+1.56%)
- 確定トレード: 70件 (TP 24 / SL 45 / EXP 1)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.56
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.48** / 初期 $100.00 (+220.48%)
- 確定: 2656件 (Win 845 / Loss 897 / Flat 914) / skip 2356件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.50% 残高後 $320.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 640件 (Win 152 / Loss 158 / Flat 330) / skip 1222件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0159 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T18:08:00.021537+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=63989.8
- Funnel: target 847 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +21.07% | $30,571,574.56 |
| KORU/USDT:USDT | +6.11% | $5,607,120.21 |
| USELESS/USDT:USDT | +4.86% | $1,589,218.06 |
| EDGE/USDT:USDT | +4.51% | $10,287,328.26 |
| SOXL/USDT:USDT | +3.92% | $19,046,035.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| METASTOCK/USDT:USDT | below_1h_threshold | +1.21% | +1.48% |
| DEXE/USDT:USDT | below_1h_threshold | +1.00% | +1.27% |
| US/USDT:USDT | below_1h_threshold | +0.48% | +0.76% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +0.47% | +0.74% |
| DASH/USDT:USDT | below_1h_threshold | +0.41% | +0.68% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
