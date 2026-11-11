# Decision Report

- generated_at: 2026-11-11T15:56:34.162051+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18690**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18690, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.72% | **-2.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 17/20 | 85.0% | +0.94% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.25% | **+0.38%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.23% | **+2.42%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.74% | **+1.68%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.95% | **+1.62%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +4.82% | **+1.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.89** / 初期 $100.00 (+20.89%)
- 確定トレード: 270件 (TP 97 / SL 165 / EXP 8)
- 最新: SNXX/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.89
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,712.85** / 初期 $100.00 (+1612.85%)
- 確定: 7222件 (Win 2079 / Loss 2309 / Flat 2834) / skip 8029件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RKLBSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $1,712.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4778件 (Win 1283 / Loss 1056 / Flat 2439) / skip 7323件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1050 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6851件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000192 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T15:56:17.543566+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.53% price=73932.4
- Funnel: target 1103 → liquid 146 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.5 >= 65=1, 4h RSI 78.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +196.43% | $25,031,135.23 |
| SNXX/USDT:USDT | +36.05% | $39,870,820.04 |
| MUU/USDT:USDT | +31.16% | $13,548,420.77 |
| MVLL/USDT:USDT | +26.11% | $4,234,985.60 |
| SOXL/USDT:USDT | +22.81% | $691,439,926.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_relative_strength | +5.50% | +4.96% |
| NIGHT/USDT:USDT | below_1h_threshold | +4.39% | +3.86% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +3.46% | +2.93% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.09% | +2.56% |
| MUU/USDT:USDT | below_1h_threshold | +2.84% | +2.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
