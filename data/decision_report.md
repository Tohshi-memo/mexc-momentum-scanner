# Decision Report

- generated_at: 2026-10-29T14:11:16.150560+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17776**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=17776, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.33% | **+1.17%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.08% | **+0.97%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.79% | **+0.59%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.48% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.29% | **-0.14%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.82% | **-0.25%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -1.08% | **-0.43%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6803件 (Win 1975 / Loss 2180 / Flat 2648) / skip 7534件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HYPE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$364.35** / 初期 $100.00 (+264.35%)
- 確定: 4297件 (Win 1162 / Loss 977 / Flat 2158) / skip 6890件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0053 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $364.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5937件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000285 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T14:11:06.523549+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80261.9
- Funnel: target 1085 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +68.24% | $4,523,610.74 |
| BEAT/USDT:USDT | +21.15% | $15,763,517.50 |
| UAI/USDT:USDT | +17.21% | $2,329,471.32 |
| ON/USDT:USDT | +15.63% | $1,068,342.68 |
| HYPE/USDT:USDT | +13.95% | $119,747,059.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CBRSSTOCK/USDT:USDT | below_1h_threshold | +4.63% | +4.65% |
| IDOL/USDT:USDT | below_1h_threshold | +2.67% | +2.68% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +2.48% | +2.49% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.61% | +1.63% |
| BULLA/USDT:USDT | below_1h_threshold | +1.14% | +1.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
