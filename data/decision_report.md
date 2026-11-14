# Decision Report

- generated_at: 2026-11-14T12:21:31.336825+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18895**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18895, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.50% | **+0.50%** |
| LIMIT_BB3S | 10/16 | 62.5% | +0.74% | **+0.46%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.35% | **+0.31%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.43% | **+0.30%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,742.75** / 初期 $100.00 (+1642.75%)
- 確定: 7299件 (Win 2102 / Loss 2342 / Flat 2855) / skip 8157件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,742.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$419.72** / 初期 $100.00 (+319.72%)
- 確定: 4903件 (Win 1312 / Loss 1080 / Flat 2511) / skip 7403件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0687 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $419.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7055件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000229 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-14T12:21:15.082586+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=67130.1
- Funnel: target 1071 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHELL/USDT:USDT | +30.99% | $5,004,534.20 |
| DODO/USDT:USDT | +24.51% | $1,770,997.19 |
| SOPH/USDT:USDT | +19.89% | $1,679,278.93 |
| AKE/USDT:USDT | +16.79% | $83,184,499.37 |
| ARIA/USDT:USDT | +13.37% | $3,922,085.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARIA/USDT:USDT | below_1h_threshold | +3.80% | +3.97% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.30% | +2.46% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.64% | +1.81% |
| JUP/USDT:USDT | below_1h_threshold | +0.46% | +0.63% |
| SNXX/USDT:USDT | below_1h_threshold | +0.26% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
