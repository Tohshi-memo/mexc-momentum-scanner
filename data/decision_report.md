# Decision Report

- generated_at: 2026-10-25T07:16:19.596256+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17411**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17411, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.34% | **-1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 18/20 | 90.0% | +1.29% | **+1.17%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.55% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.02% | **+0.25%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.53% | **+1.77%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +4.18% | **+1.67%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.70% | **+1.35%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.35% | **+1.18%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,501.14** / 初期 $100.00 (+1401.14%)
- 確定: 6664件 (Win 1936 / Loss 2123 / Flat 2605) / skip 7308件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: T/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,501.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$309.10** / 初期 $100.00 (+209.10%)
- 確定: 3954件 (Win 1094 / Loss 927 / Flat 1933) / skip 6868件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1645 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: T/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $309.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5569件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000527 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T07:16:07.226208+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=80599.5
- Funnel: target 1071 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +44.59% | $5,598,643.10 |
| T/USDT:USDT | +39.57% | $3,594,813.75 |
| USELESS/USDT:USDT | +20.37% | $4,176,121.70 |
| AGT/USDT:USDT | +15.94% | $5,496,889.55 |
| GRASS/USDT:USDT | +11.57% | $1,863,150.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +4.43% | +4.26% |
| APR/USDT:USDT | below_1h_threshold | +2.02% | +1.84% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.32% | +1.15% |
| GRASS/USDT:USDT | below_1h_threshold | +1.21% | +1.03% |
| SPX/USDT:USDT | below_1h_threshold | +1.03% | +0.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
