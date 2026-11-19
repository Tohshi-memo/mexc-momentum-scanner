# Decision Report

- generated_at: 2026-11-19T21:11:17.191021+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19218**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19218, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.24% | **-0.20%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.59% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.46% | **+1.73%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +3.07% | **+1.23%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.75% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,692.99** / 初期 $100.00 (+1592.99%)
- 確定: 7381件 (Win 2119 / Loss 2376 / Flat 2886) / skip 8398件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANTHROPIC/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,692.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$438.72** / 初期 $100.00 (+338.72%)
- 確定: 5043件 (Win 1346 / Loss 1087 / Flat 2610) / skip 7586件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0540 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $438.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7380件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000280 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-19T21:11:06.257822+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=61994.2
- Funnel: target 1084 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +24.36% | $1,448,095.58 |
| SKY/USDT:USDT | +14.77% | $3,732,072.36 |
| UVXY/USDT:USDT | +12.33% | $2,428,980.93 |
| SOXS/USDT:USDT | +11.76% | $49,818,043.32 |
| ICNT/USDT:USDT | +8.22% | $5,391,053.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UVXY/USDT:USDT | below_1h_threshold | +2.47% | +2.63% |
| SOXS/USDT:USDT | below_1h_threshold | +1.59% | +1.76% |
| IRYS/USDT:USDT | below_1h_threshold | +1.44% | +1.61% |
| RARE/USDT:USDT | below_1h_threshold | +1.34% | +1.50% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.97% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
