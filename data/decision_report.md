# Decision Report

- generated_at: 2026-10-04T22:01:27.148759+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16138**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16138, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.85% | **-0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +2.85% | **+1.14%** |
| LIMIT_BB3S | 5/11 | 45.5% | +0.80% | **+0.36%** |
| LIMIT_6PCT | 9/20 | 45.0% | +0.63% | **+0.28%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.34% | **+0.25%** |
| LIMIT_9PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.22% | **+1.03%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.25% | **+0.94%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.43% | **+0.93%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.58% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,297.43** / 初期 $100.00 (+1197.43%)
- 確定: 6197件 (Win 1822 / Loss 1987 / Flat 2388) / skip 6502件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,297.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3609件 (Win 1005 / Loss 845 / Flat 1759) / skip 5940件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0677 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4297件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-04T22:01:13.453952+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=85972.7
- Funnel: target 1076 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +216.66% | $8,631,591.32 |
| HNT/USDT:USDT | +12.22% | $4,197,062.35 |
| VVV/USDT:USDT | +6.65% | $2,253,317.05 |
| FLOKI/USDT:USDT | +6.15% | $2,425,446.30 |
| SKY/USDT:USDT | +4.60% | $2,006,078.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +0.82% | +0.65% |
| NEAR/USDT:USDT | below_1h_threshold | +0.61% | +0.44% |
| HNT/USDT:USDT | below_1h_threshold | +0.55% | +0.38% |
| MONAD/USDT:USDT | below_1h_threshold | +0.54% | +0.38% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.44% | +0.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
