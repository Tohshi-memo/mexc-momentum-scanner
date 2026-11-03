# Decision Report

- generated_at: 2026-11-03T15:36:38.595577+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18091**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18091, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.71% | **-1.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +4.06% | **+3.25%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.74% | **+1.87%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.48% | **+1.74%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.63% | **+1.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 261件 (TP 96 / SL 157 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,500.44** / 初期 $100.00 (+1400.44%)
- 確定: 6921件 (Win 2001 / Loss 2219 / Flat 2701) / skip 7731件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ICNT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,500.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$379.73** / 初期 $100.00 (+279.73%)
- 確定: 4510件 (Win 1207 / Loss 1003 / Flat 2300) / skip 6992件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $379.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6251件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000176 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-03T15:36:21.066020+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77352.7
- Funnel: target 1084 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +77.44% | $11,650,088.59 |
| IDOL/USDT:USDT | +51.64% | $14,033,419.36 |
| ICNT/USDT:USDT | +34.86% | $4,630,691.72 |
| HOT/USDT:USDT | +22.42% | $10,334,410.57 |
| EVAA/USDT:USDT | +13.48% | $5,865,800.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRENSTOCK/USDT:USDT | below_1h_threshold | +4.57% | +4.59% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +4.33% | +4.35% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +3.34% | +3.35% |
| AGT/USDT:USDT | below_1h_threshold | +3.17% | +3.18% |
| SOXS/USDT:USDT | below_1h_threshold | +2.48% | +2.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
