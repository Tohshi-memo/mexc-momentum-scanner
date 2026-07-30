# Decision Report

- generated_at: 2026-07-30T19:51:28.966807+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9919**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9919, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.92% | **-2.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.03% | **+0.26%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.24% | **-0.18%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.69% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.43% | **+2.43%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.97% | **+2.37%** |
| MARKET_LONG | 20/20 | 100.0% | +2.31% | **+2.31%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.82% | **+2.29%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.69% | **+1.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$497.17** / 初期 $100.00 (+397.17%)
- 確定: 3521件 (Win 1114 / Loss 1147 / Flat 1260) / skip 2959件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROBO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $497.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1243件 (Win 344 / Loss 283 / Flat 616) / skip 2087件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0749 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定: 803件 (Win 262 / Loss 318 / Flat 223) / pending 2件 / skip 594件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000083 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AGT/USDT:USDT `MARKET` EXPIRED account +0.16% 残高後 $110.80

## 6. Latest Market Context

- 更新: 2026-07-30T19:51:18.832257+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=64800.0
- Funnel: target 920 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +19.79% | $5,962,964.99 |
| ESPORTS/USDT:USDT | +18.33% | $3,951,433.83 |
| ROBO/USDT:USDT | +16.26% | $2,609,055.48 |
| CAP/USDT:USDT | +16.17% | $4,007,859.29 |
| EVAA/USDT:USDT | +10.77% | $3,096,313.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MMT/USDT:USDT | below_1h_threshold | +4.34% | +4.14% |
| ROBO/USDT:USDT | below_1h_threshold | +2.95% | +2.75% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.75% | +2.55% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.66% | +2.46% |
| CAP/USDT:USDT | below_1h_threshold | +2.08% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
