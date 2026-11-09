# Decision Report

- generated_at: 2026-11-09T23:21:16.874120+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18562**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18562, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.98% | **-1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.94% | **+0.47%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.35% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.71% | **+2.03%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.96% | **+1.77%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.94% | **+1.62%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.68% | **+1.47%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,626.14** / 初期 $100.00 (+1526.14%)
- 確定: 7164件 (Win 2057 / Loss 2285 / Flat 2822) / skip 7959件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RITUAL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,626.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$387.85** / 初期 $100.00 (+287.85%)
- 確定: 4758件 (Win 1277 / Loss 1048 / Flat 2433) / skip 7215件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1291 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INIT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $387.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6724件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000418 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-09T23:21:07.817178+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=75263.9
- Funnel: target 1094 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +44.20% | $3,047,106.66 |
| NIUBI/USDT:USDT | +28.17% | $1,199,063.88 |
| CLAUDIA/USDT:USDT | +17.79% | $1,088,673.28 |
| ON/USDT:USDT | +13.56% | $5,337,718.58 |
| JCT/USDT:USDT | +6.85% | $32,122,965.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INIT/USDT:USDT | below_1h_threshold | +3.05% | +3.04% |
| NIUBI/USDT:USDT | below_1h_threshold | +2.22% | +2.21% |
| IDOL/USDT:USDT | below_1h_threshold | +0.54% | +0.53% |
| SILVER/USDT:USDT | below_1h_threshold | +0.50% | +0.50% |
| XAUT/USDT:USDT | below_1h_threshold | +0.14% | +0.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
