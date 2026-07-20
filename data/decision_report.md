# Decision Report

- generated_at: 2026-07-20T09:46:17.681219+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9104**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9104, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.67% | **+1.10%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.89% | **+0.85%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_BB3S | 4/15 | 26.7% | +0.35% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +7.03% | **+4.22%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.96% | **+2.37%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.40% | **+1.36%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$402.37** / 初期 $100.00 (+302.37%)
- 確定: 3166件 (Win 989 / Loss 1004 / Flat 1173) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $402.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.93** / 初期 $100.00 (+26.93%)
- 確定: 1065件 (Win 277 / Loss 218 / Flat 570) / skip 1450件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0650 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $126.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.81** / 初期 $100.00 (+0.81%)
- 確定: 303件 (Win 100 / Loss 134 / Flat 69) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000245 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.81

## 6. Latest Market Context

- 更新: 2026-07-20T09:46:10.900166+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=64238.0
- Funnel: target 884 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +115.04% | $15,465,223.53 |
| BANK/USDT:USDT | +72.70% | $115,844,126.43 |
| EVAA/USDT:USDT | +31.25% | $5,941,024.57 |
| PROM/USDT:USDT | +22.67% | $3,195,347.17 |
| PUMPFUN/USDT:USDT | +18.37% | $26,953,774.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +4.15% | +3.82% |
| TRADOOR/USDT:USDT | below_1h_threshold | +3.37% | +3.05% |
| ACE/USDT:USDT | below_1h_threshold | +2.86% | +2.54% |
| BULLA/USDT:USDT | below_1h_threshold | +2.51% | +2.19% |
| SYN/USDT:USDT | below_1h_threshold | +2.20% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
